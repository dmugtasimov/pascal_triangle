import itertools
import collections


def print_pascal_triangle(n):
    if n <= 1:
        #print [1]
        return [1]

    a = [0] + print_pascal_triangle(n - 1) + [0]
    b = [a[i] + a[i + 1] for i in xrange(len(a) - 1)]
    #print b
    return b


ZERO_LIST = [0]


def print_pascal_triangle_v2(n):
    if n <= 1:
        #print [1]
        return [1]

    a = ZERO_LIST + print_pascal_triangle_v2(n - 1) + ZERO_LIST
    b = [a[i] + a[i + 1] for i in xrange(len(a) - 1)]
    #print b
    return b


ZERO_TUPLE = (0,)


def print_pascal_triangle_v3(n):
    if n <= 1:
        #print (1,)
        return (1,)

    a = ZERO_TUPLE + print_pascal_triangle_v3(n - 1) + ZERO_TUPLE
    b = tuple(a[i] + a[i + 1] for i in xrange(len(a) - 1))
    #print b
    return b


def print_pascal_triangle_v4(n):
    if n <= 1:
        #print [1]
        return [1]

    a = ZERO_LIST + print_pascal_triangle_v4(n - 1) + ZERO_LIST
    ahead_iterator = iter(a)
    ahead_iterator.next()
    b = [x + ahead_iterator.next() for x in a[:-1]]
    #print b
    return b


ONE_LIST = [1]


def print_pascal_triangle_v5(height):
    if height <= 1:
        line = ONE_LIST
    else:
        prev_line = print_pascal_triangle_v5(height - 1)
        normal_iterator = itertools.chain(ZERO_LIST, prev_line)
        ahead_iterator = itertools.chain(prev_line, ZERO_LIST)
        line = [x + ahead_iterator.next() for x in normal_iterator]

    #print line
    return line


def print_pascal_triangle_v6(height):
    line = []
    for x in xrange(height):
        line = [1] + line
        for i in xrange(1, len(line)):
            try:
                line[i] += line[i + 1]
            except IndexError:
                pass
        #print line


def print_pascal_triangle_v7(height):
    line = collections.deque()
    for x in xrange(height):
        line.appendleft(1)
        for i in xrange(1, len(line)):
            try:
                line[i] += line[i + 1]
            except IndexError:
                pass
        #print line


#@profile
def print_pascal_triangle_v8(height):
    line = collections.deque()
    x = 0
    while x < height:
        line.appendleft(1)
        i = 1
        while i <= x:
            try:
                line[i] += line[i + 1]
            except IndexError:
                pass
            i += 1
        #print line
        x += 1


#@profile
def print_pascal_triangle_v9(height):
    if height <= 1:
        #print ONE_LIST
        return ONE_LIST

    prev_line = ZERO_LIST + print_pascal_triangle_v9(height - 1) + ZERO_LIST
    line = [prev_line[i] + prev_line[i + 1] for i in xrange(len(prev_line) - 1)]
    #print line
    return line


#@profile
def print_pascal_triangle_v10(height):
    line = [0] * height
    start = height - 1
    size = 1
    while size <= height:
        line[start] = 1
        i = 1
        while i < size:
            index = start + i
            try:
                line[index] += line[index + 1]
            except IndexError:
                pass
            i += 1
        #print line[start:start + size]
        start -= 1
        size += 1
