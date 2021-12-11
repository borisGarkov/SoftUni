import { html, render, page } from '../lib.js';
import { serverHost, updateNavigation } from '../utils.js';

const createTemplate = html`
<!--Create Page-->
<section class="createPage">
    <form @submit="${onSubmit}">
        <fieldset>
            <legend>Add Album</legend>

            <div class="container">
                <label for="name" class="vhide">Album name</label>
                <input id="name" name="name" class="name" type="text" placeholder="Album name">

                <label for="imgUrl" class="vhide">Image Url</label>
                <input id="imgUrl" name="imgUrl" class="imgUrl" type="text" placeholder="Image Url">

                <label for="price" class="vhide">Price</label>
                <input id="price" name="price" class="price" type="text" placeholder="Price">

                <label for="releaseDate" class="vhide">Release date</label>
                <input id="releaseDate" name="releaseDate" class="releaseDate" type="text" placeholder="Release date">

                <label for="artist" class="vhide">Artist</label>
                <input id="artist" name="artist" class="artist" type="text" placeholder="Artist">

                <label for="genre" class="vhide">Genre</label>
                <input id="genre" name="genre" class="genre" type="text" placeholder="Genre">

                <label for="description" class="vhide">Description</label>
                <textarea name="description" class="description" placeholder="Description"></textarea>

                <button class="add-album" type="submit">Add New Album</button>
            </div>
        </fieldset>
    </form>
</section>`;


async function onSubmit(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const name = formData.get('name').trim();
    const imgUrl = formData.get('imgUrl').trim();
    const price = formData.get('price').trim();
    const releaseDate = formData.get('releaseDate').trim();
    const artist = formData.get('artist').trim();
    const genre = formData.get('genre').trim();
    const description = formData.get('description').trim();


    if (name == '' || imgUrl == '' || price == '' || releaseDate == '' || artist == '' || genre == '' || description == '') {
        alert('All fields must be filled');
        return
    }

    try {
        const response = await fetch(serverHost + '/data/albums', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json',
                'X-Authorization': JSON.parse(sessionStorage.getItem('userData')).token,
            },
            body: JSON.stringify({
                name,
                imgUrl,
                price,
                releaseDate,
                artist,
                genre,
                description,
            })
        });

        if (response.ok != true) {
            const error = await response.json();
            throw new Error(error.message);
        }

        const result = await response.json();

        page.redirect('/catalog');

    } catch (error) {
        alert(error.message);
    }
}

export function createAlbumPage(ctx) {
    ctx.render(createTemplate);
}