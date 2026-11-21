/**
 * Lecteur de Diaporama Marp — EFP
 * Découpe les balises <hr> du contenu Markdown compilé en diapositives interactives.
 */

document.addEventListener("DOMContentLoaded", function () {
  const rawContainer = document.getElementById("presentation-raw-content");
  const slidesContainer = document.getElementById("slides-container");
  const btnPrev = document.getElementById("btn-prev-slide");
  const btnNext = document.getElementById("btn-next-slide");
  const btnFullscreen = document.getElementById("btn-fullscreen");
  const slideCounter = document.getElementById("slide-counter");
  const progressBar = document.getElementById("presentation-progress-bar");

  if (!rawContainer || !slidesContainer) return;

  // 1. Découpage du contenu brut en slides en utilisant <hr>
  const children = Array.from(rawContainer.children);
  const slides = [];
  let currentSlideElements = [];

  children.forEach((child) => {
    if (child.tagName.toLowerCase() === "hr") {
      if (currentSlideElements.length > 0) {
        slides.push(currentSlideElements);
        currentSlideElements = [];
      }
    } else {
      currentSlideElements.push(child);
    }
  });

  if (currentSlideElements.length > 0) {
    slides.push(currentSlideElements);
  }

  // Si aucune balise <hr> n'a été trouvée mais qu'il y a du contenu, créer une slide unique
  if (slides.length === 0 && rawContainer.innerHTML.trim() !== "") {
    slides.push(children);
  }

  // 2. Création des sections .marp-slide
  slidesContainer.innerHTML = "";
  const slideSections = [];

  slides.forEach((elements, idx) => {
    const section = document.createElement("section");
    section.className = "marp-slide";
    section.dataset.slideIndex = idx;

    elements.forEach((el) => {
      section.appendChild(el.cloneNode(true));
    });

    slidesContainer.appendChild(section);
    slideSections.push(section);
  });

  let currentIdx = 0;
  const totalSlides = slideSections.length;

  function showSlide(index) {
    if (totalSlides === 0) return;

    if (index < 0) index = 0;
    if (index >= totalSlides) index = totalSlides - 1;

    currentIdx = index;

    slideSections.forEach((s, i) => {
      if (i === currentIdx) {
        s.classList.add("active-slide");
      } else {
        s.classList.remove("active-slide");
      }
    });

    // Mise à jour du compteur
    if (slideCounter) {
      slideCounter.textContent = `${currentIdx + 1} / ${totalSlides}`;
    }

    // Mise à jour de la barre de progression
    if (progressBar) {
      const pct = ((currentIdx + 1) / totalSlides) * 100;
      progressBar.style.width = `${pct}%`;
    }

    // Mise à jour des boutons
    if (btnPrev) btnPrev.disabled = currentIdx === 0;
    if (btnNext) btnNext.disabled = currentIdx === totalSlides - 1;

    // Déclencher le rendu Mermaid si nécessaire
    if (window.mermaid) {
      try {
        window.mermaid.run({
          nodes: slideSections[currentIdx].querySelectorAll(".language-mermaid, .mermaid")
        });
      } catch (e) {
        // Ignorer si déjà rendu
      }
    }
  }

  // Navigation
  function nextSlide() {
    if (currentIdx < totalSlides - 1) {
      showSlide(currentIdx + 1);
    }
  }

  function prevSlide() {
    if (currentIdx > 0) {
      showSlide(currentIdx - 1);
    }
  }

  if (btnPrev) btnPrev.addEventListener("click", prevSlide);
  if (btnNext) btnNext.addEventListener("click", nextSlide);

  // Plein écran
  if (btnFullscreen) {
    btnFullscreen.addEventListener("click", function () {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
      } else {
        document.exitFullscreen().catch(() => {});
      }
    });
  }

  // Écoute des touches clavier
  document.addEventListener("keydown", function (e) {
    // Ne pas intercepter si focus sur un champ texte
    if (["input", "textarea", "select"].includes(document.activeElement.tagName.toLowerCase())) {
      return;
    }

    switch (e.key) {
      case "ArrowRight":
      case "ArrowDown":
      case " ":
      case "Enter":
        e.preventDefault();
        nextSlide();
        break;
      case "ArrowLeft":
      case "ArrowUp":
      case "Backspace":
        e.preventDefault();
        prevSlide();
        break;
      case "Home":
        e.preventDefault();
        showSlide(0);
        break;
      case "End":
        e.preventDefault();
        showSlide(totalSlides - 1);
        break;
      case "f":
      case "F":
        e.preventDefault();
        if (btnFullscreen) btnFullscreen.click();
        break;
    }
  });

  // Affichage initial de la première slide
  showSlide(0);
});
