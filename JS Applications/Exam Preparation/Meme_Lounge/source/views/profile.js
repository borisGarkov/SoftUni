import { html, render, page } from '../lib.js';
import { serverHost, mainSection, updateUserNav } from '../utils.js';

async function retrieveData(){
    try {
        const userId = JSON.parse(sessionStorage.getItem('userData')).id;

        const response = await fetch(serverHost + `/data/memes?where=_ownerId%3D%22${userId}%22&sortBy=_createdOn%20desc`);

        if (response.ok != true) {
            const error = await response.json();
            throw new Error(error.message);
        }

        const memes = await response.json();

        let temp = [];

        for (const meme of memes) {
            temp.push(html`<div class="user-meme">
                <p class="user-meme-title">${meme.title}</p>
                <img class="userProfileImage" alt="meme-img" src="${meme.imageUrl}">
                <a class="button" href="/meme-details/${meme._id}">Details</a>
            </div>`)
        }

        return temp;

    } catch (error) {
        alert(error.message);
    }
}

const allMemesTemplate = (temp, email, gender, username) => html`
<!-- Profile Page ( Only for logged users ) -->
<section id="user-profile-page" class="user-profile">
    <article class="user-info">
        <img id="user-avatar-url" alt="user-profile" src="/images/${gender}.png">
        <div class="user-content">
            <p>Username: ${username}</p>
            <p>Email: ${email}</p>
            <p>My memes count: ${temp.length}</p>
        </div>
    </article>
    <h1 id="user-listings-title">User Memes</h1>
    <div class="user-meme-listings">
        <!-- Display : All created memes by this user (If any) -->
        ${temp.length > 0 ?
            html`${temp}` : html`<p class="no-memes">No memes in database.</p>`
        }
    </div>
</section>`;

export async function profilePage(ctx) {
    let temp = await retrieveData();

    const email = JSON.parse(sessionStorage.getItem('userData')).email;
    const gender = JSON.parse(sessionStorage.getItem('userData')).gender;
    const username = JSON.parse(sessionStorage.getItem('userData')).username;

    ctx.render(allMemesTemplate(temp, email, gender, username));
}
