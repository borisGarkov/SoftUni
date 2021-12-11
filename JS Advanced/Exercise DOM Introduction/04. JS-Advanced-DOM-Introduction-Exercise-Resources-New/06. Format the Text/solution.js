function solve() {
  let text = document.getElementById('input').value;

  textArr = text.split('.').filter(el => el.length >= 1);
  let result = '';
  let count = 0;

  for (let index = 0; index < textArr.length; index++) {
    const element = textArr[index];

    element.trim();
    result += element + '. ';
    count += 1;

    if (count % 3 == 0) {
      count = 0;
      document.getElementById('output').innerHTML += `<p>${result.trim()}</p>`;
      result = '';
    }

    if (result != '' && index == textArr.length - 1) {
      document.getElementById('output').innerHTML += `<p>${result.trim()}</p>`;
    }
  }
}