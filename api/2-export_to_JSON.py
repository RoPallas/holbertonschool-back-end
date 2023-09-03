#!/usr/bin/python3
"""Script for API request"""
import json
import requests
from sys import argv

if __name__ == "__main__":

    try:
        emp_id = int(argv[1])
    except Exception:
        exit()

    emp_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{emp_id}').json()
    todo_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos').json()

    user_name = emp_response['username']
    file_name = f"{emp_id}.json"

    user_to_dict = {emp_id: []}
    for task in todo_response:
        user_to_dict[emp_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user_name
        })

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(user_to_dict, file, indent=4)
