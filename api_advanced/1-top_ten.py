#!/usr/bin/python3
"""Print the titles of the first 10 hot posts for a given subreddit"""
import requests


def top_ten(subreddit):
    """The top ten titles for a given subreddit"""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            json_data = response.json().get('data', {})
            children = json_data.get('children', [])
            
            if len(children) == 0:
                print(None)
            else:
                for post in children:
                    print(post.get('data', {}).get('title', None))
        else:
            print(None)
    except Exception:
        print(None)
