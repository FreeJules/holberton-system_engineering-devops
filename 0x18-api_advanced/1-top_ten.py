#!/usr/bin/python3
"""
Write a function that queries the Reddit API (https://www.reddit.com/dev/api/)
and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    If not a valid subreddit, print None
    """
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    r = requests.get(url, headers={'User-agent': 'holberton 0.1'},
                     allow_redirects=False)
    if not r:
        print(None)
        return
    json = r.json()
    data = json.get("data")
    children = data.get("children")
    titles = []
    for child in children[:10]:
        title = child.get("data", {}).get("title")
        titles.append(title)
    for title in titles:
        print(title)
