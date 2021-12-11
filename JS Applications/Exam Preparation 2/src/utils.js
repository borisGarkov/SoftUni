const serverHost = 'http://localhost:3030';
const userData = () => JSON.parse(sessionStorage.getItem('userData'));
const mainSection = document.getElementById('site-content');

function updateNavigation() {

    if (userData()) {
        document.querySelector('#guest').style.display = 'none';
        document.querySelector('#user').style.display = 'block';
        document.querySelector('#user span').textContent = `Welcome, ${userData().email}`;

    } else {
        document.querySelector('#guest').style.display = 'block';
        document.querySelector('#user').style.display = 'none';
    }
}

export {
    serverHost,
    userData,
    updateNavigation,
    mainSection,
}