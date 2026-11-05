"""
Coverage Areas page content generator for Sevenseas Broadband.
"""

def get_content():
    return """
    <!-- PAGE HERO -->
    <section class="page-hero">
      <div class="container">
        <nav aria-label="Breadcrumb" class="breadcrumbs">
          <a href="index.html">Home</a>
          <span>/</span>
          <span aria-current="page">Coverage Areas</span>
        </nav>
        <div style="max-width: 760px;">
          <span class="subheading-badge">Live Optical Network Map</span>
          <h1 class="display-title" style="margin-bottom: var(--space-4);">
            Check Fiber Broadband Availability in Your Neighborhood
          </h1>
          <p class="lead">
            Sevenseas operates a dense, growing optical fiber ring across key residential sectors, apartment societies, and residential hubs. Search your society or address below.
          </p>
        </div>
      </div>
    </section>

    <!-- INTERACTIVE COVERAGE SEARCH -->
    <section class="section">
      <div class="container">
        <div style="background-color: var(--color-white); border: 1.5px solid var(--color-border); border-radius: var(--radius-lg); padding: var(--space-8); box-shadow: var(--shadow-md); max-width: 840px; margin: 0 auto var(--space-12);">
          <div style="text-align: center; margin-bottom: var(--space-6);">
            <span class="badge badge-emerald"><span class="pulse-dot"></span> Optical Coverage Engine Active</span>
            <h3 style="margin-top: var(--space-2); margin-bottom: var(--space-1);">Instant Building Fiber Check</h3>
            <p class="text-muted" style="font-size: var(--text-sm); margin: 0;">Enter your building name, residential society, or street address.</p>
          </div>

          <form class="coverage-checker-bar" onsubmit="event.preventDefault(); document.getElementById('coveragePageResult').style.display = 'block';">
            <div style="display: flex; align-items: center; gap: var(--space-2); flex: 1; padding: 0 0.5rem;">
              <svg class="icon icon-sm" style="color: var(--color-orange);"><use href="#icon-map-pin"></use></svg>
              <input type="text" id="coverageSearchInput" placeholder="e.g. Hiranandani Gardens, Lokhandwala, Seawoods..." required aria-label="Enter your building or locality" />
            </div>
            <button type="submit" class="btn btn-primary">Check Availability</button>
          </form>

          <!-- Interactive Results Reveal -->
          <div id="coveragePageResult" style="display: none; margin-top: var(--space-6); padding: var(--space-6); background-color: var(--tint-emerald); border: 1px solid rgba(15, 157, 117, 0.25); border-radius: var(--radius-md);">
            <div style="display: flex; align-items: flex-start; gap: var(--space-4);">
              <div style="width: 36px; height: 36px; border-radius: 50%; background: var(--color-emerald); color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.2rem; flex-shrink: 0;">✓</div>
              <div>
                <strong style="color: var(--color-emerald-text); font-size: var(--text-lg); display: block; margin-bottom: 4px;">Gigabit Fiber is Live at This Address!</strong>
                <p style="font-size: var(--text-sm); color: var(--color-ink); margin-bottom: var(--space-4);">
                  Your residential complex is connected to our primary 10 Gbps optical distribution ring. Free doorstep installation and complimentary dual-band ONT are available immediately.
                </p>
                <div style="display: flex; gap: var(--space-3); flex-wrap: wrap;">
                  <a href="new-connection.html" class="btn btn-emerald btn-sm">Book Same-Day Installation &rarr;</a>
                  <a href="plans.html" class="btn btn-outline-navy btn-sm">Review Plans</a>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- ACTIVE RESIDENTIAL FIBER HUBS -->
        <div class="section-header text-center">
          <span class="subheading-badge">Current Coverage Footprint</span>
          <h2>Primary Residential Fiber Hubs</h2>
          <p class="lead" style="margin-left: auto; margin-right: auto;">High-density optical rings currently live with same-day installation capability.</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--space-6);">
          
          <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-3);">
              <h4 style="margin: 0; color: var(--color-navy);">Andheri West &amp; Lokhandwala</h4>
              <span class="badge badge-emerald" style="font-size: 0.7rem;"><span class="pulse-dot"></span> Live</span>
            </div>
            <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-3);">Oshiwara, Yamuna Nagar, Lokhandwala Complex, Versova Link Road.</p>
            <div style="font-size: var(--text-xs); color: var(--color-ink); border-top: 1px solid var(--color-border); padding-top: var(--space-2);">
              <strong>Avg Ping:</strong> 3.2ms • <strong>Hub Ring:</strong> Dual 10G
            </div>
          </div>

          <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-3);">
              <h4 style="margin: 0; color: var(--color-navy);">Bandra &amp; Khar West</h4>
              <span class="badge badge-emerald" style="font-size: 0.7rem;"><span class="pulse-dot"></span> Live</span>
            </div>
            <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-3);">Pali Hill, Carter Road, Turner Road, 14th Road, Khar Danda.</p>
            <div style="font-size: var(--text-xs); color: var(--color-ink); border-top: 1px solid var(--color-border); padding-top: var(--space-2);">
              <strong>Avg Ping:</strong> 2.9ms • <strong>Hub Ring:</strong> Redundant Optical
            </div>
          </div>

          <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-3);">
              <h4 style="margin: 0; color: var(--color-navy);">Powai &amp; Hiranandani</h4>
              <span class="badge badge-emerald" style="font-size: 0.7rem;"><span class="pulse-dot"></span> Live</span>
            </div>
            <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-3);">Hiranandani Gardens, Raheja Vihar, Chandivali, Saki Vihar Road.</p>
            <div style="font-size: var(--text-xs); color: var(--color-ink); border-top: 1px solid var(--color-border); padding-top: var(--space-2);">
              <strong>Avg Ping:</strong> 3.4ms • <strong>Hub Ring:</strong> Pure FTTH
            </div>
          </div>

          <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-3);">
              <h4 style="margin: 0; color: var(--color-navy);">Thane West</h4>
              <span class="badge badge-emerald" style="font-size: 0.7rem;"><span class="pulse-dot"></span> Live</span>
            </div>
            <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-3);">Ghopbunder Road, Hiranandani Estate, Vasant Vihar, Pokhran Road.</p>
            <div style="font-size: var(--text-xs); color: var(--color-ink); border-top: 1px solid var(--color-border); padding-top: var(--space-2);">
              <strong>Avg Ping:</strong> 4.1ms • <strong>Hub Ring:</strong> Gigabit Backbone
            </div>
          </div>

          <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-3);">
              <h4 style="margin: 0; color: var(--color-navy);">Navi Mumbai</h4>
              <span class="badge badge-emerald" style="font-size: 0.7rem;"><span class="pulse-dot"></span> Live</span>
            </div>
            <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-3);">Seawoods, Nerul, Vashi Sectors, Kharghar Hiranandani.</p>
            <div style="font-size: var(--text-xs); color: var(--color-ink); border-top: 1px solid var(--color-border); padding-top: var(--space-2);">
              <strong>Avg Ping:</strong> 3.8ms • <strong>Hub Ring:</strong> Redundant Ring
            </div>
          </div>

          <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-3);">
              <h4 style="margin: 0; color: var(--color-navy);">Goregaon &amp; Malad West</h4>
              <span class="badge badge-emerald" style="font-size: 0.7rem;"><span class="pulse-dot"></span> Live</span>
            </div>
            <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-3);">Mindspace, Chincholi Bunder, Bangur Nagar, New Link Road.</p>
            <div style="font-size: var(--text-xs); color: var(--color-ink); border-top: 1px solid var(--color-border); padding-top: var(--space-2);">
              <strong>Avg Ping:</strong> 3.5ms • <strong>Hub Ring:</strong> 10G Ring
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- REQUEST EXPANSION FOR UNLISTED BUILDINGS -->
    <section class="section section-alt">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1fr; gap: var(--space-8); align-items: center;" class="editorial-split-grid">
          <div>
            <span class="subheading-badge">Bring Fiber to Your Building</span>
            <h2>Is Your Society Not on the Map Yet?</h2>
            <p class="lead" style="margin-bottom: var(--space-4);">
              We expand our optical rings into new residential housing societies upon request by residents or managing committees.
            </p>
            <p style="font-size: var(--text-sm); line-height: var(--leading-relaxed); color: var(--color-ink); margin-bottom: var(--space-4);">
              If your apartment complex or society has 10 or more interested households, our network engineering team can pull dedicated optical cabling and install an on-premise distribution hub within 72 hours—at zero capital expense to your society.
            </p>

            <ul class="feature-list" style="margin-bottom: var(--space-6);">
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> Zero cost to Housing Society or RWA</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> Neat, concealed optical riser cabling</li>
              <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> Society office gets a complimentary high-speed connection</li>
            </ul>

            <a href="contact.html?type=society" class="btn btn-secondary">Request Society Survey</a>
          </div>

          <div>
            <div class="card" style="padding: var(--space-8); background-color: var(--color-white); border-radius: var(--radius-lg); box-shadow: var(--shadow-md);">
              <h3 style="margin-bottom: var(--space-2); color: var(--color-navy);">Request Expansion in Your Area</h3>
              <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-4);">Submit your details and our local field surveyor will contact you.</p>

              <form data-validate data-ajax="true">
                <div class="form-group">
                  <label class="form-label" for="reqName">Your Name</label>
                  <input type="text" id="reqName" class="form-input" placeholder="e.g. Rahul Sharma" required />
                  <div class="form-error" id="error-reqName" style="display: none;">Please provide your name</div>
                </div>

                <div class="form-group">
                  <label class="form-label" for="reqPhone">Mobile Number</label>
                  <input type="tel" id="reqPhone" class="form-input" placeholder="e.g. 98200 12345" required />
                  <div class="form-error" id="error-reqPhone" style="display: none;">Please enter a valid phone number</div>
                </div>

                <div class="form-group">
                  <label class="form-label" for="reqSociety">Building / Society &amp; Area</label>
                  <input type="text" id="reqSociety" class="form-input" placeholder="e.g. Green Meadows CHS, Sector 19" required />
                  <div class="form-error" id="error-reqSociety" style="display: none;">Please enter your building name</div>
                </div>

                <div class="form-success-alert" style="display: none; padding: var(--space-3); background: var(--tint-emerald); color: var(--color-emerald-text); border-radius: var(--radius-xs); font-size: var(--text-xs); margin-bottom: var(--space-3);">
                  ✓ Request recorded! Our local expansion team will survey your building.
                </div>

                <button type="submit" class="btn btn-primary" style="width: 100%;">Submit Expansion Request</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
    """
