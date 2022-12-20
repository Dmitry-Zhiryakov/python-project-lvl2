import pytest
from gendiff.parser import parse


@pytest.fixture
def file_path_json():
    return 'tests/fixtures/nested/file1.json'  


@pytest.fixture
def file_path_yaml():
    return 'tests/fixtures/nested/file1.yaml' 


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


def test_parse(file_path_json, file_path_yaml, result_dict):
    assert parse(file_path_json) == result_dict
    assert parse(file_path_json) == parse(file_path_yaml)
