#!/usr/bin/python3

import json
import requests
import sys


if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(sys.argv[1]))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(sys.argv[1]))

    data_user = user.json()
    data_todos = todos.json()

    new_dict = {}
    all_list = []

    for data in data_todos:
        user_task = {}
        user_task["task"] = data["title"]
        user_task["completed"] = data["completed"]
        user_task["username"] = data_user["username"]
        all_list.append(user_task)

    new_dict[sys.argv[1]] = all_list #create the dict output

    with open (sys.argv[1] + ".json", "w") as jf:
        json.dump(new_dict, jf)
