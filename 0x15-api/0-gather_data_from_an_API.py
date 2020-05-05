#!/usr/bin/python3
""" Api to request certain information """

import requests
from sys import argv


if __name__ == "__main__":

    EMPLOYEE_NAME = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(argv[1])).json().get('name')

    NUMBER_OF_DONE_TASKS = requests.get(
            'https://jsonplaceholder.typicode.com/'
            'todos?userId={}&&completed=true'
            .format(argv[1])).json()

    TOTAL_NUMBER_OF_TASKS = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(argv[1])).json()

    print("Employee {} is done with tasks({}/{}):".format(
            EMPLOYEE_NAME,
            len(NUMBER_OF_DONE_TASKS),
            len(TOTAL_NUMBER_OF_TASKS)))

    for lists in NUMBER_OF_DONE_TASKS:
        print('\t {}'.format(lists.get('title')))
