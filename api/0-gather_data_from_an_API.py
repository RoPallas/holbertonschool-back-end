#!/usr/bin/python3
"""Script for API request"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Given employee ID, returns information about his/her todo list
    progress.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    user_data = user_response.json()

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    t_tasks = len(todos_data)
    c_tasks = sum(1 for todo in todos_data if todo["completed"])
    name = user_data['name']
    print(f"Employee {name} is done with tasks({c_tasks}/{t_tasks}):")

    for todo in todos_data:
        if todo["completed"]:
            print(f"\t {todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
