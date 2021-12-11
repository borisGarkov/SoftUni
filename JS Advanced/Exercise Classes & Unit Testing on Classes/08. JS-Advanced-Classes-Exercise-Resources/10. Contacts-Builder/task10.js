class Contact {
    constructor(firstName, lastName, phone, email) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.phone = phone;
        this.email = email;
        this._online = false;
        this.info;
        this.title;
        this.btn;
    }

    get online() {
        return this._online;
    }

    set online(value) {
        if (this.title) {
            if (value == true) {
                this.info.style.display = 'block';
                this.title.classList.add('online');
            } else {
                this.info.style.display = 'none';
                this.title.classList.remove('online');
            }
        }
        this._online = value
    }

    render(id) {
        let article = document.createElement('article');
        article.innerHTML = `
            <div class="title">${this.firstName} ${this.lastName}<button>&#8505;</button></div>
            <div class="info">
                <span>&phone; ${this.phone}</span>
                <span>&#9993; ${this.email}</span>
            </div>
        `
        document.getElementById(id).appendChild(article)

        this.info = Array.from(document.getElementsByClassName('info')).pop();
        this.info.style.display = 'none';

        this.title = Array.from(document.getElementsByClassName('title')).pop();

        this.btn = Array.from(document.getElementsByTagName('button')).pop();

        this.btn.addEventListener('click', () => {
            this.online = this.online == true ? false : true
        })
    }
}

let contacts = [
    new Contact("Ivan", "Ivanov", "0888 123 456", "i.ivanov@gmail.com"),
    new Contact("Maria", "Petrova", "0899 987 654", "mar4eto@abv.bg"),
    new Contact("Jordan", "Kirov", "0988 456 789", "jordk@gmail.com")
];

contacts.forEach(c => {
    c.render('main');
    c.online = true;
});


