const loadBooksBtn = document.getElementById('loadBooks');
const tbody = document.querySelector('tbody');
const submitBtn = document.getElementById('submit');
const edit = document.getElementById('edit');

const titleInput = document.querySelector('input[name=title]');
const authorInput = document.querySelector('input[name=author]');

const url = 'http://localhost:3030/jsonstore/collections/books';

loadBooksBtn.addEventListener('click', getBooks);
submitBtn.addEventListener('click', onFormSubmit.bind(null, 'post', url));
tbody.addEventListener('click', updateBook);


async function getBooks(event) {

    let response = await fetch(url);
    let data = await response.json();

    let elementsToAddArray = [];

    for (const [key, value] of Object.entries(data)) {
        let trElement = e('tr', {},
            e('td', { 'textContent': `${value.title}` }),
            e('td', { 'textContent': `${value.author}` }),
            e('td', {},
                e('button', { 'textContent': 'Edit', 'name': `${key}` }),
                e('button', { 'textContent': 'Delete', 'name': `${key}` })
            )
        )

        elementsToAddArray.push(trElement);
    }

    tbody.replaceChildren(...elementsToAddArray);
    console.log(data);
    console.log(Object.entries(data));
}

async function updateBook(event) {

    if (event.target.tagName == 'BUTTON' && event.target.textContent == 'Edit') {

        let id = event.target.name;
        let currentURL = `http://localhost:3030/jsonstore/collections/books/${id}`;
        let response = await fetch(currentURL);
        let data = await response.json();

        titleInput.value = data.title;
        authorInput.value = data.author;

        console.log(data);
        edit.addEventListener('click', onFormSubmit.bind(null, 'put', currentURL));
        edit.style.display = 'block';
        submitBtn.style.display = 'none';
    }
}

async function onFormSubmit(method, url, event) {
    event.preventDefault();

    let form = new FormData(event.target.parentElement);

    const title = form.get('title');
    const author = form.get('author');

    if (title == '' || author == '') {
        alert('Title or Author is empty');
        return
    }

    let response = await fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            author: author.trim(),
            title: title.trim(),
        })
    })

    let data = await response.json();
    
    edit.style.display = 'none';
    submitBtn.style.display = 'block';

    getBooks();
    event.target.parentElement.reset();
}


function e(type, attr, ...content) {
    const element = document.createElement(type);

    for (const prop in attr) {
        element[prop] = attr[prop];
    }

    for (const item of content) {
        if (typeof item == 'string' || typeof item == 'number') {
            item = document.createTextNode(item);
        }
        element.appendChild(item);
    }

    return element;
}