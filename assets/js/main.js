// Dropdown functionality for mobile
document.addEventListener('DOMContentLoaded', function() {
  const dropdowns = document.querySelectorAll('.dropdown');

  dropdowns.forEach(function(dropdown) {
    const dropbtn = dropdown.querySelector('.dropbtn');

    if (dropbtn) {
      dropbtn.addEventListener('click', function(e) {
        e.stopPropagation();
        dropdown.classList.toggle('active');

        // Close other dropdowns
        dropdowns.forEach(function(otherDropdown) {
          if (otherDropdown !== dropdown) {
            otherDropdown.classList.remove('active');
          }
        });
      });
    }
  });

  // Close dropdowns when clicking outside
  document.addEventListener('click', function() {
    dropdowns.forEach(function(dropdown) {
      dropdown.classList.remove('active');
    });
  });
});
