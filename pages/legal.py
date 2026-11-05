"""
Legal pages generators for Sevenseas Broadband:
- privacy.html
- terms.html
- refund-policy.html
"""

def get_privacy_content():
    return """
    <!-- PAGE HERO -->
    <section class="page-hero">
      <div class="container">
        <nav aria-label="Breadcrumb" class="breadcrumbs">
          <a href="index.html">Home</a>
          <span>/</span>
          <span aria-current="page">Privacy Policy</span>
        </nav>
        <div style="max-width: 760px;">
          <span class="subheading-badge">Data Protection</span>
          <h1 class="display-title" style="margin-bottom: var(--space-4);">Privacy Policy</h1>
          <p class="lead">Last Updated: October 2026. Aligned with the Digital Personal Data Protection (DPDP) Act and Department of Telecommunications regulations.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 840px;">
        <div class="card" style="padding: var(--space-8); line-height: var(--leading-relaxed); font-size: var(--text-sm);">
          
          <h3 style="color: var(--color-navy); margin-top: 0;">1. Introduction &amp; Commitment</h3>
          <p>Sevenseas Broadband Pvt. Ltd. ("Sevenseas", "we", "us", or "our") respects the privacy of our subscribers and visitors. This Privacy Policy explains how we collect, store, process, and protect your personal data when you visit our website, apply for a new broadband connection, or use our residential internet services.</p>

          <h3 style="color: var(--color-navy);">2. Information We Collect</h3>
          <p>To provide telecommunications services in compliance with statutory licensing requirements, we collect:</p>
          <ul class="feature-list" style="margin-bottom: var(--space-4);">
            <li><strong>KYC &amp; Identity Data:</strong> Name, government-issued photo identity (Aadhaar, Passport, Voter ID), digital photograph, and proof of residential address as mandated by the Department of Telecommunications (DoT).</li>
            <li><strong>Contact Details:</strong> Mobile number, alternate contact number, email address, and complete physical installation address.</li>
            <li><strong>Billing &amp; Payment Data:</strong> Transaction references, plan subscription history, and payment method details. (Note: Card numbers are processed directly through RBI-authorized payment gateways and are never stored on our servers).</li>
            <li><strong>Technical &amp; Telemetry Data:</strong> IP address allocations, MAC addresses of the Optical Network Terminal (ONT), bandwidth utilization counters, and network uptime telemetry necessary for service maintenance.</li>
          </ul>

          <h3 style="color: var(--color-navy);">3. How We Use Your Data</h3>
          <p>We use your personal data strictly for:</p>
          <ol style="padding-left: var(--space-5); margin: 0 0 var(--space-4);">
            <li>Verifying your identity and provisioning optical fiber connectivity at your premises.</li>
            <li>Generating monthly invoices, processing subscription renewals, and providing customer support.</li>
            <li>Monitoring network health, diagnosing Wi-Fi performance, and resolving optical line outages.</li>
            <li>Complying with statutory reporting requirements issued by the DoT, TRAI, and law enforcement agencies.</li>
          </ol>
          <p><strong>We never sell, rent, or trade your personal information to third-party advertising brokers under any circumstances.</strong></p>

          <h3 style="color: var(--color-navy);">4. Data Security &amp; Encryption</h3>
          <p>All subscriber records and KYC submissions are stored in ISO 27001-certified data centers located within the Republic of India. Data in transit is secured using modern TLS 1.3 encryption, and subscriber records at rest are secured with AES-256 bit encryption.</p>

          <h3 style="color: var(--color-navy);">5. Data Retention &amp; Erasure</h3>
          <p>We retain customer information for the active duration of your subscription and for the statutory minimum period required under Indian telecommunications regulations. Following account termination and settlement of dues, non-statutory records are securely anonymized or destroyed.</p>

          <h3 style="color: var(--color-navy);">6. Grievance Redressal Officer</h3>
          <p>In accordance with the Information Technology Act and DPDP Rules, the contact details of our appointed Grievance Officer are:</p>
          <div style="background: var(--tint-navy); padding: var(--space-4); border-radius: var(--radius-sm); border-left: 4px solid var(--color-navy);">
            <strong>Grievance Officer:</strong> Mr. Alok Sengupta<br>
            <strong>Email:</strong> grievance@sevenseasbroadband.in<br>
            <strong>Phone:</strong> 022-6892-4015 (Mon–Fri, 10:00 AM – 5:00 PM)<br>
            <strong>Address:</strong> Shop-1, Dharmjeevan Co-op Housing Society, near Railway Station, Sector 3, Airoli, Navi Mumbai, Maharashtra 400708.
          </div>

        </div>
      </div>
    </section>
    """

