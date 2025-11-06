import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        
    Returns:
        None: Prints the post titles or None if subreddit is invalid.
    """
    # Set a custom User-Agent header as required by Reddit API
    headers = {'User-Agent': 'MyBot/0.0.1'}
    
    # Construct the URL for the hot posts in the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Make the GET request, disabling redirect following
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful and not a redirect
    if response.status_code != 200:
        print("None")
        return
        
    try:
        # Parse JSON response
        data = response.json()
        posts = data['data']['children']
        
        # Check if any posts were returned
        if not posts:
            print("None")
            return
            
        # Print titles of the first 10 hot posts
        for post in posts:
            print(post['data']['title'])
            
    except (KeyError, ValueError):
        # Handle cases where JSON parsing fails or data structure is unexpected
        print("None")