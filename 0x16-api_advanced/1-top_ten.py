#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Print the titles of the 10 hottest posts on a given subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {"User-Agent": "request"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    data = response.json().get("data", {}).get("children", [])

    # Extract titles and join them with newline
    top_10_post = "\n".join(post.get("data", {}).get("title") for post in data)
    print(top_10_post)
