import { html, render } from '../lib.js';
import { serverHost, userData } from '../utils.js';

const catalogTemplate = (albums) => html`<!--Catalog-->
<section id="catalogPage">
    <h1>All Albums</h1>
    ${albums.length > 0 ? html`${albums}` : html`<p>No Albums in Catalog!</p>`}
</section>`

async function retrieveData() {
    try {
        const response = await fetch(serverHost + '/data/albums?sortBy=_createdOn%20desc&distinct=name',);

        if (response.ok != true) {
            const error = await response.json();
            throw new Error(error.message);
        }

        const result = await response.json();
        let albums = [];

        for (const album of result) {
            albums.push(html`<div class="card-box">
    <img src="${album.imgUrl}">
    <div>
        <div class="text-center">
            <p class="name">Name: ${album.name}</p>
            <p class="artist">Artist: ${album.artist}</p>
            <p class="genre">Genre: ${album.genre}</p>
            <p class="price">Price: $${album.price}</p>
            <p class="date">Release Date: ${album.releaseDate}</p>
        </div>

        ${userData() ? html`<div class="btn-group">
            <a href="/details/${album._id}" id="details">Details</a>
        </div>` : null
        }
    </div>
</div>`);
        }

        return albums

    } catch (error) {
        alert(error.message);
    }
}

export async function catalogPage(ctx) {
    let albums = await retrieveData();

    ctx.render(catalogTemplate(albums));
}