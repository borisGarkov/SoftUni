import { page, render } from './lib.js';
import { mainSection, updateUserNav } from './utils.js';

import { homePage } from './views/home.js';
import { loginPage } from './views/login.js';
import { logoutPage } from './views/logout.js';
import { registerPage } from './views/register.js';
import { allMemesPage } from './views/allMemes.js';
import { profilePage } from './views/profile.js';
import { createMemePage } from './views/createMeme.js';
import { editMemePage } from './views/editMeme.js';
import { memeDetailsPage } from './views/memeDetails.js';
import { deleteMemePage } from './views/deleteMeme.js';

page(decorateContext);
page('/', homePage);
page('/login', loginPage);
page('/logout', logoutPage);
page('/register', registerPage);
page('/all-memes', allMemesPage);
page('/profile', profilePage);
page('/create-meme', createMemePage);
page('/edit-meme/:id', editMemePage);
page('/meme-details/:id', memeDetailsPage);
page.start();

function decorateContext(ctx, next) {
    ctx.render = (template) => render(template, mainSection);
    updateUserNav();
    console.log(ctx);
    next();
}