import { html, render, page } from '../lib.js';
import { serverHost, updateNavigation } from '../utils.js';

const loginTemplate = html`<!-- Login Page ( Only for Guest users ) -->
<section id="login-page" class="login">
    <form @submit="${onSubmit}" id="login-form" action="" method="">
        <fieldset>
            <legend>Login Form</legend>
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
            <input class="button submit" type="submit" value="Login">
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