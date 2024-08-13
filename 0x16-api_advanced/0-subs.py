#!/usr/bin/python3
"""This module gets the number of subs for a subreddit"""

import requests


def number_of_subscribers(subreddit):
    """gets the number of subscribbers in a given subreddit
    Args:
        subreddit (str): specific section, community or topic
    Returns:
        int: number of subscribers.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    data = requests.get(url, headers={'User-agent': 'my-bot'})
    if data.status_code == 200:
        return data.json()['data']['subscribers']
    else:
        return 0
