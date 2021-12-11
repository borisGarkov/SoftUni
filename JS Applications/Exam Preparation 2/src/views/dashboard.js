import { html, render } from '../lib.js';
import { serverHost } from '../utils.js';

const template = (books) =>
    html`<section id="dashboard-page" class="dashboard">
    <h1>Dashboard</h1>
    ${books.length > 0 ? html`<ul class="other-books-list">${books}</ul>` : html`<p class="no-books">No books in database!</p>`}
</section>`

async function retrieveData() {
    try {
        const response = await fetch(serverHost + '/data/books?sortBy=_createdOn%20desc',);

        if (response.ok != true) {
            const error = await response.json();
            throw new Error(error.message);
        }

        const result = await response.json();
        let books = [];

        for (const book of result) {
            books.push(
                html`<li class="otherBooks">
    <h3>${book.title}</h3>
    <p>Type: ${book.type}</p>
    <p class="img"><img src="${book.imageUrl}"></p>
    <a class="button" href="/details/${book._id}">${book.description}</a>
</li>`);
        }

        return books

    } catch (error) {
        alert(error.message);
    }
}

export async function dashboardPage(ctx) {
    let books = await retrieveData();

    ctx.render(template(books));
}
