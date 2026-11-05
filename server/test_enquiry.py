#!/usr/bin/env python3
"""
Unit test suite for Sevenseas Broadband Enquiry Server logic
Tests:
1. Strict Mobile Regex (^[6-9]\\d{9}$)
2. Full Name validation & escaping
3. Honeypot detection
4. Rate Limiting enforcement
5. SQLite lead storage & JSON serialization
"""

import os
import sys
import json
import sqlite3
import unittest

# Import server components directly
sys.path.insert(0, os.path.dirname(__file__))
from app import validate_enquiry, save_lead, is_rate_limited, RATE_LIMIT_MAP, DB_PATH, LEADS_JSON_PATH

class TestEnquiryValidation(unittest.TestCase):
    def setUp(self):
        RATE_LIMIT_MAP.clear()

    def test_valid_enquiry(self):
        valid_data = {
            "fullName": "Amit Verma",
            "mobileNumber": "9820012345",
            "areaLocality": "Sector 3, Airoli",
            "societyBuilding": "Dharmjeevan CHS",
            "preferredPlan": "Popular 200 Mbps",
            "consent": True,
            "b_website": ""
        }
        errors, cleaned = validate_enquiry(valid_data)
        self.assertEqual(len(errors), 0, f"Expected no errors, got: {errors}")
        self.assertEqual(cleaned["mobileNumber"], "9820012345")
        self.assertEqual(cleaned["fullName"], "Amit Verma")

    def test_invalid_mobile_numbers(self):
        invalid_numbers = [
            "1234567890",   # Starts with 1
            "5555555555",   # Starts with 5
            "98200",        # Less than 10 digits
            "98200123456",  # More than 10 digits
            "98200abcde",   # Contains letters
            "+919820012345",# Raw string with +91 (needs 10 digits)
        ]
        for num in invalid_numbers:
            data = {
                "fullName": "Test User",
                "mobileNumber": num,
                "areaLocality": "Airoli",
                "consent": True,
                "b_website": ""
            }
            errors, _ = validate_enquiry(data)
            self.assertTrue(
                any("Indian mobile number" in err for err in errors),
                f"Number {num} was expected to fail validation, but passed."
            )

    def test_valid_mobile_prefixes(self):
        for prefix in ["6", "7", "8", "9"]:
            num = prefix + "123456789"
            data = {
                "fullName": "Valid User",
                "mobileNumber": num,
                "areaLocality": "Airoli",
                "consent": True,
                "b_website": ""
            }
            errors, cleaned = validate_enquiry(data)
            self.assertEqual(len(errors), 0, f"Prefix {prefix} should be valid, errors: {errors}")
            self.assertEqual(cleaned["mobileNumber"], num)

    def test_honeypot_rejection(self):
        bot_data = {
            "fullName": "Bot Spammer",
            "mobileNumber": "9820012345",
            "areaLocality": "Airoli",
            "consent": True,
            "b_website": "http://spamsite.com"
        }
        errors, _ = validate_enquiry(bot_data)
        self.assertTrue(any("bot" in err.lower() for err in errors), "Honeypot should reject submission.")

    def test_consent_required(self):
        data = {
            "fullName": "No Consent",
            "mobileNumber": "9820012345",
            "areaLocality": "Airoli",
            "consent": False,
            "b_website": ""
        }
        errors, _ = validate_enquiry(data)
        self.assertTrue(any("consent" in err.lower() or "authorize" in err.lower() for err in errors))

    def test_rate_limiting(self):
        test_ip = "192.168.1.100"
        # First 5 requests should pass
        for i in range(5):
            self.assertFalse(is_rate_limited(test_ip), f"Request {i+1} should not be rate-limited.")
        # 6th request must be blocked
        self.assertTrue(is_rate_limited(test_ip), "6th request should be rate-limited.")

    def test_lead_storage_sqlite_and_json(self):
        lead_data = {
            "fullName": "Priya Sharma",
            "mobileNumber": "9664985535",
            "areaLocality": "Airoli Sector 4",
            "societyBuilding": "Galaxy Heights",
            "preferredPlan": "Starter 100 Mbps"
        }
        lead_id = save_lead(lead_data, "127.0.0.1")
        self.assertTrue(lead_id.startswith("SSB-"))

        # Verify in SQLite DB
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT full_name, mobile_number, area_locality, preferred_plan FROM leads WHERE id = ?", (lead_id,))
        row = c.fetchone()
        conn.close()

        self.assertIsNotNone(row, "Lead should exist in SQLite database.")
        self.assertEqual(row[0], "Priya Sharma")
        self.assertEqual(row[1], "9664985535")
        self.assertEqual(row[2], "Airoli Sector 4")

        # Verify in JSON backup file
        self.assertTrue(os.path.exists(LEADS_JSON_PATH))
        with open(LEADS_JSON_PATH, "r", encoding="utf-8") as f:
            leads = json.load(f)
        matching = [l for l in leads if l["id"] == lead_id]
        self.assertEqual(len(matching), 1, "Lead must be saved in JSON file.")

if __name__ == "__main__":
    unittest.main()
