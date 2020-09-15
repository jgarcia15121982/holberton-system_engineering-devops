#!/usr/bin/python3
"""
Dictionary of list of dictionaries
"""

import json
import requests


if __name__ == "__main__":
    bs_url = "https://jsonplaceholder.typicode.com/"

    url = bs_url + 'users/'
    users_resp = requests.get(url)
    users = users_resp.json()

    users_dict = {}
    for current_user in users:
        url = bs_url + 'todos'
        resp = requests.get(url)

        empl_id = current_user.get('id')

        tasks = [task for task in resp.json()
                 if task.get('userId') is int(empl_id)]

        my_list = []
        for task in tasks:
            new_dict = {"username": current_user['username'],
                        "task": task['title'],
                        "completed": task['completed'],
                        }
            my_list.append(new_dict)
        users_dict[current_user.get('id')] = my_list

    with open('{}.json'.format('todo_all_employees'), 'w') as f:
        json.dump(users_dict, f)
