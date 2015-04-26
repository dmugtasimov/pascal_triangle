import timeit
import inspect
from pascal_triangle.pascal_triangle import PascalTriangleTestable

_TEST_CLASS = PascalTriangleTestable

"""
import timeit

from pascal_triangle import (print_pascal_triangle, print_pascal_triangle_v2,
                             print_pascal_triangle_v3, print_pascal_triangle_v4,
                             print_pascal_triangle_v5, print_pascal_triangle_v6,
                             print_pascal_triangle_v7, print_pascal_triangle_v8,
                             print_pascal_triangle_v9, print_pascal_triangle_v10)
from cypascal_triangle import (cyprint_pascal_triangle_v1, cyprint_pascal_triangle_v2,
                               cyprint_pascal_triangle_v3)
from cpascal_triangle import (cprint_pascal_triangle_v1, casmprint_pascal_triangle_v2,
                              casmprint_pascal_triangle_v3)


FUNCS = (
    print_pascal_triangle,
    print_pascal_triangle_v2,
    print_pascal_triangle_v3,
    print_pascal_triangle_v4,
    print_pascal_triangle_v5,
    print_pascal_triangle_v6,
    print_pascal_triangle_v7,
    print_pascal_triangle_v8,
    print_pascal_triangle_v9,
    print_pascal_triangle_v10,
    cyprint_pascal_triangle_v1,
    cyprint_pascal_triangle_v2,
    cyprint_pascal_triangle_v3,
    cprint_pascal_triangle_v1,
    casmprint_pascal_triangle_v2,
    casmprint_pascal_triangle_v3,
)

CYCLES = 100
HEIGHT = 200
for func in (f.__name__ for f in FUNCS):
    print '%s(%s) done for %s times in %s seconds' % (func, HEIGHT, CYCLES,
            timeit.timeit('%s(%s)' % (func, HEIGHT), setup='from __main__ import %s' % func,
                          number=CYCLES))
"""

SETUP = """
from __main__ import %s
pascal_triangle_testable = %s()
pascal_triangle_testable._print = lambda self: None
""" % (_TEST_CLASS.__name__, _TEST_CLASS.__name__)

STATEMENT = 'pascal_triangle_testable.%s(%s)'


def run_performance_test(height, cycles):
    method_names = (name for name, method in
                    inspect.getmembers(_TEST_CLASS, predicate=inspect.ismethod)
                    if not name.startswith('_'))
    for method_name in method_names:
        statement = STATEMENT % (method_name, height)
        duration = timeit.timeit(statement, setup=SETUP, number=cycles)
        print '%s seconds: %s times: %s(%s)' % (duration, cycles, method_name, height)


if __name__ == '__main__':
    run_performance_test(200, 100)
