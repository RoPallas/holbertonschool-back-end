#!/usr/bin/python3
"""Script for API request"""
import json
import requests


if __name__ == "__main__":

    emp_user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/').json()
    todo_response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos').json()

    user_to_dict = {}
    file_name = "todo_all_employees.json"

    for user in emp_user:
        id = user.get("id")
        user_to_dict[id] = []
        for task in todo_response:
            if user.get("id") == task.get("userId"):
                user_to_dict[id].append({
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(user_to_dict, file, indent=4)
