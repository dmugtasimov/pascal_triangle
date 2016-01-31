#!/usr/bin/env bash

set -x

seq 0 $(( `nproc` - 1 )) | xargs --verbose -I{} sudo cpufreq-set -c {} -g performance

deactivate
workon pascal_triangle
python -m pascal_triangle.tests.limitation_test > limitation_test.rst
python -m pascal_triangle.tests.performance_test --height 34 > cpython_performance_test_34.rst
python -m pascal_triangle.tests.performance_test --height 34 --json > cpython_performance_test_34.json
python -m pascal_triangle.tests.performance_test --height 67 > cpython_performance_test_67.rst
python -m pascal_triangle.tests.performance_test --cycles 5 --height 900 > cpython_performance_test_900.rst
python -m pascal_triangle.tests.performance_test --cycles 5 --height 3000 > cpython_performance_test_3000.rst
deactivate

workon pascal_triangle_pypy
python -m pascal_triangle.tests.performance_test --height 34 > pypy_performance_test_34.rst
python -m pascal_triangle.tests.performance_test --height 34 --json > pypy_performance_test_34.json
python -m pascal_triangle.tests.performance_test --height 67 > pypy_performance_test_67.rst
python -m pascal_triangle.tests.performance_test --cycles 5 --height 900 > pypy_performance_test_900.rst
python -m pascal_triangle.tests.performance_test --cycles 5 --height 3000 > pypy_performance_test_3000.rst
deactivate

workon pascal_triangle

python -m pascal_triangle.tests.compare cpython_performance_test_34.json pypy_performance_test_34.json > cpython_vs_cython_vs_pypy.rst