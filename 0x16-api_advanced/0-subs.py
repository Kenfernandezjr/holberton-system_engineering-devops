#!/usr/bin/python3
""" python requesting subscribers from given reddit """

import requests


def number_of_subscribers(subreddit):
    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'Taskrabbitpower'}
    response = requests.get(url, headers=headers)

    try:
        return response.json()['data']['subscribers']
    except Exception:
        return (0)
