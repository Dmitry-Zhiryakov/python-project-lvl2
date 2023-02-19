### python-project-lvl2
### Hexlet tests and linter status:
[![Actions Status](https://github.com/Dmitry-Zhiryakov/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Dmitry-Zhiryakov/python-project-lvl2/actions)
[![Github Actions](https://github.com/Dmitry-Zhiryakov/python-project-lvl2/actions/workflows/github-actions.yml/badge.svg)](https://github.com/Dmitry-Zhiryakov/python-project-lvl2/actions/workflows/github-actions.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/37bac00e4bb34750ead6/maintainability)](https://codeclimate.com/github/Dmitry-Zhiryakov/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/37bac00e4bb34750ead6/test_coverage)](https://codeclimate.com/github/Dmitry-Zhiryakov/python-project-lvl2/test_coverage)

# Gendiff

"Gendiff" is a CLI utility that generates the difference between two files. 

#### Utility features:
- Support for different input formats: `.json`, `.yaml`.
- Three report formats: `stylish`, `plain`, and `json`.


## Installation:

Using pip [(Demonstration)](https://asciinema.org/a/3IhP87MV4a3oCpiviDCCjxFXb):

```
pip3 install --user git+https://github.com/Dmitry-Zhiryakov/python-project-lvl2.git
```

## Usage:

```
gendiff [-h] [-f FORMAT] first_file second_file
```

Positional arguments:
`first_file`
`second_file`

Options:

`-h`, `--help` show this help message and exit.

`-f`, `--format` set format of output.

The absence of a plus or minus indicates that the key is in both files, and its values are the same. In all other situations, the key value is either different, or the key is only in one file.

## Examples of using:
Comparing files (result output in `stylish` format by default):
- JSON
  - [Plain](https://asciinema.org/a/vtJwPQ0DKFB4spgwc2SC6tEZA)
  - [Nested](https://asciinema.org/a/lSK0viexNIB05nL3zbGKFgcQJ)
- YAML
  - [Plain](https://asciinema.org/a/xAwIhgaKbj97LMfLXydU7a1Lm)
  - [Nested](https://asciinema.org/a/j1n2FpFmm9QCFeARdtKMu91CX)
- JSON / YAML
  - [Plain](https://asciinema.org/a/LZFvz8BCsh2TPJNwN46FyR2uF)
  - [Nested](https://asciinema.org/a/SaWbKCl9piU6qcTe1Q8YYtDWF)

Result output: 
- [-f plain](https://asciinema.org/a/wyRVn4TYXMwBc4a76yf6EqxRm)
- [-f json](https://asciinema.org/a/uLsYJUiJqULbiwBHh7rlYL42x)
