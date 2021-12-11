async function getInfo() {

    let stopID = document.getElementById('stopId');
    let busesList = document.getElementById('buses');
    let stopName = document.getElementById('stopName');
    let btnSubmit = document.getElementById('submit');

    busesList.innerHTML = '';
    stopName.textContent = '';

    try {
        stopName.textContent = 'Loading...';
        btnSubmit.disabled = true;

        let response = await fetch(`http://localhost:3030/jsonstore/bus/businfo/${stopID.value}`);

        if (response.status != 200 || stopID.value == '') {
            throw new Error('invalid stop');
        }

        let textJSON = await response.json();

        for (const [busID, timeToArrive] of Object.entries(textJSON.buses)) {
            let liElement = document.createElement('li');
            liElement.textContent = `Bus ${busID} arrives in ${timeToArrive} minutes`
            busesList.appendChild(liElement);
        }
        stopName.textContent = `${textJSON.name}`;
    } catch (error) {
        stopName.textContent = 'Error';
    }

    stopID.value = '';
    btnSubmit.disabled = false;
}