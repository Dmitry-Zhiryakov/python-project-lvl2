import itertools


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
    children = tree.get('children')
    lines = map(lambda child: iter(child, depth + 1), children)

    def iter(node, depth):
        indent = get_indent(depth)

        if node['type'] == 'deleted':
            return f"{indent}{SIGN_DEL} {node['key']}:" \
                   f" {convert_to_string(node['value'], depth)}"

        elif node['type'] == 'added':
            return f"{indent}{SIGN_ADD} {node['key']}:" \
                   f" {convert_to_string(node['value'], depth)}"

        elif node['type'] == 'nested':
            nest_l = map(lambda n: iter(n, depth + 1), node['children'])
            result = '\n'.join(nest_l)
            return f"{indent}  {node['key']}: {{\n{result}\n  {indent}}}"

        elif node['type'] == 'unchanged':
            return f"{indent}  {node['key']}:" \
                   f" {convert_to_string(node['value'], depth)}"

        elif node['type'] == 'changed':
            line_1 = f"{indent}{SIGN_DEL} {node['key']}:" \
                     f" {convert_to_string(node['value_from_dict1'], depth)}\n"
            line_2 = f"{indent}{SIGN_ADD} {node['key']}:" \
                     f" {convert_to_string(node['value_from_dict2'], depth)}"
            return line_1 + line_2

    result = itertools.chain("{", lines, "}")
    return '\n'.join(result)
