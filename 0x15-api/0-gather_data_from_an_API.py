#!/usr/bin/python3
""" Api to request certain information """

from sys import argv
import requests


def return_todolist(employee_id):
    """ function to print todo list """
    EMPLOYEE_NAME = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            employee_id)).json().get("name")

    NUMBER_OF_DONE_TASKS = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}&&completed=true'
        .format(employee_id)).json()

    TOTAL_NUMBER_OF_TASKS = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(employee_id)).json()

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, len(NUMBER_OF_DONE_TASKS), len(TOTAL_NUMBER_OF_TASKS)))

    for lists in NUMBER_OF_DONE_TASKS:
        print('\t {}'.format(lists.get('title')))


if __name__ == "__main__":
    return_todolist(int(argv[1]))
