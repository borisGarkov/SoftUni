function validate() {
    let input = document.getElementById('email');
    input.addEventListener('change', (e) => {

        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(input.value)) {
            input.classList.remove('error');
        } else {
            input.classList.add('error');
        }
    });
}