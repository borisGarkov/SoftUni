import { page, html, render } from './lib.js';
import { updateNavigation, mainSection } from './utils.js'

import { dashboardPage } from './views/dashboard.js';
import { loginPage } from './views/login.js';
import { registerPage } from './views/register.js';
import { logoutPage } from './views/logout.js';
import { createBookPage } from './views/create.js';
import { detailsPage } from './views/details.js';
import { onDelete } from './views/delete.js';


page(decorateContext);
page('/', dashboardPage);
page('/login', loginPage);
page('/register', registerPage);
page('/logout', logoutPage);
page('/create', createBookPage);
page('/details/:id', detailsPage);
page('/delete/:id', onDelete);

page.start();

function decorateContext(ctx, next) {
    ctx.render = (template) => render(template, mainSection);
    updateNavigation();
    next();
}