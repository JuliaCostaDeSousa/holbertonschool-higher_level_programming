#!/usr/bin/python3
"""
Module task_02_requests
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all post from JSONPlaceholder
    """

    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        response_json = r.json()
        for post in response_json:
            print(post["title"])
    else:
        print("Request error")


def fetch_and_save_posts():
    """
    Fetches all post from JSONPlaceholder
    """

    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        response_json = r.json()
        with open('posts.csv', 'w', newline='') as csvfile:
            csv_w = csv.writer(csvfile, delimiter=',')
            csv_w.writerow(["id", "title", "body"])
            for line in response_json:
                csv_w.writerow([line["id"], line["title"], line["body"]])
    else:
        print("Request error")
