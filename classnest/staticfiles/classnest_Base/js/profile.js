function toggleTheme() {
    const body = document.body;
  
    // Toggle dark mode by adding/removing a CSS class
    body.classList.toggle('dark-mode');
  
    // Change button text and appearance based on theme
    const themeBtn = document.getElementById('theme-toggle-btn');
    if (body.classList.contains('dark-mode')) {
        themeBtn.innerText = "☀️ Light Mode";
        themeBtn.style.backgroundColor = "#333"; // Darker background
        themeBtn.style.color = "#fff"; // White text
    } else {
        themeBtn.innerText = "🌙 Dark Mode";
        themeBtn.style.backgroundColor = "#4A90E2"; // Default blue
        themeBtn.style.color = "#fff"; // White text
    }
  }