function attachEvents() {

    let submitBtn = document.getElementById('submit');
    let location = document.getElementById('location');
    let cityCode = '';

    submitBtn.addEventListener('click', onClick);

    async function onClick(event) {

        let url = 'http://localhost:3030/jsonstore/forecaster/locations';
        let response = await fetch(url);
        let locationTextJSON = await response.json();

        for (el of locationTextJSON) {
            if (el.name.toLowerCase() == location.value.toLowerCase()) {
                cityCode = el.code;
                break;
            }
        }

        url = `http://localhost:3030/jsonstore/forecaster/today/${cityCode}`;
        response = await fetch(url);
        let todayForecastJSON = await response.json();

        url = `http://localhost:3030/jsonstore/forecaster/upcoming/${cityCode}`;
        response = await fetch(url);
        let threeDaysForecastJSON = await response.json();

        console.log(threeDaysForecastJSON);
    }
}

attachEvents();