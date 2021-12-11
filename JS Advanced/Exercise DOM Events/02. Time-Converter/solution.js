function attachEventsListeners() {

    let time = ['days', 'hours', 'minutes', 'seconds'];

    for (const t of time) {
        document.getElementById(t + 'Btn').addEventListener('click', onClick);
    }

    function onClick(e) {
        let inputId = e.currentTarget.id.split('Btn')[0];
        let inputField = document.getElementById(inputId).value;

        let map = {
            'days': 1,
            'hours': 24,
            'minutes': 1440,
            'seconds': 86400,
        }

        let convertValueToDays = map[inputId];
        inputField /= convertValueToDays;

        function checkElement(element) {
            return time.includes(element.id)
        }

        let arrInputElements = Array.from(document.getElementsByTagName('input')).filter(checkElement);

        for (const el of arrInputElements) {
            let multuplyByValue = map[el.id];
            document.getElementById(el.id).value = multuplyByValue * inputField;
        }

    }
}