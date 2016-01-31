import timeit
import argparse

from pascal_triangle.implementations import ALL_IMPLEMENTATIONS
from pascal_triangle.utils import RSTTable


SETUP = """
from pascal_triangle.implementations import {implementation_class_name}

implementation = {implementation_class_name}()
# Mock _print() for more precise measurement
implementation._print = lambda arg: None
"""

CODE_TEMPLATE = 'implementation.build({height})'

TITLE_TEMPLATE = 'Each {statement} called for {cycles} times'
FLOAT_FORMAT = '{0:.06f}'
HEADER = ['#', 'Implementation', 'Language', 'Duration, secs', 'Fraction of (*) duration',
          '% faster than (*)']
COLUMN_JUSTIFICATION = {0: 'left', 1: 'left', 2: 'left', 3: 'right', 4: 'right', 5: 'right'}


def print_table_data(table_data, title):
    table_data = [[str(n + 1)] + v for n, v in enumerate(table_data)]
    table_data.insert(0, HEADER)

    table = RSTTable(table_data)
    table.justify_columns = COLUMN_JUSTIFICATION
    print title
    print ''
    print table.table


def run_performance_test(height, cycles, sorted_by_performance=True):
    statement = CODE_TEMPLATE.format(height=height)

    table_data = []

    base_duration = None
    for implementation_class in ALL_IMPLEMENTATIONS:

        if implementation_class.max_height is not None and implementation_class.max_height < height:
            continue

        implementation_class_name = implementation_class.__name__

        table_line = [implementation_class_name, implementation_class.language]
        setup = SETUP.format(implementation_class_name=implementation_class_name)
        statement = CODE_TEMPLATE.format(height=height)

        try:
            duration = timeit.timeit(statement, setup=setup, number=cycles)
            if implementation_class.original:
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

        table_data.append(table_line)

    title = TITLE_TEMPLATE.format(statement=statement, cycles=cycles)

    if sorted_by_performance:
        title += ' (ordered by performance)'
        table_data = sorted(table_data, key=lambda x: x[-1])

    print_table_data(list(v[:-1] for v in table_data), title)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Run performance test of building Pascal\'s Triangle',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-s', '--height', default=34, type=int,
                        help='height of Pascal\'s Triangle')
    parser.add_argument('-c', '--cycles', default=1000, type=int,
                        help='number of cycles to run for each implementation')
    parser.add_argument('--chronological-order', action='store_true', default=False)

    args = parser.parse_args()
    run_performance_test(args.height, args.cycles,
                         sorted_by_performance=not args.chronological_order)
