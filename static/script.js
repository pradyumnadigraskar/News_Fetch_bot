function fetchNews() {
    let category = document.getElementById("category").value;
    fetch("/get_news", {
        method: "POST",
        body: new URLSearchParams({ category }),
        headers: { "Content-Type": "application/x-www-form-urlencoded" }
    })
    .then(response => response.json())
    .then(data => {
        let newsContainer = document.getElementById("news-container");
        newsContainer.innerHTML = "";

        if (data.articles) {
            data.articles.forEach(article => {
                let newsItem = `<div class="news-item">
                                    <img src="${article.urlToImage}" alt="News Image">
                                    <div>
                                        <h2>${article.title}</h2>
                                        <p>${article.description || "No description available."}</p>
                                        <a href="${article.url}" target="_blank">Read more</a>
                                    </div>
                                </div>`;
                newsContainer.innerHTML += newsItem;
            });
        } else {
            newsContainer.innerHTML = `<p>No news found.</p>`;
        }
    })
    .catch(error => console.error("Error:", error));
}
