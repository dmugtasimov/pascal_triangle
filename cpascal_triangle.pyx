import collections

ZERO_LIST = [0]
ONE_LIST = [1]


def cprint_pascal_triangle_v1(height):
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


def cprint_pascal_triangle_v2(height):
    if height <= 1:
        #print ONE_LIST
        return ONE_LIST

    prev_line = ZERO_LIST + cprint_pascal_triangle_v2(height - 1) + ZERO_LIST
    line = [prev_line[i] + prev_line[i + 1] for i in xrange(len(prev_line) - 1)]
    #print line
    return line
