import pytest
from gendiff import generate_diff


@pytest.fixture
def file_path1():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def file_path2():
    return 'tests/fixtures/file2.json'


@pytest.fixture
def result_json():
    with open('tests/fixtures/result_json.txt', "r") as file:
        return file.read()


def test_generate_diff(file_path1, file_path2, result_json):
    result = generate_diff(file_path1, file_path2)
    assert result == result_json
