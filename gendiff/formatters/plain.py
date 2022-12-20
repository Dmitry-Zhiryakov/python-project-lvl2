import itertools


def convert_to_string(value):
    if isinstance(value, dict):
        return '[complex value]'

    elif isinstance(value, int):
        return value

    elif isinstance(value, bool):
        return 'true' if value else 'false'

    elif value is None:
        return 'null'

    else:
        return f"'{value}'"


def get_plain(tree):

    def iter_(node, path=''):
        current_path = f"{path}{node['key']}"

        if node['type'] == 'removed':
            return f"Property '{current_path}' was removed"

        elif node['type'] == 'added':
            return f"Property '{current_path}' was added" \
                   f" with value: {convert_to_string(node['value'])}"

        elif node['type'] == 'nested':
            nested_lines = map(
                lambda child: iter_(
                    child, f"{current_path}."), node['children'])
            result = itertools.chain(nested_lines)
            return '\n'.join(filter(lambda item: item, result))

        elif node['type'] == 'changed':
            return f"Property '{current_path}' was updated." \
                   f" From {convert_to_string(node['value_from_dict1'])}" \
                   f" to {convert_to_string(node['value_from_dict2'])}"

    children = tree.get('children')
    lines = map(lambda child: iter_(child), children)
    result = itertools.chain(lines)
    return '\n'.join(filter(lambda item: item, result))
