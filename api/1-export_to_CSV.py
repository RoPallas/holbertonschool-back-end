#!/usr/bin/python3
"""Script for API request"""
import requests
from sys import argv

if __name__ == "__main__":

    try:
        emp_id = int(argv[1])
    except Exception:
        exit()

    emp_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{emp_id}").json()
    todo_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos").json()

    name = emp_response['username']
    file_name = f"{emp_id}.csv"
    with open(file_name, "w", encoding="utf-8") as file:
        for task in todo_response:
            task_completed = task.get('completed')
            task_title = task.get('title')
            file.write(
                f'"{emp_id}","{name}","{task_completed}","{task_title}"\n')
