function validate() {
    let isCompanyField = document.getElementById('company');
    let companyNumber = document.getElementById('companyNumber');
    let companyInfo = document.getElementById('companyInfo');

    let counterIsValid = 0;

    let submitBtn = document.getElementById('submit');
    submitBtn.addEventListener('click', onSubmitClick);

    let validSection = document.getElementById('valid');

    let username = document.getElementById('username');
    let password = document.getElementById('password');
    let confirmPassword = document.getElementById('confirm-password');
    let email = document.getElementById('email');


    isCompanyField.addEventListener('change', (e) => {
        isCompanyField.checked ? companyInfo.style.display = 'block' : companyInfo.style.display = 'none';
    });

    function onSubmitClick(e) {
        e.preventDefault();

        if (username.value.match('^[A-Za-z0-9]+$') && 3 <= username.value.length && username.value.length <= 20) {
            username.style.border = 'none';
            counterIsValid += 1;
        } else {
            username.style.borderColor = 'red';
        }

        if (password.value.match('^[A-Za-z0-9_]+$') && 5 <= password.value.length && password.value.length <= 15) {
            password.style.border = 'none';
            counterIsValid += 1;

            if (password.value == confirmPassword.value) {
                counterIsValid += 1;
            }

        } else {
            password.style.borderColor = 'red';
        }

        if (confirmPassword.value.match('^[A-Za-z0-9_]+$') &&
            5 <= confirmPassword.value.length && confirmPassword.value.length <= 15) {
            confirmPassword.style.border = 'none';
            counterIsValid += 1;
        } else {
            confirmPassword.style.borderColor = 'red';
        }

        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email.value)) {
            email.style.border = 'none';
            counterIsValid += 1;
        } else {
            email.style.borderColor = 'red';
        }

        if (isCompanyField.checked && !isNaN(companyNumber.value) && companyNumber.value >= 1000 && companyNumber.value <= 9999) {
            companyNumber.style.border = 'none';
            counterIsValid += 1;
        } else if (isCompanyField.checked) {
            companyNumber.style.borderColor = 'red';
        }

        if (counterIsValid == 6 && isCompanyField.checked) {
            validSection.style.display = 'block';
        } else if (counterIsValid == 5 && !isCompanyField.checked) {
            validSection.style.display = 'block';
        } else {
            validSection.style.display = 'none';
        }

    }

}
