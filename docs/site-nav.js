// Shows the "Buy me a coffee" button in the top bar when donations are enabled in site-config.js.
(function () {
  var s = window.FORGE_SITE_CONFIG && window.FORGE_SITE_CONFIG.donations;
  var b = document.getElementById("forge-bar-coffee");
  if (b && s && s.enabled === true && typeof s.url === "string" && /^https:\/\/(www\.)?ko-fi\.com\/[a-zA-Z0-9._-]+\/?$/.test(s.url)) {
    b.href = s.url;
    b.hidden = false;
  }
})();
