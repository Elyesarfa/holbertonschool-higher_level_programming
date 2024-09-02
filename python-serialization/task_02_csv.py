#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(csv_filename: str) -> bool:
    """
    Converts data from a CSV file to JSON format and saves it to `data.json`.
    :param csv_filename: The path to the CSV file to be converted.
    :return: `True` if the conversion was successful, `False` otherwise.
    """
    try:
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data_list = [row for row in reader]
        with open('data.json', 'w') as json_file:
            json.dump(data_list, json_file, indent=4)
        print(f"Data from {csv_filename} has been converted to data.json.")
        return True
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
