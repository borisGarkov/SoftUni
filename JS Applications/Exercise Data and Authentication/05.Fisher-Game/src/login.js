
const form = document.querySelector('form');
form.addEventListener('submit', onLogin);

async function onLogin(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const email = formData.get('email');
    const password = formData.get('password');


    try {

        const response = await fetch('http://localhost:3030/users/login', {
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
        console.log(sessionStorage);

        window.location = 'index.html';
        
    } catch (error) {
        alert(error.message);
    }

}