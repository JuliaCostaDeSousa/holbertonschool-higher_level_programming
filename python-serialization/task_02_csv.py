#!/usr/bin/python3
"""
Module task_02_csv
"""
import json
import csv


def convert_csv_to_json(CSVfile):
    """
    Converts CSV file to JSON file
    """

    try:
        with open(CSVfile, 'r') as csvfile:
            filereader = csv.DictReader(csvfile)
            data = list(filereader)

        with open('data.json', 'w', encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        return False
