#!/usr/bin/python3
""" A Script that queries "reddit api" for number of subscribers"""

import requests

def number_of_subscribers(subreddit):
"""A functiont that returns number of subscribers """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0"}

    data = requests.get(url, headers=header, allow_redirects=False)

    if data.status_code == 200:
        subscribers = data.json().get("data").get("subscribers")
        return subscribers
    return 0
