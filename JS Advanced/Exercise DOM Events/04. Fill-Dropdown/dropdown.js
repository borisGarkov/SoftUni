function addItem() {

    text = document.getElementById('newItemText').value;
    value = document.getElementById('newItemValue').value;

    if (text != '' && value != '') {
        let option = document.createElement('option');
        option.textContent = text;
        option.value = value;
        document.getElementById('menu').appendChild(option);

        document.getElementById('newItemText').value = '';
        document.getElementById('newItemValue').value = '';
    }
}