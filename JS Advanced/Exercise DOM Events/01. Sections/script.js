function create(words) {

   for (const word of words) {
      let div = document.createElement('div');
      let text = document.createElement('p');
      text.textContent = word;
      text.style.display = 'none';
      document.getElementById('content').appendChild(div).appendChild(text);
   }

   let content = document.getElementById('content');
   content.addEventListener('click', displayParagraphText);

   function displayParagraphText(e) {
      console.log(e.currentTarget.children[0].tagName);
   }
}