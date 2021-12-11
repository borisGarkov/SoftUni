import { html, render, page } from '../lib.js';
import { serverHost, updateNavigation } from '../utils.js';

const addBookTemplate = html`
<!-- Create Page ( Only for logged-in users ) -->
<section id="create-page" class="create">
    <form @submit="${onSubmit}" id="create-form" action="" method="">
        <fieldset>
            <legend>Add new Book</legend>
            <p class="field">
                <label for="title">Title</label>
                <span class="input">
                    <input type="text" name="title" id="title" placeholder="Title">
                </span>
            </p>
            <p class="field">
                <label for="description">Description</label>
                <span class="input">
                    <textarea name="description" id="description" placeholder="Description"></textarea>
                </span>
            </p>
            <p class="field">
                <label for="image">Image</label>
                <span class="input">
                    <input type="text" name="imageUrl" id="image" placeholder="Image">
                </span>
            </p>
            <p class="field">
                <label for="type">Type</label>
                <span class="input">
                    <select id="type" name="type">
                        <option value="Fiction">Fiction</option>
                        <option value="Romance">Romance</option>
                        <option value="Mistery">Mistery</option>
                        <option value="Classic">Clasic</option>
                        <option value="Other">Other</option>
                    </select>
                </span>
            </p>
            <input class="button submit" type="submit" value="Add Book">
        </fieldset>
    </form>
</section>`;

async function onSubmit(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const title = formData.get('title').trim();
    const description = formData.get('description').trim();
    const imageUrl = formData.get('imageUrl').trim();
    const type = formData.get('type');

    if (title == '' || description == '' || imageUrl == '') {
        notify('All fields must be filled');
        return
    }

    try {
        const response = await fetch(serverHost + '/data/books', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json',
                'X-Authorization': JSON.parse(sessionStorage.getItem('userData')).token,
            },
            body: JSON.stringify({
                title,
                description,
                imageUrl,
                type,
            })
        });

        if (response.ok != true) {
            const error = await response.json();
            throw new Error(error.message);
        }

        const result = await response.json();

        page.redirect('/');

    } catch (error) {
        alert(error.message);
    }
}

export function createBookPage(ctx) {
    ctx.render(addBookTemplate);
}