import json
from gendiff.parser import parse


_add = '+ '
_miss = '- '
_ident = '  '


def generate_diff(file_path1, file_path2):
    file1 = parse(file_path1)
    file2 = parse(file_path2)
    diff_list = []
    for key1, value1 in file1.items():
        value_from_file2 = file2.pop(key1, None)
        if value_from_file2:
            if value1 == value_from_file2:
                diff_list.append((_ident + key1, value1))
            else:
                diff_list.extend([(_miss + key1, value1), (_add + key1, value_from_file2)])
        else:
            diff_list.append((_miss + key1, value1))
    for key2, value2 in file2.items():
        diff_list.append((_add + key2, value2))
    diff_list.sort(key=lambda x: x[0][2:])
    diff_dict = {key: value for (key, value) in diff_list}
    return json.dumps(diff_dict, indent=2).replace('"', '').replace(',', '')
