#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If not a valid subreddit, prints None.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    
    # Disable redirects to avoid fake subreddit redirects
    response = requests.get(subreddit_url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])
        if not posts:
            print(None)
            return

        for post in posts[:10]:
            print(post.get('data', {}).get('title'))
    except Exception:
        print(None)
