from gendiff.parser import parse
from gendiff.diff_tree import build_tree
from gendiff.formatting import get_formatter


def generate_diff(file_path1, file_path2, format='stylish'):
    dict1 = parse(file_path1)
    dict2 = parse(file_path2)
    tree = build_tree(dict1, dict2)
    diff = get_formatter(tree, format)
    return diff
