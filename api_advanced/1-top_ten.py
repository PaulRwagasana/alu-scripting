#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Main function"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    headers = {'User-Agent': 'MyAPI/0.0.1'}
    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        HOT_POSTS = RESPONSE.json().get("data").get("children")
        [print(post.get('data').get('title')) for post in HOT_POSTS]
    except Exception:
        print(None)
