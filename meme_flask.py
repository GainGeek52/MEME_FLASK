#!/usr/bin/python
from flask import Flask, render_template
import praw
import logging

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

# Configure the Reddit API client
reddit = praw.Reddit(
    client_id="LZGteG0BpZq6wzjPdegNCQ",  # Replace with your actual client_id
    client_secret="tP6_TrjVJW_tlyvNPkChbeSUFhSZ2w",  # Replace with your actual client_secret
    user_agent="MemeSite/1.0",
)

DEFAULT_IMAGE = "https://i.imgur.com/XJuq3GN.png"

# Get memes from a specific subreddit
def get_meme(subreddit="dankmemes", count=5):
    try:
        memes = []
        # Fetch memes from subreddit
        for submission in reddit.subreddit(subreddit).hot(limit=count):
            if not submission.over_18:  # Skip NSFW content
                memes.append({
                    'image': submission.url,
                    'subreddit': submission.subreddit.display_name,
                    'title': submission.title,
                    'author': submission.author.name if submission.author else 'Unknown',
                    'ups': submission.ups,
                    'postLink': f"https://reddit.com{submission.permalink}"
                })
        
        return memes

    except Exception as e:
        app.logger.error(f"Error fetching memes: {str(e)}")
        return [{
            'image': DEFAULT_IMAGE,
            'subreddit': 'memes',
            'title': 'Failed to load meme :(',
            'author': 'System',
            'ups': 0,
            'postLink': '#'
        }]

@app.route("/")
@app.route("/<subreddit>")
@app.route("/<subreddit>/<int:count>")
def index(subreddit="dankmemes", count=6):  # Default to "dankmemes"
    count = min(max(count, 1), 50)  # Ensure count is between 1 and 50
    memes = get_meme(subreddit, count)
    return render_template("meme_index.html", memes=memes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
