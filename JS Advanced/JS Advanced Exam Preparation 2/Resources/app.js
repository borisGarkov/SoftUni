window.addEventListener('load', solve);


function solve() {
    let inputFields = document.querySelectorAll('form input');
    let addBtn = document.querySelector('form button');

    let allHitsContainer = document.getElementsByClassName('all-hits-container')[0];

    let genre = inputFields[0];
    let songName = inputFields[1];
    let songAuthor = inputFields[2];
    let dateCreattion = inputFields[3];

    addBtn.addEventListener('click', onAddBtnClick);

    function onAddBtnClick(event) {
        event.preventDefault()

        if (genre.value == '' || songName.value == '' || songAuthor.value == '' || dateCreattion.value == '' ||
            typeof genre.value !== 'string' || typeof songName.value !== 'string' || typeof songAuthor.value !== 'string' ||
            typeof dateCreattion.value !== 'string') {
            return
        }

        let genreValue = genre.value;
        let songNameValue = songName.value;
        let songAuthorValue = songAuthor.value;
        let dateCreattionValue = dateCreattion.value;

        let saveSongBtn = e('button', { 'className': 'save-btn', 'textContent': 'Save song' });
        let likeSongBtn = e('button', { 'className': 'like-btn', 'textContent': 'Like song' });
        let deleteSongBtn = e('button', { 'className': 'delete-btn', 'textContent': 'Delete' });

        let divContent = e('div', { 'className': 'hits-info' },
            e('img', { 'src': './static/img/img.png' }),
            e('h2', { 'textContent': `Genre: ${genre.value}` }),
            e('h2', { 'textContent': `Name: ${songName.value}` }),
            e('h2', { 'textContent': `Author: ${songAuthor.value}` }),
            e('h3', { 'textContent': `Date: ${dateCreattion.value}` }),
            saveSongBtn,
            likeSongBtn,
            deleteSongBtn,
        )

        document.getElementsByTagName('form')[0].reset()

        likeSongBtn.addEventListener('click', onLikeBtnClick);
        deleteSongBtn.addEventListener('click', onDeleteBtnClick.bind(null, divContent));
        saveSongBtn.addEventListener('click', onSaveBtnClick.bind(
            null, divContent, deleteSongBtn, genreValue, songNameValue, songAuthorValue, dateCreattionValue
        ));

        allHitsContainer.appendChild(divContent);

    }

    function onSaveBtnClick(divContent, deleteSongBtn, genreValue, songNameValue, songAuthorValue, dateCreattionValue, event) {

        divContent.remove();

        divContent = e('div', { 'className': 'hits-info' },
            e('img', { 'src': './static/img/img.png' }),
            e('h2', { 'textContent': `Genre: ${genreValue}` }),
            e('h2', { 'textContent': `Name: ${songNameValue}` }),
            e('h2', { 'textContent': `Author: ${songAuthorValue}` }),
            e('h3', { 'textContent': `Date: ${dateCreattionValue}` }),
            deleteSongBtn,
        )

        deleteSongBtn.addEventListener('click', onDeleteBtnClick.bind(null, divContent));

        document.getElementsByClassName('saved-container')[0].appendChild(divContent);
    }

    function onLikeBtnClick(event) {
        event.target.disabled = true;
        let likesPara = document.querySelector('#total-likes p').textContent;
        let currentLikes = Number(likesPara.split(': ')[1]);
        currentLikes += 1;

        document.querySelector('#total-likes p').textContent = `Total Likes: ${currentLikes}`;
    }

    function onDeleteBtnClick(divContent, event) {
        divContent.remove();
    }

    function e(type, attr, ...content) {
        const element = document.createElement(type);

        for (const prop in attr) {
            element[prop] = attr[prop];
        }

        for (const item of content) {
            if (typeof item == 'string' || typeof item == 'number') {
                item = document.createTextNode(item);
            }
            element.appendChild(item);
        }

        return element;
    }
}