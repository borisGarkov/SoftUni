function solve() {

    let onScreenBtn = document.querySelector('#container button');
    onScreenBtn.addEventListener('click', onClick);
    let [nameBtn, hall, ticketPrice] = document.querySelectorAll('#container input');
    let movies = document.querySelector('#movies ul');
    let archive = document.querySelector('#archive ul');
    let archiveClearBtn = document.querySelector('#archive button');
    archiveClearBtn.addEventListener('click', onClear);

    function onClick(e) {
        e.preventDefault();

        if (nameBtn.value != '' && hall.value != '' && ticketPrice.value != '' && !isNaN(ticketPrice.value)) {
            let liElement = document.createElement('li');

            liElement.innerHTML =
                `<span>${nameBtn.value}</span>
                <strong>Hall: ${hall.value}</strong>
                <div>
                    <strong>${Number(ticketPrice.value).toFixed(2)}</strong>
                    <input placeholder="Tickets Sold">
                    <button>Archive</button>
                </div>`;

            movies.appendChild(liElement);
            archiveBtns = document.querySelectorAll('#movies ul li button');
            currentBtn = archiveBtns[archiveBtns.length - 1];

            currentBtn.addEventListener('click', onArchive);
            
            nameBtn.value = '';
            hall.value = '';
            ticketPrice.value = '';
        }

    }

    function onArchive(e) {
        let quantity = e.target.parentElement.querySelector('input').value;
        let name = e.target.parentElement.parentElement.querySelector('span').textContent;
        let price = Number(e.target.parentElement.querySelector('strong').textContent);

        let row = e.target.parentElement.parentElement;

        if (quantity != '' && !isNaN(quantity)) {
            row.remove();

            let liElement = document.createElement('li');

            liElement.innerHTML =
                `<span>${name}</span>
                <strong>Total amount: ${(Number(quantity) * price).toFixed(2)}</strong>
                <button>Delete</button>`;

            archive.appendChild(liElement);

            archiveBtns = document.querySelectorAll('#archive ul li button');
            currentBtn = archiveBtns[archiveBtns.length - 1];

            currentBtn.addEventListener('click', onDelete);
        }
    }

    function onDelete(e) {
        e.target.parentElement.remove();
    }

    function onClear(e) {
        let liElements = document.querySelector('#archive ul li')
        liElements.remove();
    }
}