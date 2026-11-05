#!/usr/bin/env python3
"""
build_all.py — Assembles and writes all 16 pages of Sevenseas Broadband website.
"""

import os
from generate_all_pages import render_page
from pages import home, about, plans, fiber, residential, coverage, new_connection, contact, faq, legal, future

PAGES = [
    {
        "filename": "about.html",
        "title": "About Us — Building Reliable Residential Fiber Infrastructure",
        "description": "Learn how Sevenseas Broadband is bridging communities with pure optical glass FTTH architecture, redundant rings, and dedicated neighborhood field support.",
        "active_key": "about",
        "content_fn": about.get_content
    },
    {
        "filename": "plans.html",
        "title": "Fiber Broadband Plans — Transparent Pricing from ₹499/mo",
        "description": "Explore transparent symmetrical broadband plans from 150 Mbps to 1 Gbps. Zero hidden fees, free Wi-Fi 6 router on annual plans, and premium OTT bundles.",
        "active_key": "plans",
        "content_fn": plans.get_content
    },
    {
        "filename": "fiber-internet.html",
        "title": "Pure Fiber-to-the-Home (FTTH) Technology — Sevenseas Optical Network",
        "description": "Discover the science behind pure 9µm silica glass optical fiber, symmetrical upload/download speeds, weather-proof transmission, and direct gaming peering.",
        "active_key": "fiber",
        "content_fn": fiber.get_content
    },
    {
        "filename": "residential.html",
        "title": "Residential Internet — Family-Oriented High-Speed Fiber",
        "description": "Broadband engineered for modern homes: bufferless multi-room 4K streaming, remote work, student learning, online gaming, and whole-home Wi-Fi 6 mesh coverage.",
        "active_key": "residential",
        "content_fn": residential.get_content
    },
    {
        "filename": "new-connection.html",
        "title": "Book New Connection — Same-Day Fiber Installation",
        "description": "Get connected in 3 simple steps: choose your plan, pick an installation time slot, and get free doorstep cabling with a complimentary Wi-Fi 6 router.",
        "active_key": "more",
        "content_fn": new_connection.get_content
    },
    {
        "filename": "contact.html",
        "title": "Contact Us — Toll-Free Helpline, WhatsApp & Head Office",
        "description": "Reach Sevenseas customer care 24/7 on 1800-233-7327 or message our verified WhatsApp desk for instant assistance, bill payment, and society tie-ups.",
        "active_key": "more",
        "content_fn": contact.get_content
    },
    {
        "filename": "faq.html",
        "title": "Frequently Asked Questions — Answers to All Connection Inquiries",
        "description": "Detailed answers to over 20 frequent customer questions regarding speeds, symmetrical uploads, router setup, billing, relocation, and KYC requirements.",
        "active_key": "more",
        "content_fn": faq.get_content
    },
    {
        "filename": "privacy.html",
        "title": "Privacy Policy — Digital Personal Data Protection",
        "description": "Official privacy policy for Sevenseas Broadband subscribers and visitors, compliant with the DPDP Act and DoT telecommunications regulations.",
        "active_key": "more",
        "content_fn": legal.get_privacy_content
    },
    {
        "filename": "terms.html",
        "title": "Terms and Conditions — Residential Subscriber Agreement",
        "description": "Master Service Agreement governing residential optical internet access, equipment care, billing terms, and acceptable usage guidelines.",
        "active_key": "more",
        "content_fn": legal.get_terms_content
    },
    {
        "filename": "refund-policy.html",
        "title": "Refund and Cancellation Policy — 7-Day Money-Back Guarantee",
        "description": "Plain-English cancellation terms, 7-day initial money-back guarantee, and hardware security deposit refund procedures within 5-7 business days.",
        "active_key": "more",
        "content_fn": legal.get_refund_content
    },
    {
        "filename": "business.html",
        "title": "Business Broadband & Dedicated Leased Lines (DIA)",
        "description": "Enterprise-grade dedicated internet access with 99.95% uptime SLA, 1:1 unshared CIR bandwidth, static IP allocations, and 24/7 priority NOC support.",
        "active_key": "business",
        "content_fn": future.get_business_content
    },
    {
        "filename": "installation.html",
        "title": "Internet Installation Guide — What to Expect on Installation Day",
        "description": "A 4-step walkthrough of your installation appointment: doorstep fiber routing, clean optical splicing, router placement tips, and live speed tests.",
        "active_key": "more",
        "content_fn": future.get_installation_content
    },
    {
        "filename": "support.html",
        "title": "Customer Support Hub, Diagnostic Guide & Quick Bill Pay",
        "description": "Diagnose ONT router status LEDs, pay monthly bills online in seconds, raise support tickets, and optimize your residential Wi-Fi channels.",
        "active_key": "more",
        "content_fn": future.get_support_content
    },
    {
        "filename": "localities.html",
        "title": "Broadband in Individual Localities — Neighborhood Network Directory",
        "description": "Discover optical fiber hubs across Bandra, Andheri, Powai, Thane, Navi Mumbai, and Malad with authentic neighborhood network architecture.",
        "active_key": "more",
        "content_fn": future.get_localities_content
    }
]

def main():
    print("Building all 16 Sevenseas Broadband pages...")
    for p in PAGES:
        html = render_page(
            title=p["title"],
            description=p["description"],
            active_key=p["active_key"],
            content=p["content_fn"](),
            filename=p["filename"]
        )
        with open(p["filename"], "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated: {p['filename']} ({len(html)} bytes)")

    print(f"\nSuccessfully created all {len(PAGES)} pages!")

if __name__ == "__main__":
    main()
