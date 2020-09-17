#!/usr/bin/python3
"""How many subs?"""
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """
    bs_url = 'https://www.reddit.com/r/'
    url = bs_url + subreddit + "/about.json"
    credentials = {'User-Agent': "jgarcia15"}
    response = requests.get(url, headers=credentials, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get("data").get("subscribers")
