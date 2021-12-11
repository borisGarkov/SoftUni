// import { html, render } from './node_modules/lit-html/lit-html.js';
// const { html, render } = require('./node_modules/lit-html/lit-html.js');

import { html, render } from './node_modules/lit-html/lit-html.js';

const button = document.getElementById('btnLoadTowns');
const tows = document.getElementById('towns');
const root = document.getElementById('root');

button.addEventListener('click', onClick);
  
function onClick(event) {
    event.preventDefault();

    if (tows.value.trim() == '') {
        return;
    }

    const myTemplate = (data) => html`
    <ul>
    ${data.map((item) => html`<li>${item}</li>`)}
    </ul>
    `

    render(myTemplate(tows.value.split(', ')), root);
}