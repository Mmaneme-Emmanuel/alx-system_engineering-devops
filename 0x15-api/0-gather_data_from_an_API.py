#!/usr/bin/python3
import requests
import sys

# Get the employee ID from command-line arguments
employee_id = sys.argv[1]

# Fetch employee details
url = "https://jsonplaceholder.typicode.com/"  # Assuming this is the base URL
response = requests.get(url + "users/{}".format(employee_id))
employee = response.json()

# Fetch todos for the employee
todo_response = requests.get(url + "todos?userId={}".format(employee_id))
todos = todo_response.json()

# Collect completed tasks
completed = []

for todo in todos:
    if todo.get("completed"):
        completed.append(todo)

# Print the result
print("{} is done with {}/{}".format(employee['name'],
      len(completed), len(todos)))

for task in completed:
    print("\t {}".format(task['title']))
