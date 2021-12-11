import { html, render } from '../lib.js';
import { serverHost, userData } from '../utils.js';

const detailsTemplate = (album, isOwner) => html`<!--Details Page-->
<section id="detailsPage">
    <div class="wrapper">
        <div class="albumCover">
            <img src="${album.imgUrl}">
        </div>
        <div class="albumInfo">
            <div class="albumText">

                <h1>Name: ${album.name}</h1>
                <h3>Artist: ${album.artist}</h3>
                <h4>Genre: ${album.genre}</h4>
                <h4>Price: $${album.price}</h4>
                <h4>Date: ${album.releaseDate}</h4>
                <p>${album.description}</p>
            </div>

            <!-- Only for registered user and creator of the album-->
            ${isOwner ? html`<div class="actionBtn">
                <a href="/edit/${album._id}" class="edit">Edit</a>
                <a href="/delete/${album._id}" class="remove">Delete</a>
            </div>` : null}

        </div>
    </div>
</section>`;


async function retieveData(albumId) {
    try {

        const response = await fetch(serverHost + `/data/albums/${albumId}`);

        if (response.ok != true) {
            const error = await response.json();
            throw new Error(error.message);
        }

        const album = await response.json();

        const data = userData();

        const isOwner = data && album._ownerId == data.id;

        return detailsTemplate(album, isOwner);

    } catch (error) {
        alert(error.message);
    }
}


export async function detailsPage(ctx) {
    const albumId = ctx.params.id;

    let template = await retieveData(albumId);
    ctx.render(template);
}