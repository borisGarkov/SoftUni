import { page, html, render } from './lib.js';
import { updateNavigation, mainSection } from './utils.js';
import { catalogPage } from './views/catalog.js';
import { createAlbumPage } from './views/create.js';
import { onDelete } from './views/delete.js';
import { detailsPage } from './views/details.js';
import { editPage } from './views/edit.js';
import { homePage } from './views/home.js';
import { loginPage } from './views/login.js';
import { logoutPage } from './views/logout.js';
import { registerPage } from './views/register.js';
import { searchPage } from './views/search.js';


page(decorateContext);
page('/', homePage);
page('/login', loginPage);
page('/register', registerPage);
page('/logout', logoutPage);
page('/catalog', catalogPage);
page('/create', createAlbumPage);
page('/details/:id', detailsPage);
page('/delete/:id', onDelete);
page('/edit/:id', editPage);
page('/search', searchPage);


page.start();

function decorateContext(ctx, next) {
    ctx.render = (template) => render(template, mainSection);
    updateNavigation();
    next();
}