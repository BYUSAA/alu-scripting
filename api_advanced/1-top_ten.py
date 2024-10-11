#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Main function to print top 10 hot posts for a subreddit"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        if RESPONSE.status_code == 200:
            HOT_POSTS = RESPONSE.json().get("data", {}).get("children", [])
            if not HOT_POSTS:
                print("None")
            else:
                for post in HOT_POSTS:
                    print(post.get('data', {}).get('title'))
            print("OK")  # Output OK for successful subreddit retrieval
        else:
            print("None")  # Output None for non-existent subreddit
    except Exception:
        print("None")


# Testing the function
if __name__ == "__main__":
    top_ten('subreddit_name')  # Replace 'subreddit_name' with any subreddit name

