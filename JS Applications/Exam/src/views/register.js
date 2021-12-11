import { html, render, page } from '../lib.js';
import { serverHost, updateNavigation } from '../utils.js';

const registerTemplate = html`<!--Registration-->
<section id="registerPage">
    <form @submit="${onRegister}">
        <fieldset>
            <legend>Register</legend>

            <label for="email" class="vhide">Email</label>
            <input id="email" class="email" name="email" type="text" placeholder="Email">

            <label for="password" class="vhide">Password</label>
            <input id="password" class="password" name="password" type="password" placeholder="Password">

            <label for="conf-pass" class="vhide">Confirm Password:</label>
            <input id="conf-pass" class="conf-pass" name="conf-pass" type="password" placeholder="Confirm Password">

            <button type="submit" class="register">Register</button>

            <p class="field">
                <span>If you already have profile click <a href="/login">here</a></span>
            </p>
        </fieldset>
    </form>
</section>`;

async function onRegister(event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    const email = formData.get('email').trim();
    const password = formData.get('password').trim();
    const repeatPass = formData.get('conf-pass').trim();

    if (email == '' || password == '') {
        alert('All fields must be completed');
        return;
    }

    if (password != repeatPass) {
        alert('Passwords do not match');
        return;
    }

    try {

        const response = await fetch(serverHost + '/users/register', {
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

export function registerPage(ctx) {
    ctx.render(registerTemplate);
}