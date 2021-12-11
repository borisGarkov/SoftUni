import { html, render, page } from '../lib.js';
import { mainSection, serverHost, updateUserNav, notify } from '../utils.js';

const registerTemplate = html`
<!-- Register Page ( Only for guest users ) -->
<section id="register">
    <form @submit=${onRegister} id="register-form">
        <div class="container">
            <h1>Register</h1>
            <label for="username">Username</label>
            <input id="username" type="text" placeholder="Enter Username" name="username">
            <label for="email">Email</label>
            <input id="email" type="text" placeholder="Enter Email" name="email">
            <label for="password">Password</label>
            <input id="password" type="password" placeholder="Enter Password" name="password">
            <label for="repeatPass">Repeat Password</label>
            <input id="repeatPass" type="password" placeholder="Repeat Password" name="repeatPass">
            <div class="gender">
                <input type="radio" name="gender" id="female" value="female">
                <label for="female">Female</label>
                <input type="radio" name="gender" id="male" value="male" checked>
                <label for="male">Male</label>
            </div>
            <input type="submit" class="registerbtn button" value="Register">
            <div class="container signin">
                <p>Already have an account?<a href="/login">Sign in</a>.</p>
            </div>
        </div>
    </form>
</section>`;

export function registerPage() {
    render(registerTemplate, mainSection);
}

async function onRegister(event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    const username = formData.get('username').trim();
    const email = formData.get('email').trim();
    const password = formData.get('password').trim();
    const repeatPass = formData.get('repeatPass').trim();
    const gender = formData.get('gender');

    if (username == '' || email == '' || password == '') {
        notify('All fields must be completed');
        return;
    }

    if (password != repeatPass) {
        notify('Passwords do not match');
        return;
    }

    console.log(gender);

    try {

        const response = await fetch(serverHost + '/users/register', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username,
                email,
                password,
                gender,
            })
        });

        if (response.ok != true) {
            const error = await response.json();
            throw new Error(error.message);
        }

        const result = await response.json();

        console.log(result);

        const userData = {
            email: result.email,
            id: result._id,
            token: result.accessToken,
        };

        sessionStorage.setItem('userData', JSON.stringify(userData));

        console.log(sessionStorage);

        page.redirect('/all-memes');
        updateUserNav();


    } catch (error) {
        notify(error.message);
    }
}