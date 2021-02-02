#!/usr/bin/python3
"""Exporting data to CSV"""


import csv
import requests
import sys


if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(sys.argv[1]))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(sys.argv[1]))

    data_user = user.json()
    data_todos = todos.json()

with open(sys.argv[1] + '.csv', mode='w') as user_file:
    user_writer = csv.writer(user_file, delimiter=',', quoting=csv.QUOTE_ALL)

    for t in data_todos:
        user_writer.writerow([t["userId"], data_user["username"],
                              t["completed"], t["title"]])
