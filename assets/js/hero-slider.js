/**
 * Sevenseas Broadband — Hero Carousel Controller
 * Features:
 * - 4-Slide Full-Width Cinematic Background Carousel
 * - Autoplay every 6.5s with pause on hover, focus, and tab hidden
 * - Keyboard (ArrowLeft / ArrowRight) and touch swipe navigation
 * - Real-time slide counter and indicator synchronization
 * - Accessible ARIA attributes management
 * - Prefers-reduced-motion compliance
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', initHeroSlider);

  function initHeroSlider() {
    const slider = document.querySelector('.hero-slider-section');
    if (!slider) return;

    const slides = Array.from(slider.querySelectorAll('.hero-slide'));
    const indicators = Array.from(slider.querySelectorAll('.hero-indicator-btn'));
    const prevBtn = slider.querySelector('.prev-btn');
    const nextBtn = slider.querySelector('.next-btn');
    const counterCurrent = slider.querySelector('.hero-counter-current');

    if (slides.length === 0) return;

    let currentIndex = 0;
    const totalSlides = slides.length;
    const autoPlayDelay = 6500;
    let autoPlayTimer = null;
    let isPaused = false;

    // Check reduced motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Set initial state
    goToSlide(0, false);

    // Start Autoplay if not reduced motion
    if (!prefersReducedMotion) {
      startAutoPlay();
    }

    // Event Listeners for Prev/Next
    if (prevBtn) {
      prevBtn.addEventListener('click', function (e) {
        e.preventDefault();
        goToPrev();
        restartAutoPlay();
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', function (e) {
        e.preventDefault();
        goToNext();
        restartAutoPlay();
      });
    }

    // Indicator clicks
    indicators.forEach((indicator, index) => {
      indicator.addEventListener('click', function (e) {
        e.preventDefault();
        goToSlide(index);
        restartAutoPlay();
      });
    });

    // Pause on Hover
    slider.addEventListener('mouseenter', function () {
      pauseAutoPlay();
    });

    slider.addEventListener('mouseleave', function () {
      resumeAutoPlay();
    });

    // Pause on Focus (accessibility)
    slider.addEventListener('focusin', function () {
      pauseAutoPlay();
    });

    slider.addEventListener('focusout', function () {
      resumeAutoPlay();
    });

    // Pause on tab hidden (visibilitychange)
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) {
        pauseAutoPlay();
      } else {
        resumeAutoPlay();
      }
    });

    // Keyboard navigation
    slider.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') {
        goToPrev();
        restartAutoPlay();
      } else if (e.key === 'ArrowRight') {
        goToNext();
        restartAutoPlay();
      }
    });

    // Touch Swipe Support
    let touchStartX = 0;
    let touchEndX = 0;
    let touchStartY = 0;
    let touchEndY = 0;

    slider.addEventListener('touchstart', function (e) {
      if (e.changedTouches && e.changedTouches[0]) {
        touchStartX = e.changedTouches[0].screenX;
        touchStartY = e.changedTouches[0].screenY;
      }
    }, { passive: true });

    slider.addEventListener('touchend', function (e) {
      if (e.changedTouches && e.changedTouches[0]) {
        touchEndX = e.changedTouches[0].screenX;
        touchEndY = e.changedTouches[0].screenY;
        handleSwipe();
      }
    }, { passive: true });

    function handleSwipe() {
      const diffX = touchEndX - touchStartX;
      const diffY = touchEndY - touchStartY;
      // Only trigger if horizontal swipe is significantly greater than vertical scroll
      if (Math.abs(diffX) > Math.abs(diffY) && Math.abs(diffX) > 40) {
        if (diffX < 0) {
          // Swipe left -> next
          goToNext();
        } else {
          // Swipe right -> prev
          goToPrev();
        }
        restartAutoPlay();
      }
    }

    function goToSlide(index, animate = true) {
      if (index < 0) index = totalSlides - 1;
      if (index >= totalSlides) index = 0;

      currentIndex = index;

      slides.forEach((slide, i) => {
        const isActive = i === currentIndex;
        slide.classList.toggle('active', isActive);
        slide.setAttribute('aria-hidden', isActive ? 'false' : 'true');

        // Manage focusability of links inside inactive slides
        const focusableElements = slide.querySelectorAll('a, button');
        focusableElements.forEach(el => {
          if (isActive) {
            el.removeAttribute('tabindex');
          } else {
            el.setAttribute('tabindex', '-1');
          }
        });
      });

      // Update indicators
      indicators.forEach((indicator, i) => {
        const isActive = i === currentIndex;
        indicator.classList.toggle('active', isActive);
        indicator.setAttribute('aria-selected', isActive ? 'true' : 'false');
      });

      // Update slide counter
      if (counterCurrent) {
        counterCurrent.textContent = String(currentIndex + 1).padStart(2, '0');
      }
    }

    function goToNext() {
      goToSlide(currentIndex + 1);
    }

    function goToPrev() {
      goToSlide(currentIndex - 1);
    }

    function startAutoPlay() {
      stopAutoPlay();
      autoPlayTimer = setInterval(function () {
        if (!isPaused) {
          goToNext();
        }
      }, autoPlayDelay);
    }

    function stopAutoPlay() {
      if (autoPlayTimer) {
        clearInterval(autoPlayTimer);
        autoPlayTimer = null;
      }
    }

    function pauseAutoPlay() {
      isPaused = true;
    }

    function resumeAutoPlay() {
      isPaused = false;
    }

    function restartAutoPlay() {
      if (!prefersReducedMotion) {
        startAutoPlay();
      }
    }
  }
})();
