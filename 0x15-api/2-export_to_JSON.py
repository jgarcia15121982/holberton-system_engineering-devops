#!/usr/bin/python3
"""
Export to CSV
"""

import json
import requests
import sys


if __name__ == "__main__":
    empl_id = sys.argv[1]
    bs_url = "https://jsonplaceholder.typicode.com/"

    url = bs_url + "users/" + empl_id
    response = requests.get(url)

    empl_username = response.json().get('username')

    url = bs_url + 'todos'
    response = requests.get(url)

    tasks = [task for task in response.json()
             if task.get('userId') is int(empl_id)]

    my_list = []
    for task in tasks:
        new_dict = {"task": task['title'],
                    "completed": task['completed'],
                    "username": empl_username}
        my_list.append(new_dict)

    tasks_dictionary = {sys.argv[1]: my_list}
    with open('{}.json'.format(sys.argv[1]), 'w') as f:
        json.dump(tasks_dictionary, f)
