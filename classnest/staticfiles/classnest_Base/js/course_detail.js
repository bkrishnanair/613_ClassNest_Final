// Function to show the delete confirmation modal
function showDeleteConfirmation() {
  const modal = document.getElementById('deleteModal');
  modal.style.display = 'flex'; // Show the modal
}

// Function to close the modal
function closeModal() {
  const modal = document.getElementById('deleteModal');
  modal.style.display = 'none'; // Hide the modal
}

// Function to confirm and execute the delete action
function confirmDelete() {
  // Redirect to the delete URL
  window.location.href = deleteCourseUrl;
}
