import { html, render, page } from '../lib.js';
import { serverHost, updateNavigation, userData, mainSection } from '../utils.js';

const searchTemplate = html`<!--Search Page-->
<section id="searchPage">
    <h1>Search by Name</h1>

    <div class="search">
        <input id="search-input" type="text" name="search" placeholder="Enter desired albums's name">
        <button id='search' class="button-list">Search</button>
    </div>

    <h2>Results:</h2>
</section>`;

const resultsTemplate = (albums) => html`<!--Search Page-->
<section id="searchPage">
    <h1>Search by Name</h1>

    <div class="search">
        <input id="search-input" type="text" name="search" placeholder="Enter desired albums's name">
        <button id='search' class="button-list">Search</button>
    </div>

    <h2>Results:</h2>

    <!--Show after click Search button-->
    <div class="search-result">
        <!--If have matches-->
        ${albums.length > 0 ? html`${albums}` : html`<p class="no-result">No result.</p>`};
    </div>
</section>`;


async function onSubmit(event) {
    event.preventDefault();

    const query = document.getElementById('search-input').value.trim();

    if (query == '') {
        return alert('All fields must be filled');
    }

    try {
        const response = await fetch(serverHost + `/data/albums?where=name%20LIKE%20%22${query}%22`,);

        if (response.ok != true) {
            const error = await response.json();
            throw new Error(error.message);
        }

        const results = await response.json();

        let albums = [];

        for (const album of results) {
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
                    ${userData() ? html`<div class="btn-group"> <a href="/details/${album._id}" id="details">Details</a></div>` :
                                null}
                </div>
            </div>`);
        }

        render(resultsTemplate(albums), mainSection);

    } catch (error) {
        alert(error.message);
    }
}


export function searchPage(ctx) {
    ctx.render(searchTemplate);

    const button = document.getElementById('search');
    button.addEventListener('click', onSubmit);
}