const button = document.getElementById('red_header');
const header = document.querySelector('header');

button.addEventListener("click", () => {
  header.style.color = '#FF0000';
});
