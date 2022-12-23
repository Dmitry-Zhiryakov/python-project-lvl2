import pytest
from gendiff.parser import read_file, parse


@pytest.fixture
def file_data_json():
    file_data_json, _ = read_file('tests/fixtures/nested/file1.json')
    return file_data_json


@pytest.fixture
def file_data_yaml():
    file_data_yaml, _ = read_file('tests/fixtures/nested/file1.yaml')
    return file_data_yaml


@pytest.fixture
def result_dict():
    nested_file1_dict = {
        "common": {
            "setting1": "Value 1",
            "setting2": 200,
            "setting3": True,
            "setting6": {
                "key": "value",
                "doge": {
                    "wow": ""
                }
            }
        },
        "group1": {
            "baz": "bas",
            "foo": "bar",
            "nest": {
                "key": "value"
            }
        },
        "group2": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    }
    return nested_file1_dict


def test_parse(file_data_json, file_data_yaml, result_dict):
    assert parse(file_data_json, '.json') == result_dict
    assert parse(file_data_json, '.json') == parse(file_data_yaml, '.yaml')
    assert parse(file_data_json, '.json') == parse(file_data_yaml, '.yml')
