#!/usr/bin/python3
"""
Function that queries the Reddit API and
returns the number of subscribers (not active users,
total subscribers) for a given subreddit.
If an invalid subreddit is given,
the function should return 0.
"""


import json
import requests


def number_of_subscribers(subreddit):

    res = requests.get("https://reddit.com/r/{}/about.json".format(subreddit),
                       headers={'User-agent': 'Fun_Cryptographer108'})
    a = res.json()

    if (res.status_code != 200):
        return 0

    else:
        return a["data"]["subscribers"]
