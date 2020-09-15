#!/usr/bin/python3
"""
Export to CSV
"""

import csv
import requests
import sys


if __name__ == "__main__":
    empl_id = sys.argv[1]
    bs_url = "https://jsonplaceholder.typicode.com/"

    url = bs_url + "users/" + empl_id
    response = requests.get(url)

    empl_name = response.json().get('username')

    url = bs_url + 'todos'
    response = requests.get(url)

    tasks = [task for task in response.json()
             if task.get('userId') is int(empl_id)]

    with open('{}.csv'.format(sys.argv[1]), 'w') as f:
        fields = ["userId", "name", "completed", "title"]
        writer = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_ALL)
        for task in tasks:
            task['name'] = empl_name
            del task['id']
            writer.writerow(task)
