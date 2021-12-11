import { cats } from "./catSeeder.js";
import { html, render } from 'https://unpkg.com/lit-html?module';

const allCats = document.getElementById('allCats');

const itemTemplates = [];

for (const cat of cats) {
    itemTemplates.push(
        html`
        <li>
            <img src="./images/${cat.imageLocation}.jpg" width="250" height="250" alt="Card image cap">
            <div class="info">
                <button class="showBtn">Show status code</button>
                <div class="status" style="display: none" id="${cat.id}">
                    <h4>Status Code: ${cat.statusCode}</h4>
                    <p>${cat.statusMessage}</p>
                </div>
            </div>
        </li>
        `
    )
}

const template = html`<ul>${itemTemplates}</ul>`;

render(template, allCats);

allCats.addEventListener('click', onClick);

function onClick(event) {
    if (event.target.tagName != 'BUTTON') {
        return
    }

    const button = event.target;
    const statusSection = event.target.parentElement.getElementsByClassName('status')[0];

    if (button.textContent == 'Show status code') {
        statusSection.style.display = 'block';
        button.textContent = 'Hide status code';
    } else {
        statusSection.style.display = 'none';
        button.textContent = 'Show status code';
    }
}