#!/usr/bin/python3
import requests
from sys import argv


def fetch_employee_todos(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url + "users/{}".format(employee_id))
    employee = response.json()

    todo_response = requests.get(url + "todos?userId={}".format(employee_id))
    todos = todo_response.json()

    completed = [todo for todo in todos if todo.get("completed")]

    # Print the result
    print("{} is done with {}/{}".format(employee['name'],
          len(completed), len(todos)))

    for task in completed:
        print("\t {}".format(task['title']))


if __name__ == "__main__":
    employee_id = argv[1]
    fetch_employee_todos(employee_id)
