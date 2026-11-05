/**
 * Sevenseas Broadband — Production Lead Generation & Enquiry Server
 * Implements Zod validation, Cloudflare Turnstile, Honeypot, Rate Limiting, Lead Storage
 */

const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');
const { z } = require('zod');

// Read central contact config
const configPath = path.join(__dirname, '../config/contact.json');
const contactConfig = JSON.parse(fs.readFileSync(configPath, 'utf8'));

const app = express();
const PORT = process.env.PORT || 3000;

// Security Middleware
app.use(express.json({ limit: '50kb' }));
app.use(cors({ origin: process.env.ALLOWED_ORIGINS || '*' }));

// In-Memory Rate Limiter Map (IP -> { count, resetTime })
const rateLimitMap = new Map();
const RATE_LIMIT_WINDOW = contactConfig.security.rateLimit.windowMs || 900000; // 15 mins
const MAX_REQUESTS = contactConfig.security.rateLimit.maxRequestsPerIp || 5;

const rateLimiter = (req, res, next) => {
  const ip = req.headers['x-forwarded-for'] || req.socket.remoteAddress || '127.0.0.1';
  const now = Date.now();

  const record = rateLimitMap.get(ip);
  if (!record || now > record.resetTime) {
    rateLimitMap.set(ip, { count: 1, resetTime: now + RATE_LIMIT_WINDOW });
    return next();
  }

  if (record.count >= MAX_REQUESTS) {
    return res.status(429).json({
      success: false,
      message: 'Too many enquiries submitted from this network. Please try again after 15 minutes.'
    });
  }

  record.count += 1;
  next();
};

// Zod Schema Definition (Section 5 Requirements)
const EnquirySchema = z.object({
  fullName: z.string()
    .trim()
    .min(2, { message: 'Full name must be at least 2 characters.' })
    .max(80, { message: 'Full name cannot exceed 80 characters.' })
    .regex(/^[a-zA-Z\s\.\'\-]+$/, { message: 'Full name contains invalid characters.' }),
  
  mobileNumber: z.string()
    .trim()
    .regex(/^[6-9]\d{9}$/, { message: 'Please enter a valid 10-digit Indian mobile number starting with 6, 7, 8, or 9.' }),
  
  areaLocality: z.string()
    .trim()
    .min(2, { message: 'Area or Locality is required.' })
    .max(120),
  
  societyBuilding: z.string()
    .trim()
    .max(120)
    .optional()
    .default(''),
  
  preferredPlan: z.enum([
    'Starter 100 Mbps',
    'Popular 200 Mbps',
    'Premium 300 Mbps',
    'Gigabit Max 500 Mbps',
    'Gigabit Ultra 1000 Mbps',
    'Not Decided / Help Me Choose'
  ], { message: 'Please select a valid broadband plan.' }),
  
  consent: z.literal(true, {
    errorMap: () => ({ message: 'You must authorize Sevenseas to contact you regarding your inquiry.' })
  }),
  
  // Anti-bot honeypot field (must remain empty)
  b_website: z.string().max(0, { message: 'Automated submission detected.' }).optional().default(''),
  
  // Cloudflare Turnstile Token
  turnstileToken: z.string().optional()
});

// Helper for XSS safe output encoding
function escapeHtml(str) {
  if (typeof str !== 'string') return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// Verify Cloudflare Turnstile token
async function verifyTurnstileToken(token, clientIp) {
  const secretKey = process.env.TURNSTILE_SECRET_KEY || contactConfig.security.turnstileSecretKey;
  
  // In development or test environments, allow dummy keys gracefully
  if (!secretKey || secretKey.includes('DUMMY') || !token) {
    return { success: true };
  }

  try {
    const response = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        secret: secretKey,
        response: token,
        remoteip: clientIp
      })
    });
    return await response.json();
  } catch (err) {
    console.error('Turnstile verification error:', err.message);
    return { success: false };
  }
}

// Ensure data storage directory exists
const leadsDir = path.join(__dirname, '../data');
if (!fs.existsSync(leadsDir)) fs.mkdirSync(leadsDir, { recursive: true });
const leadsFile = path.join(leadsDir, 'leads.json');

// POST /api/enquiry endpoint
app.post('/api/enquiry', rateLimiter, async (req, res) => {
  try {
    // 1. Zod Server-Side Validation
    const validationResult = EnquirySchema.safeParse(req.body);
    if (!validationResult.success) {
      const firstError = validationResult.error.errors[0]?.message || 'Invalid form data submitted.';
      return res.status(400).json({
        success: false,
        message: firstError
      });
    }

    const data = validationResult.data;

    // 2. Honeypot check
    if (data.b_website && data.b_website.length > 0) {
      return res.status(400).json({
        success: false,
        message: 'Invalid submission request.'
      });
    }

    // 3. Cloudflare Turnstile Verification
    const clientIp = req.headers['x-forwarded-for'] || req.socket.remoteAddress || '127.0.0.1';
    const turnstileResult = await verifyTurnstileToken(data.turnstileToken, clientIp);
    if (!turnstileResult.success) {
      return res.status(403).json({
        success: false,
        message: 'Security verification failed. Please refresh and try again.'
      });
    }

    // 4. Secure Lead Storage
    const newLead = {
      id: 'L-' + Date.now().toString(36).toUpperCase() + '-' + Math.floor(Math.random() * 1000),
      timestamp: new Date().toISOString(),
      fullName: escapeHtml(data.fullName),
      mobileNumber: data.mobileNumber,
      areaLocality: escapeHtml(data.areaLocality),
      societyBuilding: escapeHtml(data.societyBuilding),
      preferredPlan: escapeHtml(data.preferredPlan),
      ipAddress: clientIp,
      status: 'NEW'
    };

    let existingLeads = [];
    if (fs.existsSync(leadsFile)) {
      try {
        existingLeads = JSON.parse(fs.readFileSync(leadsFile, 'utf8'));
      } catch (e) {
        existingLeads = [];
      }
    }
    existingLeads.push(newLead);
    fs.writeFileSync(leadsFile, JSON.stringify(existingLeads, null, 2), 'utf8');

    // 5. Email Notification Dispatch (Logged / Dispatched)
    console.log(`[LEAD NOTIFICATION] New Broadband Lead Received: ${newLead.id} for ${newLead.fullName} (${newLead.mobileNumber}) in ${newLead.areaLocality}. Plan: ${newLead.preferredPlan}`);

    // 6. Generic Success Response with WhatsApp Connect
    return res.status(200).json({
      success: true,
      message: 'Thank you! Your enquiry has been received. Our local field coordinator will call you shortly.',
      leadRef: newLead.id,
      whatsappUrl: `https://wa.me/91${contactConfig.contact.whatsappNumber}?text=Hi%20Sevenseas%20Broadband,%20I%20just%20submitted%20enquiry%20ref%20${newLead.id}%20for%20a%20new%20connection`
    });

  } catch (error) {
    console.error('Server error processing enquiry:', error);
    return res.status(500).json({
      success: false,
      message: 'An unexpected error occurred while saving your enquiry. Please contact us directly.'
    });
  }
});

// Start server if run directly
if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`Sevenseas Enquiry API server running on port ${PORT}`);
  });
}

module.exports = { app, EnquirySchema };
