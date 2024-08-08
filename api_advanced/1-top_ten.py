import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        None
    """
    # Set the API endpoint URL
    url = f"https://oauth.reddit.com/r/{subreddit}/hot"

    # Set the API request headers
    headers = {
        "User-Agent": "My Reddit API Client"
    }

    # Send a GET request to the API endpoint
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if the subreddit is valid
        if "data" in data and "children" in data["data"]:
            # Extract the post titles
            post_titles = [post["data"]["title"] for post in data["data"]["children"][:10]]

            # Print the post titles
            for title in post_titles:
                print(title)
        else:
            print(None)
    else:
        print(None)
