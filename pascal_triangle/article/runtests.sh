#!/usr/bin/env bash

set -x

seq 0 $(( `nproc` - 1 )) | xargs --verbose -I{} sudo cpufreq-set -c {} -g performance

workon pascal_triangle
python -m pascal_triangle.tests.limitation_test > limitation_test.rst
python -m pascal_triangle.tests.performance_test --height 34 --output-format=json > cpython_performance_test_34.json

python -m pascal_triangle.tests.performance_test --height 34 --output-format=rst > cpython_performance_test_34.rst
python -m pascal_triangle.tests.performance_test --height 67 --output-format=rst > cpython_performance_test_67.rst
python -m pascal_triangle.tests.performance_test --cycles 5 --height 900 --output-format=rst > cpython_performance_test_900.rst
python -m pascal_triangle.tests.performance_test --cycles 5 --height 3000 --output-format=rst > cpython_performance_test_3000.rst

workon pascal_triangle_pypy

python -m pascal_triangle.tests.performance_test --height 34 --output-format=json > pypy_performance_test_34.json

python -m pascal_triangle.tests.performance_test --height 34 --output-format=rst > pypy_performance_test_34.rst
python -m pascal_triangle.tests.performance_test --height 67 --output-format=rst > pypy_performance_test_67.rst
python -m pascal_triangle.tests.performance_test --cycles 5 --height 900 --output-format=rst > pypy_performance_test_900.rst
python -m pascal_triangle.tests.performance_test --cycles 5 --height 3000 --output-format=rst > pypy_performance_test_3000.rst

workon pascal_triangle

python -m pascal_triangle.tests.compare cpython_performance_test_34.json pypy_performance_test_34.json > cpython_vs_cython_vs_pypy.rst

../../ccpascal_triangle_normal 34 1000 > ccpascal_triangle_normal.txt
../../ccpascal_triangle_O2 34 1000 > ccpascal_triangle_O2.txt
../../ccpascal_triangle_O3 34 1000 > ccpascal_triangle_O3.txt
../../ccpascal_triangle_Ofast 34 1000 > ccpascal_triangle_Ofast.txt
