"""
Future-ready pages generators for Sevenseas Broadband:
- business.html
- installation.html
- support.html
- localities.html
"""

def get_business_content():
    return """
    <!-- PAGE HERO -->
    <section class="page-hero">
      <div class="container">
        <nav aria-label="Breadcrumb" class="breadcrumbs">
          <a href="index.html">Home</a>
          <span>/</span>
          <span aria-current="page">Business Broadband</span>
        </nav>
        <div style="max-width: 760px;">
          <span class="subheading-badge">Enterprise &amp; Commercial</span>
          <h1 class="display-title" style="margin-bottom: var(--space-4);">
            Enterprise Dedicated Internet Access &amp; Leased Lines
          </h1>
          <p class="lead">
            Mission-critical connectivity for growing enterprises, creative studios, co-working spaces, and corporate offices with 99.95% guaranteed uptime SLA and 1:1 unshared CIR bandwidth.
          </p>
        </div>
      </div>
    </section>

    <!-- ENTERPRISE FEATURES -->
    <section class="section">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1fr; gap: var(--space-8); align-items: center;" class="editorial-split-grid">
          <div>
            <span class="subheading-badge">1:1 Unshared CIR</span>
            <h2>Dedicated Optical Bandwidth for Seamless Business Operations</h2>
            <p style="font-size: var(--text-base); line-height: var(--leading-relaxed); color: var(--color-ink); margin-bottom: var(--space-4);">
              Unlike residential connections where bandwidth is aggregated across a neighborhood cluster, <strong>Sevenseas Business Leased Lines</strong> provide dedicated, symmetrical Committed Information Rate (CIR) fiber straight to your server room or office switch.
            </p>
            <p style="font-size: var(--text-base); line-height: var(--leading-relaxed); color: var(--color-ink); margin-bottom: var(--space-4);">
              Whether your team hosts on-premise application servers, executes continuous cloud video edits, or operates high-frequency financial trading algorithms, our network delivers uncompromising throughput.
            </p>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4); margin-bottom: var(--space-6);">
              <div class="card" style="padding: var(--space-4);">
                <strong style="color: var(--color-navy); font-size: var(--text-sm); display: block;">99.95% SLA Guarantee</strong>
                <span class="text-muted" style="font-size: var(--text-xs);">Financially backed service level agreement with 2-hour MTTR.</span>
              </div>
              <div class="card" style="padding: var(--space-4);">
                <strong style="color: var(--color-orange-text); font-size: var(--text-sm); display: block;">Static Public IPv4/IPv6</strong>
                <span class="text-muted" style="font-size: var(--text-xs);">Clean IP allocations for hosting VPNs, firewalls, and mail servers.</span>
              </div>
            </div>

            <div style="display: flex; gap: var(--space-3); flex-wrap: wrap;">
              <a href="#business-quote" class="btn btn-primary">Request Enterprise Quote</a>
              <a href="tel:02268924000" class="btn btn-outline-navy">Call Corporate Desk: 022-6892-4000</a>
            </div>
          </div>

          <div>
            <picture>
              <source srcset="public/assets/images/remote-work.avif" type="image/avif">
              <img src="public/assets/images/remote-work.jpg" alt="Commercial office team working with high-speed internet" style="width: 100%; height: auto; border-radius: var(--radius-lg); box-shadow: var(--shadow-lg); display: block;" loading="lazy">
            </picture>
          </div>
        </div>
      </div>
    </section>

    <!-- BUSINESS TIERS -->
    <section class="section section-alt">
      <div class="container">
        <div class="section-header text-center">
          <span class="subheading-badge">Business Plans</span>
          <h2>Commercial Fiber Tiers</h2>
          <p class="lead" style="margin-left: auto; margin-right: auto;">Scalable throughput with dedicated optical transceivers and enterprise firewall support.</p>
        </div>

        <div class="pricing-grid">
          
          <div class="fiber-card">
            <span class="badge badge-navy" style="margin-bottom: var(--space-3);">Small Office / Studio</span>
            <h3 style="margin-bottom: var(--space-1);">Business Pro 300</h3>
            <p class="text-muted" style="font-size: var(--text-sm); margin-bottom: var(--space-4);">For startups, architectural agencies, and retail offices up to 15 workstations.</p>
            <div style="margin-bottom: var(--space-4);">
              <span class="price-value" style="font-size: var(--text-4xl); color: var(--color-navy);">₹1,499</span>
              <span class="price-unit">/ month</span>
            </div>
            <ul class="feature-list">
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> 300 Mbps Symmetrical CIR</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> 1 Static IPv4 Address Included</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> Commercial Gigabit Gateway</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> 4-Hour Resolution SLA</li>
            </ul>
            <a href="#business-quote" class="btn btn-outline-navy" style="width: 100%;">Inquire Pro 300</a>
          </div>

          <div class="fiber-card featured">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-3);">
              <span class="badge badge-orange">Enterprise Core</span>
              <span class="badge badge-emerald" style="font-size: 0.7rem;">99.95% SLA</span>
            </div>
            <h3 style="margin-bottom: var(--space-1); color: var(--color-navy);">Enterprise 1 Gbps</h3>
            <p class="text-muted" style="font-size: var(--text-sm); margin-bottom: var(--space-4);">For corporate headquarters, IT development offices, and co-working floors.</p>
            <div style="margin-bottom: var(--space-4);">
              <span class="price-value" style="font-size: var(--text-4xl); color: var(--color-orange);">₹3,999</span>
              <span class="price-unit">/ month</span>
            </div>
            <ul class="feature-list">
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> 1,000 Mbps (1 Gbps) Dedicated</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> 2 Static IPv4 Addresses</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> Dual-Path Redundant Fiber Ring</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> Dedicated Relationship Manager</li>
            </ul>
            <a href="#business-quote" class="btn btn-primary" style="width: 100%;">Inquire 1 Gbps Core</a>
          </div>

          <div class="fiber-card">
            <span class="badge badge-violet" style="margin-bottom: var(--space-3);">Custom Carrier DIA</span>
            <h3 style="margin-bottom: var(--space-1);">Dedicated Leased Line</h3>
            <p class="text-muted" style="font-size: var(--text-sm); margin-bottom: var(--space-4);">Custom optical dark fiber or managed multi-gigabit connections up to 10 Gbps.</p>
            <div style="margin-bottom: var(--space-4);">
              <span class="price-value" style="font-size: var(--text-4xl); color: var(--color-navy);">Custom</span>
              <span class="price-unit">/ SLA Contract</span>
            </div>
            <ul class="feature-list">
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> 1 Gbps to 10 Gbps Custom Pipe</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> BGP Peering &amp; ASN Routing</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> 24/7 Dedicated NOC Engineer</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> Sub-2 Hour Hardware Replacement</li>
            </ul>
            <a href="#business-quote" class="btn btn-outline-navy" style="width: 100%;">Contact Enterprise Sales</a>
          </div>

        </div>
      </div>
    </section>

    <!-- INQUIRY FORM -->
    <section class="section" id="business-quote">
      <div class="container" style="max-width: 680px;">
        <div class="card" style="padding: var(--space-8); box-shadow: var(--shadow-md);">
          <h3 style="color: var(--color-navy); margin-bottom: var(--space-2); text-align: center;">Request Corporate Feasibility &amp; Quote</h3>
          <p class="text-muted" style="font-size: var(--text-sm); text-align: center; margin-bottom: var(--space-6);">An enterprise solution architect will review your commercial building feasibility and share a custom proposal.</p>

          <form data-validate data-ajax="true">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4);">
              <div class="form-group">
                <label class="form-label" for="bContactName">Contact Person</label>
                <input type="text" id="bContactName" class="form-input" placeholder="e.g. Anand Kulkarni" required />
              </div>
              <div class="form-group">
                <label class="form-label" for="bCompany">Company Name</label>
                <input type="text" id="bCompany" class="form-input" placeholder="e.g. Apex Media Labs" required />
              </div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4);">
              <div class="form-group">
                <label class="form-label" for="bPhone">Work Phone</label>
                <input type="tel" id="bPhone" class="form-input" placeholder="e.g. 98200 99887" required />
              </div>
              <div class="form-group">
                <label class="form-label" for="bEmail">Corporate Email</label>
                <input type="email" id="bEmail" class="form-input" placeholder="e.g. anand@apexmedia.com" required />
              </div>
            </div>

            <div class="form-group">
              <label class="form-label" for="bAddress">Office Commercial Building &amp; Locality</label>
              <input type="text" id="bAddress" class="form-input" placeholder="e.g. Unit 401, Mindspace IT Park, Malad West" required />
            </div>

            <div class="form-success-alert" style="display: none; padding: var(--space-3); background: var(--tint-emerald); color: var(--color-emerald-text); border-radius: var(--radius-xs); font-size: var(--text-xs); margin-bottom: var(--space-3);">
              ✓ Feasibility inquiry logged! Our enterprise desk will contact you within 2 business hours.
            </div>

            <button type="submit" class="btn btn-primary" style="width: 100%;">Submit Corporate Request</button>
          </form>
        </div>
      </div>
    </section>
    """

