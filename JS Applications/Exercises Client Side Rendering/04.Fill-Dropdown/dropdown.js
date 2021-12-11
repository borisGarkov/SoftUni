import { html, render } from 'https://unpkg.com/lit-html?module';

const menu = document.getElementById('menu');
const button = document.querySelector('input[type=submit]');
const inputText = document.querySelector('input[type=text]');

button.addEventListener('click', addItem);


async function retrieveData() {
    const response = await fetch('http://localhost:3030/jsonstore/advanced/dropdown');
    const jsonData = await response.json();

    let optionsData = [];

    for (const [key, value] of Object.entries(jsonData)) {
        let town = value.text;
        let id = value._id;
        optionsData.push(html`<option value="${id}">${town}</option>`);
    }

    const template = html`${optionsData}`;

    render(template, menu);
}

retrieveData()

async function addItem(event) {
    event.preventDefault();
    const input = inputText.value.trim()

    if (input == '') {
        return;
    }

    const response = await fetch('http://localhost:3030/jsonstore/advanced/dropdown', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: input,
        })
    })

    retrieveData();
    inputText.value = '';
}