import timeit
import argparse

import terminaltables

from pascal_triangle.implementations import ALL_IMPLEMENTATIONS


SETUP = """
from pascal_triangle.implementations import {implementation_class_name}

implementation = {implementation_class_name}()
# Mock _print() for more precise measurement
implementation._print = lambda arg: None
"""

STATEMENT = 'implementation.build({height})'

TITLE_TEMPLATE = 'Each {statement} called for {cycles} times'
FLOAT_FORMAT = '{0:.06f}'
HEADER = ['#', 'Implementation', 'Language', 'Duration, secs', 'Fraction of (*) duration',
          '% faster than (*)']
COLUMN_JUSTIFICATION = {0: 'left', 1: 'left', 2: 'left', 3: 'right', 4: 'right', 5: 'right'}


def print_table_data(table_data, title):
    table_data = [[str(n + 1)] + v for n, v in enumerate(table_data)]
    table_data.insert(0, HEADER)

    table = terminaltables.SingleTable(table_data)
    table.title = title
    table.justify_columns = COLUMN_JUSTIFICATION
    print table.table


def run_performance_test(height, cycles):
    statement = STATEMENT.format(height=height)

    table_data = []
    table_data_2 = []

    base_duration = None
    for implementation_class in ALL_IMPLEMENTATIONS:

        implementation_class_name = implementation_class.__name__

        table_line = [implementation_class_name, implementation_class.language]
        setup = SETUP.format(implementation_class_name=implementation_class_name)
        statement = STATEMENT.format(height=height)

        try:
            duration = timeit.timeit(statement, setup=setup, number=cycles)
            if not table_data:
                table_line[0] += '*'
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
        table_data_2.append(table_line)
        # if method_name == BASE_IMPLEMENTATION_METHOD_NAME:
        #     base_duration = duration
        #     line += '*'

    title = TITLE_TEMPLATE.format(statement=statement, cycles=cycles)
    print_table_data(table_data, title)
    print_table_data(list(v[:-1] for v in sorted(table_data_2, key=lambda x: x[-1])),
                     title + ' (sorted by performance)')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Run performance test of building Pascal\'s Triangle')
    parser.add_argument('-s', '--height', default=34, type=int,
                        help='height of Pascal\'s Triangle')
    parser.add_argument('-c', '--cycles', default=1000, type=int,
                        help='number of cycles to run for each implementation (default: 1000)')

    args = parser.parse_args()
    run_performance_test(args.height, args.cycles)
