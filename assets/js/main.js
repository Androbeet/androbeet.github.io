// ===== Androbeet — shared site script =====

(function () {
  "use strict";

  // ---- Theme toggle ----
  var root = document.documentElement;
  var STORAGE_KEY = "androbeet-theme";

  function applyTheme(theme) {
    if (theme === "light" || theme === "dark") {
      root.setAttribute("data-theme", theme);
    } else {
      root.removeAttribute("data-theme");
    }
  }

  function currentTheme() {
    try {
      return localStorage.getItem(STORAGE_KEY);
    } catch (e) {
      return null;
    }
  }

  function systemPrefersDark() {
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  }

  applyTheme(currentTheme());

  document.addEventListener("DOMContentLoaded", function () {
    var btn = document.getElementById("theme-toggle");
    if (!btn) return;

    function label() {
      var saved = currentTheme();
      var isDark = saved ? saved === "dark" : systemPrefersDark();
      btn.textContent = isDark ? "☀ Light" : "● Dark";
    }
    label();

    btn.addEventListener("click", function () {
      var saved = currentTheme();
      var isDark = saved ? saved === "dark" : systemPrefersDark();
      var next = isDark ? "light" : "dark";
      applyTheme(next);
      try { localStorage.setItem(STORAGE_KEY, next); } catch (e) {}
      label();
    });
  });

  // ---- Mobile-safe external links ----
  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('a[href^="http"]').forEach(function (a) {
      if (a.hostname !== window.location.hostname) {
        a.setAttribute("target", "_blank");
        a.setAttribute("rel", "noopener");
      }
    });
  });
})();
