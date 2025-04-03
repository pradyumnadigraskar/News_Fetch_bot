
from flask import Flask, request, jsonify, render_template, send_from_directory
from news_fetch.fetch_news import fetch_news
import os
app = Flask(__name__, static_folder="static", static_url_path="/static")


@app.route("/")
def index():
    return render_template("index.html") 


@app.route("/get_news", methods=["POST"])
def get_news():
    
    category = request.form.get("category") 

    if not category:
        return jsonify({"error": "Please select a category."}), 400

    news_data = fetch_news(category)
    return jsonify(news_data)

if __name__ == "__main__":
    app.run(debug=True)
