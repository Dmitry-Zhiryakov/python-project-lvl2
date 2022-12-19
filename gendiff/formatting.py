from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain


def get_formatter(tree, format):
    if format == 'stylish':
        return get_stylish(tree)
    if format == 'plain':
        return get_plain(tree)
