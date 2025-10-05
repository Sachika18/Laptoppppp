// 3d-animations.js
// Adds 3D and scroll-triggered animations to the form elements

document.addEventListener('DOMContentLoaded', function() {
  // 3D tilt effect for the container
  const container = document.querySelector('.container');
  if (container) {
    container.addEventListener('mousemove', function(e) {
      const rect = container.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const rotateX = ((y - centerY) / centerY) * 10;
      const rotateY = ((x - centerX) / centerX) * 10;
      container.style.transform = `perspective(700px) rotateX(${-rotateX}deg) rotateY(${rotateY}deg)`;
    });
    container.addEventListener('mouseleave', function() {
      container.style.transform = 'perspective(700px) rotateX(0deg) rotateY(0deg)';
    });
  }

  // Scroll-triggered animation for form fields
  const formFields = document.querySelectorAll('label, select, input, button');
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-in');
      }
    });
  }, { threshold: 0.2 });

  formFields.forEach(field => {
    observer.observe(field);
  });
});
