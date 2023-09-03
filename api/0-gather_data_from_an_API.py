#!/usr/bin/python3
"""Script for API request"""
import requests
from sys import argv

if __name__ == "__main__":

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    try:
        emp_id = int(argv[1])
    except Exception:
        exit()

    emp_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{emp_id}")
    todo_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos")

    for task in todo_response.json():
        if task.get("completed") is True:
            NUMBER_OF_DONE_TASKS += 1
            TOTAL_NUMBER_OF_TASKS += 1
            TASK_TITLE.append(task.get("title"))
        else:
            TOTAL_NUMBER_OF_TASKS += 1

    EMPLOYEE_NAME = emp_response.json()["name"]

    print("Employee {} is done with tasks({}/{}):".
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in TASK_TITLE:
        print("\t {}".format(task))
