function encodeAndDecodeMessages() {
    let content = document.getElementById('main');
    content.addEventListener('click', onClick);

    function onClick(e) {
        if (e.target.tagName == 'BUTTON') {
            if (e.target.textContent == 'Encode and send it') {
                textInput = document.getElementsByTagName('textarea')[0].value;
                if (textInput != '') {
                    let result = '';

                    for (let index = 0; index < textInput.length; index++) {
                        asciiCode = textInput.charCodeAt(index);

                        result += String.fromCharCode(asciiCode + 1);
                    }

                    document.getElementsByTagName('textarea')[0].value = '';
                    document.getElementsByTagName('textarea')[1].value = result;
                }
            } else {
                textInput = document.getElementsByTagName('textarea')[1].value;
                if (textInput != '') {
                    let result = '';

                    for (let index = 0; index < textInput.length; index++) {
                        asciiCode = textInput.charCodeAt(index);

                        result += String.fromCharCode(asciiCode - 1);
                    }

                    document.getElementsByTagName('textarea')[1].value = result;

                }
            }
        }
    }
}