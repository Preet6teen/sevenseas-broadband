"""
New Connection booking page generator for Sevenseas Broadband.
Integrates Phase 5 Lead-Generation form, strict mobile validation,
honeypot, Turnstile security, and WhatsApp handover.
"""

def get_content():
    return """
    <!-- PAGE HERO -->
    <section class="page-hero">
      <div class="container">
        <nav aria-label="Breadcrumb" class="breadcrumbs">
          <a href="index.html">Home</a>
          <span>/</span>
          <span aria-current="page">New Connection</span>
        </nav>
        <div style="max-width: 760px;">
          <span class="subheading-badge">Doorstep Service in Airoli</span>
          <h1 class="display-title" style="margin-bottom: var(--space-4);">
            Book Your Sevenseas Fiber Connection in 2 Minutes
          </h1>
          <p class="lead">
            Select your preferred plan, share your locality in Airoli, and get connected with complimentary optical fiber hardware. ₹0 Installation and zero advance payment required.
          </p>
        </div>
      </div>
    </section>

    <!-- BOOKING SECTION -->
    <section class="section">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1fr; gap: var(--space-8);" class="editorial-split-grid">
          
          <!-- Booking Form Card -->
          <div>
            <div class="card" style="padding: var(--space-8); background-color: var(--color-white); border-radius: var(--radius-lg); box-shadow: var(--shadow-md);">
              <h3 style="margin-bottom: var(--space-1); color: var(--color-navy);">New Connection Booking</h3>
              <p class="text-muted" style="font-size: var(--text-sm); margin-bottom: var(--space-6);">Fill out your details to receive an instant verification call and schedule your technician visit.</p>

              <form id="newConnectionForm" novalidate>
                
                <!-- Status & Error Alert Container -->
                <div class="enquiry-status-alert" id="newConnectionForm-status" role="alert" style="display: none;"></div>

                <!-- Anti-Bot Honeypot Field -->
                <div class="visually-hidden-field" aria-hidden="true">
                  <label for="nc_b_website">Leave this field blank</label>
                  <input type="text" id="nc_b_website" name="b_website" tabindex="-1" autocomplete="off" />
                </div>

                <!-- 1. Preferred Internet Plan -->
                <div class="form-group">
                  <label class="form-label" for="ncPlan">1. Select Your Fiber Speed Plan *</label>
                  <select id="ncPlan" name="preferredPlan" class="form-input" style="cursor: pointer;" required>
                    <option value="Popular 200 Mbps" selected>Popular 200 Mbps — ₹599/month (Most Popular for Homes)</option>
                    <option value="Starter 100 Mbps">Starter 100 Mbps — ₹499/month (Affordable Unlimited)</option>
                    <option value="Premium 300 Mbps">Premium 300 Mbps — ₹699/month (Ultra HD 4K &amp; Pro Gaming)</option>
                    <option value="Gigabit Max 500 Mbps">Gigabit Max 500 Mbps</option>
                    <option value="Gigabit Ultra 1000 Mbps">Gigabit Ultra 1000 Mbps (1 Gbps)</option>
                  </select>
                </div>

                <!-- 2. Full Name -->
                <div class="form-group">
                  <label class="form-label" for="ncFullName">2. Full Name *</label>
                  <input type="text" id="ncFullName" name="fullName" class="form-input" placeholder="e.g. Aditi Deshmukh" required />
                  <div class="form-error" id="error-ncFullName" style="display: none;"></div>
                </div>

                <!-- 3. Mobile Number (Strict: ^[6-9]\d{9}$) -->
                <div class="form-group">
                  <label class="form-label" for="ncMobileNumber">3. Mobile Number *</label>
                  <div style="position: relative;">
                    <span style="position: absolute; left: 12px; top: 50%; transform: translateY(-50%); font-weight: bold; color: var(--color-muted); font-size: var(--text-sm);">+91</span>
                    <input type="tel" id="ncMobileNumber" name="mobileNumber" class="form-input" style="padding-left: 48px;" placeholder="98200 54321" pattern="^[6-9]\d{9}$" maxlength="10" required />
                  </div>
                  <div class="form-error" id="error-ncMobileNumber" style="display: none;"></div>
                  <span class="text-muted" style="font-size: 0.75rem; display: block; margin-top: 4px;">10-digit Indian mobile number (e.g. 9664985535).</span>
                </div>

                <!-- 4. Area / Locality & Society / Building -->
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4);">
                  <div class="form-group">
                    <label class="form-label" for="ncAreaLocality">4. Area / Locality *</label>
                    <input type="text" id="ncAreaLocality" name="areaLocality" class="form-input" placeholder="e.g. Sector 3, Airoli" value="Airoli" required />
                    <div class="form-error" id="error-ncAreaLocality" style="display: none;"></div>
                  </div>
                  <div class="form-group">
                    <label class="form-label" for="ncSocietyBuilding">Society / Building <span style="font-weight: normal; color: var(--color-muted);">(optional)</span></label>
                    <input type="text" id="ncSocietyBuilding" name="societyBuilding" class="form-input" placeholder="e.g. Palm Grove CHS, Sector 8" />
                  </div>
                </div>

                <!-- 5. Security Verification (Cloudflare Turnstile) -->
                <div class="form-group">
                  <label class="form-label">Security Verification</label>
                  <div class="cf-turnstile-wrap">
                    <div class="cf-turnstile" data-sitekey="0x4AAAAAAAx_DUMMY_TURNSTILE_KEY" data-theme="light"></div>
                  </div>
                </div>

                <!-- 6. Consent Checkbox -->
                <div class="form-group">
                  <label class="form-checkbox-label" for="ncConsent">
                    <input type="checkbox" id="ncConsent" name="consent" required />
                    <span>I authorize Sevenseas Broadband to contact me to coordinate installation availability and schedule my technician visit.</span>
                  </label>
                </div>

                <!-- Submit Button -->
                <button type="submit" class="btn btn-primary btn-lg" style="width: 100%; margin-top: var(--space-3);">
                  Book Connection Now
                </button>
                <p style="text-align: center; font-size: var(--text-xs); color: var(--color-muted); margin-top: var(--space-2);">
                  Zero payment required right now. Pay securely only after your technician completes the live speed test at your doorstep.
                </p>

              </form>
            </div>
          </div>

          <!-- Process & KYC Checklist Aside -->
          <div>
            <div style="background-color: var(--color-white); border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: var(--space-8); margin-bottom: var(--space-6);">
              <h4 style="margin-bottom: var(--space-4); color: var(--color-navy);">What Happens Next?</h4>
              
              <div style="display: flex; flex-direction: column; gap: var(--space-4);">
                <div style="display: flex; gap: var(--space-3); align-items: flex-start;">
                  <div style="width: 28px; height: 28px; border-radius: 50%; background: var(--tint-navy); color: var(--color-navy); display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.85rem; flex-shrink: 0;">1</div>
                  <div>
                    <strong style="color: var(--color-navy); font-size: var(--text-sm); display: block;">Instant Telephonic Confirmation</strong>
                    <span class="text-muted" style="font-size: var(--text-xs);">Our Airoli coordinator calls +91 96649 85535 / your number to verify building entry and schedule your time slot.</span>
                  </div>
                </div>

                <div style="display: flex; gap: var(--space-3); align-items: flex-start;">
                  <div style="width: 28px; height: 28px; border-radius: 50%; background: var(--tint-orange); color: var(--color-orange-text); display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.85rem; flex-shrink: 0;">2</div>
                  <div>
                    <strong style="color: var(--color-navy); font-size: var(--text-sm); display: block;">Neat Optical Doorstep Cabling</strong>
                    <span class="text-muted" style="font-size: var(--text-xs);">Uniformed technician arrives with optical splicing gear and terminates your fiber line neatly with zero mess.</span>
                  </div>
                </div>

                <div style="display: flex; gap: var(--space-3); align-items: flex-start;">
                  <div style="width: 28px; height: 28px; border-radius: 50%; background: var(--tint-emerald); color: var(--color-emerald-text); display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.85rem; flex-shrink: 0;">3</div>
                  <div>
                    <strong style="color: var(--color-navy); font-size: var(--text-sm); display: block;">Live Speed Test &amp; Handover</strong>
                    <span class="text-muted" style="font-size: var(--text-xs);">We verify symmetrical speeds and low ping on your phone or laptop before you make any payment.</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- KYC Checklist Card -->
            <div class="card" style="background-color: var(--tint-navy); border-color: #CBD5E1;">
              <h4 style="margin-bottom: var(--space-2); color: var(--color-navy);">DoT Mandatory KYC Checklist</h4>
              <p class="text-muted" style="font-size: var(--text-xs); margin-bottom: var(--space-4);">Please keep the following documents ready for digital verification upon technician arrival:</p>
              
              <ul class="feature-list" style="margin: 0; font-size: var(--text-xs);">
                <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> <strong>Proof of Identity:</strong> Aadhaar Card, Passport, or Voter ID</li>
                <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> <strong>Proof of Address:</strong> Aadhaar, Electricity Bill, or Registered Rent Agreement in Airoli</li>
                <li><svg class="icon icon-sm"><use href="#icon-check"></use></svg> <strong>Photograph:</strong> Digital live selfie taken by technician during activation</li>
              </ul>
            </div>

            <!-- Office Desk Quick Reference -->
            <div style="margin-top: var(--space-4); padding: var(--space-4); background: #FFFFFF; border: 1px solid var(--color-border); border-radius: var(--radius-sm); font-size: var(--text-xs); color: var(--color-ink);">
              <strong>Need urgent assistance?</strong> Call our Airoli office directly at <a href="tel:9664985535" style="color: var(--color-orange-text); font-weight: bold;">+91 96649 85535</a> / <a href="tel:7400222922" style="color: var(--color-navy); font-weight: bold;">+91 74002 22922</a>.
            </div>

          </div>

        </div>
      </div>
    </section>
    """
