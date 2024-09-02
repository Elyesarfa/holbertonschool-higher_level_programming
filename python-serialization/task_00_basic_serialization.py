import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.
    
    :param data: A Python dictionary to be serialized.
    :param filename: The path to the JSON file where the data will be saved.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file into a Python dictionary.
    
    :param filename: The path to the JSON file to be read.
    :return: A Python dictionary containing the deserialized JSON data.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
