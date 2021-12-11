import { html, render, page } from '../lib.js';
import { mainSection, serverHost, userData, notify } from '../utils.js';


const createMemeTemplate = html`
<!-- Create Meme Page ( Only for logged users ) -->
<section id="create-meme">
    <form @submit="${onSubmit}" id="create-form">
        <div class="container">
            <h1>Create Meme</h1>
            <label for="title">Title</label>
            <input id="title" type="text" placeholder="Enter Title" name="title">
            <label for="description">Description</label>
            <textarea id="description" placeholder="Enter Description" name="description"></textarea>
            <label for="imageUrl">Meme Image</label>
            <input id="imageUrl" type="text" placeholder="Enter meme ImageUrl" name="imageUrl">
            <input type="submit" class="registerbtn button" value="Create Meme">
        </div>
    </form>
</section>`;


export function createMemePage(ctx) {
    ctx.render(createMemeTemplate, mainSection);
}

async function onSubmit(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const title = formData.get('title').trim();
    const description = formData.get('description').trim();
    const imageUrl = formData.get('imageUrl').trim();

    if (title == '' || description == '' || imageUrl == '') {
        notify('All fields must be filled');
        return
    }

    try {
        const response = await fetch(serverHost + '/data/memes', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json',
                'X-Authorization': JSON.parse(sessionStorage.getItem('userData')).token,
            },
            body: JSON.stringify({
                title,
                description,
                imageUrl,
            })
        });

        if (response.ok != true) {
            const error = await response.json();
            throw new Error(error.message);
        }

        const result = await response.json();

        page.redirect('/all-memes');

    } catch (error) {
        notify(error.message);
    }
}