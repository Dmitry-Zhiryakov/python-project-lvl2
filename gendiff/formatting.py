from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json


def get_formatter(tree, format):
    if format == 'stylish':
        return get_stylish(tree)
    elif format == 'plain':
        return get_plain(tree)
    elif format == 'json':
        return get_json(tree)
