#!/usr/bin/python3
"""makes an api call for top ten post"""
import requests


def top_ten(subreddit):
    """ get the top ten hot posts in a given subreddit
    Args:
        subreddit(str) - The name of the subreddit to check"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    data = requests.get(url, headers={'User-agent': 'my-bot'},
                        allow_redirects=False)
    if data.status_code == 200:
        all_posts = data.json()['data']['children']
        count = 0
        for post in all_posts:
            if count == 10:
                break
            print(post['data']['title'])
            count = count + 1
    else:
        print("None")
