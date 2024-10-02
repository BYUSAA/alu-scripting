#!/usr/bin/python3
"""Module that fetches the top ten hot posts from a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts for a given subreddit.
    
    If the subreddit is valid, prints the titles of the posts. 
    If not a valid subreddit, prints None.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = f"https://reddit.com/r/{subreddit}.json"
    response = requests.get(subreddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json()
        for i in range(10):
            print(
                json_data.get('data')
                .get('children')[i]
                .get('data')
                .get('title')
            )
    else:
        print(None)


# This block is for testing the function
if __name__ == "__main__":
    import sys  # Import sys module for command-line argument handling

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
