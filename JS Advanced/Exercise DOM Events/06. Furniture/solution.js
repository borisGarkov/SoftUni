function solve() {
  let buttons = Array.from(document.getElementsByTagName('button'))
  for (const b of buttons) {
    b.addEventListener('click', onClick);
  }

  function onClick(e) {
    if (e.target.textContent == 'Generate') {
      let textInput = document.getElementsByTagName('textarea')[0].value;
      let objects = JSON.parse(textInput);

      for (const obj of objects) {

        let row = document.createElement('tr');

        let image = document.createElement('img');
        image.src = obj['img'];
        let colImage = document.createElement('td');
        colImage.appendChild(image);

        let name = document.createElement('p');
        name.textContent = obj['name'];
        let colName = document.createElement('td');
        colName.appendChild(name);

        let price = document.createElement('p');
        price.textContent = obj['price'];
        let colPrice = document.createElement('td');
        colPrice.appendChild(price);

        let decFactor = document.createElement('p');
        decFactor.textContent = obj['decFactor'];
        let colFactor = document.createElement('td');
        colFactor.appendChild(decFactor);

        let checkbox = document.createElement('input');
        checkbox.setAttribute('type', 'checkbox');
        let colCheck = document.createElement('td');
        colCheck.appendChild(checkbox);


        for (const iterator of [colImage, colName, colPrice, colFactor, colCheck]) {
          row.appendChild(iterator);
        }

        document.getElementsByTagName('tbody')[0].appendChild(row);
      }
    } else {
      let checkboxes = Array.from(document.querySelectorAll('input[type=checkbox]:checked'));
      let items = [];
      let totalPrice = 0;
      let avgFactor = [];

      if (checkboxes.length > 0) {
        for (const checkbox of checkboxes) {
          let name = checkbox.parentElement.parentElement.getElementsByTagName('td')[1].textContent;
          let price = Number(checkbox.parentElement.parentElement.getElementsByTagName('td')[2].textContent);
          let decFactor = Number(checkbox.parentElement.parentElement.getElementsByTagName('td')[3].textContent);

          items.push(name);
          totalPrice += price;
          avgFactor.push(decFactor);
        }

        average = avgFactor.reduce((a, b) => a + b, 0) / avgFactor.length;

        document.getElementsByTagName('textarea')[1].value = 
        `Bought furniture: ${items.join(', ')}\nTotal price: ${totalPrice.toFixed(2)}\nAverage decoration factor: ${average}`;

      }
    }
  }
}