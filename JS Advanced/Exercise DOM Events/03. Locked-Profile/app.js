function lockedProfile() {

    let buttons = Array.from(document.getElementsByTagName('button'));
    for (const b of buttons) {
        b.addEventListener('click', onClick)
    }

    function onClick(e) {
        let text = e.target.textContent;
        let checkId = e.target.parentNode.getElementsByTagName('div')[0].id;
        let radioButton = e.target.parentNode.querySelector('input[type="radio"]:checked').value;

        if (radioButton == 'unlock') {
            if (text == 'Hide') {
                e.target.textContent = 'Show more';
                document.getElementById(checkId).style.display = 'none';

            } else {
                e.target.textContent = 'Hide';
                document.getElementById(checkId).style.display = 'inline-block';
            }
        }
    }
}