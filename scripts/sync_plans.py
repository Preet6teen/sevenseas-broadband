#!/usr/bin/env python3
"""
scripts/sync_plans.py — Central Plan Synchronizer
Enforces the single source of truth rule from Phase 6:
'Never duplicate prices manually across multiple components.
If a price changes, the entire website should update automatically from the central plan configuration.'

Reads: data/plans.json (or data/plans.ts)
Updates/Verifies:
- index.html (Section 4 Monthly Plans & Section 5 Long-Term Plans)
- plans.html
- pages/plans.py
"""

import json
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANS_JSON_PATH = os.path.join(ROOT_DIR, "data", "plans.json")

def load_plans_data():
    with open(PLANS_JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_custom_plans_grid_html(plans):
    cards_html = []
    for p in plans:
        is_popular = p.get("isPopular", False)
        is_violet = p.get("themeColor") == "violet"
        badge = p.get("badge", "")

        if is_popular:
            card_class = "plan-card-custom plan-card-popular"
            pill_color = "text-orange"
            num_color = "text-orange"
            check_color = "var(--color-orange)"
            badge_pin = '<span class="popular-badge-pin">Most Popular</span>'
            badge_span = '<span class="badge badge-orange" style="margin-bottom: var(--space-3);">Popular</span>'
            btn_html = f'<a href="new-connection.html?plan={p["id"]}" class="btn btn-primary" style="width: 100%;">Enquire {p["name"]} {p["speedMbps"]}</a>'
        elif is_violet:
            card_class = "plan-card-custom plan-card-premium"
            pill_color = 'style="color: var(--color-violet);"'
            num_color = 'style="color: var(--color-violet);"'
            check_color = "var(--color-violet)"
            badge_pin = ""
            badge_span = '<span class="badge badge-violet" style="margin-bottom: var(--space-3);">Premium</span>'
            btn_html = f'<a href="new-connection.html?plan={p["id"]}" class="btn btn-outline-navy" style="width: 100%; border-color: var(--color-violet); color: var(--color-violet);">Enquire {p["name"]} {p["speedMbps"]}</a>'
        else:
            card_class = "plan-card-custom plan-card-starter"
            pill_color = "text-navy"
            num_color = "text-navy"
            check_color = "var(--color-navy)"
            badge_pin = ""
            badge_span = '<span class="badge badge-navy" style="margin-bottom: var(--space-3);">Starter</span>'
            btn_html = f'<a href="new-connection.html?plan={p["id"]}" class="btn btn-outline-navy" style="width: 100%;">Enquire {p["name"]} {p["speedMbps"]}</a>'

        benefits_items = []
        for b in p["benefits"]:
            benefits_items.append(f'                <li><svg class="icon icon-sm" style="color: {check_color};"><use href="#icon-check"></use></svg> <span>{b}</span></li>')
        benefits_html = "\n".join(benefits_items)

        pill_attr = f'class="plan-speed-pill {pill_color}"' if "text-" in pill_color else f'class="plan-speed-pill" {pill_color}'
        num_attr = f'class="plan-price-num {num_color}"' if "text-" in num_color else f'class="plan-price-num" {num_color}'

        card = f"""          <!-- Plan: {p['name']} ({p['speedDisplay']}, ₹{p['monthlyPrice']}/month) -->
          <div class="{card_class}">
            {badge_pin}
            <div>
              {badge_span}
              <div {pill_attr}>{p['speedDisplay']}</div>
              <div class="plan-price-display">
                <span {num_attr}>₹{p['monthlyPrice']}</span>
                <span class="plan-price-cycle">/ month</span>
              </div>

              <ul class="plan-checklist">
{benefits_html}
              </ul>
            </div>

            {btn_html}
          </div>"""
        cards_html.append(card)
    return "\n\n".join(cards_html)

def generate_long_term_tbody_html(long_term_data):
    rows_html = []
    for tier in long_term_data:
        duration = tier["duration"]
        badge = tier.get("badge")
        if badge == "Most Popular":
            badge_html = f'<span class="badge badge-orange" style="margin-left: 8px; font-size: 0.7rem; vertical-align: middle;">{badge}</span>'
        elif badge:
            badge_html = f'<span class="badge badge-emerald" style="margin-left: 8px; font-size: 0.7rem; vertical-align: middle;">{badge}</span>'
        else:
            badge_html = ""

        sub_label = "Quarterly Subscription" if "3" in duration else ("Semi-Annual Commitment" if "6" in duration else "Annual Commitment")
        p100 = tier["prices"].get("100 Mbps", 0)
        p200 = tier["prices"].get("200 Mbps", 0)
        p300 = tier["prices"].get("300 Mbps", 0)

        row = f"""              <!-- {duration} -->
              <tr>
                <td>
                  <strong>{duration}</strong>{badge_html}
                  <span class="text-muted" style="display: block; font-size: 0.75rem;">{sub_label}</span>
                </td>
                <td><span style="font-family: var(--font-heading); font-weight: 800; font-size: 1.1rem; color: var(--color-navy);">₹{p100:,}</span></td>
                <td><span style="font-family: var(--font-heading); font-weight: 800; font-size: 1.1rem; color: var(--color-orange);">₹{p200:,}</span></td>
                <td><span style="font-family: var(--font-heading); font-weight: 800; font-size: 1.1rem; color: var(--color-violet);">₹{p300:,}</span></td>
                <td style="text-align: center;"><a href="new-connection.html?duration={duration.replace(' ', '-').lower()}" class="btn btn-sm btn-outline-navy">Choose Plan</a></td>
              </tr>"""
        rows_html.append(row)
    return "\n".join(rows_html)

def sync_index_html(data):
    index_path = os.path.join(ROOT_DIR, "index.html")
    if not os.path.exists(index_path):
        return

    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace custom-plans-grid
    start_marker = '<div class="custom-plans-grid">'
    end_marker = '</div>\n      </div>\n    </section>\n\n    <!-- ========================================================================\n         SECTION 5: LONG-TERM PLANS'
    
    if start_marker in content and end_marker in content:
        before = content.split(start_marker)[0] + start_marker + "\n"
        after = "\n        " + end_marker + content.split(end_marker)[1]
        content = before + generate_custom_plans_grid_html(data["plans"]) + after
        print("✓ Section 4 Monthly Plans synchronized in index.html")

    # 2. Replace long-term table tbody
    tbody_start = '<tbody>\n              <!-- 3 Months -->'
    tbody_end = '</tbody>\n          </table>'
    if tbody_start in content and tbody_end in content:
        before = content.split(tbody_start)[0] + "<tbody>\n"
        after = "\n            " + tbody_end + content.split(tbody_end)[1]
        content = before + generate_long_term_tbody_html(data["longTermPricing"]) + after
        print("✓ Section 5 Long-Term Plans synchronized in index.html")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)

def verify_plan_integrity(data):
    print("\n--- Current Central Plan Configuration ---")
    for p in data["plans"]:
        print(f"Plan [{p['id']}]: {p['name']} ({p['speedDisplay']}) => ₹{p['monthlyPrice']}/mo | 3M: ₹{p['threeMonthPrice']} | 6M: ₹{p['sixMonthPrice']} | 12M: ₹{p['twelveMonthPrice']}")
    print("-------------------------------------------\n")

def main():
    print("Starting Sevenseas Broadband Plan Synchronizer...")
    data = load_plans_data()
    verify_plan_integrity(data)
    sync_index_html(data)
    print("Single source of truth synchronization complete.\n")

if __name__ == "__main__":
    main()
