// Fade-in on page load
document.body.style.opacity = 0;

window.addEventListener("load", () => {
  document.body.style.transition = "opacity 0.6s ease";
  document.body.style.opacity = 1;
});


const wrapper = document.querySelector(".carousel-wrapper");
const track = document.querySelector(".carousel-track");
const slides = document.querySelectorAll(".carousel-card");
const dots = document.querySelectorAll(".dot");

let index = 1; // start at first real slide
const gap = 32;
let autoPlayInterval;
let isPaused = false;

// --------------------
// UPDATE + CENTER
// --------------------
function updateCarousel(animate = true) {
  if (!slides[index]) return;

  const slideWidth = slides[index].offsetWidth;
  const wrapperWidth = wrapper.offsetWidth;

  const offset =
    index * (slideWidth + gap) -
    (wrapperWidth / 2 - slideWidth / 2);

  track.style.transition = animate
    ? "transform 1s cubic-bezier(0.4, 0, 0.2, 1)"
    : "none";

  track.style.transform = `translateX(-${offset}px)`;

  slides.forEach(s => s.classList.remove("active"));
  slides[index].classList.add("active");

  dots.forEach(d => d.classList.remove("active"));
  if (dots[index - 1]) dots[index - 1].classList.add("active");
}

// --------------------
// INFINITE LOOP FIX
// --------------------
track.addEventListener("transitionend", () => {
  if (!slides[index]) return;

  if (slides[index].classList.contains("clone")) {
    track.style.transition = "none";

    if (index === slides.length - 1) {
      index = 1;
    } else if (index === 0) {
      index = slides.length - 2;
    }

    updateCarousel(false);
  }
});

// --------------------
// DOT NAVIGATION
// --------------------
dots.forEach((dot, i) => {
  dot.addEventListener("click", () => {
    index = i + 1;
    updateCarousel();
  });
});

// --------------------
// AUTOPLAY (SAFE)
// --------------------
function startAutoplay() {
  autoPlayInterval = setInterval(() => {
    if (!isPaused) {
      index++;
      if (index >= slides.length) index = slides.length - 1;
      updateCarousel();
    }
  }, 9000);
}

function stopAutoplay() {
  clearInterval(autoPlayInterval);
}

// Pause on hover
wrapper.addEventListener("mouseenter", () => {
  isPaused = true;
});

wrapper.addEventListener("mouseleave", () => {
  isPaused = false;
});

// --------------------
// KEYBOARD SUPPORT
// --------------------
document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowRight") {
    index++;
    if (index >= slides.length) index = slides.length - 1;
    updateCarousel();
  }

  if (e.key === "ArrowLeft") {
    index--;
    if (index < 0) index = 0;
    updateCarousel();
  }
});

// --------------------
// SWIPE SUPPORT
// --------------------
let startX = 0;
let isDragging = false;

wrapper.addEventListener("touchstart", (e) => {
  startX = e.touches[0].clientX;
  isDragging = true;
  isPaused = true;
});

wrapper.addEventListener("touchend", (e) => {
  if (!isDragging) return;

  const endX = e.changedTouches[0].clientX;
  const diff = startX - endX;

  if (diff > 50) {
    index++;
    if (index >= slides.length) index = slides.length - 1;
  } else if (diff < -50) {
    index--;
    if (index < 0) index = 0;
  }

  updateCarousel();
  isDragging = false;
  isPaused = false;
});

// --------------------
// INIT
// --------------------
updateCarousel(false);
startAutoplay();



