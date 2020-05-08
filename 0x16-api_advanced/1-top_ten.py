#!/usr/bin/python3
""" python requesting subscribers from given reddit """

import requests


def top_ten(subreddit):
    url = 'https://reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'user-agent': 'Taskrabbitpower'}
    response = requests.get(url, headers=headers)

    try:
        for index in response.json()['data']['children']:
            print(index['data']['title'])
    except Exception:
        print (None)
