#!/usr/bin/env python
from gendiff.cli import get_args
from gendiff import generate_diff


def main():
    first_file, second_file, format = get_args()
    print(generate_diff(first_file, second_file, format))


if __name__ == '__main__':
    main()