def get_terms_content():
    return """
    <!-- PAGE HERO -->
    <section class="page-hero">
      <div class="container">
        <nav aria-label="Breadcrumb" class="breadcrumbs">
          <a href="index.html">Home</a>
          <span>/</span>
          <span aria-current="page">Terms and Conditions</span>
        </nav>
        <div style="max-width: 760px;">
          <span class="subheading-badge">Subscriber Agreement</span>
          <h1 class="display-title" style="margin-bottom: var(--space-4);">Terms and Conditions</h1>
          <p class="lead">Standard terms governing the provisioning, usage, and billing of Sevenseas residential fiber broadband services.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 840px;">
        <div class="card" style="padding: var(--space-8); line-height: var(--leading-relaxed); font-size: var(--text-sm);">
          
          <h3 style="color: var(--color-navy); margin-top: 0;">1. Provisioning of Service</h3>
          <p>Sevenseas Broadband agrees to provide residential optical internet access to the subscriber at the designated installation address subject to physical feasibility, society NOC approvals, and successful completion of KYC verification as required by DoT regulations.</p>

          <h3 style="color: var(--color-navy);">2. Customer Premises Equipment (ONT Router)</h3>
          <p>The Optical Network Terminal (ONT) device installed at the subscriber's premises remains the exclusive capital property of Sevenseas Broadband unless explicitly purchased outright by the customer. The subscriber is responsible for maintaining the ONT in safe operating condition with adequate power surge protection. In the event of subscription termination, the ONT and power adapter must be returned in good working order.</p>

          <h3 style="color: var(--color-navy);">3. Symmetrical Speeds &amp; Bandwidth</h3>
          <p>All advertised plans feature symmetrical download and upload bandwidth up to the Optical Network Terminal port. Wi-Fi speeds measured on end-user wireless devices may vary depending on device capabilities, distance from router, concrete wall interference, and 5 GHz frequency support.</p>

          <h3 style="color: var(--color-navy);">4. Acceptable Use &amp; Fair Usage Policy (FUP)</h3>
          <p>Sevenseas residential broadband plans are provided for personal, family, student, and work-from-home residential use. Reselling bandwidth, operating commercial proxy servers, or engaging in illegal cyber activities (as defined under the Indian Information Technology Act) is strictly prohibited and constitutes grounds for immediate termination without refund.</p>

          <h3 style="color: var(--color-navy);">5. Billing Cycles &amp; Renewals</h3>
          <p>Broadband services operate on a prepaid billing cycle. Renewal invoices are generated 5 days prior to the expiration date. In the absence of renewal payment upon cycle expiry, services are automatically paused until payment is received, with zero reactivation penalties.</p>

          <h3 style="color: var(--color-navy);">6. Service Availability &amp; SLA</h3>
          <p>Sevenseas strives to deliver 99.9% network availability across its optical rings. Planned maintenance windows are scheduled between 2:00 AM and 5:00 AM with prior email/SMS notification. Outages caused by force majeure (civic road construction cuts, severe natural disasters, or grid power failures) will be resolved on an expedited priority basis.</p>

          <h3 style="color: var(--color-navy);">7. Governing Law &amp; Jurisdiction</h3>
          <p>This agreement shall be governed by and construed in accordance with the laws of the Republic of India. Any disputes arising under this agreement shall be subject to the exclusive jurisdiction of the courts located in Mumbai, Maharashtra.</p>

        </div>
      </div>
    </section>
    """

def get_refund_content():
    return """
    <!-- PAGE HERO -->
    <section class="page-hero">
      <div class="container">
        <nav aria-label="Breadcrumb" class="breadcrumbs">
          <a href="index.html">Home</a>
          <span>/</span>
          <span aria-current="page">Refund &amp; Cancellation Policy</span>
        </nav>
        <div style="max-width: 760px;">
          <span class="subheading-badge">Customer Protection</span>
          <h1 class="display-title" style="margin-bottom: var(--space-4);">Refund &amp; Cancellation Policy</h1>
          <p class="lead">Transparent, hassle-free cancellation and refund guidelines for all Sevenseas residential subscribers.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 840px;">
        <div class="card" style="padding: var(--space-8); line-height: var(--leading-relaxed); font-size: var(--text-sm);">
          
          <h3 style="color: var(--color-navy); margin-top: 0;">1. 7-Day Money-Back Trial Guarantee</h3>
          <p>We are confident in the speed and stability of our pure optical network. If you are not satisfied with your Sevenseas Broadband connection within the first <strong>7 days of initial installation</strong>, you may request a complete cancellation. We will refund 100% of your plan subscription amount, with zero cancellation fees.</p>

          <h3 style="color: var(--color-navy);">2. Cancellation Prior to Installation</h3>
          <p>If you submit a new connection booking and make an advance payment, but cancel before the optical line is installed or feasibility fails, 100% of the advance amount will be refunded to your original payment source within <strong>3 to 5 business days</strong>.</p>

          <h3 style="color: var(--color-navy);">3. Mid-Term Cancellation on Long-Term Plans</h3>
          <p>Subscribers on quarterly, semi-annual, or annual plans who wish to cancel before the plan tenure ends may request disconnection. The refund amount will be calculated by deducting the consumed months at the standard monthly plan tariff from the total amount paid. The balance amount will be credited to the subscriber's bank account.</p>

          <h3 style="color: var(--color-navy);">4. Hardware Security Deposit Refund</h3>
          <p>For plans requiring a refundable hardware security deposit for the Wi-Fi 6 ONT gateway, the deposit is refunded in full upon collection of the undamaged equipment by our field technician. Refunds are initiated via direct NEFT bank transfer or UPI within <strong>5 to 7 business days</strong> of equipment receipt.</p>

          <h3 style="color: var(--color-navy);">5. Network Outage Compensation Credits</h3>
          <p>In the unlikely event of an unscheduled network outage exceeding 24 continuous hours attributable directly to Sevenseas infrastructure (and not caused by customer premises power failures or customer-side optical fiber snapping), subscribers will receive an automatic pro-rata extension of their billing cycle corresponding to the outage period.</p>

          <h3 style="color: var(--color-navy);">6. How to Initiate a Cancellation or Refund Request</h3>
          <p>To submit a cancellation or refund claim, you can:</p>
          <ul class="feature-list">
            <li>Email our billing desk at: <strong>billing@sevenseasbroadband.in</strong> with your Customer ID and reason.</li>
            <li>Call our 24/7 Toll-Free Helpline: <strong>1800-233-7327</strong>.</li>
            <li>Send a message to our verified WhatsApp desk: <strong>+91 98200 73270</strong>.</li>
          </ul>

        </div>
      </div>
    </section>
    """
