#!/usr/bin/python3
"""Script that gets all employees and returns their TODO list progress."""

import json
import requests
"""module for the task"""


def get_employee_tasks():
    """A function to return the info about all employees."""
    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_response = requests.get(url + "users")
        user_data = user_response.json()

        """ Getting the all employee data in dictionary """
        all_employee_data = {}
        for user in user_data:
            employee_id = user['id']
            employee_name = user['username']

            """This is for getting todos"""
            todos_response = requests.get(url + f"todos?userId={employee_id}")
            todos_list = todos_response.json()

            """ Prepare data to export """
            tasks = [
                {
                    'username': employee_name,
                    "task": task['title'],
                    "completed": task['completed']
                }
                for task in todos_list
            ]
            all_employee_data[str(employee_id)] = tasks

        """ Save to a JSON file """
        json_filename = 'todos_all_employee.json'
        with open(json_filename, mode='w') as json_file:
            json.dump(all_employee_data, json_file, indent=4)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_employee_tasks()
