---
---
let deferredPrompt = null;

const installButton = document.querySelector(".install-button");
const mobileNav = document.querySelector(".mobile-nav");
const isStandalone = window.matchMedia("(display-mode: standalone)").matches || window.navigator.standalone;

if (isStandalone) {
  document.documentElement.classList.add("is-standalone");
}

if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("{{ '/sw.js' | relative_url }}", {
      scope: "{{ '/' | relative_url }}"
    }).catch(() => {});
  });
}

window.addEventListener("beforeinstallprompt", (event) => {
  event.preventDefault();
  deferredPrompt = event;
  if (installButton) {
    installButton.hidden = false;
  }
});

window.addEventListener("appinstalled", () => {
  deferredPrompt = null;
  if (installButton) {
    installButton.hidden = true;
  }
});

if (installButton) {
  installButton.addEventListener("click", async () => {
    if (!deferredPrompt) {
      return;
    }

    deferredPrompt.prompt();
    await deferredPrompt.userChoice;
    deferredPrompt = null;
    installButton.hidden = true;
  });
}

if (mobileNav) {
  const mobileBreakpoint = window.matchMedia("(max-width: 759px)");

  const updateMobileNavVisibility = () => {
    if (!mobileBreakpoint.matches) {
      mobileNav.classList.remove("is-visible");
      return;
    }

    const threshold = 120;
    const scrollBottom = window.scrollY + window.innerHeight;
    const pageBottom = document.documentElement.scrollHeight - threshold;
    mobileNav.classList.toggle("is-visible", scrollBottom >= pageBottom);
  };

  updateMobileNavVisibility();
  window.addEventListener("scroll", updateMobileNavVisibility, { passive: true });
  window.addEventListener("resize", updateMobileNavVisibility);
  mobileBreakpoint.addEventListener("change", updateMobileNavVisibility);
}
