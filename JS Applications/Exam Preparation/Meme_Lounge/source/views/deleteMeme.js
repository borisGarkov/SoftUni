import { page } from '../lib.js';
import { serverHost, updateUserNav } from '../utils.js';


export async function deleteMemePage(ctx) {
    const memeID = ctx.params.id;

    const choice = confirm('Do you want to delete this meme?');

    if (choice) {
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

            ctx.page.redirect('/all-memes');

        } catch (error) {
            alert(error.message);
        }
    }
}