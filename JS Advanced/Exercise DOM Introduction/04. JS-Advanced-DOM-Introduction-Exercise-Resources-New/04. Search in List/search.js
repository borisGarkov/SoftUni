function search() {
   let towns = document.getElementsByTagName('li');
   let searchedString = document.getElementById('searchText').value;

   towns = Array.from(towns);

   count = 0;

   for (let index = 0; index < towns.length; index++) {
      currentTown = towns[index].innerText;

      if (currentTown.includes(searchedString) && searchedString != '') {
         count += 1;
         document.getElementsByTagName('li')[index].style.fontWeight = 'bold';
         document.getElementsByTagName('li')[index].style.textDecoration = 'underline';
      } else {
         document.getElementsByTagName('li')[index].style.fontWeight = 'normal';
         document.getElementsByTagName('li')[index].style.textDecoration = 'none';
      }

   }

   document.getElementById('result').innerHTML = `${count} matches found`;
   console.log(count);
}
