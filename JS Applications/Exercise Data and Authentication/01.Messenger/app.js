function attachEvents() {
    const author = document.querySelector('input[name=author]');
    const content = document.querySelector('input[name=content]');

    const submitBtn = document.getElementById('submit');
    const refreshBtn = document.getElementById('refresh');
    const textarea = document.getElementById('messages');

    submitBtn.addEventListener('click', onSubmit);
    refreshBtn.addEventListener('click', onRefresh);


    async function onSubmit(event) {
        event.preventDefault();

        url = 'http://localhost:3030/jsonstore/messenger';

        data = {
            author: author.value.trim(),
            content: content.value.trim(),
        };

        body = {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        };

        await fetch(url, body);
    }

    async function onRefresh(event) {
        event.preventDefault();

        url = 'http://localhost:3030/jsonstore/messenger';

        const res = await fetch(url);
        const result = await res.json();

        let resultArray = [];

        for (const [key, value] of Object.entries(result)) {
            resultArray.push(`${value.author}: ${value.content}`)
        }

        textarea.textContent = resultArray.join('\n');
    }
}

attachEvents();