#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    - If not a valid subreddit, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User-Agent"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(None)
        return

    data = response.json().get("data", {})
    children = data.get("children", [])

    if not children:
        print(None)
        return

    for post in children:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
        else:
            print(None)
