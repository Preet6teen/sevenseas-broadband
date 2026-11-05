#!/usr/bin/env python3
"""
generate_site.py — Generates all 16 pages of the Sevenseas Broadband website.
"""

import os

pages_data = {}

def add_page(filename, title, description, active_key, content, extra_head=""):
    pages_data[filename] = {
        "title": title,
        "description": description,
        "active_key": active_key,
        "content": content,
        "extra_head": extra_head
    }

# Read common template from build_pages.py
with open("build_pages.py", "r") as f:
    code = f.read()

# We can import COMMON_HEAD and COMMON_FOOTER from build_pages
import build_pages
COMMON_HEAD = build_pages.COMMON_HEAD
COMMON_FOOTER = build_pages.COMMON_FOOTER

print("Imported base templates.")
