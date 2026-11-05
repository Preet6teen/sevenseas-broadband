import { NextRequest, NextResponse } from "next/server";
import { EnquirySchema, escapeHtml } from "@/lib/validation";
import { verifyTurnstileToken } from "@/lib/turnstile";
import { insertLead } from "@/lib/db";
import { sendEnquiryNotification } from "@/lib/email";

// Simple in-memory IP rate limiter for App Router
interface RateLimitRecord {
  count: number;
  resetTime: number;
}
const rateLimitMap = new Map<string, RateLimitRecord>();
const RATE_LIMIT_WINDOW_MS = 15 * 60 * 1000; // 15 mins
const MAX_REQUESTS_PER_WINDOW = 5;

export async function POST(req: NextRequest) {
  try {
    // 1. IP Rate Limiting
    const forwardedFor = req.headers.get("x-forwarded-for");
    const ip = forwardedFor ? forwardedFor.split(",")[0].trim() : "127.0.0.1";
    const now = Date.now();

    const record = rateLimitMap.get(ip);
    if (!record || now > record.resetTime) {
      rateLimitMap.set(ip, { count: 1, resetTime: now + RATE_LIMIT_WINDOW_MS });
    } else {
      if (record.count >= MAX_REQUESTS_PER_WINDOW) {
        return NextResponse.json(
          {
            success: false,
            message: "Too many enquiries submitted from this network. Please wait 15 minutes."
          },
          { status: 429 }
        );
      }
      record.count += 1;
    }

    // 2. Parse & Validate Payload
    let body;
    try {
      body = await req.json();
    } catch {
      return NextResponse.json(
        { success: false, message: "Invalid JSON format." },
        { status: 400 }
      );
    }

    const validationResult = EnquirySchema.safeParse(body);
    if (!validationResult.success) {
      const firstError = validationResult.error.errors[0]?.message || "Invalid submission data.";
      return NextResponse.json(
        { success: false, message: firstError },
        { status: 400 }
      );
    }

    const data = validationResult.data;

    // 3. Honeypot check (anti-bot)
    if (data.b_website && data.b_website.length > 0) {
      // Silently discard bot spam
      return NextResponse.json({
        success: true,
        message: "Thank you for your enquiry. Our team will contact you shortly."
      });
    }

    // 4. Cloudflare Turnstile Verification
    const turnstileResult = await verifyTurnstileToken(data.turnstileToken, ip);
    if (!turnstileResult.success) {
      return NextResponse.json(
        { success: false, message: "Security verification failed. Please try again." },
        { status: 403 }
      );
    }

    // 5. Store Lead in PostgreSQL (or file audit fallback)
    const leadId = `SSB-${Date.now()}-${Math.floor(Math.random() * 900 + 100)}`;
    await insertLead({
      id: leadId,
      fullName: escapeHtml(data.fullName),
      mobileNumber: data.mobileNumber,
      areaLocality: escapeHtml(data.areaLocality),
      societyBuilding: escapeHtml(data.societyBuilding || ""),
      preferredPlan: data.preferredPlan,
      ipAddress: ip
    });

    // 6. Send Email Notification via Resend / SMTP
    await sendEnquiryNotification({
      leadId,
      fullName: data.fullName,
      mobileNumber: data.mobileNumber,
      areaLocality: data.areaLocality,
      societyBuilding: data.societyBuilding,
      preferredPlan: data.preferredPlan
    });

    // 7. Generate pre-filled WhatsApp link
    const whatsappMsg = encodeURIComponent(
      `Hi Sevenseas Broadband! I submitted an enquiry (Ref: ${leadId}) for ${data.preferredPlan} in ${data.areaLocality}. Please confirm installation availability.`
    );
    const whatsappUrl = `https://wa.me/919664985535?text=${whatsappMsg}`;

    return NextResponse.json({
      success: true,
      leadId,
      whatsappUrl,
      message: "Thank you! Your enquiry has been received. Our local field team will call you within 2 hours."
    });
  } catch (err: any) {
    console.error("Enquiry API Route error:", err);
    return NextResponse.json(
      {
        success: false,
        message: "An internal server error occurred. Please call +91 96649 85535 directly."
      },
      { status: 500 }
    );
  }
}
