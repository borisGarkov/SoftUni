function toggle() {
    action = document.querySelector('.button').innerHTML;

    if (action == 'More'){
        document.querySelector('.button').innerHTML = 'Less';
        document.getElementById('extra').style.display = 'block';
    } else {
        document.querySelector('.button').innerHTML = 'More';
        document.getElementById('extra').style.display = 'none';
    }

}