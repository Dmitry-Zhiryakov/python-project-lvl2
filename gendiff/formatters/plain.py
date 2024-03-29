import itertools
from gendiff.diff_tree import REMOVED, ADDED, NESTED, CHANGED


def convert_to_string(value):
    if isinstance(value, dict):
        return '[complex value]'

    elif isinstance(value, bool):
        return 'true' if value else 'false'

    elif isinstance(value, int):
        return value

    elif value is None:
        return 'null'

    else:
        return f"'{value}'"


def get_plain(tree):

    def iter_(node, path=''):
        current_path = f"{path}{node['key']}"

        if node['type'] == REMOVED:
            return f"Property '{current_path}' was removed"

        elif node['type'] == ADDED:
            return f"Property '{current_path}' was added" \
                   f" with value: {convert_to_string(node['value'])}"

        elif node['type'] == NESTED:
            node_children = sorted(
                node['children'], key=lambda item: item['key'])
            nested_lines = map(
                lambda child: iter_(
                    child, f"{current_path}."), node_children)
            result = itertools.chain(nested_lines)
            return '\n'.join(filter(lambda item: item, result))

        elif node['type'] == CHANGED:
            return f"Property '{current_path}' was updated." \
                   f" From {convert_to_string(node['value_from_dict1'])}" \
                   f" to {convert_to_string(node['value_from_dict2'])}"

    children = children = sorted(
        tree.get('children'), key=lambda item: item['key'])
    lines = map(lambda child: iter_(child), children)
    result = itertools.chain(lines)
    return '\n'.join(filter(lambda item: item, result))
