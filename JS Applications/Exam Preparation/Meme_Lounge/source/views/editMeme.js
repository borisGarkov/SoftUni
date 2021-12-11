import { html, render, page } from '../lib.js';
import { mainSection, updateUserNav, userData, serverHost, notify } from '../utils.js';


const editMemeTemplate = (meme) => html`
<!-- Edit Meme Page ( Only for logged user and creator to this meme )-->
<section id="edit-meme">
    <form @submit="${onEdit.bind(null, meme._id)}" id="edit-form">
        <h1>Edit Meme</h1>
        <div class="container">
            <label for="title">Title</label>
            <input id="title" type="text" placeholder="Enter Title" name="title" value="${meme.title}">
            <label for="description">Description</label>
            <textarea id="description" placeholder="Enter Description" name="description"
                >${meme.description}</textarea>
            <label for="imageUrl">Image Url</label>
            <input id="imageUrl" type="text" placeholder="Enter Meme ImageUrl" name="imageUrl" value=${meme.imageUrl}>
            <input type="submit" class="registerbtn button" value="Edit Meme">
        </div>
    </form>
</section>`;

async function retieveData(memeID) {
    try {

        const response = await fetch(serverHost + `/data/memes/${memeID}`);

        if (response.ok != true) {
            const error = await response.json();
            throw new Error(error.message);
        }

        const result = await response.json();

        console.log(result);
        return editMemeTemplate(result);

    } catch (error) {
        notify(error.message);
    }
}

export async function editMemePage(ctx) {
    const memeID = ctx.params.id;

    let template = await retieveData(memeID);

    ctx.render(template);
}

async function onEdit(memeID, event) {
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
        const response = await fetch(serverHost + `/data/memes/${memeID}`, {
            method: 'put',
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