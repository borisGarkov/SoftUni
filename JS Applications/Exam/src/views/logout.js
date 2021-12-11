import { page } from '../lib.js';
import { serverHost, updateNavigation } from '../utils.js';

export async function logoutPage() {
    try {

        const response = await fetch(serverHost + '/users/logout', {
            method: 'get',
            headers: {
                'Content-Type': 'application/json',
                'X-Authorization': JSON.parse(sessionStorage.userData).token,
            },
        });

        if (response.ok != true) {
            const error = await response.json();
            throw new Error(error.message);
        }

        sessionStorage.clear();

        updateNavigation();
        page.redirect('/');

    } catch (error) {
        alert(error.message);
    }
}