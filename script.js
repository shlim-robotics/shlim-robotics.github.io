(() => {
  "use strict";

  const navigationLinks = Array.from(document.querySelectorAll(".navigation a"));
  const sections = Array.from(document.querySelectorAll("main > section[id]"));

  function updateNavigation() {
    const active = sections.reduce((current, section) => {
      return section.getBoundingClientRect().top <= 150 ? section.id : current;
    }, sections[0]?.id);
    navigationLinks.forEach((link) => {
      if (link.getAttribute("href") === `#${active}`) {
        link.setAttribute("aria-current", "location");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  }

  let framePending = false;
  window.addEventListener("scroll", () => {
    if (framePending) return;
    framePending = true;
    window.requestAnimationFrame(() => {
      updateNavigation();
      framePending = false;
    });
  }, { passive: true });
  window.addEventListener("resize", updateNavigation);
  updateNavigation();
})();
