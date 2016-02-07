import timeit
import argparse
import json

import terminaltables

from pascal_triangle.implementations import ALL_IMPLEMENTATIONS
from pascal_triangle.utils import RSTTable, format_float_safe


SETUP = """
from pascal_triangle.implementations import {implementation_class_name}

implementation = {implementation_class_name}()
# Mock _print() for more precise measurement
implementation._print = lambda arg: None
"""

CODE_TEMPLATE = 'implementation.build({height})'

TITLE_TEMPLATE = 'Each {statement} called for {cycles} times'
HEADER = ['#', 'Implementation', 'Language', 'Duration, secs', 'Fraction of (*) duration',
          '% faster than (*)']
COLUMN_JUSTIFICATION = {0: 'left', 1: 'left', 2: 'left', 3: 'right', 4: 'right', 5: 'right'}


def run_performance_test(height, cycles, sorted_by_performance=True, output_format='console'):
    statement = CODE_TEMPLATE.format(height=height)

    table_data = []

    base_duration = None
    for implementation_class in ALL_IMPLEMENTATIONS:

        if implementation_class.max_height is not None and implementation_class.max_height < height:
            continue

        implementation_class_name = implementation_class.__name__

        table_line = {
            'implementation': implementation_class_name,
            'language': implementation_class.language
        }
        setup = SETUP.format(implementation_class_name=implementation_class_name)
        statement = CODE_TEMPLATE.format(height=height)

        try:
            duration = timeit.timeit(statement, setup=setup, number=cycles)
            if implementation_class.original:
                base_duration = duration

        except Exception as e:
            import traceback
            traceback.print_exc()
            table_line['duration'] = repr(e)
            duration = None
        else:
            table_line['duration'] = duration

        table_line['factor'] = (duration / base_duration) if base_duration is not None else '-'
        table_line['percent'] = ((100 * base_duration / duration - 100)
                                 if base_duration is not None else '-')

        table_data.append(table_line)

    if output_format == 'json':
        print json.dumps(table_data)
    else:
        title = TITLE_TEMPLATE.format(statement=statement, cycles=cycles)

        if sorted_by_performance:
            title += ' (ordered by performance)'
            table_data = sorted(table_data, key=lambda x: x['duration'])

        table_data_local = [HEADER] + [
            [
                str(n + 1),
                '`{}`_'.format(v['implementation'])
                    if output_format == 'rst' else v['implementation'],
                v['language'],
                format_float_safe(v['duration']),
                format_float_safe(v['factor']),
                format_float_safe(v['percent']),
            ] for n, v in enumerate(table_data)
        ]

        if output_format == 'console':
            table_class = terminaltables.AsciiTable
        elif output_format == 'rst':
            table_class = RSTTable
        else:
            raise ValueError('Unknown output format: {}'.format(output_format))

        table = table_class(table_data_local)
        table.justify_columns = COLUMN_JUSTIFICATION

        print title
        print ''
        print table.table


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Run performance test of building Pascal\'s Triangle',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-s', '--height', default=34, type=int,
                        help='height of Pascal\'s Triangle')
    parser.add_argument('-c', '--cycles', default=1000, type=int,
                        help='number of cycles to run for each implementation')
    parser.add_argument('--chronological-order', action='store_true', default=False)
    parser.add_argument('--output-format', choices=('rst', 'json', 'console'), default='console')

    args = parser.parse_args()
    run_performance_test(args.height, args.cycles,
                         sorted_by_performance=not args.chronological_order,
                         output_format=args.output_format)
