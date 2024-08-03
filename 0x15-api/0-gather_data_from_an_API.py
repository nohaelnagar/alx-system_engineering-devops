#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import requests
import sys


def fetch_employee_data(employee_id):
    """ Fetch employee data from the REST API """
    # Base URL for the REST API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch employee data
    employee_url = f'{base_url}/users/{employee_id}'
    response_employee = requests.get(employee_url)
    if response_employee.status_code != 200:
        print(f'Error fetching employee data: {response_employee.status_code}')
        return None

    employee_data = response_employee.json()

    # Fetch TODO list data
    todos_url = f'{base_url}/users/{employee_id}/todos'
    response_todos = requests.get(todos_url)
    if response_todos.status_code != 200:
        print(f'Error fetching TODO list data: {response_todos.status_code}')
        return None

    todos_data = response_todos.json()

    return employee_data, todos_data


def display_todo_progress(employee_id):
    """ Display the TODO list progress of an employee """
    employee_data, todos_data = fetch_employee_data(employee_id)

    if employee_data is None or todos_data is None:
        return

    employee_name = employee_data.get('name')
    total_tasks = len(todos_data)
    done_tasks = [todo for todo in todos_data if todo['completed']]
    number_of_done_tasks = len(done_tasks)

    print(
        f'Employee {employee_name} is done with tasks(\
{number_of_done_tasks}/{total_tasks}):')

    for task in done_tasks:
        print(f'\t {task["title"]}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 0-gather_data_from_an_API.py <employee_id>')
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print('Employee ID must be an integer.')
        sys.exit(1)

    display_todo_progress(employee_id)

