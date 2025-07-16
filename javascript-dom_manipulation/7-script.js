const ul = document.getElementById('list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(response => response.json())
.then(film => {
    for (let i = 0; i < film.results.length; i++) {
        const new_li = document.createElement('li');
        new_li.textContent = film.results[i].title;
        ul.appendChild(new_li);
    };
});
