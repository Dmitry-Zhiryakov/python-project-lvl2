from gendiff.parser import read_file, parse
from gendiff.diff_tree import build_tree
from gendiff.formatting import get_formatter


def generate_diff(file_path1, file_path2, format='stylish'):
    file_data_1, file_extension_1 = read_file(file_path1)
    file_data_2, file_extension_2 = read_file(file_path2)
    dict1 = parse(file_data_1, file_extension_1)
    dict2 = parse(file_data_2, file_extension_2)
    tree = build_tree(dict1, dict2)
    diff = get_formatter(tree, format)
    return diff
