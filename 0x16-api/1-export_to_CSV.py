#!/usr/bin/python3
"""
0-gather_data_from_an_API.py
"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    file_name = str(user_id) + '.csv'
    url = 'https://jsonplaceholder.typicode.com'
    url_users = url + '/users'
    url_todos = url + '/todos'
    """get user name"""
    r_user = requests.get(url_users + '/?id=' + str(user_id))
    user_username = r_user.json()[0].get("username")
    """get to-dos of a user"""
    completed_todos = 0
    completed_titles = []
    r_todos = requests.get(url_todos + '/?userId=' + str(user_id))
    user_todos = r_todos.json()
    """add data to file"""
    with open(file_name, 'a') as f:
        for todo in user_todos:
            f.write('"{}","{}","{}","{}"\n'.
                    format(str(user_id), user_username,
                           todo.get("completed"), todo.get("title")))
