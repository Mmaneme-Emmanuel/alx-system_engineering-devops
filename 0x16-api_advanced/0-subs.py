#!/usr/bin/python3
"""
    Queries the Reddit API and returns the number of subscribers.
"""
import requests
"""the module to use in this project"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; Python script)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    # Safely extract the 'data' dictionary
    data = response.json().get("data", {})
    # Safely get the number of subscribers, defaulting to 0 if not found
    num_subs = data.get("subscribers", 0)

    return num_subs
