"""
Fiber Internet technology page content generator for Sevenseas Broadband.
"""

def get_content():
    return """
    <!-- PAGE HERO -->
    <section class="page-hero">
      <div class="container">
        <nav aria-label="Breadcrumb" class="breadcrumbs">
          <a href="index.html">Home</a>
          <span>/</span>
          <span aria-current="page">Fiber Internet</span>
        </nav>
        <div style="max-width: 760px;">
          <span class="subheading-badge">100% Optical Glass FTTH</span>
          <h1 class="display-title" style="margin-bottom: var(--space-4);">
            Pure Fiber Optics: The Technology Behind Seamless Connectivity
          </h1>
          <p class="lead">
            Discover why pulses of light traveling through ultra-pure silica glass strands deliver lower latency, immune signal integrity, and true symmetrical gigabit speeds compared to aging copper networks.
          </p>
        </div>
      </div>
    </section>

    <!-- FIBER VS COPPER DEEP DIVE -->
    <section class="section">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1fr; gap: var(--space-8); align-items: center;" class="editorial-split-grid">
          <div>
            <span class="subheading-badge">The Technology</span>
            <h2>Light-Speed Data Transmission</h2>
            <p style="font-size: var(--text-base); line-height: var(--leading-relaxed); color: var(--color-ink); margin-bottom: var(--space-4);">
              Traditional cable broadband relies on electrical signals passing through copper coaxial cables. Over distance, copper suffers from signal degradation, heat loss, and heavy electromagnetic interference caused by elevators, power lines, and monsoons.
            </p>
            <p style="font-size: var(--text-base); line-height: var(--leading-relaxed); color: var(--color-ink); margin-bottom: var(--space-4);">
              <strong>Sevenseas Fiber-to-the-Home (FTTH)</strong> replaces electrical copper entirely. Data is encoded into laser light pulses that travel through hair-thin strands of ultra-pure silica glass at approximately 200,000 kilometers per second. Because light doesn't conduct electricity, your connection remains crystal clear even during thunderstorms.
            </p>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4); margin-top: var(--space-6);">
              <div style="background: var(--tint-emerald); padding: var(--space-4); border-radius: var(--radius-sm); border: 1px solid rgba(15, 157, 117, 0.2);">
                <strong style="color: var(--color-emerald-text); font-size: var(--text-sm); display: block; margin-bottom: 2px;">Pure FTTH Fiber</strong>
                <span class="text-muted" style="font-size: var(--text-xs);">Light pulses • Symmetrical upload/download • Weatherproof • &lt;5ms ping</span>
              </div>
              <div style="background: #F8F9FA; padding: var(--space-4); border-radius: var(--radius-sm); border: 1px solid var(--color-border);">
                <strong style="color: #64748B; font-size: var(--text-sm); display: block; margin-bottom: 2px;">Legacy Copper Cable</strong>
                <span class="text-muted" style="font-size: var(--text-xs);">Electrical signals • Asymmetric slow upload • Prone to rain noise • 30-80ms ping</span>
              </div>
            </div>
          </div>

          <div>
            <picture>
              <source srcset="public/assets/images/fiber-infrastructure.avif" type="image/avif">
              <img src="public/assets/images/fiber-infrastructure.jpg" alt="Macro photograph of glowing optical fiber distribution patch cables in telecom rack" style="width: 100%; height: auto; border-radius: var(--radius-lg); box-shadow: var(--shadow-lg); display: block;" loading="lazy">
            </picture>
          </div>
        </div>
      </div>
    </section>

    <!-- ARCHITECTURAL CABLE CUTAWAY -->
    <section class="section section-alt">
      <div class="container">
        <div class="section-header text-center">
          <span class="subheading-badge">Cable Architecture</span>
          <h2>Inside the Sevenseas Optical Fiber Cable</h2>
          <p class="lead" style="margin-left: auto; margin-right: auto;">Engineered with 4 defensive layers for zero attenuation and lifelong residential durability.</p>
        </div>

        <div style="max-width: 800px; margin: 0 auto;">
          <img src="public/assets/images/fiber-cable-cutaway.svg" alt="Sevenseas Optical Fiber Cable Anatomy" style="width: 100%; height: auto; border-radius: var(--radius-md); box-shadow: var(--shadow-md); margin-bottom: var(--space-6);" />

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: var(--space-4);">
            <div class="card" style="padding: var(--space-4);">
              <strong style="color: var(--color-navy); font-size: var(--text-sm); display: block;">1. LSZH Outer Jacket</strong>
              <p class="text-muted" style="font-size: var(--text-xs); margin: 4px 0 0;">Low-smoke zero-halogen flame-retardant outer layer protecting against UV and bends.</p>
            </div>
            <div class="card" style="padding: var(--space-4);">
              <strong style="color: var(--color-orange-text); font-size: var(--text-sm); display: block;">2. Kevlar Aramid Yarn</strong>
              <p class="text-muted" style="font-size: var(--text-xs); margin: 4px 0 0;">Ultra-high tensile strength synthetic fibers that prevent cable stretching during pulling.</p>
            </div>
            <div class="card" style="padding: var(--space-4);">
              <strong style="color: var(--color-navy); font-size: var(--text-sm); display: block;">3. Silica Cladding (125µm)</strong>
              <p class="text-muted" style="font-size: var(--text-xs); margin: 4px 0 0;">Lower refractive index glass that reflects light pulses back into the center core.</p>
            </div>
            <div class="card" style="padding: var(--space-4);">
              <strong style="color: var(--color-emerald-text); font-size: var(--text-sm); display: block;">4. Glass Core (9µm)</strong>
              <p class="text-muted" style="font-size: var(--text-xs); margin: 4px 0 0;">Single-mode optical waveguide carrying high-frequency data photons at the speed of light.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SYMMETRICAL SPEED EXPLAINED -->
    <section class="section">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1fr; gap: var(--space-8); align-items: center;" class="editorial-split-grid">
          <div>
            <span class="subheading-badge">Symmetrical Advantage</span>
            <h2>Why Upload Speed Matters Just as Much as Download</h2>
            <p style="font-size: var(--text-base); line-height: var(--leading-relaxed); color: var(--color-ink); margin-bottom: var(--space-4);">
              Most legacy ISPs offer "asymmetric" internet—giving you 100 Mbps download but throttling your upload to an abysmal 5 or 10 Mbps. That made sense fifteen years ago when users only browsed web pages.
            </p>
            <p style="font-size: var(--text-base); line-height: var(--leading-relaxed); color: var(--color-ink); margin-bottom: var(--space-4);">
              In modern homes, everything you do requires high-speed upload bandwidth:
            </p>
            <ul class="feature-list" style="margin-bottom: var(--space-6);">
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> <strong>HD Two-Way Video Calls:</strong> Zoom, Microsoft Teams, and Google Meet transmit your camera feed via your upload pipe.</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> <strong>Cloud Photo &amp; Video Backups:</strong> Google Drive, iCloud, and OneDrive upload in the background seamlessly.</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> <strong>Smart Home Security Feeds:</strong> Live 1080p surveillance streams upload constantly from home cameras.</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> <strong>Multiplayer Online Gaming:</strong> Game controllers send continuous input coordinates to multiplayer game servers.</li>
            </ul>

            <div style="display: flex; gap: var(--space-4); flex-wrap: wrap;">
              <a href="plans.html" class="btn btn-primary">Choose Symmetrical Fiber Plan</a>
              <a href="new-connection.html" class="btn btn-outline-navy">Book Doorstep Installation</a>
            </div>
          </div>

          <div>
            <div class="card" style="padding: var(--space-8); background-color: var(--color-white); border-radius: var(--radius-lg); box-shadow: var(--shadow-lg);">
              <h3 style="margin-bottom: var(--space-4); color: var(--color-navy);">The Sevenseas Speed Guarantee</h3>
              <div style="display: flex; flex-direction: column; gap: var(--space-6);">
                <div>
                  <div style="display: flex; justify-content: space-between; font-size: var(--text-sm); margin-bottom: 4px;">
                    <span>Download Speed</span>
                    <strong style="color: var(--color-orange);">500 Mbps</strong>
                  </div>
                  <div style="height: 12px; background: var(--tint-orange); border-radius: 6px; overflow: hidden;">
                    <div style="width: 100%; height: 100%; background: var(--color-orange);"></div>
                  </div>
                </div>

                <div>
                  <div style="display: flex; justify-content: space-between; font-size: var(--text-sm); margin-bottom: 4px;">
                    <span>Upload Speed</span>
                    <strong style="color: var(--color-emerald-text);">500 Mbps (100% Symmetrical)</strong>
                  </div>
                  <div style="height: 12px; background: var(--tint-emerald); border-radius: 6px; overflow: hidden;">
                    <div style="width: 100%; height: 100%; background: var(--color-emerald);"></div>
                  </div>
                </div>

                <div style="border-top: 1px solid var(--color-border); padding-top: var(--space-4); display: flex; justify-content: space-between; align-items: center;">
                  <span class="text-muted" style="font-size: var(--text-xs);">Direct Peering Ping</span>
                  <span class="status-indicator"><span class="pulse-dot"></span> &lt; 4ms (NIXI / Extreme IX)</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    """
