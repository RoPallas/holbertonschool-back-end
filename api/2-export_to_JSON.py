#!/usr/bin/python3
"""Script for API request"""
import json
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

    json_filename = f"{employee_id}.json"
    json_data = {str(employee_id): []}

    for todo in todos_data:
        json_data[str(employee_id)].append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": user_data['username']
        })

    with open(json_filename, mode="w") as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
