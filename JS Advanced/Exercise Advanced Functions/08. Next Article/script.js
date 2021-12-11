function getArticleGenerator(articles) {

    let div = document.getElementById('content')

    function generate() {
        if (articles.length > 0) {
            let article = document.createElement('article');
            let text = articles.shift();
            article.textContent = text;

            div.appendChild(article)
        }
    }

    return generate
}
