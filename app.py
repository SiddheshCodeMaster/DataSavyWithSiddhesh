from flask import Flask, jsonify, render_template
import feedparser
from bs4 import BeautifulSoup

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

MEDIUM_FEED_URL = "https://medium.com/feed/@siddhesh.codemaster.github"

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/api/medium/blogs")
def api_medium_blogs():
    feed = feedparser.parse(MEDIUM_FEED_URL)
    blogs = []

    for entry in feed.entries:
        # STEP 1: Try media_thumbnail
        thumbnail = None
        if "media_thumbnail" in entry:
            thumbnail = entry.media_thumbnail[0]["url"]

        # STEP 2: Try enclosure images
        if not thumbnail and "links" in entry:
            for link in entry.links:
                if link.get("rel") == "enclosure":
                    thumbnail = link.get("href")

        # STEP 3: Extract <img> from HTML content (MOST ACCURATE)
        if not thumbnail and "content" in entry:
            soup = BeautifulSoup(entry.content[0].value, "html.parser")
            img = soup.find("img")
            if img:
                thumbnail = img.get("src")

        blogs.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published if hasattr(entry, "published") else "",
            "summary": entry.summary if hasattr(entry, "summary") else "",
            "thumbnail": thumbnail
        })

    return jsonify({"blogs": blogs})

if __name__ == '__main__':
    app.run(debug=True)
