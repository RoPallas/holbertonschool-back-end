#!/usr/bin/python3
import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Given employee ID, returns information about his/her td list
    progress.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    u_data = user_response.json()

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode="w", newline="") as csv_file:
        cw = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)

        for td in todos_data:
            cw.writerow([u_data['id'], u_data['username'], td['completed'], td['title']])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
