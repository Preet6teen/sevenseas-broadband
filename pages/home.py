"""
Homepage content generator for Sevenseas Broadband.
"""

def get_content():
    return """
    <!-- HERO SECTION -->
    <section class="section" style="padding-top: var(--space-8); padding-bottom: var(--space-12); background: linear-gradient(180deg, #FFFFFF 0%, var(--color-bg) 100%);">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1fr; gap: var(--space-8); align-items: center;">
          
          <!-- Top Grid: Content & Photography -->
          <div style="display: grid; grid-template-columns: 1fr; gap: var(--space-8); align-items: center;" class="hero-split-grid">
            <div>
              <div style="display: inline-flex; align-items: center; gap: var(--space-2); margin-bottom: var(--space-4);">
                <span class="badge badge-emerald">
                  <span class="pulse-dot"></span> Pure FTTH Fiber
                </span>
                <span class="badge badge-navy">Connecting Every Home</span>
              </div>
              
              <h1 class="display-title" style="margin-bottom: var(--space-4); color: var(--color-navy);">
                Ultra-Fast Fiber Internet for Every Home
              </h1>
              
              <p class="lead" style="margin-bottom: var(--space-6); color: var(--color-muted);">
                Experience unthrottled gigabit speeds, symmetrical uploads, and jitter-free connectivity tailored for modern families, remote workers, students, and entertainment enthusiasts.
              </p>

              <!-- Coverage Checker Bar -->
              <div style="background-color: var(--color-white); border: 1.5px solid var(--color-border); border-radius: var(--radius-md); padding: var(--space-3); box-shadow: var(--shadow-md); margin-bottom: var(--space-4); max-width: 580px;">
                <form class="coverage-checker-bar" onsubmit="event.preventDefault(); document.getElementById('homeCoverageResult').style.display = 'flex';">
                  <div style="display: flex; align-items: center; gap: var(--space-2); flex: 1; padding: 0 0.5rem;">
                    <svg class="icon icon-sm" style="color: var(--color-orange);"><use href="#icon-map-pin"></use></svg>
                    <input type="text" id="homeBuildingInput" placeholder="Enter your building, society, or area..." required aria-label="Enter your building or locality to check fiber availability" />
                  </div>
                  <button type="submit" class="btn btn-primary btn-sm">Check Coverage</button>
                </form>

                <div id="homeCoverageResult" style="display: none; align-items: center; gap: var(--space-3); margin-top: var(--space-3); padding: var(--space-3); background-color: var(--tint-emerald); border-radius: var(--radius-sm); border: 1px solid rgba(15, 157, 117, 0.2);">
                  <svg class="icon icon-sm" style="color: var(--color-emerald);"><use href="#icon-check"></use></svg>
                  <div style="font-size: var(--text-xs);">
                    <strong style="color: var(--color-emerald-text); display: block;">High-Speed Fiber is Available in Your Area!</strong>
                    <span style="color: var(--color-ink);">Same-day free installation with complimentary Wi-Fi 6 router. <a href="new-connection.html" style="color: var(--color-emerald-text); font-weight: bold; text-decoration: underline;">Book Slot &rarr;</a></span>
                  </div>
                </div>
              </div>

              <!-- Quick Perks Row -->
              <div style="display: flex; gap: var(--space-4); flex-wrap: wrap; font-size: var(--text-xs); color: var(--color-muted);">
                <span style="display: inline-flex; align-items: center; gap: 4px;">
                  <svg class="icon icon-xs" style="color: var(--color-emerald);"><use href="#icon-infinity"></use></svg> Truly Unlimited Data
                </span>
                <span style="display: inline-flex; align-items: center; gap: 4px;">
                  <svg class="icon icon-xs" style="color: var(--color-orange);"><use href="#icon-gauge"></use></svg> Equal Upload &amp; Download
                </span>
                <span style="display: inline-flex; align-items: center; gap: 4px;">
                  <svg class="icon icon-xs" style="color: var(--color-navy);"><use href="#icon-router"></use></svg> Zero Installation Cost*
                </span>
              </div>
            </div>

            <!-- Commercial Hero Image Showcase -->
            <div style="position: relative; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-xl); border: 1px solid var(--color-border); background-color: #0F1B2D;">
              <picture>
                <source srcset="public/assets/images/hero-family.avif 1376w, public/assets/images/hero-family-640.avif 640w" type="image/avif" sizes="(max-width: 768px) 100vw, 680px">
                <source srcset="public/assets/images/hero-family.jpg 1376w, public/assets/images/hero-family-640.jpg 640w" type="image/jpeg" sizes="(max-width: 768px) 100vw, 680px">
                <img src="public/assets/images/hero-family.jpg" 
                     alt="Joyful contemporary Indian family enjoying fast reliable Sevenseas Broadband internet on a laptop in their sunlit modern living room" 
                     style="width: 100%; height: auto; display: block; object-fit: cover; max-height: 480px;" 
                     loading="eager" />
              </picture>
              
              <!-- Floating Pill Indicator -->
              <div style="position: absolute; bottom: 16px; left: 16px; background: rgba(15, 27, 45, 0.88); backdrop-filter: blur(8px); padding: 0.6rem 1rem; border-radius: var(--radius-pill); border: 1px solid rgba(255, 255, 255, 0.15); display: flex; align-items: center; gap: var(--space-3); color: #FFFFFF;">
                <span class="pulse-dot"></span>
                <span style="font-size: var(--text-xs); font-family: var(--font-heading); font-weight: 700;">
                  Live Ping: <span style="color: var(--color-emerald);">&lt; 4ms</span> • 99.9% Optical Uptime
                </span>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- KEY STATS STRIP (Asymmetrical Telecom Layout) -->
    <section style="background-color: var(--color-white); border-bottom: 1px solid var(--color-border); padding: var(--space-8) 0;">
      <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: var(--space-6);">
          <div style="display: flex; align-items: center; gap: var(--space-3);">
            <div class="icon-box icon-box-orange">
              <svg class="icon"><use href="#icon-infinity"></use></svg>
            </div>
            <div>
              <div class="stat-number" style="font-size: var(--text-2xl);">Unlimited</div>
              <div class="stat-unit">No Data Caps or FUP throttling</div>
            </div>
          </div>

          <div style="display: flex; align-items: center; gap: var(--space-3);">
            <div class="icon-box icon-box-emerald">
              <svg class="icon"><use href="#icon-gauge"></use></svg>
            </div>
            <div>
              <div class="stat-number" style="font-size: var(--text-2xl);">Symmetrical</div>
              <div class="stat-unit">Equal Download &amp; Upload Speed</div>
            </div>
          </div>

          <div style="display: flex; align-items: center; gap: var(--space-3);">
            <div class="icon-box icon-box-violet">
              <svg class="icon"><use href="#icon-gamepad-2"></use></svg>
            </div>
            <div>
              <div class="stat-number" style="font-size: var(--text-2xl);">&lt; 5ms Ping</div>
              <div class="stat-unit">Direct Regional Game Peering</div>
            </div>
          </div>

          <div style="display: flex; align-items: center; gap: var(--space-3);">
            <div class="icon-box">
              <svg class="icon"><use href="#icon-headset"></use></svg>
            </div>
            <div>
              <div class="stat-number" style="font-size: var(--text-2xl);">24/7 Local</div>
              <div class="stat-unit">Dedicated Neighborhood Teams</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- POPULAR BROADBAND PLANS -->
    <section class="section" id="plans">
      <div class="container">
        <div class="section-header text-center">
          <span class="subheading-badge">Simple &amp; Transparent</span>
          <h2>High-Speed Home Fiber Plans</h2>
          <p class="lead" style="margin-left: auto; margin-right: auto;">
            No hidden taxes, no surprise installation fees. Pure optical fiber bandwidth designed for every budget and home size.
          </p>

          <!-- Billing Switcher -->
          <div class="billing-switcher" role="tablist" aria-label="Billing frequency switcher">
            <button class="billing-tab active" data-billing-toggle="monthly" role="tab" aria-selected="true">Monthly Billing</button>
            <button class="billing-tab" data-billing-toggle="quarterly" role="tab" aria-selected="false">Quarterly (5% Off)</button>
            <button class="billing-tab" data-billing-toggle="annual" role="tab" aria-selected="false">Annual (2 Months Free)</button>
          </div>
        </div>

        <!-- Plans Grid -->
        <div class="pricing-grid">
          
          <!-- Plan 1: 150 Mbps -->
          <div class="fiber-card">
            <div style="margin-bottom: var(--space-3);">
              <span class="badge badge-navy">Smart Starter</span>
            </div>
            <h3 style="margin-bottom: var(--space-1);">Fiber Stream 150</h3>
            <p class="text-muted" style="font-size: var(--text-sm); margin-bottom: var(--space-4);">Perfect for 1–3 bedroom apartments, smart TVs, and daily study.</p>

            <div class="price-dynamic" data-price-monthly="₹499" data-price-quarterly="₹1,420" data-price-annual="₹4,990" style="margin-bottom: var(--space-4);">
              <span class="price-value" style="font-size: var(--text-4xl);">₹499</span>
              <span class="price-unit">/ month</span>
            </div>

            <ul class="feature-list">
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> 150 Mbps Symmetrical Speed</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> Truly Unlimited Data</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> Dual-Band Wi-Fi Router Included</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> 99.9% Uptime Guarantee</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> 24/7 Neighborhood Support</li>
            </ul>

            <a href="new-connection.html?plan=150" class="btn btn-outline-navy" style="width: 100%;">Choose 150 Mbps</a>
          </div>

          <!-- Plan 2: 300 Mbps -->
          <div class="fiber-card">
            <div style="margin-bottom: var(--space-3);">
              <span class="badge badge-emerald">Family Favorite</span>
            </div>
            <h3 style="margin-bottom: var(--space-1);">Fiber Turbo 300</h3>
            <p class="text-muted" style="font-size: var(--text-sm); margin-bottom: var(--space-4);">Designed for multi-device households streaming 4K and working from home.</p>

            <div class="price-dynamic" data-price-monthly="₹649" data-price-quarterly="₹1,850" data-price-annual="₹6,490" style="margin-bottom: var(--space-4);">
              <span class="price-value" style="font-size: var(--text-4xl); color: var(--color-navy);">₹649</span>
              <span class="price-unit">/ month</span>
            </div>

            <ul class="feature-list">
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> 300 Mbps Up &amp; Down</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> Truly Unlimited Data</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> Gigabit Dual-Band Wi-Fi 5 ONT</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> Free Zero-Cost Installation</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> Priority Support Queue</li>
            </ul>

            <a href="new-connection.html?plan=300" class="btn btn-secondary" style="width: 100%;">Choose 300 Mbps</a>
          </div>

          <!-- Plan 3: 500 Mbps (Featured) -->
          <div class="fiber-card featured">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-3);">
              <span class="badge badge-orange">Best Value &amp; Performance</span>
              <span class="badge badge-emerald" style="font-size: 0.7rem;"><span class="pulse-dot"></span> Popular</span>
            </div>
            <h3 style="margin-bottom: var(--space-1); color: var(--color-navy);">Gigabit Max 500</h3>
            <p class="text-muted" style="font-size: var(--text-sm); margin-bottom: var(--space-4);">For heavy streamers, competitive gamers, and households with 10+ devices.</p>

            <div class="price-dynamic" data-price-monthly="₹799" data-price-quarterly="₹2,275" data-price-annual="₹7,990" style="margin-bottom: var(--space-4);">
              <span class="price-value" style="font-size: var(--text-4xl); color: var(--color-orange);">₹799</span>
              <span class="price-unit">/ month</span>
            </div>

            <ul class="feature-list">
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> 500 Mbps Symmetrical Fiber</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> Truly Unlimited Data</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> <strong>Next-Gen Wi-Fi 6 Router Included</strong></li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> Sub-5ms Gaming Peering</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> OTT Apps Bundle Eligible</li>
            </ul>

            <a href="new-connection.html?plan=500" class="btn btn-primary" style="width: 100%;">Get Gigabit Max 500</a>
          </div>

          <!-- Plan 4: 1 Gbps -->
          <div class="fiber-card">
            <div style="margin-bottom: var(--space-3);">
              <span class="badge badge-violet">Power Creator</span>
            </div>
            <h3 style="margin-bottom: var(--space-1);">Gigabit Ultra 1000</h3>
            <p class="text-muted" style="font-size: var(--text-sm); margin-bottom: var(--space-4);">The ultimate 1 Gbps symmetrical optical pipe for content creators and large villas.</p>

            <div class="price-dynamic" data-price-monthly="₹1,199" data-price-quarterly="₹3,415" data-price-annual="₹11,990" style="margin-bottom: var(--space-4);">
              <span class="price-value" style="font-size: var(--text-4xl);">₹1,199</span>
              <span class="price-unit">/ month</span>
            </div>

            <ul class="feature-list">
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> 1,000 Mbps (1 Gbps) Symmetrical</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> Unlimited Bandwidth</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> Dual-Node Wi-Fi 6 Mesh System</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> Dedicated Static IP Option</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> VIP Account Manager</li>
            </ul>

            <a href="new-connection.html?plan=1000" class="btn btn-outline-navy" style="width: 100%;">Choose 1 Gbps</a>
          </div>

        </div>

        <div style="text-align: center; margin-top: var(--space-8);">
          <p class="text-muted" style="font-size: var(--text-sm); margin-bottom: var(--space-3);">Need a custom configuration or multiple connections for your residential society?</p>
          <a href="plans.html" class="btn btn-outline-navy">View Full Plan Comparison &amp; OTT Bundles &rarr;</a>
        </div>
      </div>
    </section>

    <!-- SECTION: THE SEVENSEAS FIBER DIFFERENCE -->
    <section class="section section-alt">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1fr; gap: var(--space-8); align-items: center;" class="editorial-split-grid">
          <div>
            <span class="subheading-badge">100% Optical Glass FTTH</span>
            <h2>Why Sevenseas Fiber is Built Different</h2>
            <p class="lead" style="margin-bottom: var(--space-6);">
              Unlike traditional cable internet that relies on aging copper coaxial cables susceptible to rain, electrical interference, and evening throttling, Sevenseas delivers pure optical glass strands directly into your home.
            </p>

            <div style="display: flex; flex-direction: column; gap: var(--space-4);">
              <div style="display: flex; gap: var(--space-4); align-items: flex-start;">
                <div class="icon-box icon-box-emerald">
                  <svg class="icon"><use href="#icon-gauge"></use></svg>
                </div>
                <div>
                  <h4 style="margin-bottom: 4px;">True Symmetrical Speeds</h4>
                  <p class="text-muted" style="font-size: var(--text-sm); margin: 0;">Upload speeds match your download speeds. Back up family photos, send large work files, and broadcast 4K video instantly.</p>
                </div>
              </div>

              <div style="display: flex; gap: var(--space-4); align-items: flex-start;">
                <div class="icon-box icon-box-orange">
                  <svg class="icon"><use href="#icon-shield-check"></use></svg>
                </div>
                <div>
                  <h4 style="margin-bottom: 4px;">Weatherproof Optical Transmission</h4>
                  <p class="text-muted" style="font-size: var(--text-sm); margin: 0;">Light pulses traveling through glass cores are completely immune to electromagnetic noise, monsoons, and voltage surges.</p>
                </div>
              </div>

              <div style="display: flex; gap: var(--space-4); align-items: flex-start;">
                <div class="icon-box icon-box-navy">
                  <svg class="icon"><use href="#icon-network"></use></svg>
                </div>
                <div>
                  <h4 style="margin-bottom: 4px;">Direct Peering Ring</h4>
                  <p class="text-muted" style="font-size: var(--text-sm); margin: 0;">Direct interconnects with Google, Netflix, Amazon AWS, and major gaming hubs mean zero routing detours.</p>
                </div>
              </div>
            </div>

            <div style="margin-top: var(--space-6);">
              <a href="fiber-internet.html" class="btn btn-secondary">Explore Our Optical Technology &rarr;</a>
            </div>
          </div>

          <!-- Technical Diagram -->
          <div>
            <div class="card" style="padding: var(--space-6); background: var(--color-white); border-radius: var(--radius-lg);">
              <h4 style="margin-bottom: var(--space-2); color: var(--color-navy);">Sevenseas 9µm Pure Optical Core</h4>
              <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-4);">Engineered for zero signal degradation across kilometers of neighborhood fiber.</p>
              <img src="public/assets/images/fiber-cable-cutaway.svg" alt="Optical Fiber Cable Anatomy" style="width: 100%; height: auto; border-radius: var(--radius-sm);" />
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION: RESIDENTIAL USE CASES -->
    <section class="section">
      <div class="container">
        <div class="section-header text-center">
          <span class="subheading-badge">Built For Real Homes</span>
          <h2>Internet Tailored to Everyday Living</h2>
          <p class="lead" style="margin-left: auto; margin-right: auto;">
            From morning Zoom conferences to late-night gaming sessions, Sevenseas ensures every family member gets uninterrupted connectivity.
          </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--space-6);">
          
          <div class="card" style="padding: 0; overflow: hidden;">
            <picture>
              <source srcset="public/assets/images/family-entertainment.avif" type="image/avif">
              <img src="public/assets/images/family-entertainment.jpg" alt="Family watching 4K smart TV in living room" style="width: 100%; height: 200px; object-fit: cover; display: block;" loading="lazy">
            </picture>
            <div style="padding: var(--space-5);">
              <span class="badge badge-navy" style="margin-bottom: var(--space-2);">Cinema &amp; OTT</span>
              <h4 style="margin-bottom: var(--space-2);">Multi-Screen 4K Entertainment</h4>
              <p class="text-muted" style="font-size: var(--text-sm); margin: 0;">Stream Netflix, Hotstar, and YouTube simultaneously in full 4K HDR across three rooms with zero buffer wheels.</p>
            </div>
          </div>

          <div class="card" style="padding: 0; overflow: hidden;">
            <picture>
              <source srcset="public/assets/images/remote-work.avif" type="image/avif">
              <img src="public/assets/images/remote-work.jpg" alt="Remote professional working on video call" style="width: 100%; height: 200px; object-fit: cover; display: block;" loading="lazy">
            </picture>
            <div style="padding: var(--space-5);">
              <span class="badge badge-emerald" style="margin-bottom: var(--space-2);">Remote Career</span>
              <h4 style="margin-bottom: var(--space-2);">Zero-Lag Work From Home</h4>
              <p class="text-muted" style="font-size: var(--text-sm); margin: 0;">Crystal-clear video conferencing, instantaneous cloud file syncing, and rock-solid VPN stability all day.</p>
            </div>
          </div>

          <div class="card" style="padding: 0; overflow: hidden;">
            <picture>
              <source srcset="public/assets/images/student-learning.avif" type="image/avif">
              <img src="public/assets/images/student-learning.jpg" alt="Student studying with laptop and notes" style="width: 100%; height: 200px; object-fit: cover; display: block;" loading="lazy">
            </picture>
            <div style="padding: var(--space-5);">
              <span class="badge badge-violet" style="margin-bottom: var(--space-2);">Academic Success</span>
              <h4 style="margin-bottom: var(--space-2);">Online Learning &amp; Research</h4>
              <p class="text-muted" style="font-size: var(--text-sm); margin: 0;">Uncompromised download bandwidth for online examinations, college webinars, and academic databases.</p>
            </div>
          </div>

          <div class="card" style="padding: 0; overflow: hidden;">
            <picture>
              <source srcset="public/assets/images/gaming-experience.avif" type="image/avif">
              <img src="public/assets/images/gaming-experience.jpg" alt="Gamer in gaming setup with headset" style="width: 100%; height: 200px; object-fit: cover; display: block;" loading="lazy">
            </picture>
            <div style="padding: var(--space-5);">
              <span class="badge badge-orange" style="margin-bottom: var(--space-2);">Low-Ping Esports</span>
              <h4 style="margin-bottom: var(--space-2);">Competitive Online Gaming</h4>
              <p class="text-muted" style="font-size: var(--text-sm); margin: 0;">Sub-5ms local server ping and jitter-free fiber ensure your reaction times translate to instant in-game wins.</p>
            </div>
          </div>

        </div>

        <div style="text-align: center; margin-top: var(--space-8);">
          <a href="residential.html" class="btn btn-outline-navy">See How We Power Residential Homes &rarr;</a>
        </div>
      </div>
    </section>

    <!-- SECTION: HARDWARE & INSTALLATION SHOWCASE -->
    <section class="section section-alt">
      <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: var(--space-8); align-items: center;">
          
          <div>
            <picture>
              <source srcset="public/assets/images/technician-install.avif" type="image/avif">
              <img src="public/assets/images/technician-install.jpg" alt="Sevenseas certified technician performing clean residential installation" style="width: 100%; height: auto; border-radius: var(--radius-lg); box-shadow: var(--shadow-lg); display: block;" loading="lazy">
            </picture>
          </div>

          <div>
            <span class="subheading-badge">White-Glove Service</span>
            <h2>Same-Day Doorstep Optical Setup</h2>
            <p class="lead" style="margin-bottom: var(--space-6);">
              Our certified broadband technicians handle everything from outer optical fiber routing to inside-home ONT modem configuration with precision tools and zero wall damage.
            </p>

            <ul class="feature-list" style="margin-bottom: var(--space-6);">
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> <strong>Neat &amp; Concealed Cabling:</strong> Sleek yellow optical micro-cable terminated neatly into your wall plate.</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> <strong>Wi-Fi Coverage Survey:</strong> Optimal router positioning to ensure strong signal across all bedrooms.</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> <strong>Live Speed Certification:</strong> Technician conducts speed and ping verification on your devices before signoff.</li>
            </ul>

            <div style="display: flex; gap: var(--space-4); flex-wrap: wrap;">
              <a href="installation.html" class="btn btn-secondary">Installation Walkthrough</a>
              <a href="new-connection.html" class="btn btn-primary">Book Free Installation</a>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- FAQ SECTION PREVIEW -->
    <section class="section">
      <div class="container">
        <div class="section-header text-center">
          <span class="subheading-badge">Got Questions?</span>
          <h2>Frequently Asked Questions</h2>
          <p class="lead" style="margin-left: auto; margin-right: auto;">Everything you need to know about getting started with Sevenseas Broadband.</p>
        </div>

        <div class="faq-accordion">
          
          <div class="faq-item is-active">
            <button class="faq-question" aria-expanded="true">
              <span>How long does a new connection installation take?</span>
              <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
            </button>
            <div class="faq-answer">
              <p>In verified fiber-ready buildings, installation is completed within <strong>4 to 8 hours</strong> of booking. Our field technician will call you to confirm your preferred time slot and complete the optical line termination and Wi-Fi setup on the same day.</p>
            </div>
          </div>

          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              <span>Is the Wi-Fi router really included for free?</span>
              <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
            </button>
            <div class="faq-answer">
              <p>Yes! Every Sevenseas broadband connection comes with a high-performance Dual-Band Optical Network Terminal (ONT) with built-in Wi-Fi provided at zero additional hardware rental. For our Gigabit Max 500 and Ultra 1000 plans, an advanced <strong>Wi-Fi 6 Gigabit Gateway</strong> is provided complimentary.</p>
            </div>
          </div>

          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              <span>Are download and upload speeds really symmetrical?</span>
              <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
            </button>
            <div class="faq-answer">
              <p>Yes. Because we use 100% optical fiber technology (FTTH) rather than legacy copper coaxial cable, you get the exact same speed in both directions. If you subscribe to a 300 Mbps plan, you will receive 300 Mbps download AND 300 Mbps upload.</p>
            </div>
          </div>

          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              <span>Is there any Fair Usage Policy (FUP) limit?</span>
              <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
            </button>
            <div class="faq-answer">
              <p>Our residential plans come with <strong>truly unlimited unthrottled data</strong>. You can stream in 4K, back up large datasets, and download video games all month without ever worrying about mid-month speed drops.</p>
            </div>
          </div>

          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              <span>What documents are required for a new connection?</span>
              <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
            </button>
            <div class="faq-answer">
              <p>As per Department of Telecommunications (DoT) guidelines, we require: (1) Proof of Identity (Aadhaar Card, Passport, or Voter ID), (2) Proof of Address (Electricity bill, rental agreement, or Aadhaar), and (3) One passport-size photograph or digital verification selfie.</p>
            </div>
          </div>

        </div>

        <div style="text-align: center; margin-top: var(--space-8);">
          <a href="faq.html" class="btn btn-outline-navy">View All 20+ Frequently Asked Questions &rarr;</a>
        </div>
      </div>
    </section>

    <!-- FINAL CALL TO ACTION STRIP -->
    <section style="background-color: var(--color-navy); color: #FFFFFF; padding: var(--space-12) 0; position: relative;">
      <div class="container" style="text-align: center;">
        <span class="badge badge-orange" style="margin-bottom: var(--space-3);">Limited Time Neighborhood Offer</span>
        <h2 style="color: #FFFFFF; font-size: var(--text-3xl); margin-bottom: var(--space-3);">Connect Your Home to Pure Optical Fiber Today</h2>
        <p style="color: #CBD5E1; font-size: var(--text-base); max-width: 600px; margin: 0 auto var(--space-6);">
          Get free same-day installation, complimentary Wi-Fi 6 ONT hardware, and 2 months free with any annual plan.
        </p>
        <div style="display: flex; gap: var(--space-4); justify-content: center; flex-wrap: wrap;">
          <a href="new-connection.html" class="btn btn-primary btn-lg">Book New Connection</a>
          <a href="tel:9664985535" class="btn btn-outline-navy" style="color: #FFFFFF; border-color: rgba(255,255,255,0.4);">
            <svg class="icon icon-sm"><use href="#icon-phone"></use></svg> Call: +91 96649 85535
          </a>
        </div>
      </div>
    </section>
    """
