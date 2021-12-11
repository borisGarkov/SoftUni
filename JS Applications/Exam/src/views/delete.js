import { html, render, page } from '../lib.js';
import { serverHost, updateNavigation, userData } from '../utils.js';


async function deleteByID(albumId) {
    try {
        const response = await fetch(serverHost + `/data/albums/${albumId}`, {
            method: 'delete',
            headers: {
                'Content-Type': 'application/json',
                'X-Authorization': userData().token,
            },
        });

        if (response.ok != true) {
            const error = await response.json();
            throw new Error(error.message);
        }

        const result = await response.json();

    } catch (error) {
        alert(error.message);
    }
}

export async function onDelete(ctx) {
    const albumId = ctx.params.id;
    const choice = confirm('Do you want to delete this meme?');

    if (choice) {
        await deleteByID(albumId);
        ctx.page.redirect('/catalog');
    }
}