#!/usr/bin/env python3
"""
generate_all_pages.py
Creates all 16 pages for Sevenseas Broadband with rich, production-grade markup.
"""

import os
from build_pages import COMMON_HEAD, COMMON_FOOTER

def render_page(title, description, active_key, content, extra_head="", filename="index.html"):
    active_map = {
        "home": "",
        "plans": "",
        "fiber": "",
        "residential": "",
        "business": "",
        "coverage": "",
        "about": "",
        "more": ""
    }
    if active_key in active_map:
        active_map[active_key] = "active"

    # Derive human readable page name for Breadcrumb
    page_name = filename.replace(".html", "").replace("-", " ").title()
    if filename == "index.html":
        page_name = "Home"

    header = COMMON_HEAD.format(
        title=title,
        description=description,
        filename=filename,
        page_name=page_name,
        active_home=active_map["home"],
        active_plans=active_map["plans"],
        active_fiber=active_map["fiber"],
        active_residential=active_map["residential"],
        active_business=active_map["business"],
        active_coverage=active_map["coverage"],
        active_about=active_map["about"],
        active_more=active_map["more"],
        extra_head=extra_head
    )
    return header + content + COMMON_FOOTER

print("Renderer ready.")
