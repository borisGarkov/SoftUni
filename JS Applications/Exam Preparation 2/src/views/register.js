import { html, render, page } from '../lib.js';
import { serverHost, updateNavigation } from '../utils.js';

const registerTemplate = html`<!-- Register Page ( Only for Guest users ) -->
<section id="register-page" class="register">
    <form @submit="${onRegister}" id="register-form" action="" method="">
        <fieldset>
            <legend>Register Form</legend>
            <p class="field">
                <label for="email">Email</label>
                <span class="input">
                    <input type="text" name="email" id="email" placeholder="Email">
                </span>
            </p>
            <p class="field">
                <label for="password">Password</label>
                <span class="input">
                    <input type="password" name="password" id="password" placeholder="Password">
                </span>
            </p>
            <p class="field">
                <label for="repeat-pass">Repeat Password</label>
                <span class="input">
                    <input type="password" name="confirm-pass" id="repeat-pass" placeholder="Repeat Password">
                </span>
            </p>
            <input class="button submit" type="submit" value="Register">
        </fieldset>
    </form>
</section>`;

async function onRegister(event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    const email = formData.get('email').trim();
    const password = formData.get('password').trim();
    const repeatPass = formData.get('confirm-pass').trim();

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