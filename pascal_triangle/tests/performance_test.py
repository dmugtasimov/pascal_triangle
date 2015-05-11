import timeit
import argparse

from .utils import test_methods
from pascal_triangle.pascal_triangle import PyPascalTriangle, CyPascalTriangle, CPascalTriangle

TEST_CLASSES = (PyPascalTriangle, CyPascalTriangle, CPascalTriangle)

SETUP = """
from __main__ import %s
pascal_triangle_testable = %s()
from pascal_triangle.pascal_triangle import PyPascalTriangle, CyPascalTriangle, CPascalTriangle

TEST_CLASSES = (PyPascalTriangle, CyPascalTriangle, CPascalTriangle)
pascal_triangle_testable._print = lambda arg: None
"""

STATEMENT = 'pascal_triangle_testable.%s(%s)'
BASE_IMPLEMENTATION_METHOD_NAME = 'print_pascal_triangle_testable_fixed_better_naming'


def run_performance_test(height, cycles):
    results = []
    base_duration = None
    for test_class, method_name in test_methods():
        class_name = test_class.__name__
        setup = SETUP % (class_name, class_name)
        statement = STATEMENT % (method_name, height)
        try:
            duration = timeit.timeit(statement, setup=setup, number=cycles)
        except Exception as e:
            line = '%r while %s.%s(%s)' % (e, class_name, method_name, height)
            duration = None
        else:
            line = '%.06f seconds: %s times: %s.%s(%s)' % (duration, cycles, class_name, method_name,
                                                           height)
        if method_name == BASE_IMPLEMENTATION_METHOD_NAME:
            base_duration = duration
            line += '*'
        print line
        results.append((duration, line))

    print '-' * 40

    print '---=== SORTED ===---'
    for duration, line in (_ for _ in sorted(results, key=lambda x: x[0])):
        if base_duration is not None:
            if duration is None:
                factor = 'Exception:            '
            elif duration < base_duration:
                factor = '%-6.02f times faster:  ' % (base_duration / float(duration))
            elif duration == base_duration:
                factor = 'The same performance: '
            else:
                factor = '%-6.02f times slower:  ' % (duration / float(base_duration))
            line = factor + line
        print line


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run performance test of building Pascal\'s Triangle')
    parser.add_argument('-s', '--height', default=34, type=int,
                        help='height of Pascal\'s Triangle')
    parser.add_argument('-c', '--cycles', default=1000, type=int,
                        help='number of cycles to run for each implementation (default: 1000)')

    args = parser.parse_args()
    run_performance_test(args.height, args.cycles)
