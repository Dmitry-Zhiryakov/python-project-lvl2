from gendiff.formatters.stylish import get_stylish


def get_formatter(tree, format):
    if format == 'stylish':
        return get_stylish(tree)
