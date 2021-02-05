#!/usr/bin/python3
"""
Recursive function that queries the Reddit API
and returns a list containing the titles of all
hot articles for a given subreddit. If no results
are found for the given subreddit, the function
should return None.
"""


import requests


def recurse(subreddit, hot_list=[], after=""):
    """Function to return all hot titles"""
    after = {'after': after}
    res = requests.get("https://reddit.com/r/{}/hot.json?after={}".
                       format(subreddit, after),
                       headers={'User-agent': 'Fun_Cryptographer108'},
                       allow_redirects=False)

    if (res.status_code == 200):
        hot_list += res.json().get("data", {}).get("children", [])
        after_list = res.json().get("data", {}).get("after", None)

        if after_list:
            return recurse(subreddit, hot_list, after_list)

        else:
            return hot_list

    else:
        return None
