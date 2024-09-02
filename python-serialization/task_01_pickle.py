#!/usr/bin/env python

import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        """
        Serializes the object and writes it to a file.
        :param filename: The path to the file where the serialized object will be saved.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object serialized and saved to {filename}.")
        except Exception as e:
            print(f"Failed to serialize object: {e}")

    @classmethod
    def deserialize(cls, filename: str):
        """
        Deserializes an instance of `CustomObject` from a specified file.
        :param filename: The path to the file from which the object will be deserialized.
        :return: An instance of `CustomObject`, or `None` if deserialization is unsuccessful.

        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            if isinstance(obj, cls):
                print(f"Object deserialized from {filename}.")
                return obj
            else:
                print(f"Error: {cls.__name__} object.")
                return None
        except (FileNotFoundError, pickle.UnpicklingError, EOFError) as e:
            print(f"Failed to deserialize object: {e}")
            return None
