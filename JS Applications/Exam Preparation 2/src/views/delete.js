import { html, render, page } from '../lib.js';
import { serverHost, updateNavigation, userData } from '../utils.js';


async function deleteByID(bookId) {
    try {
        const response = await fetch(serverHost + `/data/books/${bookId}`, {
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
    const bookId = ctx.params.id;
    console.log(bookId);

    const choice = confirm('Do you want to delete this meme?');

    if (choice) {
        await deleteByID(bookId);
        ctx.page.redirect('/');
    }
}