def get_installation_content():
    return """
    <!-- PAGE HERO -->
    <section class="page-hero">
      <div class="container">
        <nav aria-label="Breadcrumb" class="breadcrumbs">
          <a href="index.html">Home</a>
          <span>/</span>
          <span aria-current="page">Internet Installation</span>
        </nav>
        <div style="max-width: 760px;">
          <span class="subheading-badge">Step-by-Step Transparency</span>
          <h1 class="display-title" style="margin-bottom: var(--space-4);">
            What to Expect on Installation Day
          </h1>
          <p class="lead">
            We respect your home and time. Our certified broadband optical technicians follow strict residential cabling standards to deliver clean, concealed fiber lines with zero mess.
          </p>
        </div>
      </div>
    </section>

    <!-- 4 STAGES OF INSTALLATION -->
    <section class="section">
      <div class="container">
        
        <div style="display: grid; grid-template-columns: 1fr; gap: var(--space-8); align-items: center; margin-bottom: var(--space-12);" class="editorial-split-grid">
          <div>
            <picture>
              <source srcset="public/assets/images/technician-install.avif" type="image/avif">
              <img src="public/assets/images/technician-install.jpg" alt="Certified fiber technician installing optical termination plate" style="width: 100%; height: auto; border-radius: var(--radius-lg); box-shadow: var(--shadow-lg); display: block;" loading="lazy">
            </picture>
          </div>

          <div>
            <span class="subheading-badge">The 4-Step Process</span>
            <h2>From Booking to Gigabit Speeds in 4 Simple Steps</h2>
            <p class="lead" style="margin-bottom: var(--space-6);">
              Here is exactly how our field engineers set up your new connection:
            </p>

            <div style="display: flex; flex-direction: column; gap: var(--space-4);">
              
              <div style="display: flex; gap: var(--space-3); align-items: flex-start;">
                <div style="width: 32px; height: 32px; border-radius: 50%; background: var(--color-navy); color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0;">1</div>
                <div>
                  <strong style="color: var(--color-navy); font-size: var(--text-base); display: block;">Arrival &amp; Home Wi-Fi Survey (10 mins)</strong>
                  <p class="text-muted" style="font-size: var(--text-sm); margin: 2px 0 0;">The technician checks your apartment layout, discusses optimal router placement (living room vs hallway), and checks for power sockets.</p>
                </div>
              </div>

              <div style="display: flex; gap: var(--space-3); align-items: flex-start;">
                <div style="width: 32px; height: 32px; border-radius: 50%; background: var(--color-orange); color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0;">2</div>
                <div>
                  <strong style="color: var(--color-navy); font-size: var(--text-base); display: block;">Precision Optical Fiber Pulling (20 mins)</strong>
                  <p class="text-muted" style="font-size: var(--text-sm); margin: 2px 0 0;">Using bend-insensitive yellow optical micro-cables, the technician runs a dedicated line from the society floor distribution box neatly along door moldings.</p>
                </div>
              </div>

              <div style="display: flex; gap: var(--space-3); align-items: flex-start;">
                <div style="width: 32px; height: 32px; border-radius: 50%; background: var(--color-violet); color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0;">3</div>
                <div>
                  <strong style="color: var(--color-navy); font-size: var(--text-base); display: block;">Fusion Splicing &amp; ONT Setup (15 mins)</strong>
                  <p class="text-muted" style="font-size: var(--text-sm); margin: 2px 0 0;">The optical fiber is fusion-spliced with optical power calibration and plugged into your new Dual-Band ONT router. Both 2.4 GHz and 5 GHz wireless channels are initialized.</p>
                </div>
              </div>

              <div style="display: flex; gap: var(--space-3); align-items: flex-start;">
                <div style="width: 32px; height: 32px; border-radius: 50%; background: var(--color-emerald); color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0;">4</div>
                <div>
                  <strong style="color: var(--color-navy); font-size: var(--text-base); display: block;">Device Speed Verification &amp; KYC Handover (10 mins)</strong>
                  <p class="text-muted" style="font-size: var(--text-sm); margin: 2px 0 0;">The technician conducts live Ookla speed tests on your phone and laptop, verifies symmetrical upload/download throughput, and completes digital KYC verification.</p>
                </div>
              </div>

            </div>
          </div>
        </div>

        <!-- ROUTER PLACEMENT TIPS -->
        <div class="card" style="padding: var(--space-8); background-color: var(--color-white); border-radius: var(--radius-lg); box-shadow: var(--shadow-sm);">
          <div class="section-header text-center" style="margin-bottom: var(--space-6);">
            <span class="subheading-badge">Pro Installation Advice</span>
            <h3 style="margin: 0; color: var(--color-navy);">Where to Place Your Wi-Fi Router for Best Speed</h3>
            <p class="text-muted" style="font-size: var(--text-sm); margin-top: 4px;">Small placement tweaks can increase your wireless range and speed by up to 40%.</p>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: var(--space-6);">
            <div>
              <h4 style="color: var(--color-emerald-text); font-size: var(--text-base); margin-bottom: var(--space-2);">✔ Recommended Practices</h4>
              <ul class="feature-list" style="margin: 0; font-size: var(--text-xs);">
                <li>Place the router in an elevated central location (on a console table 3–4 feet off the floor).</li>
                <li>Keep the router in the open living room rather than tucked away inside a closed wooden cabinet.</li>
                <li>Connect smart TVs, gaming PCs, and streaming boxes via direct Ethernet cable where possible.</li>
              </ul>
            </div>

            <div>
              <h4 style="color: var(--color-danger); font-size: var(--text-base); margin-bottom: var(--space-2);">✖ Things to Avoid</h4>
              <ul class="feature-list" style="margin: 0; font-size: var(--text-xs);">
                <li>Do not place the router directly behind thick concrete pillars or large metal mirrors.</li>
                <li>Keep the router at least 3 feet away from microwave ovens and cordless phone stations.</li>
                <li>Never tightly bend or kink the thin yellow fiber cable entering the back of the ONT.</li>
              </ul>
            </div>
          </div>
        </div>

        <div style="text-align: center; margin-top: var(--space-8);">
          <a href="new-connection.html" class="btn btn-primary btn-lg">Book Same-Day Installation Now</a>
        </div>
      </div>
    </section>
    """

