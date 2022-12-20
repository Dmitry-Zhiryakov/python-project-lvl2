import pytest
from gendiff import generate_diff


cases = [
    ('tests/fixtures/plain/file1.json',
     'tests/fixtures/plain/file2.yaml',
     'stylish',
     'tests/fixtures/plain/result_stylish.txt'
     ),
    ('tests/fixtures/nested/file1.json',
     'tests/fixtures/nested/file2.yaml',
     'stylish',
     'tests/fixtures/nested/result_stylish.txt'
     ),
    ('tests/fixtures/plain/file1.json',
     'tests/fixtures/plain/file2.yaml',
     'plain',
     'tests/fixtures/plain/result_plain.txt'
     ),
    ('tests/fixtures/nested/file1.json',
     'tests/fixtures/nested/file2.yaml',
     'plain',
     'tests/fixtures/nested/result_plain.txt'
     )
]


@pytest.mark.parametrize("file_path1,file_path2,format,path_to_expected", cases)
def test_generate_diff(file_path1, file_path2, format, path_to_expected):
    with open(path_to_expected, 'r') as file:
        expected = file.read()
    assert generate_diff(file_path1, file_path2, format) == expected
