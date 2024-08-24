#!/usr/bin/python3
"""
    queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "request"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    num_subs = data.get("subscribers")

    return num_subs
