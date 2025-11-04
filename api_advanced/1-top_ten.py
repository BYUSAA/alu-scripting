#!/usr/bin/python3
"""
Query the Reddit API and print the titles of the first 10 hot posts
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditBot/1.0"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data")
        if not data or "children" not in data:
            print(None)
            return

        posts = data.get("children")
        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get("data").get("title"))
    except Exception:
        print(None)
