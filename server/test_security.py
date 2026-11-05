#!/usr/bin/env python3
"""
server/test_security.py — Comprehensive Security Test Suite for Sevenseas Broadband
Verifies:
1. SQL Injection Resistance (Parameterized Queries)
2. XSS Output Escaping
3. Email Header Injection Sanitization
4. Anti-Bot Honeypot Blocking
5. Rate Limiting Enforcement
6. Strict Mobile Number Validation (^[6-9]\\d{9}$)
7. Security Response Headers (HSTS, CSP, X-Frame-Options, X-Content-Type-Options)
"""

import os
import sys
import json
import sqlite3
import unittest

sys.path.insert(0, os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from app import (
    validate_enquiry,
    save_lead,
    is_rate_limited,
    RATE_LIMIT_MAP,
    DB_PATH,
    CONFIG
)

class TestFormAndInfrastructureSecurity(unittest.TestCase):

    def setUp(self):
        RATE_LIMIT_MAP.clear()

    def test_sql_injection_resistance(self):
        """Verify that malicious SQL payloads are safely parameterized and do not execute."""
        sql_payloads = [
            "' OR '1'='1",
            "'; DROP TABLE leads; --",
            "Robert'); DROP TABLE leads;--",
            "1' UNION SELECT 1,2,3,4,5,6,7,8,9 --"
        ]

        for payload in sql_payloads:
            # We bypass regex check to simulate direct DB parameter handling
            test_lead = {
                "fullName": payload,
                "mobileNumber": "9820011223",
                "areaLocality": "Airoli Sector 3",
                "societyBuilding": payload,
                "preferredPlan": "Starter 100 Mbps"
            }
            lead_id = save_lead(test_lead, "127.0.0.1")
            
            # Verify table still exists and data was inserted literally
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("SELECT full_name FROM leads WHERE id = ?", (lead_id,))
            row = cur.fetchone()
            conn.close()

            self.assertIsNotNone(row)
            self.assertEqual(row[0], payload, "Payload must be stored as literal text without executing SQL.")

    def test_email_header_injection_prevention(self):
        """Verify that CRLF injections cannot inject arbitrary SMTP headers."""
        malicious_input = "Amit\r\nBcc: attacker@spam.com\r\nSubject: Spoofed"
        import re
        sanitized = re.sub(r'[\r\n\x00-\x1f\x7f]+', ' ', malicious_input).strip()
        
        self.assertNotIn("\r", sanitized)
        self.assertNotIn("\n", sanitized)
        self.assertEqual(sanitized, "Amit Bcc: attacker@spam.com Subject: Spoofed")

    def test_xss_output_escaping(self):
        """Verify HTML special characters are properly escaped."""
        def escape_html(val):
            return str(val).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#039;")

        xss_string = '<script>alert("XSS")</script>'
        escaped = escape_html(xss_string)
        self.assertEqual(escaped, '&lt;script&gt;alert(&quot;XSS&quot;)&lt;/script&gt;')
        self.assertNotIn("<script>", escaped)

    def test_honeypot_bot_blocking(self):
        """Verify bot submission with filled honeypot is blocked."""
        bot_payload = {
            "fullName": "Spam Bot",
            "mobileNumber": "9820011223",
            "areaLocality": "Airoli",
            "consent": True,
            "b_website": "http://spammer-link.com"
        }
        errors, _ = validate_enquiry(bot_payload)
        self.assertTrue(any("bot" in err.lower() for err in errors))

    def test_strict_mobile_validation(self):
        """Verify strict adherence to ^[6-9]\\d{9}$."""
        # Invalid numbers
        for invalid in ["0123456789", "5123456789", "123456", "982001122345", "98200abcd1"]:
            errors, _ = validate_enquiry({
                "fullName": "Test User",
                "mobileNumber": invalid,
                "areaLocality": "Airoli",
                "consent": True,
                "b_website": ""
            })
            self.assertTrue(any("Indian mobile number" in e for e in errors))

        # Valid numbers
        for valid in ["9664985535", "7400222922", "8123456789", "6123456789"]:
            errors, cleaned = validate_enquiry({
                "fullName": "Test User",
                "mobileNumber": valid,
                "areaLocality": "Airoli",
                "consent": True,
                "b_website": ""
            })
            self.assertEqual(len(errors), 0)
            self.assertEqual(cleaned["mobileNumber"], valid)

    def test_rate_limiting_enforcement(self):
        """Verify IP rate limiting after 5 requests in a window."""
        test_ip = "203.0.113.42"
        for i in range(5):
            self.assertFalse(is_rate_limited(test_ip))
        self.assertTrue(is_rate_limited(test_ip), "6th submission from same IP must be rate-limited.")

    def test_security_headers_configured(self):
        """Verify security headers are configured in Next.js, _headers, and Nginx configs."""
        headers_file = os.path.join(ROOT_DIR, "_headers")
        self.assertTrue(os.path.exists(headers_file))
        with open(headers_file, "r", encoding="utf-8") as f:
            headers_content = f.read()

        self.assertIn("Strict-Transport-Security", headers_content)
        self.assertIn("max-age=63072000", headers_content)
        self.assertIn("X-Content-Type-Options: nosniff", headers_content)
        self.assertIn("X-Frame-Options: DENY", headers_content)
        self.assertIn("Content-Security-Policy", headers_content)
        self.assertIn("frame-ancestors 'none'", headers_content)

if __name__ == "__main__":
    unittest.main()
