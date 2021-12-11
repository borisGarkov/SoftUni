import { towns } from './towns.js';
import { html, render } from 'https://unpkg.com/lit-html?module';


const button = document.getElementsByTagName('button')[0];
const result = document.getElementById('result');
const townsSection = document.getElementById('towns');

button.addEventListener('click', search)

function search() {
   const searchText = document.getElementById('searchText').value.trim();

   if (searchText == '') {
      return;
   }

   let tempSearch = [];

   for (const town of towns) {
      if (town.toLowerCase().includes(searchText)) {
         tempSearch.push(html`<li class='active'>${town}</li>`);
      } else {
         tempSearch.push(html`<li>${town}</li>`);
      }
   }

   let template = html`<ul>${tempSearch}</ul>`;

   render(template, townsSection);
}