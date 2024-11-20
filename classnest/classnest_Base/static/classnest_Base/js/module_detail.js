// Variables to store the form to submit
let formToSubmit;

// Show the modal
function showModal(form) {
  formToSubmit = form; // Store the form to submit
  const modal = document.getElementById('deleteModal');
  modal.style.display = 'flex';
}

// Close the modal
function closeModal() {
  const modal = document.getElementById('deleteModal');
  modal.style.display = 'none';
}


// Confirm deletion
document.getElementById('confirmDeleteButton').addEventListener('click', function() {
  if (formToSubmit) {
    formToSubmit.submit(); // Submit the stored form
  }
});

// Attach event listeners to delete buttons
document.querySelectorAll('form[action*="delete"]').forEach(form => {
  form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    showModal(form); // Show the modal
  });
});
