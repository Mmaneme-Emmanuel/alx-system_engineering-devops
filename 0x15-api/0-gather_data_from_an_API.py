#!/usr/bin/python3
import requests
from sys import argv


def fetch_employee_todos(employee_id):
    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_info = requests.get(url + f"users/{employee_id}")
        response = user_info.json()
        employee_name = response["name"]

        """getting the todolist for the employee"""
        todo_list = requests.get(url + f"todos?userId={employee_id}")
        json_converted_todos = todo_list.json()

        total_task = (json_converted_todos)
        task_done = [task for task in json_converted_todos
                     if task["completed"]]
        num_of_task_done = len(task_done)

        # Print the result
        print(f"Employee {employee_name} is done with task",
              f"{num_of_task_done}/{task_done}:")

        for task in task_done:
            print(f"\t {task['title']}")
    except Exception as e:
        print(f"an error occured {e}")


if __name__ == "__main__":
    employee_id = argv[1]
    fetch_employee_todos(employee_id)
