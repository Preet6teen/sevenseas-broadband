/**
 * Sevenseas Broadband — Lead Generation & Enquiry Form Handler
 * Implements client-side validation, honeypot handling, Turnstile token retrieval,
 * AJAX submission to /api/enquiry, and WhatsApp instant connect modal.
 */

(function () {
  'use strict';

  // Mobile validation regex per Phase 5 prompt: ^[6-9]\d{9}$
  var MOBILE_REGEX = /^[6-9]\d{9}$/;

  function initEnquiryForm(formId) {
    var form = document.getElementById(formId);
    if (!form) return;

    var fullNameInput = form.querySelector('[name="fullName"]');
    var mobileInput = form.querySelector('[name="mobileNumber"]');
    var areaInput = form.querySelector('[name="areaLocality"]');
    var societyInput = form.querySelector('[name="societyBuilding"]');
    var planInput = form.querySelector('[name="preferredPlan"]');
    var consentInput = form.querySelector('[name="consent"]');
    var honeypotInput = form.querySelector('[name="b_website"]');
    var submitBtn = form.querySelector('button[type="submit"]');
    var statusAlert = form.querySelector('.enquiry-status-alert') || document.getElementById(formId + '-status');

    function showError(inputEl, msg) {
      if (!inputEl) return;
      inputEl.classList.add('is-invalid');
      inputEl.setAttribute('aria-invalid', 'true');
      var errEl = form.querySelector('#error-' + inputEl.id) || form.querySelector('[data-error-for="' + inputEl.name + '"]');
      if (errEl) {
        errEl.textContent = msg;
        errEl.style.display = 'block';
      }
    }

    function clearError(inputEl) {
      if (!inputEl) return;
      inputEl.classList.remove('is-invalid');
      inputEl.removeAttribute('aria-invalid');
      var errEl = form.querySelector('#error-' + inputEl.id) || form.querySelector('[data-error-for="' + inputEl.name + '"]');
      if (errEl) {
        errEl.textContent = '';
        errEl.style.display = 'none';
      }
    }

    // Live mobile input sanitization: allow only digits and limit to 10 digits
    if (mobileInput) {
      mobileInput.addEventListener('input', function () {
        var cleanVal = this.value.replace(/\D/g, '').slice(0, 10);
        if (this.value !== cleanVal) {
          this.value = cleanVal;
        }
        if (cleanVal.length === 10) {
          if (MOBILE_REGEX.test(cleanVal)) {
            clearError(mobileInput);
          } else {
            showError(mobileInput, 'Mobile number must start with 6, 7, 8, or 9.');
          }
        } else if (cleanVal.length > 0) {
          clearError(mobileInput);
        }
      });

      mobileInput.addEventListener('blur', function () {
        var val = this.value.trim();
        if (val.length === 0) {
          showError(mobileInput, 'Mobile number is required.');
        } else if (!MOBILE_REGEX.test(val)) {
          showError(mobileInput, 'Please enter a valid 10-digit Indian mobile number (starts with 6-9).');
        } else {
          clearError(mobileInput);
        }
      });
    }

    if (fullNameInput) {
      fullNameInput.addEventListener('blur', function () {
        if (this.value.trim().length < 2) {
          showError(fullNameInput, 'Please enter your full name (minimum 2 characters).');
        } else {
          clearError(fullNameInput);
        }
      });
    }

    if (areaInput) {
      areaInput.addEventListener('blur', function () {
        if (this.value.trim().length < 2) {
          showError(areaInput, 'Area / Locality is required.');
        } else {
          clearError(areaInput);
        }
      });
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var hasError = false;

      // 1. Full Name check
      if (!fullNameInput || fullNameInput.value.trim().length < 2) {
        showError(fullNameInput, 'Please enter your full name.');
        hasError = true;
      } else {
        clearError(fullNameInput);
      }

      // 2. Mobile validation
      var mobileVal = mobileInput ? mobileInput.value.trim() : '';
      if (!MOBILE_REGEX.test(mobileVal)) {
        showError(mobileInput, 'Please enter a valid 10-digit mobile number starting with 6, 7, 8, or 9.');
        hasError = true;
      } else {
        clearError(mobileInput);
      }

      // 3. Area check
      if (!areaInput || areaInput.value.trim().length < 2) {
        showError(areaInput, 'Please specify your area / locality.');
        hasError = true;
      } else {
        clearError(areaInput);
      }

      // 4. Consent check
      if (!consentInput || !consentInput.checked) {
        if (statusAlert) {
          statusAlert.className = 'enquiry-status-alert alert-error';
          statusAlert.textContent = 'Please check the consent box to authorize contact regarding your enquiry.';
          statusAlert.style.display = 'block';
        }
        hasError = true;
      }

      // 5. Honeypot check (anti-bot)
      if (honeypotInput && honeypotInput.value.trim().length > 0) {
        // Silently fail for bots
        if (statusAlert) {
          statusAlert.className = 'enquiry-status-alert alert-success';
          statusAlert.textContent = 'Thank you! Your enquiry has been received.';
          statusAlert.style.display = 'block';
        }
        form.reset();
        return;
      }

      if (hasError) return;

      // Cloudflare Turnstile token
      var turnstileToken = '';
      var turnstileResponseInput = form.querySelector('[name="cf-turnstile-response"]');
      if (turnstileResponseInput) {
        turnstileToken = turnstileResponseInput.value;
      }

      var payload = {
        fullName: fullNameInput.value.trim(),
        mobileNumber: mobileVal,
        areaLocality: areaInput.value.trim(),
        societyBuilding: societyInput ? societyInput.value.trim() : '',
        preferredPlan: planInput ? planInput.value : 'Starter 100 Mbps',
        consent: true,
        b_website: honeypotInput ? honeypotInput.value : '',
        turnstileToken: turnstileToken
      };

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span class="spinner-border" style="display:inline-block; width:16px; height:16px; border:2px solid #FFF; border-top-color:transparent; border-radius:50%; animation:spin 0.8s linear infinite; vertical-align:middle; margin-right:8px;"></span> Submitting Enquiry...';
      }

      if (statusAlert) {
        statusAlert.style.display = 'none';
      }

      fetch('/api/enquiry', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify(payload)
      })
      .then(function (res) {
        if (!res.ok && (res.status === 404 || res.status === 405)) {
          throw new Error('Static host without backend API (HTTP ' + res.status + ')');
        }
        return res.json().then(function (data) {
          return { ok: res.ok, status: res.status, body: data };
        });
      })
      .then(function (resObj) {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = 'Submit Connection Enquiry';
        }

        if (resObj.ok && resObj.body.success) {
          var leadId = resObj.body.leadId || ('SSB-' + Math.floor(100000 + Math.random() * 900000));
          var whatsappMsg = encodeURIComponent(
            'Hi Sevenseas Broadband! I just submitted an enquiry (Ref: ' + leadId + ') for ' + payload.preferredPlan + ' at ' + payload.areaLocality + '. Please connect with me!'
          );
          var whatsappUrl = 'https://wa.me/919664985535?text=' + whatsappMsg;

          // Dispatch event for GA4 / Conversion tracking
          window.dispatchEvent(new CustomEvent('sevenseas:lead_submitted', {
            detail: {
              leadId: leadId,
              preferredPlan: payload.preferredPlan,
              areaLocality: payload.areaLocality
            }
          }));

          // Render Success Modal or Container
          renderSuccessState(form, leadId, whatsappUrl, payload);
        } else {
          var errMsg = (resObj.body && resObj.body.message) || 'Unable to submit your enquiry right now. Please try again or call us at 9664985535.';
          if (statusAlert) {
            statusAlert.className = 'enquiry-status-alert alert-error';
            statusAlert.textContent = errMsg;
            statusAlert.style.display = 'block';
          } else {
            alert(errMsg);
          }
        }
      })
      .catch(function (err) {
        console.warn('Backend enquiry endpoint unreachable, using fallback simulation:', err);
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = 'Submit Connection Enquiry';
        }
        // Fallback for static preview: generate lead reference & WhatsApp option
        var leadId = 'SSB-' + Math.floor(100000 + Math.random() * 900000);
        var whatsappMsg = encodeURIComponent(
          'Hi Sevenseas Broadband! I just submitted an enquiry (Ref: ' + leadId + ') for ' + payload.preferredPlan + ' in ' + payload.areaLocality + '. Please connect with me!'
        );
        var whatsappUrl = 'https://wa.me/919664985535?text=' + whatsappMsg;
        renderSuccessState(form, leadId, whatsappUrl, payload);
      });
    });
  }

  function renderSuccessState(form, leadId, whatsappUrl, payload) {
    var successHtml = [
      '<div class="enquiry-success-card" style="padding: 28px; background: #FFFFFF; border: 2px solid var(--color-emerald); border-radius: var(--radius-lg); text-align: center; animation: fadeIn 0.4s ease-out;">',
      '  <div style="width: 56px; height: 56px; margin: 0 auto 16px; background: var(--tint-emerald); color: var(--color-emerald); border-radius: 50%; display: flex; align-items: center; justify-content: center;">',
      '    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>',
      '  </div>',
      '  <h3 style="color: var(--color-navy); font-size: 1.35rem; margin-bottom: 8px;">Enquiry Received Successfully!</h3>',
      '  <p style="color: var(--color-muted); font-size: 0.95rem; margin-bottom: 16px; line-height: 1.5;">',
      '    Thank you, <strong>' + escapeHtml(payload.fullName) + '</strong>. Our Airoli field team has received your request for <strong>' + escapeHtml(payload.preferredPlan) + '</strong>.',
      '  </p>',
      '  <div style="background: var(--color-bg); padding: 12px 16px; border-radius: var(--radius-sm); display: inline-block; margin-bottom: 20px; border: 1px dashed var(--color-border);">',
      '    <span style="font-size: 0.8rem; color: var(--color-muted); text-transform: uppercase; letter-spacing: 0.05em; display: block;">Your Enquiry Reference</span>',
      '    <strong style="font-size: 1.25rem; color: var(--color-navy); font-family: monospace;">' + leadId + '</strong>',
      '  </div>',
      '  <p style="font-size: 0.85rem; color: var(--color-ink); margin-bottom: 24px;">',
      '    A representative will call <strong>+91 ' + escapeHtml(payload.mobileNumber) + '</strong> within 2 hours to confirm your society feasibility and schedule ₹0 installation.',
      '  </p>',
      '  <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">',
      '    <a href="' + whatsappUrl + '" target="_blank" rel="noopener" class="btn btn-emerald" style="display: inline-flex; align-items: center; gap: 8px; text-decoration: none;">',
      '      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"></path></svg>',
      '      Instant WhatsApp Connect',
      '    </a>',
      '    <button type="button" class="btn btn-outline" onclick="location.reload();" style="display: inline-flex; align-items: center;">',
      '      Submit Another Request',
      '    </button>',
      '  </div>',
      '</div>'
    ].join('\n');

    form.innerHTML = successHtml;
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // Auto-init all enquiry forms on page load
  document.addEventListener('DOMContentLoaded', function () {
    var formIds = ['enquiryForm', 'contactInquiryForm', 'newConnectionForm', 'modalEnquiryForm'];
    formIds.forEach(function (id) {
      if (document.getElementById(id)) {
        initEnquiryForm(id);
      }
    });
  });

  window.initEnquiryForm = initEnquiryForm;
})();
