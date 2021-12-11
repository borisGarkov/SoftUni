import { html, render } from '../lib.js';
import { serverHost, mainSection, updateUserNav } from '../utils.js';


async function retrieveData() {
    let temp = [];

    const response = await fetch(serverHost + '/data/memes?sortBy=_createdOn%20desc');
    const jsonData = await response.json();

    for (const object of jsonData) {
        temp.push(html`
        <div class="meme">
            <div class="card">
                <div class="info">
                    <p class="meme-title">${object.title}</p>
                    <img class="meme-image" alt="meme-img" src="${object.imageUrl}">
                </div>
                <div id="data-buttons">
                    <a class="button" href="/meme-details/${object._id}">Details</a>
                </div>
            </div>
        </div>`);
    }

    return temp
}

let temp = await retrieveData();

const allMemesTemplate = html`
<!-- All Memes Page ( for Guests and Users )-->
<section id="meme-feed">
    <h1>All Memes</h1>
    <div id="memes">
        ${temp.length != 0 ? html`${temp}` : html`<p class="no-memes">No memes in database.</p>`}
    </div>
</section>`;

export function allMemesPage(ctx) {
    ctx.render(allMemesTemplate)
}
