/* Google Analytics 4 loader.
 *
 * TO TURN ANALYTICS ON: paste the Measurement ID below and push. That is the
 * only edit needed. Every page loads this one file, so there is nothing to
 * repeat page by page.
 *
 * Get the ID from https://analytics.google.com -> Admin -> Data Streams ->
 * your web stream. It looks like G-XXXXXXXXXX.
 *
 * While MEASUREMENT_ID is empty this script does nothing at all: no requests,
 * no cookies, no console noise. It is safe to ship in this state.
 */
(function () {
  var MEASUREMENT_ID = '';   // <-- paste G-XXXXXXXXXX here

  if (!MEASUREMENT_ID) return;

  // Skip local previews so test traffic never pollutes the real numbers.
  var h = location.hostname;
  if (h === 'localhost' || h === '127.0.0.1' || h === '' || h.endsWith('.local')) return;

  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + MEASUREMENT_ID;
  document.head.appendChild(s);

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag('js', new Date());
  gtag('config', MEASUREMENT_ID);

  /* Redirect-domain attribution.
   * The parked domains 301 here with a ?ref= tag, for example
   * https://r3mediapro.com/?ref=rtdiii. Record it as an event so renewal
   * decisions can be made from real numbers instead of guesswork. */
  var ref = new URLSearchParams(location.search).get('ref');
  if (ref) gtag('event', 'redirect_domain', { source_domain: ref });
})();
