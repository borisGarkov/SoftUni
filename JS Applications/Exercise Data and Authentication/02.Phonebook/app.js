function attachEvents() {

    const btnLoad = document.getElementById('btnLoad');
    const phonebook = document.getElementById('phonebook');

    btnLoad.addEventListener('click', onLoad);
    phonebook.addEventListener('click', onClickDeletePhonebookButton)

    async function onLoad(event) {
        const url = 'http://localhost:3030/jsonstore/phonebook';

        const response = await fetch(url);
        const result = await response.json();
        let liArray = [];

        for (const [key, value] of Object.entries(result)) {
            let liElement = document.createElement('li');
            let button = document.createElement('button');
            liElement.textContent = `${value.person}: ${value.phone}`;

            button.textContent = 'Delete';
            button.setAttribute('data-id', key);

            liElement.appendChild(button);
            liArray.push(liElement);
        }
        phonebook.replaceChildren(...liArray);
    }

    async function onClickDeletePhonebookButton(event) {

        if (event.target.tagName != 'BUTTON' || event.target.textContent != 'Delete') {
            return
        }

        let id = event.target.dataset.id;

        let url = `http://localhost:3030/jsonstore/phonebook/${id}`

        await fetch(url, {
            method: 'delete',
        })

        event.target.parentElement.remove()
    }
}

attachEvents();