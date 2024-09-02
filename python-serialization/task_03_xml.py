#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary: dict, filename: str) -> None:
    """
    Serializes a Python dictionary into XML format and saves it to a file.
    :param dictionary: The Python dictionary to be serialized.
    :param filename: The path to the file where the XML data will be saved.

    """
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename)
        print(f"Data successfully serialized to {filename}.")
    except Exception as e:
        print(f"An error occurred : {e}")


def deserialize_from_xml(filename: str) -> dict:
    """
    Deserializes XML data from a specified file into a Python dictionary.
    :param filename: The path to the file containing the XML data.
    :return: A Python dictionary with the deserialized XML data.

    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}
        for child in root:
            result[child.tag] = child.text
        print(f"Data successfully deserialized from {filename}.")
        return result
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred while deserializing from XML: {e}")
        return {}
