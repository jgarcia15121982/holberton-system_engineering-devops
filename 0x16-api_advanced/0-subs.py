#!/usr/bin/python3
"""How many subs?"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    headers = {"User-Agent": "jgarcia"}
    resp = requests.get('https://reddit.com/r/' + subreddit + '/about.json',
                        headers=headers, allow_redirects=True)
    if subs.status_code == 404:
        return 0
    subs_json = subs.json()
    subs_data = subs_json['data']
    subs_amount = subs_data['subscribers']
    return subs_amount