def get_support_content():
    return """
    <!-- PAGE HERO -->
    <section class="page-hero">
      <div class="container">
        <nav aria-label="Breadcrumb" class="breadcrumbs">
          <a href="index.html">Home</a>
          <span>/</span>
          <span aria-current="page">Customer Support</span>
        </nav>
        <div style="max-width: 760px;">
          <span class="subheading-badge">Customer First</span>
          <h1 class="display-title" style="margin-bottom: var(--space-4);">
            Sevenseas Support &amp; Self-Service Hub
          </h1>
          <p class="lead">
            Quickly resolve common connection questions, pay your bill, diagnose ONT router status lights, or connect directly with our local neighborhood support desk.
          </p>
        </div>
      </div>
    </section>

    <!-- SUPPORT CHANNELS & QUICK PAY -->
    <section class="section">
      <div class="container">
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--space-6); margin-bottom: var(--space-12);">
          
          <div class="card" style="padding: var(--space-6);" id="quick-pay">
            <div class="icon-box icon-box-emerald" style="margin-bottom: var(--space-3);"><svg class="icon"><use href="#icon-router"></use></svg></div>
            <h3 style="margin-bottom: var(--space-2); color: var(--color-navy);">Quick Online Bill Pay</h3>
            <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-4);">Enter your registered mobile number or Customer Account ID to renew your plan instantly via UPI, Cards, or Net Banking.</p>
            <form data-validate data-ajax="true">
              <input type="text" class="form-input" placeholder="Enter Mobile No or User ID" required style="margin-bottom: var(--space-2);" />
              <button type="submit" class="btn btn-emerald btn-sm" style="width: 100%;">Fetch Bill &amp; Pay</button>
            </form>
          </div>

          <div class="card" style="padding: var(--space-6);">
            <div class="icon-box" style="margin-bottom: var(--space-3); background: rgba(37, 211, 102, 0.12); color: #25D366;"><svg class="icon" style="width: 24px; height: 24px;"><use href="#icon-whatsapp"></use></svg></div>
            <h3 style="margin-bottom: var(--space-2); color: var(--color-navy);">WhatsApp Support Desk</h3>
            <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-4);">Check your active plan expiry date, view current speed metrics, or connect directly through WhatsApp.</p>
            <a href="https://wa.me/919664985535?text=Hi%20Sevenseas%20Support" target="_blank" rel="noopener" class="btn btn-emerald btn-sm" style="width: 100%; display: inline-flex; align-items: center; justify-content: center; gap: 6px;">
              <svg class="icon icon-xs" style="width: 16px; height: 16px;"><use href="#icon-whatsapp"></use></svg> Chat on WhatsApp
            </a>
          </div>

          <div class="card" style="padding: var(--space-6);">
            <div class="icon-box icon-box-navy" style="margin-bottom: var(--space-3);"><svg class="icon"><use href="#icon-headset"></use></svg></div>
            <h3 style="margin-bottom: var(--space-2); color: var(--color-navy);">Customer Care Helplines</h3>
            <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-4);">Speak with our local technicians based in Airoli for immediate line assistance and troubleshooting.</p>
            <a href="tel:9664985535" class="btn btn-secondary btn-sm" style="width: 100%;">Call +91 96649 85535</a>
          </div>

        </div>

        <!-- SELF-SERVICE DIAGNOSTIC GUIDE -->
        <div class="card" style="padding: var(--space-8); background-color: var(--color-white); border-radius: var(--radius-lg); box-shadow: var(--shadow-sm); margin-bottom: var(--space-12);">
          <div class="section-header text-center" style="margin-bottom: var(--space-6);">
            <span class="subheading-badge">Self Diagnostic</span>
            <h2 style="margin: 0; color: var(--color-navy);">Reading Your ONT Router Status LEDs</h2>
            <p class="lead" style="margin-left: auto; margin-right: auto;">Check the small indicator lights on the front of your Sevenseas router to diagnose your line status in seconds.</p>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: var(--space-4);">
            <div style="background: var(--tint-emerald); border: 1px solid rgba(15,157,117,0.2); padding: var(--space-4); border-radius: var(--radius-sm);">
              <div style="display: flex; align-items: center; gap: var(--space-2); margin-bottom: 4px;">
                <span style="width: 12px; height: 12px; border-radius: 50%; background: var(--color-emerald);"></span>
                <strong style="color: var(--color-emerald-text);">PON Light: Solid Green</strong>
              </div>
              <span style="font-size: var(--text-xs); color: var(--color-ink);">Optical line is healthy and synchronized with the neighborhood distribution hub.</span>
            </div>

            <div style="background: var(--tint-danger); border: 1px solid rgba(217,38,28,0.2); padding: var(--space-4); border-radius: var(--radius-sm);">
              <div style="display: flex; align-items: center; gap: var(--space-2); margin-bottom: 4px;">
                <span style="width: 12px; height: 12px; border-radius: 50%; background: var(--color-danger);"></span>
                <strong style="color: var(--color-danger);">LOS Light: Blinking Red</strong>
              </div>
              <span style="font-size: var(--text-xs); color: var(--color-ink);">Loss of Signal. Check that the yellow fiber cable isn't bent, or call our NOC desk.</span>
            </div>

            <div style="background: var(--tint-navy); border: 1px solid var(--color-border); padding: var(--space-4); border-radius: var(--radius-sm);">
              <div style="display: flex; align-items: center; gap: var(--space-2); margin-bottom: 4px;">
                <span style="width: 12px; height: 12px; border-radius: 50%; background: var(--color-navy);"></span>
                <strong style="color: var(--color-navy);">LAN / Wi-Fi: Blinking Green</strong>
              </div>
              <span style="font-size: var(--text-xs); color: var(--color-ink);">Data packets are actively transmitting between devices and the optical network.</span>
            </div>
          </div>
        </div>

        <!-- TICKET SUBMISSION -->
        <div style="max-width: 680px; margin: 0 auto;">
          <div class="card" style="padding: var(--space-8);">
            <h3 style="color: var(--color-navy); margin-bottom: var(--space-2); text-align: center;">Raise a Support Ticket</h3>
            <p class="text-muted" style="font-size: var(--text-xs); text-align: center; margin-bottom: var(--space-6);">Logged tickets are assigned directly to your local area technician with under 4-hour SLA.</p>

            <form data-validate data-ajax="true">
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4);">
                <div class="form-group">
                  <label class="form-label" for="tCustId">Customer Account ID / Mobile</label>
                  <input type="text" id="tCustId" class="form-input" placeholder="e.g. SB-10492 or 98200..." required />
                </div>
                <div class="form-group">
                  <label class="form-label" for="tCategory">Issue Type</label>
                  <select id="tCategory" class="form-input" style="cursor: pointer;">
                    <option value="los">LOS Red Light / No Internet</option>
                    <option value="slow">Slow Wi-Fi Speed on Certain Devices</option>
                    <option value="relocation">Address Relocation Request</option>
                    <option value="bill">Payment / Invoicing Query</option>
                  </select>
                </div>
              </div>

              <div class="form-group">
                <label class="form-label" for="tDesc">Describe the Issue</label>
                <textarea id="tDesc" class="form-input" rows="3" placeholder="Please mention if router LEDs are green or red..." required></textarea>
              </div>

              <div class="form-success-alert" style="display: none; padding: var(--space-3); background: var(--tint-emerald); color: var(--color-emerald-text); border-radius: var(--radius-xs); font-size: var(--text-xs); margin-bottom: var(--space-3);">
                ✓ Ticket #T-4892 created! Assigned to your local field engineer.
              </div>

              <button type="submit" class="btn btn-primary" style="width: 100%;">Submit Support Ticket</button>
            </form>
          </div>
        </div>

      </div>
    </section>
    """

