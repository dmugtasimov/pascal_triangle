import types
import time

import terminaltables

from pascal_triangle.implementations.cextension.base import CPascalTriangleBase
from pascal_triangle.implementations import ALL_IMPLEMENTATIONS


MAX_HEIGHT = 4096
MAX_TIME_SECONDS = 1

CODE_TEMPLATE = 'implementation.build({height})'


def _print(self, arg):
    self._print_last_call = list(arg)


def get_code(class_name, height):
    return CODE_TEMPLATE.format(class_name=class_name, height=height)


def run_limitation_test():
    powers_of_2 = tuple(2 ** p for p in xrange(MAX_HEIGHT + 1))

    table_data = [
        ['#', 'Implementation', 'Language', 'Height limit', 'Duration, s', 'Reason', 'Info']
    ]
    for test_class in ALL_IMPLEMENTATIONS:
        class_name = test_class.__name__
        if issubclass(test_class, CPascalTriangleBase):
            pascal_triangle = test_class(return_list=True)
        else:
            pascal_triangle = test_class()
        pascal_triangle._print_last_call = None
        pascal_triangle._print = types.MethodType(_print, pascal_triangle)

        lower = 0
        upper = 1
        height = lower
        duration = None
        last_error = {}
        print 'Estimating implementation: {}...'.format(class_name)
        while lower < upper <= MAX_HEIGHT:
            start = time.time()
            try:
                result = pascal_triangle.build(upper)
            except Exception as e:
                last_error = {'limit': upper,
                              'reason': 'exception', 'info': repr(e)}
                upper = (lower + upper) / 2
                continue
            finish = time.time()
            duration = finish - start

            if result is not None:
                result = list(result)
                total_sum = sum(result)
                if total_sum != powers_of_2[upper]:
                    last_error = {'limit': height,
                                  'reason': 'overflow or error'}
                    upper = (lower + upper) / 2
                    continue

            if duration > MAX_TIME_SECONDS:
                last_error = {'limit': height,
                              'reason': 'timeout',
                              'info': '{timeout:.06f} s, (duration: {duration:.06f} s)'.format(
                                  timeout=MAX_TIME_SECONDS, duration=duration)}
                upper = (lower + upper) / 2
                continue
            lower = upper
            height = lower
            upper *= 2
        else:
            table_data.append([
                str(len(table_data)), class_name, test_class.language,
                str(height), '{0:.06f}'.format(duration) if duration is not None else '-',
                last_error.get('reason', ''), last_error.get('info', '')
            ])

    table = terminaltables.SingleTable(table_data)
    print table.table


if __name__ == '__main__':
    run_limitation_test()
