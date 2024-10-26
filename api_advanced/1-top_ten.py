#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Main function to print the top 10 hot posts of a subreddit"""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        response = requests.get(URL, headers=HEADERS, allow_redirects=False)
        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            hot_posts = response.json().get("data", {}).get("children", [])
            if hot_posts:
                # Print the title of each hot post
                for post in hot_posts:
                    print(post.get('data', {}).get('title', 'No title'))
            else:
                print(None)
        else:
            # If the subreddit does not exist or the request fails
            print(None)

    except requests.RequestException:
        # Catch network-related errors
        print(None)

    except ValueError:
        # Catch JSON decoding errors
        print(None)

