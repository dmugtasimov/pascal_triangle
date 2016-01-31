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


def compare(cpython_file, pypy_file):
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
        cython_duration = durations.get('cython', '-')
        pypy_duration = pypy_results_dict.get(implementation)
        if cpython_duration is None or pypy_duration is None:
            continue

        table_data.append(
            [implementation, format_float_safe(cpython_duration),
             format_float_safe(cython_duration),
             format_float_safe(pypy_duration), cpython_duration]
        )

    table_data = [[str(n + 1)] + r[:-1] for n, r in
                  enumerate(sorted(table_data, key=lambda x: x[-1]))]
    table_data.insert(0, ['#', 'Implementation', 'CPython', 'Cython', 'PyPy'])

    table = RSTTable(table_data)
    table.justify_columns = {0: 'right', 1: 'left', 2: 'right', 3: 'right', 4: 'right'}
    print table.table


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Compare JSON results',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('cpython_json_file', help='Base JSON file to be compared')
    parser.add_argument('pypy_json_files', help='Other JSON files to be compared')

    args = parser.parse_args()

    compare(args.cpython_json_file, args.pypy_json_files)
