function solve() {

    let btnDepart = document.getElementById('depart');
    let btnArrive = document.getElementById('arrive');
    let infoBox = document.getElementsByClassName('info')[0];
    let nextStop = 'depot';
    let stopName = '';

    async function depart() {
        btnDepart.disabled = true;
        
        let url = `http://localhost:3030/jsonstore/bus/schedule/${nextStop}`;
        let response = await fetch(url);
        let textJSON = await response.json();

        stopName = textJSON.name;

        infoBox.textContent = `Next stop ${stopName}`;

        btnArrive.disabled = false;
        nextStop = textJSON.next;
    }

    function arrive() {

        infoBox.textContent = `Arriving at ${stopName}`;

        btnDepart.disabled = false;
        btnArrive.disabled = true;
    }

    return {
        depart,
        arrive
    };
}

let result = solve();