import os
import json
import yaml


def parse(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension == '.json':
        return json.load(open(file_path))
    if file_extension == '.yml' or '.yaml':
        return yaml.load(open(file_path), Loader=yaml.FullLoader)
