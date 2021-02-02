#!/usr/bin/python3
"""Gather fake data from a API"""

import requests
import sys


if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(sys.argv[1]))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(sys.argv[1]))

    data_user = user.json()
    data_todos = todos.json()

    all_list = []
    count_task = 0
    count_all_task = 0

    for t in data_todos:
        if t["completed"] is True:  # access to the value of the key completed
            count_task += 1
            all_list.append(t["title"])
            # add the value that is in the key Title in position t
        count_all_task += 1
    print("Employee {} is done with tasks({}/{})"
          .format(data_user['name'], count_task, count_all_task))

    for x in all_list:
        print(("\t{}").format(x))
