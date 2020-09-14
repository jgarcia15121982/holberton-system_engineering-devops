#!/usr/bin/python3
"""
   Gather data from an API
"""
import json
import requests
import sys

if __name__ == "__main__":

    resp_1 = requests.get("https://jsonplaceholder.typicode.com/users/" + 
                          sys.argv[1])
    usr_dict = json.loads(resp_1.text)
    empl_name = usr_dict.get('name')
    resp_2 = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                          "?userId=" + sys.argv[1])
    all_task = json.loads(resp_2.text)
    task_done = [task for task in all_task if task.get('completed')]

    print("Employee {} is done with tasks({}/{}):".
          format(empl_name, len(task_done), len(all_task)))
    for task in task_done:
        print('\t {}'.format(task.get('title')))
