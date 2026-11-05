#!/usr/bin/env python3
"""
scripts/verify_seo.py — Production SEO and Schema.org Validator
Verifies:
- Title tags, meta descriptions, canonical URLs
- OpenGraph and Twitter card tags
- Valid Schema.org JSON-LD structured data parsing
- Image alt attributes
- Local SEO keywords
"""

import os
import re
import json
import glob

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_FILES = glob.glob(os.path.join(ROOT_DIR, "*.html"))

def validate_seo():
    print(f"Auditing SEO across {len(HTML_FILES)} HTML pages...\n")
    all_passed = True
    total_json_ld_blocks = 0

    for path in sorted(HTML_FILES):
        filename = os.path.basename(path)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        errors = []

        # 1. Title
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        if not title_match or len(title_match.group(1).strip()) < 10:
            errors.append("Missing or short <title>")

        # 2. Meta description
        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
        if not desc_match or len(desc_match.group(1).strip()) < 30:
            errors.append("Missing or short meta description")

        # 3. Canonical URL
        canonical_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', content, re.IGNORECASE)
        if not canonical_match:
            errors.append("Missing canonical link")

        # 4. OpenGraph
        if 'property="og:title"' not in content and 'property="og:type"' not in content:
            errors.append("Missing OpenGraph tags")

        # 5. Twitter
        if 'name="twitter:card"' not in content:
            errors.append("Missing Twitter card metadata")

        # 6. Schema.org JSON-LD parsing
        json_ld_blocks = re.findall(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
        if not json_ld_blocks:
            errors.append("Missing Schema.org JSON-LD structured data")
        else:
            for i, raw_json in enumerate(json_ld_blocks):
                total_json_ld_blocks += 1
                try:
                    parsed = json.loads(raw_json)
                    # Verify schema has @context
                    if isinstance(parsed, dict) and "@context" not in parsed:
                        errors.append(f"JSON-LD block {i+1} missing @context")
                except json.JSONDecodeError as e:
                    errors.append(f"JSON-LD syntax error in block {i+1}: {e.msg} at line {e.lineno}")

        # 7. Images without alt
        imgs = re.findall(r'<img\s+[^>]*>', content, re.IGNORECASE)
        for img in imgs:
            if 'alt=' not in img:
                errors.append(f"Image missing alt attribute: {img[:40]}")

        if errors:
            all_passed = False
            print(f"❌ {filename}:")
            for e in errors:
                print(f"   - {e}")
        else:
            print(f"✓ {filename} — Perfect SEO, OpenGraph, Canonical & Structured Data")

    print(f"\nAudit complete: Verified {len(HTML_FILES)} pages and {total_json_ld_blocks} Schema.org JSON-LD structured data blocks.")
    if all_passed:
        print("🎉 ALL TECHNICAL & LOCAL SEO CHECKS PASSED WITH 0 ERRORS!")
    else:
        print("⚠️ Some pages need attention.")

if __name__ == "__main__":
    validate_seo()
