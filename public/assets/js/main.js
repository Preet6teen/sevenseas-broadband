/**
 * Sevenseas Broadband — Global Interactive Scripts
 * Mobile navigation, accordions, plan billing toggles, coverage search, form validations
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Drawer Toggle
  const menuBtn = document.querySelector('.mobile-menu-btn');
  const navMenu = document.querySelector('.site-nav');
  const overlay = document.querySelector('.nav-overlay');

  if (menuBtn && navMenu) {
    const toggleNav = () => {
      const isExpanded = menuBtn.getAttribute('aria-expanded') === 'true';
      menuBtn.setAttribute('aria-expanded', !isExpanded);
      navMenu.classList.toggle('is-open');
      if (overlay) overlay.classList.toggle('is-open');
      document.body.style.overflow = !isExpanded ? 'hidden' : '';
    };

    menuBtn.addEventListener('click', toggleNav);
    if (overlay) overlay.addEventListener('click', toggleNav);
  }

  // 2. Interactive FAQ Accordions
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const trigger = item.querySelector('.faq-question');
    if (!trigger) return;

    trigger.addEventListener('click', () => {
      const isOpen = item.classList.contains('is-active');
      // Close other open accordions in the same group if needed
      const parentGroup = item.closest('.faq-accordion');
      if (parentGroup) {
        parentGroup.querySelectorAll('.faq-item').forEach(other => {
          if (other !== item) {
            other.classList.remove('is-active');
            const otherBtn = other.querySelector('.faq-question');
            if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
          }
        });
      }

      item.classList.toggle('is-active');
      trigger.setAttribute('aria-expanded', !isOpen);
    });
  });

  // 3. Plan Billing Cycle Switcher (Monthly, Quarterly, Annual)
  const billingBtns = document.querySelectorAll('[data-billing-toggle]');
  if (billingBtns.length > 0) {
    billingBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        const cycle = btn.getAttribute('data-billing-toggle');
        billingBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        document.querySelectorAll('.price-dynamic').forEach(priceEl => {
          const newPrice = priceEl.getAttribute(`data-price-${cycle}`);
          const newPeriod = priceEl.getAttribute(`data-period-${cycle}`) || '/ month';
          if (newPrice) {
            const valEl = priceEl.querySelector('.price-value');
            const unitEl = priceEl.querySelector('.price-unit');
            if (valEl) valEl.textContent = newPrice;
            if (unitEl) unitEl.textContent = newPeriod;
          }
        });

        // Show/hide annual discount badge
        document.querySelectorAll('.annual-discount-pill').forEach(pill => {
          pill.style.display = cycle === 'annual' ? 'inline-flex' : 'none';
        });
      });
    });
  }

  // 4. Client-Side Form Validation with Accessible Error States
  const forms = document.querySelectorAll('form[data-validate]');
  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      let isValid = true;
      const requiredInputs = form.querySelectorAll('[required]');

      requiredInputs.forEach(input => {
        const errorEl = form.querySelector(`#error-${input.id}`) || input.nextElementSibling;
        if (!input.value.trim()) {
          isValid = false;
          input.classList.add('is-invalid');
          if (errorEl && errorEl.classList.contains('form-error')) {
            errorEl.style.display = 'flex';
          }
        } else {
          input.classList.remove('is-invalid');
          if (errorEl && errorEl.classList.contains('form-error')) {
            errorEl.style.display = 'none';
          }
        }
      });

      if (!isValid) {
        e.preventDefault();
        const firstInvalid = form.querySelector('.is-invalid');
        if (firstInvalid) firstInvalid.focus();
      } else if (form.getAttribute('data-ajax') === 'true') {
        e.preventDefault();
        const successBox = form.querySelector('.form-success-alert');
        if (successBox) {
          successBox.style.display = 'flex';
          form.reset();
        }
      }
    });
  });
});
