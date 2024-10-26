#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests

def top_ten(subreddit):
    """Return the titles of the top ten posts from the given subreddit.
    If the subreddit is invalid, return 0."""
    
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://reddit.com/r/{}.json".format(subreddit)
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])
        for i in range(min(10, len(posts))):  # Handle fewer than 10 posts
            print(posts[i].get('data').get('title'))
    else:
        print("Invalid subreddit")  # Changed output for invalid subreddit

# Example usage:
# top_ten('python')
