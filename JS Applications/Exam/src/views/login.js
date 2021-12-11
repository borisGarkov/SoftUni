import { html, render, page } from '../lib.js';
import { serverHost, updateNavigation } from '../utils.js';

const loginTemplate = html`<!--Login-->
<section id="loginPage">
    <form @submit="${onSubmit}">
        <fieldset>
            <legend>Login</legend>

            <label for="email" class="vhide">Email</label>
            <input id="email" class="email" name="email" type="text" placeholder="Email">

            <label for="password" class="vhide">Password</label>
            <input id="password" class="password" name="password" type="password" placeholder="Password">

            <button type="submit" class="login">Login</button>

            <p class="field">
                <span>If you don't have profile click <a href="/register">here</a></span>
            </p>
        </fieldset>
    </form>
</section>`;

async function onSubmit(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const email = formData.get('email');
    const password = formData.get('password');

    if (email == '' || password == '') {
        return alert('All fields must be filled');
    }

    try {

        const response = await fetch(serverHost + '/users/login', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email,
                password,
            })
        });

        if (response.ok != true) {
            const error = await response.json();
            throw new Error(error.message);
        }

        const result = await response.json();

        const userData = {
            email: result.email,
            id: result._id,
            token: result.accessToken,
        };

        sessionStorage.setItem('userData', JSON.stringify(userData));

        updateNavigation();
        page.redirect('/');

    } catch (error) {
        alert(error.message);
    }
}


export function loginPage(ctx) {
    ctx.render(loginTemplate);
}