document.addEventListener('DOMContentLoaded', () => {
  const coursesContainer = document.getElementById('courses-container');
  const coursesCount = document.getElementById('courses-count');

  // Mock data for courses
  const courses = [];

  // Update courses count and display message if no courses are enrolled
  coursesCount.textContent = courses.length;
  if (courses.length === 0) {
    coursesContainer.innerHTML = '<p class="empty-message">No courses enrolled yet.</p>';
  }
});
