const serverHost = 'http://localhost:3030';
const mainSection = document.getElementsByTagName('main')[0];
let userData = JSON.parse(sessionStorage.getItem('userData'));

function updateUserNav() {
    let userData = JSON.parse(sessionStorage.getItem('userData'));

    if (userData) {
        document.querySelector('.user').style.display = 'block';
        document.querySelector('.guest').style.display = 'none';
        document.querySelector('.profile span').textContent = `Welcome, ${userData.email}`;
    } else {
        document.querySelector('.user').style.display = 'none';
        document.querySelector('.guest').style.display = 'block';
    }
}

const spanElement = document.querySelector('#errorBox span');
const notification = document.getElementsByClassName('notification')[0];

function notify(message) {

    spanElement.textContent = message;
    notification.style.display = 'block';

    setTimeout(() => {
        notification.style.display = 'none';
    }, 3000);
}

export {
    serverHost,
    mainSection,
    updateUserNav,
    userData,
    notify,
}