const serverHost = 'http://localhost:3030';
const userData = () => JSON.parse(sessionStorage.getItem('userData'));
const mainSection = document.getElementById('main-content');

function updateNavigation() {

    const login = document.getElementById('login');
    const register = document.getElementById('register');

    const create = document.getElementById('create');
    const logout = document.getElementById('logout');

    if (userData()) {
        login.style.display = 'none';
        register.style.display = 'none';

        create.style.display = 'inline-block';
        logout.style.display = 'inline-block';

    } else {
        login.style.display = 'inline-block';
        register.style.display = 'inline-block';

        create.style.display = 'none';
        logout.style.display = 'none';
    }
}

export {
    serverHost,
    userData,
    updateNavigation,
    mainSection,
}