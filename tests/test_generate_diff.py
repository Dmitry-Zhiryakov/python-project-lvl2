import pytest
from gendiff import generate_diff


@pytest.fixture
def file1_plain_json():
    return 'tests/fixtures/plain/file1.json'


@pytest.fixture
def file2_plain_json():
    return 'tests/fixtures/plain/file2.json'


@pytest.fixture
def file1_plain_yaml():
    return 'tests/fixtures/plain/file1.yaml'


@pytest.fixture
def file2_palin_yaml():
    return 'tests/fixtures/plain/file2.yaml'


@pytest.fixture
def file1_nested_json():
    return 'tests/fixtures/nested/file1.json'


@pytest.fixture
def file2_nested_json():
    return 'tests/fixtures/nested/file2.json'


@pytest.fixture
def file1_nested_yaml():
    return 'tests/fixtures/nested/file1.yaml'


@pytest.fixture
def file2_nested_yaml():
    return 'tests/fixtures/nested/file2.yaml'


@pytest.fixture
def diff_result_plain():
    with open('tests/fixtures/plain/diff_result.txt', "r") as file:
        return file.read()


@pytest.fixture
def diff_result_nested():
    with open('tests/fixtures/nested/diff_result.txt', "r") as file:
        return file.read()


def test_generate_diff(file1_plain_json, file2_plain_json, diff_result_plain):
    result = generate_diff(file1_plain_json, file2_plain_json)
    assert result == diff_result_plain


def test_generate_diff(file1_plain_yaml, file2_plain_yaml, diff_result_plain):
    result = generate_diff(file1_plain_yaml, file2_plain_yaml)
    assert result == diff_result_plain


def test_generate_diff(file1_nested_json, file2_nested_json, diff_result_nested):
    result = generate_diff(file1_nested_json, file2_nested_json)
    assert result == diff_result_nested


def test_generate_diff(file1_nested_yaml, file2_nested_yaml, diff_result_nested):
    result = generate_diff(file1_nested_yaml, file2_nested_yaml)
    assert result == diff_result_nested
