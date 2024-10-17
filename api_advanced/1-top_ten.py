#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests

def top_ten(subreddit):
    """Main function to print the titles of the top 10 hot posts in a subreddit."""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        # Make the request and only proceed if the status code is 200 (OK)
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        if RESPONSE.status_code == 200:
            HOT_POSTS = RESPONSE.json().get("data", {}).get("children", [])

            if HOT_POSTS:
                for post in HOT_POSTS:
                    print(post.get("data", {}).get("title"))
            else:
                print(None)  # No posts found
        else:
            print(None)  # Subreddit does not exist or request failed
    except Exception:
        print(None)  # Catch any other exceptions and return None

