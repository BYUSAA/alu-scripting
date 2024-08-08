import praw
from prawcore.exceptions import NotFound, Redirect

def top_ten(subreddit):
    # Initialize a Reddit instance
    reddit = praw.Reddit(
        client_id="your_client_id",
        client_secret="your_client_secret",
        user_agent="your_user_agent"
    )
    
    try:
        # Get the subreddit
        subreddit = reddit.subreddit(subreddit)
        
        # Fetch the top 10 hot posts
        hot_posts = subreddit.hot(limit=10)
        
        # Print the titles of the hot posts
        for post in hot_posts:
            print(post.title)
    
    except (NotFound, Redirect):
        # Handle invalid subreddit
        print(None)
    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")

