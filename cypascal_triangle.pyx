import collections

ZERO_LIST = [0]
ONE_LIST = [1]


def cprint_pascal_triangle_v1(height):
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


def cprint_pascal_triangle_v2(height):
    if height <= 1:
        #print ONE_LIST
        return ONE_LIST

    prev_line = ZERO_LIST + cprint_pascal_triangle_v2(height - 1) + ZERO_LIST
    line = [prev_line[i] + prev_line[i + 1] for i in xrange(len(prev_line) - 1)]
    #print line
    return line


def cprint_pascal_triangle_v3(int height):
    if height > 200:
        raise ValueError('height may not be greater than 200')
    cdef int line[200]
    cdef int start
    cdef size
    cdef int i

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
