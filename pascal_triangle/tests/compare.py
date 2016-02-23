import json
import argparse

import collections

from pascal_triangle.utils import RSTTable, format_float_safe


CYTHON_PYHTON_MAP = {
    'CyPascalTriangleNonRecursiveLessCLike': 'PyPascalTriangleNonRecursiveLessCLike',
    'CyPascalTriangleNonRecursiveCTypesULong': 'PyPascalTriangleNonRecursiveCTypesULong',
    'CyPascalTriangleNonRecursiveCLikeMoreImproved': 'PyPascalTriangleNonRecursiveCLikeMoreImproved',
    'CyPascalTriangleNonRecursiveIterators': 'PyPascalTriangleNonRecursiveIterators',
    'CyPascalTriangleNonRecursiveCLikeImproved': 'PyPascalTriangleNonRecursiveCLikeImproved',
    'CyPascalTriangleConstantLists': 'PyPascalTriangleConstantLists',
    'CyPascalTriangleNonRecursiveCTypes': 'PyPascalTriangleNonRecursiveCTypes',
    'CyPascalTriangleNonRecursive': 'PyPascalTriangleNonRecursive',
    'CyPascalTriangleIterators': 'PyPascalTriangleIterators'
}


def compare(cpython_file, pypy_file, output_format):
    with open(cpython_file, 'r') as f:
        cpython_results = json.load(f)

    cpython_results_dict = collections.defaultdict(dict)
    for result in cpython_results:
        implementation = result['implementation']
        mapped_cpython_implementation = CYTHON_PYHTON_MAP.get(implementation)
        if mapped_cpython_implementation:
            cpython_results_dict[mapped_cpython_implementation]['cython'] = result['duration']
        else:
            cpython_results_dict[implementation]['cpython'] = result['duration']

    with open(pypy_file, 'r') as f:
        pypy_results = json.load(f)

    pypy_results_dict = {result['implementation']: result['duration'] for result in pypy_results}

    table_data = []
    for implementation, durations in cpython_results_dict.iteritems():
        cpython_duration = durations.get('cpython')
        cython_duration = durations.get('cython')
        pypy_duration = pypy_results_dict.get(implementation)
        if cpython_duration is None or (cython_duration is None and pypy_duration is None):
            continue

        cpython_text = '{0:.06f}'.format(cpython_duration)
        if cython_duration:
            cython_percent = ((cpython_duration / cython_duration) - 1) * 100
            cython_text = '{0:.06f} / {1:+.02f}'.format(cython_duration, cython_percent)
        else:
            cython_text = '-'

        if pypy_duration:
            pypy_percent = ((cpython_duration / pypy_duration) - 1) * 100
            pypy_text = '{0:.06f} / {1:+.02f}'.format(pypy_duration, pypy_percent)
        else:
            pypy_text = '-'

        table_data.append([
            '`{}`_'.format(implementation) if output_format == 'rst' else implementation,
            cpython_text, cython_text, pypy_text, cpython_duration])

    table_data = [[str(n + 1)] + r[:-1] for n, r in
                  enumerate(sorted(table_data, key=lambda x: x[-1]))]
    table_data.insert(0, ['#', 'Implementation', 'CPython, s', 'Cython, s / % faster',
                          'PyPy, s / % faster'])

    table = RSTTable(table_data)
    table.justify_columns = {0: 'right', 1: 'left', 2: 'center', 3: 'center', 4: 'center'}
    print table.table


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Compare JSON results',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('cpython_json_file', help='Base JSON file to be compared')
    parser.add_argument('pypy_json_files', help='Other JSON files to be compared')
    parser.add_argument('--output-format', choices=('rst', 'console'), default='console')

    args = parser.parse_args()

    compare(args.cpython_json_file, args.pypy_json_files, args.output_format)
