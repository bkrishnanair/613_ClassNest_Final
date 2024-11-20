const modal = document.getElementById('composeModal');
const form = document.getElementById('composeForm');

    function openComposeModal() {
      modal.classList.add('active');
      window.location.href = 'compose.html'; 
    }

    function closeComposeModal() {
      modal.classList.remove('active');
    }

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('Email sent successfully!');
      closeComposeModal();
    });