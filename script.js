(() => {
  "use strict";

  const filters = document.querySelector(".publication-filters");
  const buttons = Array.from(document.querySelectorAll("[data-filter]"));
  const papers = Array.from(document.querySelectorAll(".paper"));
  const status = document.getElementById("publication-status");

  function filterPublications(filter, announce = true) {
    let visible = 0;
    papers.forEach((paper) => {
      paper.hidden = filter === "selected" && paper.dataset.selected !== "true";
      if (!paper.hidden) visible += 1;
    });
    buttons.forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.filter === filter));
    });
    if (announce) status.textContent = `Showing ${visible} ${filter === "selected" ? "selected " : ""}publications.`;
  }

  if (filters && status) {
    buttons.forEach((button) => {
      button.addEventListener("click", () => filterPublications(button.dataset.filter));
    });
    filters.hidden = false;
    filterPublications("selected", false);
  }

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
