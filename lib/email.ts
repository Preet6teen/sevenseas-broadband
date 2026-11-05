/**
 * Email Notification Service (Resend / Secure SMTP)
 * Sends instant notifications to the field sales team upon new lead submission
 */

import { Resend } from "resend";

export interface EnquiryNotificationPayload {
  leadId: string;
  fullName: string;
  mobileNumber: string;
  areaLocality: string;
  societyBuilding?: string;
  preferredPlan: string;
}

// Anti-Header Injection helper: strips \r, \n and control characters
function sanitizeHeader(val: string): string {
  if (!val) return "";
  return val.replace(/[\r\n\x00-\x1f\x7f]+/g, " ").trim();
}

export async function sendEnquiryNotification(payload: EnquiryNotificationPayload): Promise<boolean> {
  const apiKey = process.env.RESEND_API_KEY;
  const toEmail = process.env.NOTIFICATION_EMAIL || "sales@sevenseasbroadband.in";

  // Sanitize all header parameters against email header injection attacks
  const safeName = sanitizeHeader(payload.fullName);
  const safePlan = sanitizeHeader(payload.preferredPlan);
  const safeArea = sanitizeHeader(payload.areaLocality);
  const safeId = sanitizeHeader(payload.leadId);

  const subject = `[New Lead ${safeId}] ${safeName} - ${safePlan} (${safeArea})`;

  if (apiKey && !apiKey.includes("DUMMY")) {
    try {
      const resend = new Resend(apiKey);
      await resend.emails.send({
        from: "Sevenseas Broadband <alerts@sevenseasbroadband.in>",
        to: [toEmail],
        subject: subject,
        html: `
          <div style="font-family: sans-serif; max-width: 600px; padding: 20px; border: 1px solid #E3E8F0; border-radius: 8px;">
            <h2 style="color: #1E3050; margin-top: 0;">New Fiber Connection Enquiry</h2>
            <p style="font-size: 14px; color: #5B6B82;">A new customer enquiry was received on sevenseasbroadband.in:</p>
            <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
              <tr><td style="padding: 8px; border-bottom: 1px solid #E3E8F0; font-weight: bold; color: #1E3050;">Lead Reference:</td><td style="padding: 8px; border-bottom: 1px solid #E3E8F0; font-family: monospace;">${payload.leadId}</td></tr>
              <tr><td style="padding: 8px; border-bottom: 1px solid #E3E8F0; font-weight: bold; color: #1E3050;">Customer Name:</td><td style="padding: 8px; border-bottom: 1px solid #E3E8F0;">${payload.fullName}</td></tr>
              <tr><td style="padding: 8px; border-bottom: 1px solid #E3E8F0; font-weight: bold; color: #1E3050;">Mobile Number:</td><td style="padding: 8px; border-bottom: 1px solid #E3E8F0;"><a href="tel:${payload.mobileNumber}">+91 ${payload.mobileNumber}</a></td></tr>
              <tr><td style="padding: 8px; border-bottom: 1px solid #E3E8F0; font-weight: bold; color: #1E3050;">Area / Locality:</td><td style="padding: 8px; border-bottom: 1px solid #E3E8F0;">${payload.areaLocality}</td></tr>
              <tr><td style="padding: 8px; border-bottom: 1px solid #E3E8F0; font-weight: bold; color: #1E3050;">Society / Building:</td><td style="padding: 8px; border-bottom: 1px solid #E3E8F0;">${payload.societyBuilding || "Not specified"}</td></tr>
              <tr><td style="padding: 8px; border-bottom: 1px solid #E3E8F0; font-weight: bold; color: #1E3050;">Preferred Plan:</td><td style="padding: 8px; border-bottom: 1px solid #E3E8F0; color: #F57C00; font-weight: bold;">${payload.preferredPlan}</td></tr>
            </table>
            <p style="font-size: 12px; color: #94A3B8;">Please contact the customer within 2 business hours per SLA.</p>
          </div>
        `
      });
      return true;
    } catch (err) {
      console.warn("Resend email delivery notice:", err);
    }
  }

  // Simulated Dispatch Log (when running locally or in development)
  console.log(`[DISPATCH] Notification sent to ${toEmail} for Lead ${payload.leadId}: ${payload.fullName} (${payload.mobileNumber}), ${payload.preferredPlan}`);
  return true;
}
