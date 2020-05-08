#!/usr/bin/python3
""" Getting queries for all titles """
import requests


def recurse(subreddit, hot_list=[], added=""):
    url = 'https://reddit.com/r/{}/hot.json?after={}'.format(subreddit, added)
    headers = {'user-agent': 'Taskrabbitpower'}
    response = requests.get(url, headers=headers)

    try:
        for index in response.json()['data']['children']:
            hot_list.append(index['data']['title'])
        added = response.json()['data']['after']
        if added is not None:
            return recurse(subreddit, hot_list, added)
        else:
            return (hot_list)
    except Exception:
        return None
