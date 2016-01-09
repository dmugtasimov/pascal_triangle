import timeit
import argparse

import terminaltables

from .utils import test_methods
from pascal_triangle.pascal_triangle import PyPascalTriangle, CyPascalTriangle, CPascalTriangle
from pascal_triangle.implementations import ALL_IMPLEMENTATIONS

TEST_CLASSES = (PyPascalTriangle, CyPascalTriangle, CPascalTriangle)

SETUP = """
from pascal_triangle.implementations import {implementation_class_name}

implementation = {implementation_class_name}()
# Silence _print() for more precise measurement
implementation._print = lambda arg: None
"""

STATEMENT = 'implementation.build({height})'
#BASE_IMPLEMENTATION_METHOD_NAME = 'print_pascal_triangle_testable_fixed_better_naming'

FLOAT_FORMAT = '{0:.06f}'


def run_performance_test(height, cycles):
    statement = STATEMENT.format(height=height)
    print 'Running each {statement} for {cycles} times'.format(statement=statement, cycles=cycles)

    table_data = [
        ['Implementation', 'Duration, secs', 'Fraction of (*) duration',
         '% faster than (*)']
    ]

    base_duration = None
    for implementation_class in ALL_IMPLEMENTATIONS:

        implementation_class_name = implementation_class.__name__

        table_line = [implementation_class_name]
        setup = SETUP.format(implementation_class_name=implementation_class_name)
        statement = STATEMENT.format(height=height)

        try:
            duration = timeit.timeit(statement, setup=setup, number=cycles)
            if len(table_data) == 1:
                table_line[-1] += '*'
                base_duration = duration

        except Exception as e:
            import traceback
            traceback.print_exc()
            table_line.append(repr(e))
            duration = None
        else:
            table_line.append(FLOAT_FORMAT.format(duration))

        table_line.append(FLOAT_FORMAT.format(duration / base_duration)
                          if base_duration is not None else '-')
        table_line.append(FLOAT_FORMAT.format(100 * base_duration / duration - 100)
                          if base_duration is not None else '-')
        table_line.append(duration)

        table_data.append(table_line[:-1])
        # if method_name == BASE_IMPLEMENTATION_METHOD_NAME:
        #     base_duration = duration
        #     line += '*'

    table = terminaltables.SingleTable(table_data)
    table.justify_columns = {0: 'left', 1: 'right', 2: 'right', 3: 'right'}

    print table.table

    return

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
    parser = argparse.ArgumentParser(
        description='Run performance test of building Pascal\'s Triangle')
    parser.add_argument('-s', '--height', default=34, type=int,
                        help='height of Pascal\'s Triangle')
    parser.add_argument('-c', '--cycles', default=1000, type=int,
                        help='number of cycles to run for each implementation (default: 1000)')

    args = parser.parse_args()
    run_performance_test(args.height, args.cycles)
