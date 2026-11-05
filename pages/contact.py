"""
Contact Us page generator for Sevenseas Broadband.
Fully integrates Phase 5 contact & enquiry requirements, verified Airoli contact details,
and central configuration hooks.
"""

def get_content():
    return """
    <!-- PAGE HERO -->
    <section class="page-hero">
      <div class="container">
        <nav aria-label="Breadcrumb" class="breadcrumbs">
          <a href="index.html">Home</a>
          <span>/</span>
          <span aria-current="page">Contact Us</span>
        </nav>
        <div style="max-width: 760px;">
          <span class="subheading-badge">We Are Here For You</span>
          <h1 class="display-title" style="margin-bottom: var(--space-4);">
            Get in Touch with Sevenseas Broadband
          </h1>
          <p class="lead">
            Have questions about our fiber plans, need help with installation, or want to verify coverage for your residential society in Airoli? Contact our local team directly.
          </p>
        </div>
      </div>
    </section>

    <!-- CONTACT CHANNELS & ENQUIRY FORM -->
    <section class="section">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1fr; gap: var(--space-8);" class="editorial-split-grid">
          
          <!-- Contact Details Column (Original Ad Info) -->
          <div>
            <span class="subheading-badge">Direct Communication</span>
            <h2>Immediate Assistance Channels</h2>
            <p class="lead" style="margin-bottom: var(--space-6);">
              Talk to real fiber broadband specialists located right in Airoli, Navi Mumbai.
            </p>

            <div style="display: flex; flex-direction: column; gap: var(--space-4); margin-bottom: var(--space-8);">
              
              <!-- Primary Phone -->
              <div class="card" style="display: flex; align-items: flex-start; gap: var(--space-4); padding: var(--space-5);">
                <div class="icon-box icon-box-navy">
                  <svg class="icon"><use href="#icon-phone"></use></svg>
                </div>
                <div>
                  <strong style="color: var(--color-navy); font-size: var(--text-base); display: block;">Customer Helplines</strong>
                  <div style="display: flex; flex-wrap: wrap; gap: var(--space-3); align-items: center; margin: 4px 0;">
                    <a href="tel:9664985535" style="color: var(--color-orange-text); font-size: var(--text-lg); font-weight: bold; text-decoration: none;">+91 96649 85535</a>
                    <span style="color: var(--color-border); font-size: 1.2rem;">|</span>
                    <a href="tel:7400222922" style="color: var(--color-navy); font-size: var(--text-lg); font-weight: bold; text-decoration: none;">+91 74002 22922</a>
                  </div>
                  <span class="text-muted" style="font-size: var(--text-xs);">Available daily for new connection bookings, plan upgrades, and customer support.</span>
                </div>
              </div>

              <!-- WhatsApp Direct Desk -->
              <div class="card" style="display: flex; align-items: flex-start; gap: var(--space-4); padding: var(--space-5);">
                <div class="icon-box" style="background: rgba(37, 211, 102, 0.12); color: #25D366;">
                  <svg class="icon" style="width: 24px; height: 24px;"><use href="#icon-whatsapp"></use></svg>
                </div>
                <div>
                  <strong style="color: var(--color-navy); font-size: var(--text-base); display: block;">WhatsApp Direct Desk</strong>
                  <a href="https://wa.me/919664985535?text=Hi%20Sevenseas%20Broadband,%20I%20am%20interested%20in%20a%20new%20fiber%20connection" target="_blank" rel="noopener" style="color: var(--color-emerald-text); font-size: var(--text-lg); font-weight: bold; text-decoration: none; display: block; margin: 2px 0;">+91 96649 85535</a>
                  <span class="text-muted" style="font-size: var(--text-xs);">Quick chat for society feasibility checks, instant plan queries, and installation scheduling.</span>
                </div>
              </div>

              <!-- Registered Local Office Address -->
              <div class="card" style="display: flex; align-items: flex-start; gap: var(--space-4); padding: var(--space-5);">
                <div class="icon-box icon-box-orange">
                  <svg class="icon"><use href="#icon-map-pin"></use></svg>
                </div>
                <div>
                  <strong style="color: var(--color-navy); font-size: var(--text-base); display: block;">Office &amp; Service Center</strong>
                  <p style="font-size: var(--text-sm); color: var(--color-ink); margin: 6px 0; line-height: 1.55;">
                    <strong>Shop-1, Dharmjeevan Co-op Housing Society</strong>,<br>
                    near Railway Station, Sector 3, Airoli,<br>
                    Navi Mumbai, Maharashtra 400708.
                  </p>
                  <span class="text-muted" style="font-size: var(--text-xs); display: block;">Working Hours: Mon–Sat 9:00 AM – 8:00 PM | Sun 10:00 AM – 5:00 PM</span>
                </div>
              </div>

              <!-- Field Support Alert -->
              <div style="background-color: var(--tint-emerald); border: 1px solid rgba(15, 157, 117, 0.25); border-radius: var(--radius-sm); padding: var(--space-4);">
                <strong style="color: var(--color-emerald-text); font-size: var(--text-sm); display: flex; align-items: center; gap: 6px; margin-bottom: 2px;">
                  <span class="pulse-dot"></span> Same-Day Local Splicing &amp; Activation
                </strong>
                <span style="font-size: var(--text-xs); color: var(--color-ink);">Because our technical teams operate right from Sector 3, Airoli, we offer fast doorstep assistance with average response times under 2 hours.</span>
              </div>

            </div>
          </div>

          <!-- Phase 5 Enquiry Form -->
          <div>
            <div class="card" style="padding: var(--space-8); background-color: var(--color-white); border-radius: var(--radius-lg); box-shadow: var(--shadow-md);">
              <span class="subheading-badge">New Connection &amp; Inquiries</span>
              <h3 style="margin-bottom: var(--space-1); color: var(--color-navy);">Send a Connection Enquiry</h3>
              <p class="text-muted" style="font-size: var(--text-sm); margin-bottom: var(--space-6);">Fill out the verified details below. Zero upfront charges required.</p>

              <form id="contactInquiryForm" novalidate>
                
                <!-- Status & Error Alert Container -->
                <div class="enquiry-status-alert" id="contactInquiryForm-status" role="alert" style="display: none;"></div>

                <!-- Anti-Bot Honeypot Field -->
                <div class="visually-hidden-field" aria-hidden="true">
                  <label for="c_b_website">Leave this field blank</label>
                  <input type="text" id="c_b_website" name="b_website" tabindex="-1" autocomplete="off" />
                </div>

                <!-- 1. Full Name -->
                <div class="form-group">
                  <label class="form-label" for="cFullName">Full Name *</label>
                  <input type="text" id="cFullName" name="fullName" class="form-input" placeholder="e.g. Rahul Sharma" required />
                  <div class="form-error" id="error-cFullName" style="display: none;"></div>
                </div>

                <!-- 2. Mobile Number (Strict: ^[6-9]\d{9}$) -->
                <div class="form-group">
                  <label class="form-label" for="cMobileNumber">Mobile Number *</label>
                  <div style="position: relative;">
                    <span style="position: absolute; left: 12px; top: 50%; transform: translateY(-50%); font-weight: bold; color: var(--color-muted); font-size: var(--text-sm);">+91</span>
                    <input type="tel" id="cMobileNumber" name="mobileNumber" class="form-input" style="padding-left: 48px;" placeholder="98765 43210" pattern="^[6-9]\d{9}$" maxlength="10" required />
                  </div>
                  <div class="form-error" id="error-cMobileNumber" style="display: none;"></div>
                  <span class="text-muted" style="font-size: 0.75rem; display: block; margin-top: 4px;">Must be a 10-digit Indian mobile number starting with 6, 7, 8, or 9.</span>
                </div>

                <!-- 3. Area / Locality & Society / Building -->
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4);">
                  <div class="form-group">
                    <label class="form-label" for="cAreaLocality">Area / Locality *</label>
                    <input type="text" id="cAreaLocality" name="areaLocality" class="form-input" placeholder="e.g. Sector 3, Airoli" value="Airoli" required />
                    <div class="form-error" id="error-cAreaLocality" style="display: none;"></div>
                  </div>
                  <div class="form-group">
                    <label class="form-label" for="cSocietyBuilding">Society / Building <span style="font-weight: normal; color: var(--color-muted);">(optional)</span></label>
                    <input type="text" id="cSocietyBuilding" name="societyBuilding" class="form-input" placeholder="e.g. Dharmjeevan CHS" />
                  </div>
                </div>

                <!-- 4. Preferred Internet Plan -->
                <div class="form-group">
                  <label class="form-label" for="cPreferredPlan">Preferred Internet Plan *</label>
                  <select id="cPreferredPlan" name="preferredPlan" class="form-input" style="cursor: pointer;" required>
                    <option value="Popular 200 Mbps" selected>Popular 200 Mbps — ₹599/month (Most Popular)</option>
                    <option value="Starter 100 Mbps">Starter 100 Mbps — ₹499/month</option>
                    <option value="Premium 300 Mbps">Premium 300 Mbps — ₹699/month</option>
                    <option value="Gigabit Max 500 Mbps">Gigabit Max 500 Mbps</option>
                    <option value="Gigabit Ultra 1000 Mbps">Gigabit Ultra 1000 Mbps (1 Gbps)</option>
                    <option value="Not Decided / Help Me Choose">Not Decided / Help Me Choose</option>
                  </select>
                </div>

                <!-- 5. Cloudflare Turnstile Verification -->
                <div class="form-group">
                  <label class="form-label">Security Verification</label>
                  <div class="cf-turnstile-wrap">
                    <div class="cf-turnstile" data-sitekey="0x4AAAAAAAx_DUMMY_TURNSTILE_KEY" data-theme="light"></div>
                  </div>
                </div>

                <!-- 6. Consent Checkbox -->
                <div class="form-group">
                  <label class="form-checkbox-label" for="cConsent">
                    <input type="checkbox" id="cConsent" name="consent" required />
                    <span>I authorize Sevenseas Broadband to contact me via phone call or WhatsApp regarding this internet connection enquiry.</span>
                  </label>
                </div>

                <!-- Submit Button -->
                <button type="submit" class="btn btn-primary btn-lg" style="width: 100%; margin-top: var(--space-4);">
                  Submit Connection Enquiry
                </button>
                <p style="text-align: center; font-size: var(--text-xs); color: var(--color-muted); margin-top: var(--space-2);">
                  Zero upfront payment. Free technician visit and feasibility inspection.
                </p>

              </form>
            </div>
          </div>

        </div>
      </div>
    </section>
    """
