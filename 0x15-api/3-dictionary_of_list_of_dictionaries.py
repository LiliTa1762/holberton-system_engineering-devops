#!/usr/bin/python3
"""Exporting all data to JSON file"""

import json
import requests
import sys


if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users/')
    data_user = user.json()

    all_dict = {}

    for name in data_user:
        todos = requests.get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'
                .format(name["id"]))
        data_todos = todos.json()

        all_list = []

        for data in data_todos:
            user_task = {}
            user_task["username"] = name["username"]
            user_task["task"] = data["title"]
            user_task["completed"] = data["completed"]
            all_list.append(user_task)

        all_dict[name["id"]] = all_list

    json_f = "todo_all_employees.json"
    with open(json_f, mode="w") as f:
        json.dump(all_dict, f)
