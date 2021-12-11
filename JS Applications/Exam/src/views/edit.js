import { html, render, page } from '../lib.js';
import { serverHost, userData } from "../utils.js";

const editTemplate = (album) => html`<!--Edit Page-->
<section class="editPage">
    <form @submit="${onEdit.bind(null, album._id)}">
        <fieldset>
            <legend>Edit Album</legend>

            <div class="container">
                <label for="name" class="vhide">Album name</label>
                <input id="name" name="name" class="name" type="text" value="${album.name}">

                <label for="imgUrl" class="vhide">Image Url</label>
                <input id="imgUrl" name="imgUrl" class="imgUrl" type="text" value="${album.imgUrl}">

                <label for="price" class="vhide">Price</label>
                <input id="price" name="price" class="price" type="text" value="${album.price}">

                <label for="releaseDate" class="vhide">Release date</label>
                <input id="releaseDate" name="releaseDate" class="releaseDate" type="text" value="${album.releaseDate}">

                <label for="artist" class="vhide">Artist</label>
                <input id="artist" name="artist" class="artist" type="text" value="${album.artist}">

                <label for="genre" class="vhide">Genre</label>
                <input id="genre" name="genre" class="genre" type="text" value="${album.genre}">

                <label for="description" class="vhide">Description</label>
                <textarea name="description" class="description" rows="10" cols="10">${album.description}</textarea>

                <button class="edit-album" type="submit">Edit Album</button>
            </div>
        </fieldset>
    </form>
</section>`;


async function retieveData(albumID) {
    try {

        const response = await fetch(serverHost + `/data/albums/${albumID}`);

        if (response.ok != true) {
            const error = await response.json();
            throw new Error(error.message);
        }

        const album = await response.json();

        return editTemplate(album);

    } catch (error) {
        alert(error.message);
    }
}

async function onEdit(albumID, event) {
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
        const response = await fetch(serverHost + `/data/albums/${albumID}`, {
            method: 'put',
            headers: {
                'Content-Type': 'application/json',
                'X-Authorization': userData().token,
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

        page.redirect(`/details/${albumID}`);

    } catch (error) {
        notify(error.message);
    }
}


export async function editPage(ctx) {
    const albumID = ctx.params.id;

    let template = await retieveData(albumID);

    ctx.render(template);
}