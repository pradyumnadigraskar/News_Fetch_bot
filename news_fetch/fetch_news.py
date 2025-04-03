
import requests
from config import API_KEY, NEWS_API_URL

CATEGORIES = {
    "pilgrimage": ["pilgrimage", "temple visit", "holy site", "religious journey", "spiritual travel"],
    "devotional": ["prayer", "chanting", "worship", "hymns", "spiritual", "devotion"]
}

def fetch_news(category):
    """Fetches news filtered by category."""
    keywords = CATEGORIES.get(category.lower())

    if not keywords:
        return {"error": f"Invalid category: {category}. Choose from {list(CATEGORIES.keys())}"}

    query = " OR ".join(keywords)

    params = {
        "apiKey": API_KEY,
        "q": query,
        "language": "en",
        "pageSize": 10
    }

    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()

    if data.get("status") == "ok" and data.get("totalResults", 0) > 0:
        for article in data["articles"]:
            if not article.get("urlToImage"):
                article["urlToImage"] = "/static/default-image.jpg"
        return {"status": "ok", "articles": data["articles"]}
    else:
        return {"message": f"No {category} news found."}
