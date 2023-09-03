#!/usr/bin/python3
import json
import requests
import sys


if __name__ == "__main__":
    """
    Given employee ID, returns information about his/her todo list
    progress.
    """
    u_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(u_id)
    response = requests.get(user_url)
    user_data = response.json()

    t_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(u_id)
    response = requests.get(t_url)
    tasks_data = response.json()

    user_tasks = {str(u_id): []}

    for task in tasks_data:
        task_data = {
            "username": user_data["username"],
            "task": task["title"],
            "completed": task["completed"]
        }
        user_tasks[str(u_id)].append(task_data)

    with open("todo_all_employees.json", "a") as json_file:
        json.dump(user_tasks, json_file)
