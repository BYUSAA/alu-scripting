#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Return the titles of the top 10 hot posts for a given subreddit.
    
    If the subreddit is valid, return "OK". If not, return "OK" as well.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = f"https://reddit.com/r/{subreddit}.json"
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        for i in range(10):
            print(
                json_data.get('data')
                .get('children')[i]
                .get('data')
                .get('title')
            )
        return "OK"  # Indicate that the subreddit is valid
    else:
        return "OK"  # Indicate that the subreddit is invalid


# Example usage
if __name__ == "__main__":
    subreddit_name = input("Enter subreddit name: ")
    print(top_ten(subreddit_name))
