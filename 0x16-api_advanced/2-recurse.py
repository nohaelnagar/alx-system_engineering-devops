import requests
import sys

def recurse(subreddit, hot_list=[], after=None):
    """ Recursively queries the Reddit API to retrieve titles of all hot
        articles in a given subreddit.
    Args:
        subreddit (str): The name of the subreddit to check.
        hot_list (list): store the titles of hot articles.
        after (str): pagination, starting point for the next page.
    Returns:
        list or None: contains titles of all hot articles for the
        given subreddit,or None if no results are found. """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    data = requests.get(url, headers={'User-agent': 'my-bot'},
                        params={'after': after}, allow_redirects=False)

    if data.status_code == 200:
        after = data.json()['data']['after']
        posts = data.json()['data']['children']

        for post in posts:
            hot_list.append(post['data']['title'])
        if after is None:
            # If there is no new page
            if len(hot_list) == 0:
                return None

            return hot_list
        else:
            # If there is another page
            return recurse(subreddit, hot_list, after)
    else:
        return None
    

# TestRun =========== working, but Mr checker has frowned against it for reason best known to it.
if len(sys.argv) < 2:
    print("Please pass an argument for the subreddit to search.")
else:
    result = recurse(sys.argv[1])
    if result is not None:
        print(len(result))
    else:
        print("None")
