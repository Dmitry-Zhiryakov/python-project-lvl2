python-project-lvl2

### Hexlet tests and linter status:
[![Actions Status](https://github.com/Dmitry-Zhiryakov/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Dmitry-Zhiryakov/python-project-lvl2/actions)
[![Github Actions](https://github.com/Dmitry-Zhiryakov/python-project-lvl2/actions/workflows/github-actions.yml/badge.svg)](https://github.com/Dmitry-Zhiryakov/python-project-lvl2/actions/workflows/github-actions.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/37bac00e4bb34750ead6/maintainability)](https://codeclimate.com/github/Dmitry-Zhiryakov/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/37bac00e4bb34750ead6/test_coverage)](https://codeclimate.com/github/Dmitry-Zhiryakov/python-project-lvl2/test_coverage)

# Вычислитель отличий

### Вычислитель отличий – программа, определяющая разницу между двумя структурами данных. 

Вывод справки
```gendiff -h```

Результат сравнения файлов может выводиться в трех разных форматах: default='stylish', plain, json.
Отсутствие плюса или минуса говорит о том, что ключ есть в обоих файлах, и его значения совпадают. Во всех остальных ситуациях значение по ключу либо отличается, либо ключ есть только в одном файле.

### Пример работы пакета

Сравнение двух плоских файлов (JSON):

[![asciicast](https://asciinema.org/a/XxKCwZ5nCS3VFBJETrpYGNmZT.svg)](https://asciinema.org/a/XxKCwZ5nCS3VFBJETrpYGNmZT)

Сравнение двух плоских файлов (YAML):

[![asciicast](https://asciinema.org/a/v6eSprvv4JJwHJVGzoVSdtP2M.svg)](https://asciinema.org/a/v6eSprvv4JJwHJVGzoVSdtP2M)

Сравнение двух файлов с рекурсивной структурой (JSON или YAML)

[![asciicast](https://asciinema.org/a/3BxQAMap4m38WuzraiqIjkE0P.svg)](https://asciinema.org/a/3BxQAMap4m38WuzraiqIjkE0P)

Плоский вид представления результата сравнения двух файлов (JSON или YAML)

[![asciicast](https://asciinema.org/a/QjqzmJbm5lKfLlql1qj3PkPRE.svg)](https://asciinema.org/a/QjqzmJbm5lKfLlql1qj3PkPRE)

Вывод результата сравнения двух файлов в формате JSON 

[![asciicast](https://asciinema.org/a/xLxZMZLOYY9ajOtn7MV9HTeFs.svg)](https://asciinema.org/a/xLxZMZLOYY9ajOtn7MV9HTeFs)