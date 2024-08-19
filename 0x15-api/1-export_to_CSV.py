#!/usr/bin/python3

import requests
from sys import argv
import csv


def get_employee_todos_progress(employee_id):
    """ A function to return the info about employee and export to CSV file """
    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_datas = requests.get(url + f"users/{employee_id}")
        user_data = user_datas.json()
        employee_name = user_data['name']
        username = user_data['username']

        """ Getting the todolist for the employee """
        todos_list = requests.get(url + f"todos?userId={employee_id}")
        json_todos_list = todos_list.json()

        total_task = len(json_todos_list)
        task_done = [task for task in json_todos_list if task["completed"]]
        num_of_task_done = len(task_done)

        """ Print the result """
        print(f"Employee {employee_name} is done with tasks("
              f"{num_of_task_done}/{total_task}):")

        for task in task_done:
            print(f"\t {task['title']}")

        """ Export to CSV """
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                            "TASK_TITLE"])
            for task in json_todos_list:
                writer.writerow([employee_id, username, task["completed"],
                                task["title"]])

        print(f"Data exported to {csv_filename} successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: Script <employee_id>")
    else:
        get_employee_todos_progress(argv[1])
