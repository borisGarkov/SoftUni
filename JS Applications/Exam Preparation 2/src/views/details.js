import { html, render } from '../lib.js';
import { serverHost, userData } from '../utils.js';

const detailsTemplate = (book, isOwner) => html`<!-- Details Page ( for Guests and Users ) -->
<section id="details-page" class="details">
    <div class="book-information">
        <h3>${book.title}</h3>
        <p class="type">Type: ${book.type}</p>
        <p class="img"><img src="${book.imageUrl}"></p>
        <div class="actions">

            <!-- Edit/Delete buttons ( Only for creator of this book )  -->
            ${isOwner ? html`<a class="button" href="#">Edit</a>
            <a class="button" href="/delete/${book._id}">Delete</a>` : null}

            <!-- Bonus -->
            <!-- Like button ( Only for logged-in users, which is not creators of the current book ) -->
            <a class="button" href="#">Like</a>

            <!-- ( for Guests and Users )  -->
            <div class="likes">
                <img class="hearts" src="/images/heart.png">
                <span id="total-likes">Likes: 0</span>
            </div>
            <!-- Bonus -->
        </div>
    </div>
    <div class="book-description">
        <h3>Description:</h3>
        <p>${book.description}</p>
    </div>
</section>`


async function retieveData(bookId) {
    try {

        const response = await fetch(serverHost + `/data/books/${bookId}`);

        if (response.ok != true) {
            const error = await response.json();
            throw new Error(error.message);
        }

        const book = await response.json();

        const data = userData();

        const isOwner = data && book._ownerId == data.id;

        return detailsTemplate(book, isOwner);

    } catch (error) {
        alert(error.message);
    }
}

export async function detailsPage(ctx) {
    const bookId = ctx.params.id;

    let template = await retieveData(bookId);
    ctx.render(template);
}