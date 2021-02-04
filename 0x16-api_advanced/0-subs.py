#!/usr/bin/python3

import requests
import json


def number_of_subscribers(subreddit):

    res = requests.get("https://reddit.com/r/{}/about.json".format(subreddit),
                       headers={'User-agent': 'Fun_Cryptographer108'})
    a = res.json()

    if (res.status_code != 200):
        return 0

    else:
        return a["data"]["subscribers"]
