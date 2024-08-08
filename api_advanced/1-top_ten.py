#!/usr/bin/python3
"""
Script that fetches the top 10 hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    If the subreddit is not valid, prints None.
    
    Args:
        subreddit (str): The name of the subreddit to query.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])
            
            if len(posts) == 0:
                print(None)
            else:
                for post in posts[:10]:
                    print(post.get("data", {}).get("title"))
        else:
            print(None)
    except Exception as e:
        print(None)
