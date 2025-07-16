const button = document.getElementById('red_header');
const header = document.querySelector('header');

button.addEventListener("click", () => {
  header.classList.add('red');
});
