import { z } from "zod";

/**
 * Sevenseas Broadband — Production Enquiry Zod Schema
 * Enforces strict validation on server and client
 */
export const INDIAN_MOBILE_REGEX = /^[6-9]\d{9}$/;

export const EnquirySchema = z.object({
  fullName: z
    .string()
    .trim()
    .min(2, { message: "Full name must be at least 2 characters." })
    .max(80, { message: "Full name cannot exceed 80 characters." })
    .regex(/^[a-zA-Z\s\.\'\-]+$/, { message: "Full name contains invalid characters." }),

  mobileNumber: z
    .string()
    .trim()
    .regex(INDIAN_MOBILE_REGEX, {
      message: "Please enter a valid 10-digit Indian mobile number starting with 6, 7, 8, or 9."
    }),

  areaLocality: z
    .string()
    .trim()
    .min(2, { message: "Area or locality is required." })
    .max(120),

  societyBuilding: z
    .string()
    .trim()
    .max(120)
    .optional()
    .default(""),

  preferredPlan: z.enum([
    "Starter 100 Mbps",
    "Popular 200 Mbps",
    "Premium 300 Mbps",
    "Gigabit Max 500 Mbps",
    "Gigabit Ultra 1000 Mbps",
    "Not Decided / Help Me Choose"
  ], {
    errorMap: () => ({ message: "Please select a valid broadband plan." })
  }),

  consent: z.literal(true, {
    errorMap: () => ({ message: "You must authorize Sevenseas to contact you regarding your inquiry." })
  }),

  // Anti-Bot Honeypot: must be empty
  b_website: z
    .string()
    .max(0, { message: "Automated submission detected." })
    .optional()
    .default(""),

  // Cloudflare Turnstile token
  turnstileToken: z.string().optional()
});

export type EnquiryInput = z.infer<typeof EnquirySchema>;

export function escapeHtml(str: string): string {
  if (!str) return "";
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}
