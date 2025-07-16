document.addEventListener('DOMContentLoaded', () => {
    const hello = document.getElementById('hello');
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
        hello.textContent = data.hello;
    });
});
