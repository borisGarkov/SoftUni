class Textbox {
    constructor(selector, regex) {
        this.selector = selector;
        this.regex = regex;
        this._elements; 
    }

    get elements() {
        return this._elements;
    }

    set elements(selector) {
        this._elements = document.querySelectorAll(this.selector);
    }


}

let textbox = new Textbox(".textbox",/[^a-zA-Z0-9]/);

let inputs = document.getElementsByClassName('.textbox');

inputs.addEventListener('click',function(){console.log(textbox.value);});
