import { html, render, page } from '../lib.js';
import { mainSection, serverHost, updateUserNav, notify } from '../utils.js';

const loginTemplate = html`
<!-- Login Page ( Only for guest users ) -->
<section id="login">
    <form @submit="${onSubmit}" id="login-form">
        <div class="container">
            <h1>Login</h1>
            <label for="email">Email</label>
            <input id="email" placeholder="Enter Email" name="email" type="text">
            <label for="password">Password</label>
            <input id="password" type="password" placeholder="Enter Password" name="password">
            <input type="submit" class="registerbtn button" value="Login">
            <div class="container signin">
                <p>Dont have an account?<a href="/register">Sign up</a>.</p>
            </div>
        </div>
    </form>
</section>`;

export function loginPage() {
    render(loginTemplate, mainSection);
}

async function onSubmit(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const email = formData.get('email');
    const password = formData.get('password');

    if (email == '' || password == '') {
        return notify('All fields must be filled');
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
            username: result.username,
            gender: result.gender,
            id: result._id,
            token: result.accessToken,
        };

        sessionStorage.setItem('userData', JSON.stringify(userData));
        console.log(sessionStorage);

        updateUserNav();
        page.redirect('/all-memes');

    } catch (error) {
        notify(error.message);
    }
}