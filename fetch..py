import requests

API_KEY = "e1a2966772e047a886c65bcc645ab4ca"  
URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(URL)
data = response.json()

for article in data['articles']:
    print(article['title'], "-", article['url'])
