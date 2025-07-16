const button = document.getElementById('add_item');
const ulist = document.querySelector('ul.my_list');

button.addEventListener("click", () => {
    const new_li = document.createElement('li');
    new_li.textContent = 'Item';
    ulist.appendChild(new_li);
});
