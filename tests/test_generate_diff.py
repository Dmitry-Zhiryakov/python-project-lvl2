import pytest
from gendiff import generate_diff


@pytest.fixture
def file1_json_path():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def file2_json_path():
    return 'tests/fixtures/file2.json'


@pytest.fixture
def file1_yaml_path():
    return 'tests/fixtures/file1.yaml'


@pytest.fixture
def file2_yaml_path():
    return 'tests/fixtures/file2.yaml'


@pytest.fixture
def diff_result():
    with open('tests/fixtures/diff_result.txt', "r") as file:
        return file.read()


def test_generate_diff_json(file1_json_path, file2_json_path, diff_result):
    result = generate_diff(file1_json_path, file2_json_path)
    assert result == diff_result


def test_generate_diff_yaml(file1_yaml_path, file2_yaml_path, diff_result):
    result = generate_diff(file1_yaml_path, file2_yaml_path)
    assert result == diff_result
