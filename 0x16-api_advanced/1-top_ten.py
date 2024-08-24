#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the top 10 hot posts for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'request'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check for a valid response that contains JSON
        if response.status_code != 200:
            print("None")
            return

        # Ensure the response is JSON
        try:
            data = response.json().get("data", {}).get("children", [])
        except ValueError:
            print("None")
            return

        if not data:
            print("None")
            return

        for post in data[:10]:
            title = post.get("data", {}).get("title")
            if title:
                print(title)
            else:
                print("None")

    except requests.exceptions.RequestException:
        print("None")
