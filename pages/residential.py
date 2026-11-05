"""
Residential Internet page content generator for Sevenseas Broadband.
"""

def get_content():
    return """
    <!-- PAGE HERO -->
    <section class="page-hero">
      <div class="container">
        <nav aria-label="Breadcrumb" class="breadcrumbs">
          <a href="index.html">Home</a>
          <span>/</span>
          <span aria-current="page">Residential Internet</span>
        </nav>
        <div style="max-width: 760px;">
          <span class="subheading-badge">Family-Oriented Broadband</span>
          <h1 class="display-title" style="margin-bottom: var(--space-4);">
            Fiber Internet Engineered for Everyday Family Living
          </h1>
          <p class="lead">
            Every connected device in your home deserves seamless speed. From living room 4K cinema to kids' online classes and remote office meetings, Sevenseas provides whole-home Wi-Fi coverage with zero dead zones.
          </p>
        </div>
      </div>
    </section>

    <!-- RESIDENTIAL HERO FEATURE BLOCK -->
    <section class="section">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1fr; gap: var(--space-8); align-items: center;" class="editorial-split-grid">
          <div>
            <span class="subheading-badge">Living Room 4K</span>
            <h2>Multi-Device Streaming Without Buffering</h2>
            <p style="font-size: var(--text-base); line-height: var(--leading-relaxed); color: var(--color-ink); margin-bottom: var(--space-4);">
              Modern households in India have between 8 to 20 devices connected at once: smart TVs, parents' laptops, kids' tablets, smartphones, and security cameras. Standard broadband chokes when multiple people stream or download simultaneously.
            </p>
            <p style="font-size: var(--text-base); line-height: var(--leading-relaxed); color: var(--color-ink); margin-bottom: var(--space-4);">
              With Sevenseas FTTH, bandwidth is delivered over dedicated optical pipelines that do not slow down during evening prime time. Your kids can watch 4K cartoons, parents can attend high-priority office calls, and grandparents can video call family abroad with zero stutter.
            </p>
            <div style="display: flex; gap: var(--space-3); flex-wrap: wrap;">
              <a href="plans.html" class="btn btn-primary">Explore Residential Plans</a>
              <a href="new-connection.html" class="btn btn-outline-navy">Book Home Installation</a>
            </div>
          </div>

          <div>
            <picture>
              <source srcset="public/assets/images/family-entertainment.avif" type="image/avif">
              <img src="public/assets/images/family-entertainment.jpg" alt="Joyful multi-generational Indian family enjoying 4K television together in warm evening living room" style="width: 100%; height: auto; border-radius: var(--radius-lg); box-shadow: var(--shadow-lg); display: block;" loading="lazy">
            </picture>
          </div>
        </div>
      </div>
    </section>

    <!-- WHOLE HOME WI-FI 6 MESH -->
    <section class="section section-alt">
      <div class="container">
        <div class="section-header text-center">
          <span class="subheading-badge">Wall-to-Wall Wi-Fi</span>
          <h2>Zero Dead Zones in Any Room</h2>
          <p class="lead" style="margin-left: auto; margin-right: auto;">
            Our Dual-Band Wi-Fi 6 routers and intelligent mesh nodes ensure strong wireless coverage across thick concrete walls, bedrooms, and balconies.
          </p>
        </div>

        <div style="display: grid; grid-template-columns: 1fr; gap: var(--space-8); align-items: center;" class="editorial-split-grid">
          <div>
            <img src="public/assets/images/wifi6-mesh-coverage.svg" alt="Sevenseas Wi-Fi 6 Mesh Coverage Map" style="width: 100%; height: auto; border-radius: var(--radius-md); box-shadow: var(--shadow-sm);" />
          </div>

          <div>
            <h3 style="margin-bottom: var(--space-4); color: var(--color-navy);">Intelligent Band Steering &amp; Roaming</h3>
            <p style="font-size: var(--text-sm); line-height: var(--leading-relaxed); color: var(--color-ink); margin-bottom: var(--space-4);">
              Traditional single routers lose speed the further you walk into your bedroom or balcony. Sevenseas equips your home with an enterprise-grade ONT router featuring intelligent band steering (2.4 GHz + 5 GHz) and optional mesh nodes.
            </p>

            <div style="display: flex; flex-direction: column; gap: var(--space-3); margin-bottom: var(--space-6);">
              <div style="display: flex; gap: var(--space-3); align-items: flex-start;">
                <svg class="icon icon-sm" style="color: var(--color-emerald);"><use href="#icon-check"></use></svg>
                <div>
                  <strong style="color: var(--color-navy); font-size: var(--text-sm);">OFDMA Technology:</strong>
                  <span class="text-muted" style="font-size: var(--text-xs); display: block;">Transmits data packets to multiple devices simultaneously, eliminating queue waiting.</span>
                </div>
              </div>
              <div style="display: flex; gap: var(--space-3); align-items: flex-start;">
                <svg class="icon icon-sm" style="color: var(--color-emerald);"><use href="#icon-check"></use></svg>
                <div>
                  <strong style="color: var(--color-navy); font-size: var(--text-sm);">Seamless Roaming:</strong>
                  <span class="text-muted" style="font-size: var(--text-xs); display: block;">Walk from your living room sofa to your balcony without dropping WhatsApp or Zoom calls.</span>
                </div>
              </div>
              <div style="display: flex; gap: var(--space-3); align-items: flex-start;">
                <svg class="icon icon-sm" style="color: var(--color-emerald);"><use href="#icon-check"></use></svg>
                <div>
                  <strong style="color: var(--color-navy); font-size: var(--text-sm);">Built-in WPA3 Security:</strong>
                  <span class="text-muted" style="font-size: var(--text-xs); display: block;">Next-generation wireless encryption protecting your home smart locks and cameras from intruders.</span>
                </div>
              </div>
            </div>

            <a href="plans.html#max-500" class="btn btn-secondary">Get Plan with Free Wi-Fi 6 Router</a>
          </div>
        </div>
      </div>
    </section>

    <!-- 4 RESIDENTIAL AUDIENCE CARDS -->
    <section class="section">
      <div class="container">
        <div class="section-header text-center">
          <span class="subheading-badge">Tailored For Every Generation</span>
          <h2>How Sevenseas Powers Your Household</h2>
          <p class="lead" style="margin-left: auto; margin-right: auto;">Engineered to support every ambition under your roof.</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--space-6);">
          
          <div class="card">
            <div class="icon-box icon-box-emerald" style="margin-bottom: var(--space-4);">
              <svg class="icon"><use href="#icon-laptop"></use></svg>
            </div>
            <h4 style="margin-bottom: var(--space-2);">Remote Professionals</h4>
            <p class="text-muted" style="font-size: var(--text-sm); line-height: var(--leading-relaxed);">
              Say goodbye to frozen video screens and delayed audio. Symmetrical gigabit fiber means you present your decks and talk to international clients with complete peace of mind.
            </p>
          </div>

          <div class="card">
            <div class="icon-box icon-box-violet" style="margin-bottom: var(--space-4);">
              <svg class="icon"><use href="#icon-monitor-play"></use></svg>
            </div>
            <h4 style="margin-bottom: var(--space-2);">Students &amp; Exam Prep</h4>
            <p class="text-muted" style="font-size: var(--text-sm); line-height: var(--leading-relaxed);">
              Instant loading of high-resolution digital textbooks, uninterrupted lecture streams, and fast upload of university assignments before deadlines.
            </p>
          </div>

          <div class="card">
            <div class="icon-box icon-box-orange" style="margin-bottom: var(--space-4);">
              <svg class="icon"><use href="#icon-gamepad-2"></use></svg>
            </div>
            <h4 style="margin-bottom: var(--space-2);">Low-Ping Gaming</h4>
            <p class="text-muted" style="font-size: var(--text-sm); line-height: var(--leading-relaxed);">
              Experience true sub-5ms latency directly to Mumbai and Chennai gaming clusters in Valorant, BGMI, and CS2 with zero packet loss.
            </p>
          </div>

          <div class="card">
            <div class="icon-box" style="margin-bottom: var(--space-4);">
              <svg class="icon"><use href="#icon-shield-check"></use></svg>
            </div>
            <h4 style="margin-bottom: var(--space-2);">Smart Home &amp; IoT</h4>
            <p class="text-muted" style="font-size: var(--text-sm); line-height: var(--leading-relaxed);">
              Connect your Alexa, Google Home, smart bulbs, robotic vacuums, and continuous cloud CCTV cameras with dedicated 2.4 GHz IoT channels.
            </p>
          </div>

        </div>
      </div>
    </section>
    """
