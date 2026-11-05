"""
About Us page content generator for Sevenseas Broadband.
"""

def get_content():
    return """
    <!-- PAGE HERO -->
    <section class="page-hero">
      <div class="container">
        <nav aria-label="Breadcrumb" class="breadcrumbs">
          <a href="index.html">Home</a>
          <span>/</span>
          <span aria-current="page">About Us</span>
        </nav>
        <div style="max-width: 760px;">
          <span class="subheading-badge">Connecting Every Home</span>
          <h1 class="display-title" style="margin-bottom: var(--space-4);">
            Building Reliable Fiber Infrastructure for Real Communities
          </h1>
          <p class="lead">
            Sevenseas Broadband was founded on a simple conviction: modern residential broadband should be dependable, ultra-fast, and transparently priced.
          </p>
        </div>
      </div>
    </section>

    <!-- MISSION & STORY -->
    <section class="section">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1fr; gap: var(--space-8); align-items: center;" class="editorial-split-grid">
          <div>
            <span class="subheading-badge">Our Story</span>
            <h2>Bridging the Last Mile with Pure Optical Glass</h2>
            <p style="font-size: var(--text-base); line-height: var(--leading-relaxed); color: var(--color-ink); margin-bottom: var(--space-4);">
              For years, residential internet in Indian neighborhoods suffered from a common set of frustrations: copper wires dangling from street poles that failed during the monsoon, peak-hour evening slowdowns, asymmetrical upload caps, and unhelpful call centers.
            </p>
            <p style="font-size: var(--text-base); line-height: var(--leading-relaxed); color: var(--color-ink); margin-bottom: var(--space-4);">
              Sevenseas Broadband was established to change this paradigm by building a dedicated, carrier-grade Fiber-to-the-Home (FTTH) network. By running pure optical glass fibers directly into residential apartments, housing societies, and independent homes, we eliminate copper bottlenecks entirely.
            </p>
            <div class="editorial-quote">
              “We believe internet connectivity is not a luxury—it is an essential household lifeline that connects students to education, parents to global careers, and families to entertainment.”
            </div>
          </div>

          <div>
            <picture>
              <source srcset="public/assets/images/family-streaming.avif" type="image/avif">
              <img src="public/assets/images/family-streaming.jpg" alt="Indian mother and daughter enjoying internet streaming in sunlit home" style="width: 100%; height: auto; border-radius: var(--radius-lg); box-shadow: var(--shadow-lg); display: block;" loading="lazy">
            </picture>
          </div>
        </div>
      </div>
    </section>

    <!-- 5 BRAND CORE PILLARS -->
    <section class="section section-alt">
      <div class="container">
        <div class="section-header text-center">
          <span class="subheading-badge">Our Commitment</span>
          <h2>The Values That Guide Sevenseas</h2>
          <p class="lead" style="margin-left: auto; margin-right: auto;">Five fundamental promises we make to every household connected to our optical network.</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: var(--space-6);">
          
          <div class="card">
            <div class="icon-box icon-box-orange" style="margin-bottom: var(--space-4);">
              <svg class="icon"><use href="#icon-message-circle"></use></svg>
            </div>
            <h4 style="margin-bottom: var(--space-2);">1. Friendly &amp; Approachable</h4>
            <p class="text-muted" style="font-size: var(--text-sm); margin: 0;">We speak plain language without confusing telecom jargon. When you call our support team, you talk to real humans who understand your neighborhood.</p>
          </div>

          <div class="card">
            <div class="icon-box icon-box-emerald" style="margin-bottom: var(--space-4);">
              <svg class="icon"><use href="#icon-shield-check"></use></svg>
            </div>
            <h4 style="margin-bottom: var(--space-2);">2. Reliable &amp; Trustworthy</h4>
            <p class="text-muted" style="font-size: var(--text-sm); margin: 0;">Our network is built on a redundant dual-ring optical architecture. If one main fiber cut occurs, traffic automatically switches routes in milliseconds.</p>
          </div>

          <div class="card">
            <div class="icon-box icon-box-navy" style="margin-bottom: var(--space-4);">
              <svg class="icon"><use href="#icon-network"></use></svg>
            </div>
            <h4 style="margin-bottom: var(--space-2);">3. Modern &amp; Tech-Focused</h4>
            <p class="text-muted" style="font-size: var(--text-sm); margin: 0;">We invest exclusively in future-ready hardware: Wi-Fi 6 Gigabit ONTs, low-loss single-mode optical fibers, and direct CDN caching servers.</p>
          </div>

          <div class="card">
            <div class="icon-box icon-box-orange" style="margin-bottom: var(--space-4);">
              <svg class="icon"><use href="#icon-monitor-play"></use></svg>
            </div>
            <h4 style="margin-bottom: var(--space-2);">4. Family-Oriented</h4>
            <p class="text-muted" style="font-size: var(--text-sm); margin: 0;">Every plan is engineered to support multi-device residential households simultaneously—smart TVs, study laptops, office PCs, and gaming consoles.</p>
          </div>

          <div class="card">
            <div class="icon-box icon-box-violet" style="margin-bottom: var(--space-4);">
              <svg class="icon"><use href="#icon-infinity"></use></svg>
            </div>
            <h4 style="margin-bottom: var(--space-2);">5. Affordable &amp; Transparent</h4>
            <p class="text-muted" style="font-size: var(--text-sm); margin: 0;">Zero hidden activation fees, zero surprise router rentals, and true unlimited data with zero mid-month throttling surprises.</p>
          </div>

        </div>
      </div>
    </section>

    <!-- NETWORK & TECHNICIANS -->
    <section class="section">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1fr; gap: var(--space-8); align-items: center;" class="editorial-split-grid">
          <div>
            <picture>
              <source srcset="public/assets/images/technician-install.avif" type="image/avif">
              <img src="public/assets/images/technician-install.jpg" alt="Sevenseas certified optical technician smiling at residential property" style="width: 100%; height: auto; border-radius: var(--radius-lg); box-shadow: var(--shadow-lg); display: block;" loading="lazy">
            </picture>
          </div>

          <div>
            <span class="subheading-badge">Local Presence</span>
            <h2>Neighborhood Support Crews, Not Distant Call Centers</h2>
            <p class="lead" style="margin-bottom: var(--space-4);">
              When an issue occurs, you don't want a generic automated chatbot ticket. You want a certified local technician who can reach your building within hours.
            </p>
            <p style="font-size: var(--text-sm); line-height: var(--leading-relaxed); color: var(--color-ink); margin-bottom: var(--space-4);">
              Sevenseas Broadband maintains dedicated rapid-response field offices stationed throughout each residential coverage zone. Our technicians are fully equipped with fusion splicers, optical power meters, and replacement ONT hardware to ensure <strong>under 4-hour mean time to repair (MTTR)</strong>.
            </p>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4); margin-bottom: var(--space-6);">
              <div style="background: var(--tint-navy); padding: var(--space-4); border-radius: var(--radius-sm);">
                <div class="stat-number" style="font-size: var(--text-2xl); color: var(--color-navy);">&lt; 4 Hours</div>
                <div class="stat-unit">Field Resolution SLA</div>
              </div>
              <div style="background: var(--tint-emerald); padding: var(--space-4); border-radius: var(--radius-sm);">
                <div class="stat-number" style="font-size: var(--text-2xl); color: var(--color-emerald-text);">99.9%</div>
                <div class="stat-unit">Network Uptime Average</div>
              </div>
            </div>

            <div style="display: flex; gap: var(--space-3); flex-wrap: wrap;">
              <a href="new-connection.html" class="btn btn-secondary">Book Your Connection</a>
              <a href="contact.html" class="btn btn-outline-navy">Contact Head Office</a>
            </div>
          </div>
        </div>
      </div>
    </section>
    """
