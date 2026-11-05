/**
 * Sevenseas Broadband — Google Analytics 4 (GA4) & Conversion Tracking
 * Tracks core business conversions: Call clicks, WhatsApp clicks, Plan selection,
 * Coverage checks, and Form submissions.
 */

(function () {
  'use strict';

  var GA_MEASUREMENT_ID = window.SEVENSEAS_CONFIG && window.SEVENSEAS_CONFIG.gaMeasurementId 
    ? window.SEVENSEAS_CONFIG.gaMeasurementId 
    : 'G-7SEASBB2026';

  // Initialize DataLayer
  window.dataLayer = window.dataLayer || [];
  function gtag() {
    window.dataLayer.push(arguments);
  }
  window.gtag = gtag;

  gtag('js', new Date());
  gtag('config', GA_MEASUREMENT_ID, {
    send_page_view: true,
    cookie_flags: 'SameSite=None;Secure'
  });

  // Track Conversion Event Helper
  function trackEvent(eventName, params) {
    if (typeof window.gtag === 'function') {
      window.gtag('event', eventName, params || {});
    }
    // Also dispatch custom DOM event for modular listeners
    window.dispatchEvent(new CustomEvent('sevenseas:' + eventName, { detail: params }));
    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
      console.log('[Analytics Event]', eventName, params);
    }
  }
  window.trackSevenseasEvent = trackEvent;

  document.addEventListener('DOMContentLoaded', function () {
    
    // 1. Track Call Button Clicks
    document.querySelectorAll('a[href^="tel:"]').forEach(function (callLink) {
      callLink.addEventListener('click', function () {
        var phoneNumber = this.getAttribute('href').replace('tel:', '');
        trackEvent('call_button_click', {
          event_category: 'Engagement',
          event_label: phoneNumber,
          phone_number: phoneNumber,
          source_page: window.location.pathname
        });
      });
    });

    // 2. Track WhatsApp Clicks
    document.querySelectorAll('a[href*="wa.me"]').forEach(function (waLink) {
      waLink.addEventListener('click', function () {
        trackEvent('whatsapp_click', {
          event_category: 'Lead Generation',
          event_label: 'WhatsApp Direct Chat',
          link_url: this.getAttribute('href'),
          source_page: window.location.pathname
        });
      });
    });

    // 3. Track Plan Selections
    document.querySelectorAll('a[href*="new-connection.html?plan="], [data-plan-select]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var href = this.getAttribute('href') || '';
        var planParam = '';
        if (href.indexOf('plan=') !== -1) {
          planParam = href.split('plan=')[1].split('&')[0];
        }
        var planName = this.getAttribute('data-plan-select') || planParam || this.textContent.trim();

        trackEvent('plan_selection', {
          event_category: 'Ecommerce / Lead Intent',
          plan_name: planName,
          source_page: window.location.pathname
        });
      });
    });

    // 4. Track Availability Enquiries (Coverage Checker)
    var coverageForms = document.querySelectorAll('.coverage-checker-bar, #coverageSearchForm');
    coverageForms.forEach(function (form) {
      form.addEventListener('submit', function () {
        var input = this.querySelector('input[type="text"]');
        var query = input ? input.value.trim() : '';
        trackEvent('availability_enquiry', {
          event_category: 'Coverage Check',
          search_locality: query,
          target_city: 'Airoli, Navi Mumbai'
        });
      });
    });

    // 5. Track Form Submissions (Listens to custom event dispatched by enquiry.js)
    window.addEventListener('sevenseas:lead_submitted', function (e) {
      var detail = e.detail || {};
      trackEvent('form_submission', {
        event_category: 'Lead Generation',
        event_label: 'Enquiry Form Submitted',
        lead_id: detail.leadId,
        preferred_plan: detail.preferredPlan,
        locality: detail.areaLocality,
        value: 1 // Conversion goal
      });
    });

  });

})();
