"""
Plans page content generator for Sevenseas Broadband.
Synchronized with data/plans.json (Single Source of Truth).
"""
import json
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANS_FILE = os.path.join(ROOT_DIR, "data", "plans.json")

def get_content():
    plans = [
        {"id": "plan-100", "name": "Starter", "speedMbps": 100, "speedDisplay": "100 Mbps", "monthlyPrice": 499, "threeMonthPrice": 1500, "sixMonthPrice": 2500, "twelveMonthPrice": 4500, "badge": "Starter", "tagline": "Reliable unlimited connectivity for small homes and daily browsing.", "benefits": ["100 Mbps Symmetrical Speed", "True Unlimited Data (Zero FUP)", "Dual-Band Wi-Fi 6 Router Included", "₹0 Installation & Doorstep Cabling", "Stable Low-Latency Connection"]},
        {"id": "plan-200", "name": "Popular", "speedMbps": 200, "speedDisplay": "200 Mbps", "monthlyPrice": 599, "threeMonthPrice": 1800, "sixMonthPrice": 3000, "twelveMonthPrice": 5500, "badge": "Most Popular", "tagline": "The ideal high-speed sweet spot for modern families, streaming, and remote work.", "benefits": ["200 Mbps Symmetrical Speed", "True Unlimited Data (Zero FUP)", "Dual-Band Wi-Fi 6 Router Included", "₹0 Installation & Doorstep Cabling", "Optimized Zoom / Teams Peering", "Priority Neighborhood Field Support"]},
        {"id": "plan-300", "name": "Premium", "speedMbps": 300, "speedDisplay": "300 Mbps", "monthlyPrice": 699, "threeMonthPrice": 2200, "sixMonthPrice": 3500, "twelveMonthPrice": 6500, "badge": "Extreme Speed", "tagline": "Ultra-low ping and unthrottled gigabit bandwidth for 4K HDR streams and competitive gaming.", "benefits": ["300 Mbps Symmetrical Speed", "True Unlimited Data (Zero FUP)", "Dual-Band Wi-Fi 6 Router Included", "₹0 Installation & Doorstep Cabling", "Sub-5ms Direct Gaming Peering", "VIP Rapid Support Dispatch"]}
    ]
    if os.path.exists(PLANS_FILE):
        try:
            with open(PLANS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                plans = data.get("plans", plans)
        except Exception:
            pass

    return f"""
    <!-- PAGE HERO -->
    <section class="page-hero" style="background: linear-gradient(180deg, rgba(247, 248, 252, 0.8) 0%, #FFFFFF 100%); padding-top: var(--space-8); padding-bottom: var(--space-12);">
      <div class="container">
        <nav aria-label="Breadcrumb" class="breadcrumbs">
          <a href="index.html">Home</a>
          <span>/</span>
          <span aria-current="page">Broadband Plans</span>
        </nav>
        <div style="max-width: 820px;">
          <span class="subheading-badge">100% Symmetrical Optical Fiber</span>
          <h1 class="display-title" style="margin-bottom: var(--space-4); font-size: clamp(2rem, 3.5vw, 3.25rem);">
            Pure Fiber Plans Built for Modern Living
          </h1>
          <p class="lead" style="color: var(--color-muted); max-width: 680px; margin-bottom: var(--space-6);">
            Unthrottled gigabit speeds, zero buffering, and ultra-reliable connectivity for your home. Every Sevenseas plan delivers equal upload and download speeds, ₹0 installation, and a free Wi-Fi 6 router across Airoli.
          </p>
          
          <!-- Proof Points Group -->
          <div style="display: flex; gap: var(--space-3); flex-wrap: wrap;">
            <span style="display: inline-flex; align-items: center; gap: 6px; background: #FFFFFF; border: 1px solid var(--color-border); padding: 6px 14px; border-radius: var(--radius-pill); font-size: var(--text-xs); font-weight: 600; color: var(--color-navy);">
              <svg class="icon icon-xs" style="color: var(--color-emerald);"><use href="#icon-check"></use></svg> ₹0 Free Installation
            </span>
            <span style="display: inline-flex; align-items: center; gap: 6px; background: #FFFFFF; border: 1px solid var(--color-border); padding: 6px 14px; border-radius: var(--radius-pill); font-size: var(--text-xs); font-weight: 600; color: var(--color-navy);">
              <svg class="icon icon-xs" style="color: var(--color-emerald);"><use href="#icon-check"></use></svg> Free Wi-Fi 6 Router
            </span>
            <span style="display: inline-flex; align-items: center; gap: 6px; background: #FFFFFF; border: 1px solid var(--color-border); padding: 6px 14px; border-radius: var(--radius-pill); font-size: var(--text-xs); font-weight: 600; color: var(--color-navy);">
              <svg class="icon icon-xs" style="color: var(--color-emerald);"><use href="#icon-check"></use></svg> 100% Symmetrical Speeds
            </span>
            <span style="display: inline-flex; align-items: center; gap: 6px; background: #FFFFFF; border: 1px solid var(--color-border); padding: 6px 14px; border-radius: var(--radius-pill); font-size: var(--text-xs); font-weight: 600; color: var(--color-navy);">
              <svg class="icon icon-xs" style="color: var(--color-emerald);"><use href="#icon-check"></use></svg> True Unlimited (Zero FUP)
            </span>
          </div>
        </div>
      </div>
    </section>

    <!-- PLANS MAIN SECTION -->
    <section class="section" style="padding-top: var(--space-4);">
      <div class="container">
        
        <!-- Interactive Duration Tabs -->
        <div style="text-align: center; margin-bottom: var(--space-8);">
          <div class="duration-tabs-wrapper" role="tablist" aria-label="Billing Duration">
            <button class="duration-tab-btn active" data-cycle="1m" role="tab" aria-selected="true" onclick="switchBillingCycle('1m', this)">
              1 Month (Monthly)
            </button>
            <button class="duration-tab-btn" data-cycle="3m" role="tab" aria-selected="false" onclick="switchBillingCycle('3m', this)">
              3 Months <span class="duration-tab-tag">Quarterly</span>
            </button>
            <button class="duration-tab-btn" data-cycle="6m" role="tab" aria-selected="false" onclick="switchBillingCycle('6m', this)">
              6 Months <span class="duration-tab-tag orange">Save 17% · Popular</span>
            </button>
            <button class="duration-tab-btn" data-cycle="12m" role="tab" aria-selected="false" onclick="switchBillingCycle('12m', this)">
              12 Months <span class="duration-tab-tag">Save 25% · Best Value</span>
            </button>
          </div>
          <p class="text-muted" style="font-size: var(--text-xs); margin: 0;" id="billing-subtitle">
            Showing standard monthly billing. Commit longer to unlock substantial advance savings.
          </p>
        </div>

        <!-- 3 Primary Central Plan Cards -->
        <div class="custom-plans-grid" style="margin-bottom: var(--space-16);">
          
          <!-- Starter 100 Mbps -->
          <div class="plan-card-custom plan-card-starter">
            <div>
              <span class="badge badge-navy" style="margin-bottom: var(--space-3);">{plans[0]['badge']}</span>
              <div class="plan-speed-pill text-navy">{plans[0]['speedDisplay']}</div>
              <div class="plan-price-display">
                <span class="plan-price-num text-navy" id="price-plan-100">₹{plans[0]['monthlyPrice']}</span>
                <span class="plan-price-cycle" id="cycle-plan-100">/ month</span>
              </div>
              <div id="savings-plan-100" style="min-height: 22px; font-size: 0.75rem; color: var(--color-emerald-text); font-weight: 700; margin-bottom: var(--space-3);"></div>
              <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-4);">{plans[0]['tagline']}</p>
              <ul class="plan-checklist">
                <li><svg class="icon icon-sm" style="color: var(--color-navy);"><use href="#icon-check"></use></svg> <strong>100 Mbps</strong> Symmetrical Speed</li>
                <li><svg class="icon icon-sm" style="color: var(--color-emerald);"><use href="#icon-check"></use></svg> Unlimited data (No FUP throttle)</li>
                <li><svg class="icon icon-sm" style="color: var(--color-navy);"><use href="#icon-check"></use></svg> Dual-band Wi-Fi 6 router included</li>
                <li><svg class="icon icon-sm" style="color: var(--color-navy);"><use href="#icon-check"></use></svg> ₹0 Free installation &amp; wiring</li>
                <li><svg class="icon icon-sm" style="color: var(--color-navy);"><use href="#icon-check"></use></svg> 24/7 Airoli field support</li>
              </ul>
            </div>
            <a href="new-connection.html?plan=starter" id="btn-plan-100" class="btn btn-outline-navy" style="width: 100%;">Enquire Starter 100</a>
          </div>

          <!-- Popular 200 Mbps (Featured) -->
          <div class="plan-card-custom plan-card-popular">
            <span class="popular-badge-pin">Most Popular</span>
            <div>
              <span class="badge badge-orange" style="margin-bottom: var(--space-3);">{plans[1]['badge']}</span>
              <div class="plan-speed-pill text-orange">{plans[1]['speedDisplay']}</div>
              <div class="plan-price-display">
                <span class="plan-price-num text-orange" id="price-plan-200">₹{plans[1]['monthlyPrice']}</span>
                <span class="plan-price-cycle" id="cycle-plan-200">/ month</span>
              </div>
              <div id="savings-plan-200" style="min-height: 22px; font-size: 0.75rem; color: var(--color-emerald-text); font-weight: 700; margin-bottom: var(--space-3);"></div>
              <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-4);">{plans[1]['tagline']}</p>
              <ul class="plan-checklist">
                <li><svg class="icon icon-sm" style="color: var(--color-orange);"><use href="#icon-check"></use></svg> <strong>200 Mbps</strong> Symmetrical Speed</li>
                <li><svg class="icon icon-sm" style="color: var(--color-emerald);"><use href="#icon-check"></use></svg> Unlimited data (No FUP throttle)</li>
                <li><svg class="icon icon-sm" style="color: var(--color-orange);"><use href="#icon-check"></use></svg> Dual-band Wi-Fi 6 router included</li>
                <li><svg class="icon icon-sm" style="color: var(--color-orange);"><use href="#icon-check"></use></svg> ₹0 Free installation &amp; wiring</li>
                <li><svg class="icon icon-sm" style="color: var(--color-orange);"><use href="#icon-check"></use></svg> Optimized Zoom / Teams peering</li>
                <li><svg class="icon icon-sm" style="color: var(--color-orange);"><use href="#icon-check"></use></svg> Priority neighborhood support</li>
              </ul>
            </div>
            <a href="new-connection.html?plan=popular" id="btn-plan-200" class="btn btn-primary" style="width: 100%;">Enquire Popular 200</a>
          </div>

          <!-- Premium 300 Mbps -->
          <div class="plan-card-custom plan-card-premium">
            <div>
              <span class="badge badge-violet" style="margin-bottom: var(--space-3);">{plans[2]['badge']}</span>
              <div class="plan-speed-pill" style="color: var(--color-violet);">{plans[2]['speedDisplay']}</div>
              <div class="plan-price-display">
                <span class="plan-price-num" style="color: var(--color-violet);" id="price-plan-300">₹{plans[2]['monthlyPrice']}</span>
                <span class="plan-price-cycle" id="cycle-plan-300">/ month</span>
              </div>
              <div id="savings-plan-300" style="min-height: 22px; font-size: 0.75rem; color: var(--color-emerald-text); font-weight: 700; margin-bottom: var(--space-3);"></div>
              <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-4);">{plans[2]['tagline']}</p>
              <ul class="plan-checklist">
                <li><svg class="icon icon-sm" style="color: var(--color-violet);"><use href="#icon-check"></use></svg> <strong>300 Mbps</strong> Symmetrical Speed</li>
                <li><svg class="icon icon-sm" style="color: var(--color-emerald);"><use href="#icon-check"></use></svg> Unlimited data (No FUP throttle)</li>
                <li><svg class="icon icon-sm" style="color: var(--color-violet);"><use href="#icon-check"></use></svg> Dual-band Wi-Fi 6 router included</li>
                <li><svg class="icon icon-sm" style="color: var(--color-violet);"><use href="#icon-check"></use></svg> ₹0 Free installation &amp; wiring</li>
                <li><svg class="icon icon-sm" style="color: var(--color-violet);"><use href="#icon-check"></use></svg> Sub-5ms gaming latency peering</li>
                <li><svg class="icon icon-sm" style="color: var(--color-violet);"><use href="#icon-check"></use></svg> VIP Rapid support dispatch</li>
              </ul>
            </div>
            <a href="new-connection.html?plan=premium" id="btn-plan-300" class="btn btn-outline-navy" style="width: 100%; border-color: var(--color-violet); color: var(--color-violet);">Enquire Premium 300</a>
          </div>

        </div>

        <!-- THE ALL-INCLUSIVE SEVENSEAS VALUE PROMISE -->
        <div style="margin-bottom: var(--space-16);">
          <div class="section-header text-center">
            <span class="subheading-badge">Transparent Standard</span>
            <h2>Included Free With Every Plan</h2>
            <p class="lead" style="margin-left: auto; margin-right: auto; max-width: 600px;">
              No hidden security deposits. No router rental fees. No unexpected bill surprises.
            </p>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: var(--space-6);">
            
            <div class="card" style="padding: var(--space-6); background: #FFFFFF; border-radius: var(--radius-lg); border: 1px solid var(--color-border);">
              <div class="icon-box icon-box-emerald" style="margin-bottom: var(--space-4);">
                <svg class="icon"><use href="#icon-wrench"></use></svg>
              </div>
              <h4 style="color: var(--color-navy); margin-bottom: var(--space-2);">₹0 Free Installation</h4>
              <p class="text-muted" style="font-size: var(--text-xs); line-height: 1.6; margin: 0;">
                Our certified technicians handle optical fiber drop cabling, terminal termination, and doorstep Wi-Fi setup with zero labor fees.
              </p>
            </div>

            <div class="card" style="padding: var(--space-6); background: #FFFFFF; border-radius: var(--radius-lg); border: 1px solid var(--color-border);">
              <div class="icon-box icon-box-orange" style="margin-bottom: var(--space-4);">
                <svg class="icon"><use href="#icon-router"></use></svg>
              </div>
              <h4 style="color: var(--color-navy); margin-bottom: var(--space-2);">Free Wi-Fi 6 Router</h4>
              <p class="text-muted" style="font-size: var(--text-xs); line-height: 1.6; margin: 0;">
                High-gain dual-band 2.4 GHz + 5 GHz hardware capable of delivering gigabit throughput across multiple rooms simultaneously.
              </p>
            </div>

            <div class="card" style="padding: var(--space-6); background: #FFFFFF; border-radius: var(--radius-lg); border: 1px solid var(--color-border);">
              <div class="icon-box icon-box-navy" style="margin-bottom: var(--space-4);">
                <svg class="icon"><use href="#icon-network"></use></svg>
              </div>
              <h4 style="color: var(--color-navy); margin-bottom: var(--space-2);">100% Optical Glass</h4>
              <p class="text-muted" style="font-size: var(--text-xs); line-height: 1.6; margin: 0;">
                Pure 9µm silica optical glass straight to your doorstep eliminates weather corrosion, copper interference, and monsoon dropouts.
              </p>
            </div>

            <div class="card" style="padding: var(--space-6); background: #FFFFFF; border-radius: var(--radius-lg); border: 1px solid var(--color-border);">
              <div class="icon-box icon-box-emerald" style="margin-bottom: var(--space-4);">
                <svg class="icon"><use href="#icon-headset"></use></svg>
              </div>
              <h4 style="color: var(--color-navy); margin-bottom: var(--space-2);">2-Hour Airoli Field Care</h4>
              <p class="text-muted" style="font-size: var(--text-xs); line-height: 1.6; margin: 0;">
                Our field support center is based right here in Sector 3, Airoli. If you ever need on-site assistance, a technician is minutes away.
              </p>
            </div>

          </div>
        </div>

        <!-- FULL PLAN COMPARISON MATRIX -->
        <div style="margin-bottom: var(--space-16);">
          <div class="section-header text-center">
            <span class="subheading-badge">Feature Breakdown</span>
            <h2>Plan Comparison Matrix</h2>
            <p class="lead" style="margin-left: auto; margin-right: auto; max-width: 600px;">
              Compare all speed tiers side-by-side to find the perfect fit for your home.
            </p>
          </div>

          <div class="plan-matrix-wrapper table-responsive">
            <table class="plan-matrix-table">
              <thead>
                <tr>
                  <th scope="col" style="width: 34%;">Feature / Capability</th>
                  <th scope="col" style="width: 22%;">Starter (100 Mbps)</th>
                  <th scope="col" style="width: 22%; background: var(--tint-orange); color: var(--color-orange-text);">Popular (200 Mbps)</th>
                  <th scope="col" style="width: 22%;">Premium (300 Mbps)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Monthly Subscription</strong></td>
                  <td><strong>₹499</strong> / mo</td>
                  <td><strong style="color: var(--color-orange-text);">₹599</strong> / mo</td>
                  <td><strong style="color: var(--color-violet);">₹699</strong> / mo</td>
                </tr>
                <tr>
                  <td><strong>Download &amp; Upload Speed</strong></td>
                  <td>100 Mbps Symmetrical</td>
                  <td>200 Mbps Symmetrical</td>
                  <td>300 Mbps Symmetrical</td>
                </tr>
                <tr>
                  <td><strong>Data Allowance</strong></td>
                  <td><span class="plan-matrix-check"><svg class="icon icon-xs"><use href="#icon-check"></use></svg></span> Unlimited</td>
                  <td><span class="plan-matrix-check"><svg class="icon icon-xs"><use href="#icon-check"></use></svg></span> Unlimited</td>
                  <td><span class="plan-matrix-check"><svg class="icon icon-xs"><use href="#icon-check"></use></svg></span> Unlimited</td>
                </tr>
                <tr>
                  <td><strong>Wi-Fi 6 Router Hardware</strong></td>
                  <td><span class="plan-matrix-check"><svg class="icon icon-xs"><use href="#icon-check"></use></svg></span> Included Free</td>
                  <td><span class="plan-matrix-check"><svg class="icon icon-xs"><use href="#icon-check"></use></svg></span> Included Free</td>
                  <td><span class="plan-matrix-check"><svg class="icon icon-xs"><use href="#icon-check"></use></svg></span> Included Free</td>
                </tr>
                <tr>
                  <td><strong>Doorstep Fiber Installation</strong></td>
                  <td><span class="plan-matrix-check"><svg class="icon icon-xs"><use href="#icon-check"></use></svg></span> ₹0 Free</td>
                  <td><span class="plan-matrix-check"><svg class="icon icon-xs"><use href="#icon-check"></use></svg></span> ₹0 Free</td>
                  <td><span class="plan-matrix-check"><svg class="icon icon-xs"><use href="#icon-check"></use></svg></span> ₹0 Free</td>
                </tr>
                <tr>
                  <td><strong>Simultaneous Devices</strong></td>
                  <td>4 – 6 Devices</td>
                  <td>8 – 12 Devices</td>
                  <td>15+ Devices</td>
                </tr>
                <tr>
                  <td><strong>Video Streaming Quality</strong></td>
                  <td>Full HD &amp; 4K Single Screen</td>
                  <td>Multiple 4K Screens</td>
                  <td>Simultaneous 4K &amp; 8K HDR</td>
                </tr>
                <tr>
                  <td><strong>Low-Latency Gaming Peering</strong></td>
                  <td>Standard Optical Ring</td>
                  <td>Direct Peering</td>
                  <td>Sub-5ms Dedicated Peering</td>
                </tr>
                <tr>
                  <td><strong>Technical Support Response</strong></td>
                  <td>Standard 24/7 Desk</td>
                  <td>Priority Field Dispatch</td>
                  <td>VIP Dedicated Support</td>
                </tr>
                <tr>
                  <td><strong>Action</strong></td>
                  <td><a href="new-connection.html?plan=starter" class="btn btn-sm btn-outline-navy">Select Starter</a></td>
                  <td><a href="new-connection.html?plan=popular" class="btn btn-sm btn-primary">Select Popular</a></td>
                  <td><a href="new-connection.html?plan=premium" class="btn btn-sm btn-outline-navy">Select Premium</a></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- SECTION 5: LONG-TERM PLANS TABLE (CENTRAL SOURCE) -->
        <div style="margin-bottom: var(--space-16);" id="long-term">
          <div class="section-header text-center">
            <span class="subheading-badge">Commit Longer &amp; Save</span>
            <h2>Long-Term Commitment Savings</h2>
            <p class="lead" style="margin-left: auto; margin-right: auto; max-width: 600px;">
              Pay upfront for 3, 6, or 12 months to lock in significant subscription savings with free installation and router hardware.
            </p>
          </div>

          <div class="longterm-table-wrapper">
            <table class="longterm-pricing-table">
              <thead>
                <tr>
                  <th scope="col" style="width: 25%;">Duration</th>
                  <th scope="col">Starter (100 Mbps)</th>
                  <th scope="col">Popular (200 Mbps)</th>
                  <th scope="col">Premium (300 Mbps)</th>
                  <th scope="col" style="text-align: center;">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>
                    <strong>1 Month</strong>
                    <span class="text-muted" style="display: block; font-size: 0.75rem;">Standard Monthly</span>
                  </td>
                  <td><strong>₹499</strong> <span class="text-muted" style="font-size: 0.75rem;">/ mo</span></td>
                  <td><strong>₹599</strong> <span class="text-muted" style="font-size: 0.75rem;">/ mo</span></td>
                  <td><strong>₹699</strong> <span class="text-muted" style="font-size: 0.75rem;">/ mo</span></td>
                  <td style="text-align: center;"><a href="new-connection.html?duration=1m" class="btn btn-sm btn-outline-navy">Book 1M</a></td>
                </tr>
                <tr>
                  <td>
                    <strong>3 Months</strong>
                    <span class="text-muted" style="display: block; font-size: 0.75rem;">Quarterly Subscription</span>
                  </td>
                  <td><strong>₹1,500</strong> <span class="text-muted" style="font-size: 0.75rem;">(₹500/mo)</span></td>
                  <td><strong>₹1,800</strong> <span class="text-muted" style="font-size: 0.75rem;">(₹600/mo)</span></td>
                  <td><strong>₹2,200</strong> <span class="text-muted" style="font-size: 0.75rem;">(₹733/mo)</span></td>
                  <td style="text-align: center;"><a href="new-connection.html?duration=3m" class="btn btn-sm btn-outline-navy">Book 3M</a></td>
                </tr>
                <tr>
                  <td>
                    <strong>6 Months</strong>
                    <span class="badge badge-orange" style="margin-left: 8px; font-size: 0.7rem; vertical-align: middle;">Save 17%</span>
                    <span class="text-muted" style="display: block; font-size: 0.75rem;">Semi-Annual Commitment</span>
                  </td>
                  <td><strong>₹2,500</strong> <span class="text-muted" style="font-size: 0.75rem;">(₹416/mo)</span></td>
                  <td><strong>₹3,000</strong> <span class="text-muted" style="font-size: 0.75rem;">(₹500/mo)</span></td>
                  <td><strong>₹3,500</strong> <span class="text-muted" style="font-size: 0.75rem;">(₹583/mo)</span></td>
                  <td style="text-align: center;"><a href="new-connection.html?duration=6m" class="btn btn-sm btn-primary">Book 6M</a></td>
                </tr>
                <tr>
                  <td>
                    <strong>12 Months</strong>
                    <span class="badge badge-emerald" style="margin-left: 8px; font-size: 0.7rem; vertical-align: middle;">Save 25% · Best Value</span>
                    <span class="text-muted" style="display: block; font-size: 0.75rem;">Annual Commitment</span>
                  </td>
                  <td><strong>₹4,500</strong> <span class="text-muted" style="font-size: 0.75rem;">(₹375/mo)</span></td>
                  <td><strong>₹5,500</strong> <span class="text-muted" style="font-size: 0.75rem;">(₹458/mo)</span></td>
                  <td><strong>₹6,500</strong> <span class="text-muted" style="font-size: 0.75rem;">(₹541/mo)</span></td>
                  <td style="text-align: center;"><a href="new-connection.html?duration=12m" class="btn btn-sm btn-primary">Book 12M</a></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- OTT ADDON BUNDLES -->
        <div style="margin-bottom: var(--space-16); background-color: var(--color-white); border: 1px solid var(--color-border); border-radius: var(--radius-xl); padding: clamp(1.5rem, 3.5vw, 2.5rem); box-shadow: 0 4px 20px rgba(15, 27, 45, 0.04);" id="ott-addons">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: var(--space-4); margin-bottom: var(--space-6);">
            <div>
              <span class="badge badge-orange" style="margin-bottom: var(--space-2);">Entertainment Super-Addon</span>
              <h3 style="margin: 0; color: var(--color-navy); font-size: clamp(1.25rem, 2vw, 1.6rem);">Add 4 Top OTT Apps for just ₹149 / month</h3>
              <p class="text-muted" style="font-size: var(--text-sm); margin-top: 6px; margin-bottom: 0;">Stream movies, live sports, and web series on your Smart TV, smartphone, or laptop on a single consolidated bill.</p>
            </div>
            <a href="new-connection.html?addon=ott" class="btn btn-outline-orange">Add OTT to Your Plan</a>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: var(--space-4);">
            <div style="background: var(--tint-navy); padding: var(--space-5); border-radius: var(--radius-md); text-align: center; border: 1px solid rgba(30, 48, 80, 0.08);">
              <strong style="color: var(--color-navy); display: block; font-size: var(--text-base); margin-bottom: 4px;">Disney+ Hotstar</strong>
              <span class="text-muted" style="font-size: var(--text-xs);">Super Plan (Live Sports &amp; 4K Movies)</span>
            </div>
            <div style="background: var(--tint-navy); padding: var(--space-5); border-radius: var(--radius-md); text-align: center; border: 1px solid rgba(30, 48, 80, 0.08);">
              <strong style="color: var(--color-navy); display: block; font-size: var(--text-base); margin-bottom: 4px;">Amazon Prime Video</strong>
              <span class="text-muted" style="font-size: var(--text-xs);">HD Streaming &amp; Fast Deliveries</span>
            </div>
            <div style="background: var(--tint-navy); padding: var(--space-5); border-radius: var(--radius-md); text-align: center; border: 1px solid rgba(30, 48, 80, 0.08);">
              <strong style="color: var(--color-navy); display: block; font-size: var(--text-base); margin-bottom: 4px;">SonyLIV Premium</strong>
              <span class="text-muted" style="font-size: var(--text-xs);">UEFA Champions League, WWE, Originals</span>
            </div>
            <div style="background: var(--tint-navy); padding: var(--space-5); border-radius: var(--radius-md); text-align: center; border: 1px solid rgba(30, 48, 80, 0.08);">
              <strong style="color: var(--color-navy); display: block; font-size: var(--text-base); margin-bottom: 4px;">Zee5 Premium</strong>
              <span class="text-muted" style="font-size: var(--text-xs);">Blockbuster Marathi &amp; Hindi Cinema</span>
            </div>
          </div>
        </div>

        <!-- PLANS FREQUENTLY ASKED QUESTIONS -->
        <div style="margin-bottom: var(--space-12);">
          <div class="section-header text-center">
            <span class="subheading-badge">Got Questions?</span>
            <h2>Broadband Plans FAQ</h2>
          </div>

          <div style="max-width: 760px; margin: 0 auto; display: flex; flex-direction: column; gap: var(--space-4);">
            <div class="card" style="padding: var(--space-5); background: #FFFFFF; border-radius: var(--radius-md); border: 1px solid var(--color-border);">
              <h4 style="color: var(--color-navy); margin-bottom: var(--space-2); font-size: var(--text-base);">Is the Wi-Fi router truly free?</h4>
              <p class="text-muted" style="font-size: var(--text-sm); margin: 0; line-height: 1.6;">
                Yes! A dual-band gigabit Wi-Fi 6 router is provided with ₹0 security deposit and zero rental fees on all our 3, 6, and 12-month advance subscription plans.
              </p>
            </div>
            <div class="card" style="padding: var(--space-5); background: #FFFFFF; border-radius: var(--radius-md); border: 1px solid var(--color-border);">
              <h4 style="color: var(--color-navy); margin-bottom: var(--space-2); font-size: var(--text-base);">What does symmetrical speed mean?</h4>
              <p class="text-muted" style="font-size: var(--text-sm); margin: 0; line-height: 1.6;">
                Unlike legacy broadband providers that offer high download speeds but severely choke upload speeds to 10–20 Mbps, Sevenseas provides equal upload and download bandwidth (e.g. 200 Mbps down AND 200 Mbps up). This ensures smooth Zoom calls, instant cloud file uploads, and lag-free gaming broadcasts.
              </p>
            </div>
            <div class="card" style="padding: var(--space-5); background: #FFFFFF; border-radius: var(--radius-md); border: 1px solid var(--color-border);">
              <h4 style="color: var(--color-navy); margin-bottom: var(--space-2); font-size: var(--text-base);">Can I upgrade my speed tier midway through my plan?</h4>
              <p class="text-muted" style="font-size: var(--text-sm); margin: 0; line-height: 1.6;">
                Absolutely. You can upgrade from 100 Mbps to 200 or 300 Mbps at any point. Your remaining balance is pro-rated toward the upgraded speed tier with zero penalties.
              </p>
            </div>
            <div class="card" style="padding: var(--space-5); background: #FFFFFF; border-radius: var(--radius-md); border: 1px solid var(--color-border);">
              <h4 style="color: var(--color-navy); margin-bottom: var(--space-2); font-size: var(--text-base);">How quickly can I get installed in Airoli?</h4>
              <p class="text-muted" style="font-size: var(--text-sm); margin: 0; line-height: 1.6;">
                Because our primary fiber distribution rings and technician hub are situated locally in Sector 3, Airoli, standard doorstep installation and live activation are typically completed within 4 to 8 hours of your booking.
              </p>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- SECTION: BESPOKE PURPLE RIBBON CTA -->
    <section class="purple-cta-section" id="ready-cta" aria-labelledby="cta-heading" style="border-top: 1px solid var(--color-border);">
      <img src="public/assets/images/cta-ribbon-left.svg" alt="" class="purple-cta-ribbon purple-cta-ribbon-left" width="420" height="420" aria-hidden="true" loading="lazy">
      <img src="public/assets/images/cta-ribbon-right.svg" alt="" class="purple-cta-ribbon purple-cta-ribbon-right" width="420" height="420" aria-hidden="true" loading="lazy">

      <div class="purple-cta-container">
        <div class="purple-cta-pill">
          <svg class="purple-cta-pill-icon" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <circle cx="8" cy="8" r="6" stroke="#7C3AED" stroke-width="1.75"/>
            <circle cx="8" cy="8" r="2.2" fill="#7C3AED"/>
          </svg>
          <span>Reliable Fiber Broadband</span>
        </div>

        <h2 id="cta-heading" class="purple-cta-heading">
          Ready for a Better<br>Internet Experience?
        </h2>

        <p class="purple-cta-desc">
          Get connected with Sevenseas Broadband today. Pure optical fiber connectivity delivered straight to your door across Airoli.
        </p>

        <div class="purple-cta-buttons">
          <a href="tel:9664985535" class="purple-cta-btn purple-cta-btn-call" aria-label="Call Sevenseas Broadband customer care at 9664985535">
            <svg class="icon icon-sm" style="width: 18px; height: 18px;" aria-hidden="true"><use href="#icon-phone"></use></svg>
            <span>Call Now</span>
          </a>
          <a href="https://wa.me/919664985535?text=Hi%20Sevenseas%20Broadband,%20I%20am%20interested%20in%20a%20new%20connection" target="_blank" rel="noopener noreferrer" class="purple-cta-btn purple-cta-btn-whatsapp" aria-label="Chat with Sevenseas Broadband on WhatsApp">
            <svg class="icon icon-sm" style="width: 18px; height: 18px;" aria-hidden="true"><use href="#icon-whatsapp"></use></svg>
            <span>WhatsApp Us</span>
          </a>
        </div>
      </div>
    </section>

    <!-- Interactive Client Script for Duration Tabs -->
    <script>
      const PRICING_DATA = {{
        "1m": {{
          subtitle: "Showing standard monthly rates. Commit longer to unlock substantial advance discounts.",
          p100: {{ price: "₹499", cycle: "/ month", savings: "" }},
          p200: {{ price: "₹599", cycle: "/ month", savings: "" }},
          p300: {{ price: "₹699", cycle: "/ month", savings: "" }}
        }},
        "3m": {{
          subtitle: "Quarterly commitment: ₹1,500 for 100 Mbps · ₹1,800 for 200 Mbps · ₹2,200 for 300 Mbps.",
          p100: {{ price: "₹1,500", cycle: "/ 3 months", savings: "Effective ₹500 / month" }},
          p200: {{ price: "₹1,800", cycle: "/ 3 months", savings: "Effective ₹600 / month" }},
          p300: {{ price: "₹2,200", cycle: "/ 3 months", savings: "Effective ₹733 / month" }}
        }},
        "6m": {{
          subtitle: "Semi-annual commitment: Save 17% on total subscription with free installation.",
          p100: {{ price: "₹2,500", cycle: "/ 6 months", savings: "Effective ₹416 / mo · Save 17%" }},
          p200: {{ price: "₹3,000", cycle: "/ 6 months", savings: "Effective ₹500 / mo · Save 17%" }},
          p300: {{ price: "₹3,500", cycle: "/ 6 months", savings: "Effective ₹583 / mo · Save 17%" }}
        }},
        "12m": {{
          subtitle: "Annual commitment: Save 25% on total subscription with guaranteed price lock.",
          p100: {{ price: "₹4,500", cycle: "/ year", savings: "Effective ₹375 / mo · Save 25%" }},
          p200: {{ price: "₹5,500", cycle: "/ year", savings: "Effective ₹458 / mo · Save 24%" }},
          p300: {{ price: "₹6,500", cycle: "/ year", savings: "Effective ₹541 / mo · Save 23%" }}
        }}
      }};

      function switchBillingCycle(cycle, btn) {{
        document.querySelectorAll('.duration-tab-btn').forEach(b => {{
          b.classList.remove('active');
          b.setAttribute('aria-selected', 'false');
        }});
        btn.classList.add('active');
        btn.setAttribute('aria-selected', 'true');

        const data = PRICING_DATA[cycle];
        if (!data) return;

        document.getElementById('billing-subtitle').textContent = data.subtitle;

        // Plan 100
        document.getElementById('price-plan-100').textContent = data.p100.price;
        document.getElementById('cycle-plan-100').textContent = data.p100.cycle;
        document.getElementById('savings-plan-100').textContent = data.p100.savings;
        document.getElementById('btn-plan-100').href = 'new-connection.html?plan=starter&duration=' + cycle;

        // Plan 200
        document.getElementById('price-plan-200').textContent = data.p200.price;
        document.getElementById('cycle-plan-200').textContent = data.p200.cycle;
        document.getElementById('savings-plan-200').textContent = data.p200.savings;
        document.getElementById('btn-plan-200').href = 'new-connection.html?plan=popular&duration=' + cycle;

        // Plan 300
        document.getElementById('price-plan-300').textContent = data.p300.price;
        document.getElementById('cycle-plan-300').textContent = data.p300.cycle;
        document.getElementById('savings-plan-300').textContent = data.p300.savings;
        document.getElementById('btn-plan-300').href = 'new-connection.html?plan=premium&duration=' + cycle;
      }}
    </script>
    """
