import sys
import itertools
import collections

ZERO_LIST = [0]
ONE_LIST = [1]


def cy_print_pascal_triangle_iterators(height):
    if height == 1:
        # print ONE_LIST
        return ONE_LIST
    elif height < 1:
        return []

    prev_line = cy_print_pascal_triangle_iterators(height - 1)
    iterator = itertools.chain(ZERO_LIST, prev_line)
    ahead_iterator = itertools.chain(prev_line, ZERO_LIST)
    line = [x + y for x, y in itertools.izip(iterator, ahead_iterator)]
    # print line
    return line


def cy_print_pascal_triangle_non_recursive_iterators(height):
    line = ONE_LIST
    # print line
    for _ in xrange(height - 1):
        iterator = itertools.chain(ZERO_LIST, line)
        ahead_iterator = itertools.chain(line, ZERO_LIST)
        line = [x + y for x, y in itertools.izip(iterator, ahead_iterator)]
        # print line


def cy_print_pascal_triangle_non_recursive_even_more_c_like_improved(height):
    line = ONE_LIST * height + ZERO_LIST
    start = height - 1
    size = 1
    while size <= height:
        index = start + 1
        while index < height:
            line[index] += line[index + 1]
            index += 1
        print_line = line[start:start + size]
        # print print_line
        start -= 1
        size += 1

def cy_print_pascal_triangle_non_recursive_less_c_like(height):
    line = ONE_LIST * height + ZERO_LIST
    start = height - 1
    for size in xrange(1, height + 1):
        for index in xrange(start + 1, height):
            line[index] += line[index + 1]
        print_line = line[start:start + size]
        # print print_line
        start -= 1


def cy_print_pascal_triangle_c_types(height):
    cdef line = ONE_LIST * height + ZERO_LIST
    cdef int start = height - 1
    cdef int size = 1
    cdef int index
    cdef int i
    cdef int finish
    while size <= height:
        index = start + 1
        while index < height:
            line[index] += line[index + 1]
            index += 1

        i = start
        finish = start + size
        while i < finish:
            # sys.stdout.write(str(line[i]))
            i += 1
        # print

        start -= 1
        size += 1

def cy_print_pascal_triangle_non_recursive_even_more_c_like_improved_plus(height):
    line = ONE_LIST * height + ZERO_LIST
    start = height - 1
    size = 1
    while size <= height:
        index = start + 1
        while index < height:
            line[index] += line[index + 1]
            index += 1

        i = start
        finish = start + size
        while i < finish:
            # sys.stdout.write(str(line[i]))
            i += 1
        # print

        start -= 1
        size += 1
