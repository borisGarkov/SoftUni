function solve() {
    let container = Array.from(document.getElementById('container').children);
    let addBtn = container.pop();
    let adoptionSection = document.getElementById('adoption').children[1];
    let adoptedSection = document.getElementById('adopted').children[1];

    addBtn.addEventListener('click', (e) => {
        e.preventDefault();
        let name = container[0].value;
        let age = container[1].value;
        let kind = container[2].value;
        let currentOwner = container[3].value;

        if (name && age && !isNaN(age) && kind && currentOwner) {

            let liElement = document.createElement('li');
            let paraElement = document.createElement('p');
            
            paraElement.innerHTML = `<strong>${name}</strong> is a <strong>${age}</strong> year old <strong>${kind}</strong>`

            let spanElement = document.createElement('span');
            let contactBtn = document.createElement('button');

            spanElement.innerText = `Owner: ${currentOwner}`;
            contactBtn.innerText = 'Contact with owner';

            liElement.appendChild(paraElement);
            liElement.appendChild(spanElement);
            liElement.appendChild(contactBtn);

            adoptionSection.appendChild(liElement);

            contactBtn.addEventListener('click', (ev) => {
                
                let subDivElement = document.createElement('div');
                let inputField = document.createElement('input');

                if (contactBtn.innerText == 'Contact with owner') {
                    
                    liElement.getElementsByTagName('button')[0].remove()

                    inputField.setAttribute('placeholder', 'Enter your names');
                    contactBtn.innerText = 'Yes! I take it!';
                    subDivElement.appendChild(inputField);
                    subDivElement.appendChild(contactBtn);

                    liElement.appendChild(subDivElement);

                } else if (contactBtn.innerText == 'Yes! I take it!') {
                    let newName = ev.target.parentElement.getElementsByTagName('input')[0].value;

                    if (newName) {

                        adoptionSection.remove(liElement);
                        adoptedSection.appendChild(liElement);
                      
                        spanElement.innerText = `New Owner: ${newName}`;
                        contactBtn.innerText = 'Checked';
                      
                        liElement.getElementsByTagName('div')[0].remove();

                        liElement.appendChild(spanElement);
                        liElement.appendChild(contactBtn);
                    }

                } else if (contactBtn.innerText == 'Checked') {
                    adoptedSection.remove(liElement);
                }
            })

            for (const element of container) {
                element.value = '';
            }
        }
    })
}

