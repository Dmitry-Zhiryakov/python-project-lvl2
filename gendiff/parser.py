import os
import json
import yaml


def read_file(file_path):
    with open(file_path, "r") as input_file:
        file_data = input_file.read()
        _, file_extension = os.path.splitext(file_path)
    return file_data, file_extension


def parse(data, file_extension='.json'):
    if file_extension == '.json':
        return json.loads(data)
    if file_extension == '.yml' or '.yaml':
        return yaml.load(data, Loader=yaml.FullLoader)
