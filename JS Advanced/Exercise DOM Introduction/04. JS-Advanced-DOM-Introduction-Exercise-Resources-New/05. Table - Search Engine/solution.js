function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      let tableRows = document.getElementsByTagName('td');
      tableRows = Array.from(tableRows);

      const searchedText = document.getElementById('searchField').value;

      for (let index = 1; index < tableRows.length; index++) {
         if (document.getElementsByTagName('td')[index].parentElement.classList.contains('select')) {
            document.getElementsByTagName('td')[index].parentElement.classList.remove('select');
         }
      }

      for (let index = 1; index < tableRows.length; index++) {
         const element = tableRows[index].innerHTML;

         if (element.includes(searchedText) && searchedText != '') {
            document.getElementsByTagName('td')[index].parentElement.classList.add('select');
         }
      }
   }
}