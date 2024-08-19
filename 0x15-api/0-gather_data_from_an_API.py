#!/usr/bin/python3
"""Script that gets a given employee ID and return his TODO list progress."""

import requests
from sys import argv
"""Above is the module to work with"""


def get_employee_todos_progress(employee_id):
    """ a function to return the info about a particular employee"""
    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_datas = requests.get(url + f"users/{employee_id}")
        user_data = user_datas.json()
        employee_name = user_data["name"]

        """getting the todolist for the employee"""
        todo_list = requests.get(url + f"todos?userId={employee_id}")
        json_converted_todos = todo_list.json()

        total_task = len(json_converted_todos)
        task_done = [task for task in json_converted_todos
                     if task["completed"]]
        num_of_task_done = len(task_done)

        """ Print the result """
        print(f"Employee {employee_name} is done with task("
              f"{num_of_task_done}/{total_task}):")

        for task in task_done:
            print(f"\t {task['title']}")
    except Exception as e:
        print(f"an error occured: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: Script <employee_id>")
    else:
        get_employee_todos_progress(argv[1])
