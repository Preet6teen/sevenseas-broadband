/**
 * Sevenseas Broadband — Section 8 Coverage Availability Checker
 * Strictly verifies confirmed service area: Airoli, Navi Mumbai (PIN 400708)
 * Displays "Our team will confirm availability in your area" for unverified locations.
 */

document.addEventListener('DOMContentLoaded', () => {
  const coverageForm = document.getElementById('hpCoverageForm');
  const verifiedBox = document.getElementById('hpCoverageVerified');
  const unverifiedBox = document.getElementById('hpCoverageUnverified');

  if (coverageForm) {
    coverageForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const pinInput = document.getElementById('hpCoveragePin');
      const localityInput = document.getElementById('hpCoverageLocality');

      const pinVal = pinInput ? pinInput.value.trim() : '';
      const localityVal = localityInput ? localityInput.value.trim().toLowerCase() : '';

      // Check if matches Airoli, Navi Mumbai (PIN 400708 or text contains 'airoli')
      const isAiroli = localityVal.includes('airoli') || pinVal === '400708';

      if (isAiroli) {
        if (unverifiedBox) unverifiedBox.style.display = 'none';
        if (verifiedBox) {
          verifiedBox.style.display = 'block';
          verifiedBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      } else {
        if (verifiedBox) verifiedBox.style.display = 'none';
        if (unverifiedBox) {
          unverifiedBox.style.display = 'block';
          unverifiedBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      }
    });
  }
});
