#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests

def top_ten(subreddit):
    """Fetches and prints the titles of the first 10 hot posts from a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "PythonRedditClient/1.0 (by /u/yourusername)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json().get("data")
            
            if data and "children" in data:
                hot_posts = data["children"]
                if hot_posts:
                    for post in hot_posts:
                        print(post["data"]["title"])
                    return
            # Handle empty or malformed data
        print(None)
    
    except requests.exceptions.RequestException as e:
        # Print exception details for debugging if needed
        print(f"Request failed: {e}")
        print(None)
