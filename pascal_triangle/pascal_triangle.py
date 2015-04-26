import itertools
import collections


def print_pascal_triangle_initial(n):
    """
    Print Pascal's Triangle of height n: initial interview solution.
    :param n: height of the triangle to print
    :return: n-th line of Pascal's Triangle
    """
    if n <= 1:
        print [1]
        return [1]

    a = [0] + print_pascal_triangle_initial(n - 1) + [0]
    b = [a[i] + a[i + 1] for i in xrange(len(a) - 1)]
    print b
    return b


class PascalTriangleTestable(object):

    ZERO_LIST = [0]
    ONE_LIST = [1]

    def _print(self, arg):
        """
        Print Pascal'S Triangle line
        :param arg: triangle line
        """
        print arg

    def print_pascal_triangle_initial(self, n):
        """
        Print Pascal's Triangle of height n: more testable interview solution.
        :param n: height of the triangle to print
        :return: n-th line of Pascal's Triangle
        """
        if n <= 1:
            self._print([1])
            return [1]

        a = [0] + self.print_pascal_triangle_initial(n - 1) + [0]
        b = [a[i] + a[i + 1] for i in xrange(len(a) - 1)]
        self._print(b)
        return b

    def print_pascal_triangle_initial_fixed(self, n):
        """
        Print Pascal's Triangle of height n: more testable interview solution with corner case bug fix.
        :param n: height of the triangle to print
        :return: n-th line of Pascal's Triangle
        """
        if n == 1:
            self._print([1])
            return [1]
        elif n < 1:
            return []

        a = [0] + self.print_pascal_triangle_initial(n - 1) + [0]
        b = [a[i] + a[i + 1] for i in xrange(len(a) - 1)]
        self._print(b)
        return b

    def print_pascal_triangle_better_naming(self, height):
        """
        Print Pascal's Triangle of height n: more testable interview solution with better variable naming.
        :param height: height of the triangle to print
        :return: n-th line of Pascal's Triangle
        """
        if height == 1:
            self._print([1])
            return [1]
        elif height < 1:
            return []

        pre_line = [0] + self.print_pascal_triangle_initial(height - 1) + [0]
        line = [pre_line[i] + pre_line[i + 1] for i in xrange(len(pre_line) - 1)]
        self._print(line)
        return line

    def print_pascal_triangle_constant_lists(self, height):
        """
        Print Pascal's Triangle of height n: with constant lists.
        :param height: height of the triangle to print
        :return: n-th line of Pascal's Triangle
        """
        if height == 1:
            self._print(self.ONE_LIST)
            return self.ONE_LIST
        elif height < 1:
            return []

        pre_line = self.ZERO_LIST + self.print_pascal_triangle_initial(height - 1) + self.ZERO_LIST
        line = [pre_line[i] + pre_line[i + 1] for i in xrange(len(pre_line) - 1)]
        self._print(line)
        return line



ZERO_LIST = [0]
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
