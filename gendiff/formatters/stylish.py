import itertools
from gendiff.diff_tree import REMOVED, ADDED, NESTED, UNCHANGED, CHANGED


INDENT = '  '
DEEP_INDENT = INDENT * 2
SIGN_ADD = '+'
SIGN_DEL = '-'


def get_indent(depth):
    if depth == 1:
        return INDENT
    else:
        return INDENT + (DEEP_INDENT * (depth - 1))


def convert_to_string(value, depth):
    current_indent = get_indent(depth)

    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            lines.append(
                f"{INDENT + current_indent + DEEP_INDENT}{key}:"
                f" {convert_to_string(val, depth + 1)}")
        result = '\n'.join(lines)
        return f'{{\n{result}\n  {current_indent}}}'

    elif isinstance(value, bool):
        return 'true' if value else 'false'

    elif value is None:
        return 'null'

    else:
        return value


def get_stylish(tree, depth=0):

    def iter_(node, depth):
        indent = get_indent(depth)

        if node['type'] == REMOVED:
            return f"{indent}{SIGN_DEL} {node['key']}:" \
                   f" {convert_to_string(node['value'], depth)}"

        elif node['type'] == ADDED:
            return f"{indent}{SIGN_ADD} {node['key']}:" \
                   f" {convert_to_string(node['value'], depth)}"

        elif node['type'] == NESTED:
            node_children = sorted(
                node['children'], key=lambda item: item['key'])
            nested_lines = map(
                lambda child: iter_(child, depth + 1), node_children)
            result = '\n'.join(nested_lines)
            return f"{indent}  {node['key']}: {{\n{result}\n  {indent}}}"

        elif node['type'] == UNCHANGED:
            return f"{indent}  {node['key']}:" \
                   f" {convert_to_string(node['value'], depth)}"

        elif node['type'] == CHANGED:
            line_1 = f"{indent}{SIGN_DEL} {node['key']}:" \
                     f" {convert_to_string(node['value_from_dict1'], depth)}\n"
            line_2 = f"{indent}{SIGN_ADD} {node['key']}:" \
                     f" {convert_to_string(node['value_from_dict2'], depth)}"
            return line_1 + line_2

    children = sorted(tree.get('children'), key=lambda item: item['key'])
    lines = map(lambda child: iter_(child, depth + 1), children)
    result = itertools.chain("{", lines, "}")
    return '\n'.join(result)
