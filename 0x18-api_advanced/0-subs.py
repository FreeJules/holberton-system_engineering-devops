#!/usr/bin/python3
"""
returns the number of subscribers (not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    """
    url = "https://www.reddit.com/r/" + subreddit + "/about/.json"
    r = requests.get(url, headers={'User-agent': 'holberton 0.1'})
    if not r:
        return 0
    json = r.json()
    data = json.get("data")
    subscribers = data.get("subscribers")
    return subscribers
