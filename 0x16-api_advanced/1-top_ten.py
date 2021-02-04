#!/usr/bin/python3
"""
Function that queries the Reddit API and
prints the titles of the first 10 hot posts
listed for a given subreddit.
"""


import json
import requests


def top_ten(subreddit):
    """Function to return the top 10 posts"""
    res = requests.get("https://reddit.com/r/{}/hot.json".format(subreddit),
                       headers={'User-agent': 'Fun_Cryptographer108'},
                       params={'limit': 10})
    a = res.json()

    if (res.status_code != 200):
        print("None")

    else:
        x = a["data"]["children"]
        for i in x:
            h = i["data"]["title"]
            print(h)
