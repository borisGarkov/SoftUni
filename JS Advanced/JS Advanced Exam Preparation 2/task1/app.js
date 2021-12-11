window.addEventListener('load', solve);

function solve() {
    let model = document.getElementById('model');
    let year = document.getElementById('year');
    let description = document.getElementById('description');
    let price = document.getElementById('price');
    let addBtn = document.getElementById('add');
    let form = document.getElementsByTagName('form')[0];
    let furnitureList = document.getElementById('furniture-list');
    let totalPrice = document.getElementsByClassName('total-price')[0];

    addBtn.addEventListener('click', onClickAddBtn);


    function onClickAddBtn(event) {
        event.preventDefault();
        if (model.value == '' || description.value == '' || year.value < 0 || 
            price.value < 0 || typeof model.value != 'string' || typeof description.value != 'string') {
            return
        }

        let moreInfoBtn = e('button', { 'className': 'moreBtn', 'innerText': 'More Info' },);
        let buyBtn = e('button', { 'className': 'buyBtn', 'innerText': 'Buy it' },)

        let tr = e('tr', { 'className': 'info' },
            e('td', { 'innerText': `${model.value}` }),
            e('td', { 'innerText': `${Number(price.value).toFixed(2)}` }),
            e('td', {}, moreInfoBtn, buyBtn),
        )

        let trElementClassHide = e('tr', {'className': 'hide'},
            e('td', {'innerText': `Year: ${year.value}`}),
            e('td', {'innerText': `Description: ${description.value}`, 'colSpan': 3})
        )

        moreInfoBtn.addEventListener('click', onClickMoreInfo.bind(null, trElementClassHide))
        buyBtn.addEventListener('click', onClickBuyBtn.bind(null, tr, trElementClassHide))

        furnitureList.appendChild(tr);
        furnitureList.appendChild(trElementClassHide);

        form.reset();
    }

    function onClickBuyBtn(tr, trElementClassHide) {
        tr.remove();
        trElementClassHide.remove();

        totalPrice.innerText = (Number(totalPrice.innerText) + Number(tr.querySelectorAll('td')[1].innerText)).toFixed(2);
    }

    function onClickMoreInfo(trElementClassHide, ev) {
        if (ev.target.innerText == 'More Info') {
            ev.target.innerText = 'Less Info';
            trElementClassHide.style.display = 'contents';
        } else {
            ev.target.innerText = 'More Info';
            trElementClassHide.style.display = 'none';
        }
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
