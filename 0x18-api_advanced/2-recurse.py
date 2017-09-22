#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    recursive function that queries the Reddit API
    """
    url = "https://www.reddit.com/r/"
    if after is None:
        new_url = url + subreddit + "/hot.json"
    else:
        new_url = url + subreddit + "/hot.json?after=" + after
    r = requests.get(new_url, headers={'User-agent': 'holberton 0.1'},
                     allow_redirects=False)
    if r.status_code != 200:
        return None
    data = r.json().get("data")
    children = data.get("children")
    for child in children:
        title = child.get("data").get("title")
        hot_list.append(title)
    after_value = data.get("after")
    if not after_value:
        return (hot_list)
    return recurse(subreddit, hot_list, after_value)