def get_localities_content():
    return """
    <!-- PAGE HERO -->
    <section class="page-hero">
      <div class="container">
        <nav aria-label="Breadcrumb" class="breadcrumbs">
          <a href="index.html">Home</a>
          <span>/</span>
          <span aria-current="page">Localities</span>
        </nav>
        <div style="max-width: 760px;">
          <span class="subheading-badge">Neighborhood Network</span>
          <h1 class="display-title" style="margin-bottom: var(--space-4);">
            Broadband in Individual Localities
          </h1>
          <p class="lead">
            Every neighborhood has distinct housing topologies—from high-rise cooperative housing societies to coastal bungalows. Explore our dedicated optical fiber points-of-presence (PoPs) and local service teams across your area.
          </p>
        </div>
      </div>
    </section>

    <!-- AUTHENTIC LOCALITY PROFILES (NOT FIND-REPLACE DUPLICATES) -->
    <section class="section">
      <div class="container">
        
        <div style="display: flex; flex-direction: column; gap: var(--space-10);">
          
          <!-- Locality 1: Bandra & Khar West -->
          <div class="editorial-card">
            <div class="editorial-card-body">
              <div style="display: flex; align-items: center; gap: var(--space-2); margin-bottom: var(--space-2);">
                <span class="badge badge-emerald"><span class="pulse-dot"></span> PoP Active</span>
                <span class="badge badge-navy">Central Western Hub</span>
              </div>
              <h3 style="margin-bottom: var(--space-3); color: var(--color-navy);">Bandra West &amp; Khar Residential Ring</h3>
              <p style="font-size: var(--text-sm); line-height: var(--leading-relaxed); color: var(--color-ink); margin-bottom: var(--space-4);">
                Serving heritage residential buildings and premier apartments along Pali Hill, Carter Road, Perry Cross Road, Turner Road, and 14th Road. Connected directly to our flagship NOC with redundant subsea cable landings nearby.
              </p>
              <div style="display: flex; gap: var(--space-4); font-size: var(--text-xs); color: var(--color-muted); margin-bottom: var(--space-4);">
                <span><strong>Avg Local Ping:</strong> 2.8ms</span>
                <span><strong>Key Societies:</strong> 120+ CHS Connected</span>
                <span><strong>Depot:</strong> Linking Road Care Center</span>
              </div>
              <div>
                <a href="new-connection.html?loc=bandra" class="btn btn-primary btn-sm">Get Bandra Fiber Connection</a>
              </div>
            </div>
            <div class="editorial-card-aside">
              <h4 style="margin-bottom: var(--space-2); font-size: var(--text-base);">Neighborhood Network Architecture:</h4>
              <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-3);">Features dual underground fiber feeder routes to prevent disruption during seasonal monsoon coastal winds and municipal road work.</p>
              <span class="status-indicator" style="font-size: 0.75rem;"><span class="pulse-dot"></span> Same-day 4-hour activation live</span>
            </div>
          </div>

          <!-- Locality 2: Andheri West & Lokhandwala -->
          <div class="editorial-card">
            <div class="editorial-card-body">
              <div style="display: flex; align-items: center; gap: var(--space-2); margin-bottom: var(--space-2);">
                <span class="badge badge-emerald"><span class="pulse-dot"></span> PoP Active</span>
                <span class="badge badge-orange">Creative &amp; Media Hub</span>
              </div>
              <h3 style="margin-bottom: var(--space-3); color: var(--color-navy);">Andheri West &amp; Lokhandwala Complex</h3>
              <p style="font-size: var(--text-sm); line-height: var(--leading-relaxed); color: var(--color-ink); margin-bottom: var(--space-4);">
                A bustling residential zone with home studios, production houses, and high-density towers across Lokhandwala, Oshiwara, Yamuna Nagar, and Versova. Symmetrical gigabit upload bandwidth ensures video editors and content creators upload 4K ProRes files effortlessly.
              </p>
              <div style="display: flex; gap: var(--space-4); font-size: var(--text-xs); color: var(--color-muted); margin-bottom: var(--space-4);">
                <span><strong>Avg Local Ping:</strong> 3.1ms</span>
                <span><strong>Key Societies:</strong> 240+ CHS Connected</span>
                <span><strong>Depot:</strong> Oshiwara Link Road Depot</span>
              </div>
              <div>
                <a href="new-connection.html?loc=andheri" class="btn btn-primary btn-sm">Get Andheri West Connection</a>
              </div>
            </div>
            <div class="editorial-card-aside">
              <h4 style="margin-bottom: var(--space-2); font-size: var(--text-base);">Media Fast-Path Peering:</h4>
              <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-3);">Direct high-throughput interconnects with YouTube, Vimeo, and Adobe Creative Cloud for instantaneous upload speeds.</p>
              <span class="status-indicator" style="font-size: 0.75rem;"><span class="pulse-dot"></span> Gigabit Max 500 in stock</span>
            </div>
          </div>

          <!-- Locality 3: Powai & Hiranandani Gardens -->
          <div class="editorial-card">
            <div class="editorial-card-body">
              <div style="display: flex; align-items: center; gap: var(--space-2); margin-bottom: var(--space-2);">
                <span class="badge badge-emerald"><span class="pulse-dot"></span> PoP Active</span>
                <span class="badge badge-violet">Tech &amp; Startup Corridor</span>
              </div>
              <h3 style="margin-bottom: var(--space-3); color: var(--color-navy);">Powai &amp; Hiranandani Gardens</h3>
              <p style="font-size: var(--text-sm); line-height: var(--leading-relaxed); color: var(--color-ink); margin-bottom: var(--space-4);">
                Engineered for engineers, remote tech executives, and modern smart homes across Hiranandani Gardens, Raheja Vihar, and Chandivali. Ultra-low latency directly to AWS Mumbai and Microsoft Azure regions.
              </p>
              <div style="display: flex; gap: var(--space-4); font-size: var(--text-xs); color: var(--color-muted); margin-bottom: var(--space-4);">
                <span><strong>Avg Local Ping:</strong> 3.2ms</span>
                <span><strong>Key Societies:</strong> 95+ High-Rise Towers</span>
                <span><strong>Depot:</strong> Central Avenue Care Center</span>
              </div>
              <div>
                <a href="new-connection.html?loc=powai" class="btn btn-primary btn-sm">Get Powai Fiber Connection</a>
              </div>
            </div>
            <div class="editorial-card-aside">
              <h4 style="margin-bottom: var(--space-2); font-size: var(--text-base);">Cloud Developer Direct Line:</h4>
              <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-3);">Optimized for continuous Git pushes, Docker container pulls, and stable VPN tunnels with zero packet drops.</p>
              <span class="status-indicator" style="font-size: 0.75rem;"><span class="pulse-dot"></span> Dual-band ONT deployment live</span>
            </div>
          </div>

          <!-- Locality 4: Thane West (Ghodbunder Road Corridor) -->
          <div class="editorial-card">
            <div class="editorial-card-body">
              <div style="display: flex; align-items: center; gap: var(--space-2); margin-bottom: var(--space-2);">
                <span class="badge badge-emerald"><span class="pulse-dot"></span> PoP Active</span>
                <span class="badge badge-navy">Large Township Clusters</span>
              </div>
              <h3 style="margin-bottom: var(--space-3); color: var(--color-navy);">Thane West &amp; Ghodbunder Road</h3>
              <p style="font-size: var(--text-sm); line-height: var(--leading-relaxed); color: var(--color-ink); margin-bottom: var(--space-4);">
                Powering major gated townships across Hiranandani Estate, Vasant Vihar, Pokhran Road No 1 &amp; 2, and Brahmand. Gated community optical risers are terminated directly in building basements.
              </p>
              <div style="display: flex; gap: var(--space-4); font-size: var(--text-xs); color: var(--color-muted); margin-bottom: var(--space-4);">
                <span><strong>Avg Local Ping:</strong> 4.0ms</span>
                <span><strong>Key Societies:</strong> 180+ Township Buildings</span>
                <span><strong>Depot:</strong> Ghodbunder Service Hub</span>
              </div>
              <div>
                <a href="new-connection.html?loc=thane" class="btn btn-primary btn-sm">Get Thane West Connection</a>
              </div>
            </div>
            <div class="editorial-card-aside">
              <h4 style="margin-bottom: var(--space-2); font-size: var(--text-base);">Township Optical Mesh:</h4>
              <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-3);">Dedicated fiber rings built in partnership with cooperative society federations with on-site standby technicians on weekends.</p>
              <span class="status-indicator" style="font-size: 0.75rem;"><span class="pulse-dot"></span> Free Wi-Fi 6 on annual plans</span>
            </div>
          </div>

          <!-- Locality 5: Navi Mumbai Seawoods & Vashi -->
          <div class="editorial-card">
            <div class="editorial-card-body">
              <div style="display: flex; align-items: center; gap: var(--space-2); margin-bottom: var(--space-2);">
                <span class="badge badge-emerald"><span class="pulse-dot"></span> PoP Active</span>
                <span class="badge badge-orange">Planned Residential Sectors</span>
              </div>
              <h3 style="margin-bottom: var(--space-3); color: var(--color-navy);">Navi Mumbai: Seawoods, Nerul &amp; Vashi</h3>
              <p style="font-size: var(--text-sm); line-height: var(--leading-relaxed); color: var(--color-ink); margin-bottom: var(--space-4);">
                Connected to wide CIDCO residential sectors across Seawoods Estate, Palm Beach Road towers, Nerul Sector 28, and Vashi Sectors 14–17. High stability optical fiber cables laid through CIDCO underground utility ducts.
              </p>
              <div style="display: flex; gap: var(--space-4); font-size: var(--text-xs); color: var(--color-muted); margin-bottom: var(--space-4);">
                <span><strong>Avg Local Ping:</strong> 3.6ms</span>
                <span><strong>Key Societies:</strong> 160+ Sectors CHS</span>
                <span><strong>Depot:</strong> Seawoods Sector 40 Hub</span>
              </div>
              <div>
                <a href="new-connection.html?loc=navimumbai" class="btn btn-primary btn-sm">Get Navi Mumbai Connection</a>
              </div>
            </div>
            <div class="editorial-card-aside">
              <h4 style="margin-bottom: var(--space-2); font-size: var(--text-base);">Duct Optical Redundancy:</h4>
              <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-3);">Underground structured utility ducts prevent accidental overhead fiber damage during civic monsoon works.</p>
              <span class="status-indicator" style="font-size: 0.75rem;"><span class="pulse-dot"></span> Same-day activation active</span>
            </div>
          </div>

        </div>

      </div>
    </section>
    """
