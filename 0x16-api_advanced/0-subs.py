#!/usr/bin/python3

import requests
"""
    queries the Reddit API and returns the number of subscribers
"""


def number_of_subscribers(subreddit):
    """Define the URL for the subreddit's about.json endpoint"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Python script)'}

    try:
        """Make a GET request to the Reddit API"""
        response = requests.get(url, headers=headers, allow_redirects=False)

        """Check if the request was successful"""
        if response.status_code == 200:
            """Parse the JSON response to get the number of subscribers"""
            data = response.json()
            return data['data']['subscribers']
        else:
            """If the subreddit is invalid or there's an error, return 0"""
            return 0
    except requests.RequestException:
        """In case of a network error, return 0"""
        return 0
