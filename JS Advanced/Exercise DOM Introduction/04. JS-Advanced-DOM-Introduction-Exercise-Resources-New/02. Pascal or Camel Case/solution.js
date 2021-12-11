function solve() {
  namingConventions = {
    'Camel Case': function (text) {
      text = text.split(' ');
      result = '';

      for (let index = 0; index < text.length; index++) {
        word = text[index].toLowerCase();

        if (index != 0) {
          word = word[0].toUpperCase() + word.slice(1);
        }

        result += word;
      }

      return result;
    },
    'Pascal Case': function (text) {
      text = text.split(' ');
      result = '';

      for (let index = 0; index < text.length; index++) {

        word = text[index].toLowerCase();
        word = word[0].toUpperCase() + word.slice(1);
        result += word;

      }

      return result;
    },
  }

  text = document.getElementById('text').value
  convention = document.getElementById('naming-convention').value

  if (namingConventions[convention] == undefined) {
    document.getElementById('result').innerHTML = 'Error!'; 
  } else {
    document.getElementById('result').innerHTML = namingConventions[convention](text);
  }
}