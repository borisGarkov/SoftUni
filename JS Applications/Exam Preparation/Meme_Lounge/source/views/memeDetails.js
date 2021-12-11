import { html, render } from '../lib.js';
import { mainSection, serverHost, updateUserNav, userData } from '../utils.js';

const memeDetailsTemplate = (meme, isOwner, onDelete) => html`
<!-- Details Meme Page (for guests and logged users) -->
<section id="meme-details">
    <h1>
        Meme Title: ${meme.title}
    </h1>
    <div class="meme-details">
        <div class="meme-img">
            <img alt="meme-alt" src="${meme.imageUrl}">
        </div>
        <div class="meme-description">
            <h2>Meme Description</h2>
            <p>
                ${meme.description}
            </p>

            <!-- Buttons Edit/Delete should be displayed only for creator of this meme  -->
            ${isOwner ? html`<a class="button warning" href="/edit-meme/${meme._id}">Edit</a>
            <button @click=${onDelete} class="button danger">Delete</button>` : null}
        </div>
    </div>
</section>`;

async function retieveData(memeID, onDelete) {
    try {

        const response = await fetch(serverHost + `/data/memes/${memeID}`);

        if (response.ok != true) {
            const error = await response.json();
            throw new Error(error.message);
        }

        const result = await response.json();

        let isOwner = JSON.parse(sessionStorage.getItem('userData')) && JSON.parse(sessionStorage.getItem('userData')).id == result._ownerId;

        console.log(result);
        return memeDetailsTemplate(result, isOwner, onDelete);

    } catch (error) {
        alert(error.message);
    }
}

async function deleteByID(memeID) {
    try {
        const response = await fetch(serverHost + `/data/memes/${memeID}`, {
            method: 'delete',
            headers: {
                'Content-Type': 'application/json',
                'X-Authorization': JSON.parse(sessionStorage.getItem('userData')).token,
            },
        });

        if (response.ok != true) {
            const error = await response.json();
            throw new Error(error.message);
        }

        const result = await response.json();
        console.log(result);

    } catch (error) {
        alert(error.message);
    }
}

export async function memeDetailsPage(ctx) {
    const memeID = ctx.params.id;

    let template = await retieveData(memeID, onDelete);
    ctx.render(template);

    async function onDelete() {
        const choice = confirm('Do you want to delete this meme?');

        if (choice) {
            await deleteByID(memeID);
            ctx.page.redirect('/all-memes');

        }
    }
}