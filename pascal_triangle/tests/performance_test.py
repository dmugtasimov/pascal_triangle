import timeit
import inspect
from pascal_triangle.pascal_triangle import PyPascalTriangle, CyPascalTriangle, CPascalTriangle

TEST_CLASSES = (PyPascalTriangle, CyPascalTriangle, CPascalTriangle)

SETUP = """
from __main__ import %s
pascal_triangle_testable = %s()
pascal_triangle_testable._print = lambda self: None
"""

STATEMENT = 'pascal_triangle_testable.%s(%s)'


def run_performance_test(height, cycles):
    results = []
    for test_class in TEST_CLASSES:
        class_name = test_class.__name__
        setup = SETUP % (class_name, class_name)
        method_names = (name for name, method in
                        inspect.getmembers(test_class, predicate=inspect.ismethod)
                        if not name.startswith('_'))
        for method_name in method_names:
            statement = STATEMENT % (method_name, height)
            duration = timeit.timeit(statement, setup=setup, number=cycles)
            line = '%.06f seconds: %s times: %s.%s(%s)' % (duration, cycles, class_name, method_name,
                                                        height)
            print line
            results.append((duration, line))

        print '-' * 40

    print '---=== SORTED ===---'
    for line in [y[1] for y in sorted(results, key=lambda x: x[0])]:
        print line


if __name__ == '__main__':
    run_performance_test(200, 100)
