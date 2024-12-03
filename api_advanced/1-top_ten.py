#!/usr/bin/python3
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check if the subreddit exists or if there is a redirect
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            
            if not posts:
                print(None)
            else:
                for post in posts:
                    print(post['data']['title'])
        else:
            print(None)

    except requests.exceptions.RequestException as e:
        print(None)
