import pytest
from gendiff import generate_diff
from gendiff.parser import read_file, parse


cases_stylish_and_plain = [
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


cases_json = [
    ('tests/fixtures/plain/file1.json',
     'tests/fixtures/plain/file2.yaml',
     'json',
     'tests/fixtures/plain/result_json.txt'
     ),
    ('tests/fixtures/nested/file1.json',
     'tests/fixtures/nested/file2.yaml',
     'json',
     'tests/fixtures/nested/result_json.txt'
     )
]


@pytest.mark.parametrize(
    "file_path1,file_path2,format,path_to_expected", cases_stylish_and_plain)
def test_generate_diff(file_path1, file_path2, format, path_to_expected):
    with open(path_to_expected, 'r') as file:
        expected = file.read()
    assert generate_diff(file_path1, file_path2, format) == expected


@pytest.mark.parametrize(
    "file_path1,file_path2,format,path_to_expected", cases_json)
def test_generate_diff_json(file_path1, file_path2, format, path_to_expected):
    data_render, extension_render = read_file(path_to_expected)
    dict_diff = parse(generate_diff(file_path1, file_path2, format))
    dict_render = parse(data_render, extension_render)

    def compare_dict(dict_1, dict_2):
        children_1 = dict_1.get('children')
        children_2 = dict_2.get('children')
        sorted_children_1 = sorted(children_1, key=lambda item: item['key'])
        sorted_children_2 = sorted(children_2, key=lambda item: item['key'])
        result = True
        i = 0
        if len(sorted_children_1) != len(sorted_children_2):
            return False
        for item in sorted_children_1:
            if item.get('type') == 'nested' and \
                    sorted_children_2[i].get('type') == 'nested':
                result = result and compare_dict(item, sorted_children_2[i])
            else:
                result = result and (sorted_children_2[i] == item)
            i = i + 1
        return result

    assert compare_dict(dict_diff, dict_render) is True
