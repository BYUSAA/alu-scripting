#!/usr/bin/python3
"""Print the titles of the first 10 hot posts for a given subreddit"""
import requests


def top_ten(subreddit):
    """Queries Reddit API and prints titles of first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.1'}  # Custom User-Agent to avoid being blocked

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the subreddit is valid (status code 200)
        if response.status_code == 200:
            json_data = response.json().get('data', {})
            posts = json_data.get('children', [])
            
            if len(posts) == 0:
                print(None)
            else:
                for post in posts:
                    title = post.get('data', {}).get('title', None)
                    print(title)
        else:
            print(None)
    except Exception:
        print(None)

