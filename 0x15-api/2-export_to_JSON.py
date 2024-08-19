#!/usr/bin/python3
"""Script that gets a given employee ID and return his TODO list progress."""

import json
import requests
from sys import argv
"""the module for this project """


def get_employee_todos_progress(employee_id):
    """ A function to return the info about a particular employee """
    try:
        url = "https://jsonplaceholder.typicode.com/"
        print(f"Fetching data for employee ID: {employee_id}")

        user_datas = requests.get(url + f"users/{employee_id}")
        print(f"User data request status: {user_datas.status_code}")
        user_data = user_datas.json()
        employee_name = user_data.get('name', 'Unknown')

        """ Getting the todo list for the employee """
        todos_list = requests.get(url + f"todos?userId={employee_id}")
        print(f"Todos data request status: {todos_list.status_code}")
        json_todos_list = todos_list.json()

        """ Prepare data to export """
        tasks = [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_name
            } for task in json_todos_list
        ]
        data_to_export = {str(employee_id): tasks}

        """ Save to a JSON file """
        json_filename = f"{employee_id}.json"
        with open(json_filename, mode='w') as json_file:
            json.dump(data_to_export, json_file, indent=4)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: script <employee_id>")
    else:
        get_employee_todos_progress(argv[1])
