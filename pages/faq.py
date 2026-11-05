"""
FAQ page content generator for Sevenseas Broadband.
"""

def get_content():
    return """
    <!-- PAGE HERO -->
    <section class="page-hero">
      <div class="container">
        <nav aria-label="Breadcrumb" class="breadcrumbs">
          <a href="index.html">Home</a>
          <span>/</span>
          <span aria-current="page">Frequently Asked Questions</span>
        </nav>
        <div style="max-width: 760px;">
          <span class="subheading-badge">Help &amp; Answers</span>
          <h1 class="display-title" style="margin-bottom: var(--space-4);">
            Frequently Asked Questions
          </h1>
          <p class="lead">
            Find immediate answers regarding our fiber broadband plans, installation timelines, Wi-Fi router setup, symmetrical speeds, and billing cycles.
          </p>
        </div>
      </div>
    </section>

    <!-- FAQS ACCORDION BY CATEGORY -->
    <section class="section">
      <div class="container">
        
        <!-- Category 1: Getting Started & Installation -->
        <div style="max-width: 820px; margin: 0 auto var(--space-12);">
          <div style="display: flex; align-items: center; gap: var(--space-3); margin-bottom: var(--space-6); border-bottom: 2px solid var(--color-border); padding-bottom: var(--space-3);">
            <div class="icon-box icon-box-orange"><svg class="icon"><use href="#icon-wrench"></use></svg></div>
            <h2 style="margin: 0; font-size: var(--text-2xl);">1. Getting Started &amp; Installation</h2>
          </div>

          <div class="faq-accordion">
            <div class="faq-item is-active">
              <button class="faq-question" aria-expanded="true">
                <span>How quickly can I get Sevenseas Fiber installed in my home?</span>
                <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
              </button>
              <div class="faq-answer">
                <p>If your residential society is already connected to our optical distribution ring, installation is completed within <strong>4 to 8 business hours</strong> of your booking. For new societies undergoing riser cabling, installation takes 24 to 48 hours.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                <span>Are there any installation or activation charges?</span>
                <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
              </button>
              <div class="faq-answer">
                <p>Installation is <strong>completely free (₹0)</strong> on all 3-month, 6-month, and annual plan subscriptions. For month-to-month plans, a nominal one-time cabling fee of ₹500 applies.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                <span>What documents do I need to keep ready for KYC?</span>
                <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
              </button>
              <div class="faq-answer">
                <p>In accordance with Department of Telecommunications (DoT) norms, you will need: (1) Proof of Identity (Aadhaar, Passport, or Voter ID), (2) Proof of Address (Aadhaar, electricity bill, or registered rent agreement), and (3) A digital photo taken by our technician during doorstep activation.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                <span>Will there be messy drilling or exposed cables inside my home?</span>
                <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
              </button>
              <div class="faq-answer">
                <p>No. Our certified optical technicians use ultra-slim, bend-insensitive optical micro-cables (G.657.A2 standard) routed neatly along existing doorframes and baseboards using discrete clips, terminated cleanly into an optical wall faceplate.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Category 2: Speeds & Technical Performance -->
        <div style="max-width: 820px; margin: 0 auto var(--space-12);">
          <div style="display: flex; align-items: center; gap: var(--space-3); margin-bottom: var(--space-6); border-bottom: 2px solid var(--color-border); padding-bottom: var(--space-3);">
            <div class="icon-box icon-box-emerald"><svg class="icon"><use href="#icon-gauge"></use></svg></div>
            <h2 style="margin: 0; font-size: var(--text-2xl);">2. Speeds &amp; Technical Performance</h2>
          </div>

          <div class="faq-accordion">
            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                <span>What does "symmetrical speeds" mean?</span>
                <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
              </button>
              <div class="faq-answer">
                <p>Symmetrical speed means your <strong>upload speed is identical to your download speed</strong>. For example, on our Gigabit Max 500 plan, you get 500 Mbps download and 500 Mbps upload. Legacy copper cable ISPs often offer only 10% upload speed.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                <span>Why is optical fiber faster and more reliable than copper cable?</span>
                <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
              </button>
              <div class="faq-answer">
                <p>Fiber optics transmit data using laser light pulses through pure glass rather than electrical signals through copper. Light pulses do not degrade over long distances, generate zero heat, and are completely unaffected by heavy rain, monsoons, or electrical noise.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                <span>What kind of ping latency can online gamers expect?</span>
                <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
              </button>
              <div class="faq-answer">
                <p>Because Sevenseas peers directly with local Internet Exchanges (NIXI, Extreme IX, and AMS-IX Mumbai), online gamers consistently receive <strong>sub-5ms ping</strong> to regional Indian servers in games like Valorant, BGMI, and Counter-Strike.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                <span>Is data truly unlimited, or is there an FUP cap?</span>
                <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
              </button>
              <div class="faq-answer">
                <p>All Sevenseas residential plans offer <strong>truly unlimited unthrottled data</strong>. There are no daily limits, weekend slowdowns, or hidden data counters.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Category 3: Wi-Fi Routers & Hardware -->
        <div style="max-width: 820px; margin: 0 auto var(--space-12);">
          <div style="display: flex; align-items: center; gap: var(--space-3); margin-bottom: var(--space-6); border-bottom: 2px solid var(--color-border); padding-bottom: var(--space-3);">
            <div class="icon-box icon-box-violet"><svg class="icon"><use href="#icon-router"></use></svg></div>
            <h2 style="margin: 0; font-size: var(--text-2xl);">3. Wi-Fi Routers &amp; Hardware</h2>
          </div>

          <div class="faq-accordion">
            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                <span>Do I need to buy my own router?</span>
                <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
              </button>
              <div class="faq-answer">
                <p>No. We provide an enterprise-grade Optical Network Terminal (ONT) with integrated dual-band Wi-Fi free of charge on loan. For our Gigabit Max 500 and Ultra 1000 plans, you receive a cutting-edge <strong>Wi-Fi 6 Gateway</strong>.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                <span>Can I use my own mesh Wi-Fi system?</span>
                <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
              </button>
              <div class="faq-answer">
                <p>Yes! Our ONT hardware supports bridge mode and connects seamlessly to any third-party mesh system (TP-Link Deco, Netgear Orbi, Asus AiMesh) via a standard Gigabit Ethernet LAN port.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                <span>How many devices can connect to the Wi-Fi at once?</span>
                <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
              </button>
              <div class="faq-answer">
                <p>Our standard dual-band router supports up to 15 simultaneous devices. Our Wi-Fi 6 Gigabit Gateway supports 30+ simultaneous smart home devices, TVs, laptops, and consoles with zero congestion.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Category 4: Billing & Relocation -->
        <div style="max-width: 820px; margin: 0 auto;">
          <div style="display: flex; align-items: center; gap: var(--space-3); margin-bottom: var(--space-6); border-bottom: 2px solid var(--color-border); padding-bottom: var(--space-3);">
            <div class="icon-box icon-box-navy"><svg class="icon"><use href="#icon-phone"></use></svg></div>
            <h2 style="margin: 0; font-size: var(--text-2xl);">4. Billing, Shifting &amp; Support</h2>
          </div>

          <div class="faq-accordion">
            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                <span>What happens if I move to a new apartment or building?</span>
                <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
              </button>
              <div class="faq-answer">
                <p>Relocation is completely free within our service coverage areas. Just notify our support team 48 hours before moving, take your ONT router along, and our field technician will reconnect you at your new address on moving day.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                <span>How do I pay my monthly bill?</span>
                <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
              </button>
              <div class="faq-answer">
                <p>You can pay instantly online through UPI (Google Pay, PhonePe, Paytm), Net Banking, Credit/Debit cards via our self-service Quick Pay portal or via direct WhatsApp payment link sent to your registered mobile number.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                <span>What is the cancellation process if I need to disconnect?</span>
                <svg class="icon icon-sm"><use href="#icon-chevron-down"></use></svg>
              </button>
              <div class="faq-answer">
                <p>You can cancel at any time with zero penalty. Simply notify us via email or call our toll-free number. Our technician will collect the loaner ONT equipment, and any eligible security deposit will be refunded to your bank account within 5 to 7 business days.</p>
              </div>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- STILL HAVE QUESTIONS CTA -->
    <section style="background-color: var(--color-navy); color: #FFFFFF; padding: var(--space-10) 0; margin-top: var(--space-12);">
      <div class="container" style="text-align: center;">
        <h3 style="color: #FFFFFF; margin-bottom: var(--space-2);">Still Have a Question We Haven't Covered?</h3>
        <p style="color: #CBD5E1; font-size: var(--text-sm); margin-bottom: var(--space-6);">Our neighborhood broadband experts are available 24/7 on call and WhatsApp.</p>
        <div style="display: flex; gap: var(--space-4); justify-content: center; flex-wrap: wrap;">
          <a href="https://wa.me/919664985535?text=Hi%20Sevenseas%20Broadband,%20I%20have%20a%20question%20about%20plans" target="_blank" rel="noopener" class="btn btn-emerald" style="display: inline-flex; align-items: center; gap: 6px;">
            <svg class="icon icon-sm" style="width: 20px; height: 20px;"><use href="#icon-whatsapp"></use></svg> Chat on WhatsApp
          </a>
          <a href="tel:9664985535" class="btn btn-primary">
            <svg class="icon icon-sm"><use href="#icon-phone"></use></svg> Call: +91 96649 85535
          </a>
        </div>
      </div>
    </section>

    <!-- Schema.org FAQPage Structured Data -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How quickly can my new fiber connection be installed?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In fiber-ready buildings across Airoli, we offer same-day installation within 4 to 6 hours. For other buildings, standard doorstep installation is completed within 24 to 48 hours."
          }
        },
        {
          "@type": "Question",
          "name": "Is there any upfront installation charge?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Installation is ₹0 completely free on our Popular 200 Mbps plan and all quarterly and annual subscription durations."
          }
        },
        {
          "@type": "Question",
          "name": "What documents are required for KYC verification?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "In accordance with DoT regulations, please have your Aadhaar Card, Passport, or Voter ID for proof of identity, and an electricity bill or rent agreement for proof of address."
          }
        },
        {
          "@type": "Question",
          "name": "What does symmetrical speed mean?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Symmetrical speed means your upload speed exactly matches your download speed. For example, on our 200 Mbps plan, you get 200 Mbps download and 200 Mbps upload."
          }
        },
        {
          "@type": "Question",
          "name": "Is there any data limit or FUP policy?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. Sevenseas Broadband provides truly unlimited, unmetered data with zero fair-usage policy (FUP) throttling."
          }
        }
      ]
    }
    </script>
    """
