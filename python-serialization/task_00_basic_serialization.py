#!/usr/bin/env python3

import json


def serialize_and_save_to_file(data, filename):
    """
    Converts a Python dictionary into a serialized format and saves it to a file.
    :param data: The dictionary to be serialized.
    :param filename: The name of the file where the serialized data will be stored.
    """
    try:
        with open(filename, 'w') as json_file:
            json.dump(data, json_file)
    except Exception as e:
        print(f"An error occurred while serializing and saving to file: {e}")


def load_and_deserialize(filename):
    """
    Reads a JSON file and converts its contents into a Python dictionary.
    :param filename: The path to the JSON file to be read.
    :return: The dictionary resulting from deserializing the JSON data.
    """
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        return data
    except Exception as e:
        print(f"An error occurred while loading : {e}")
        return None
