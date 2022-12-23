from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json


STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'


def get_formatter(tree, format):
    if format == STYLISH:
        return get_stylish(tree)
    elif format == PLAIN:
        return get_plain(tree)
    elif format == JSON:
        return get_json(tree)
