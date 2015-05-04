import itertools
import collections

from .cypascal_triangle import (cy_print_pascal_triangle_iterators,
    cy_print_pascal_triangle_non_recursive_iterators,
    cy_print_pascal_triangle_non_recursive_even_more_c_like_improved,
    cy_print_pascal_triangle_non_recursive_less_c_like,
    cy_print_pascal_triangle_c_types, cy_print_pascal_triangle_c_types_ulong,
    cy_print_pascal_triangle_non_recursive_even_more_c_like_improved_plus)
from .cpascal_triangle import (c_print_pascal_triangle, c_print_pascal_triangle_ulong,
                               c_print_pascal_triangle_inline_asm,
                               c_print_pascal_triangle_full_asm_implementation)


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


class PyPascalTriangle(object):

    ZERO_LIST = [0]
    ONE_LIST = [1]
    ZERO_TUPLE = (0,)
    ONE_TUPLE = (1,)

    def _print(self, arg):
        """
        Print Pascal'S Triangle line
        :param arg: triangle line
        """
        print arg

    def print_pascal_triangle_testable_fixed_better_naming(self, height):
        """
        Print Pascal's Triangle of `height`: testable, fixed, corner case, better variable naming.
        :param height: height of the triangle to print
        :return: n-th line of Pascal's Triangle
        """
        if height == 1:
            self._print([1])
            return [1]
        elif height < 1:
            return []

        prev_line = [0] + self.print_pascal_triangle_testable_fixed_better_naming(height - 1) + [0]
        line = [prev_line[i] + prev_line[i + 1] for i in xrange(len(prev_line) - 1)]
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

        prev_line = self.ZERO_LIST + self.print_pascal_triangle_constant_lists(height - 1) + self.ZERO_LIST
        line = [prev_line[i] + prev_line[i + 1] for i in xrange(len(prev_line) - 1)]
        self._print(line)
        return line

    def print_pascal_triangle_tuples(self, height):
        """
        Print Pascal's Triangle of height n: using tuples.
        :param height: height of the triangle to print
        :return: n-th line of Pascal's Triangle
        """
        if height == 1:
            self._print(list(self.ONE_TUPLE))
            return self.ONE_TUPLE
        elif height < 1:
            return ()

        prev_line = self.ZERO_TUPLE + self.print_pascal_triangle_tuples(height - 1) + self.ZERO_TUPLE
        line = tuple(prev_line[i] + prev_line[i + 1] for i in xrange(len(prev_line) - 1))
        self._print(list(line))
        return line

    def print_pascal_triangle_iterators(self, height):
        """
        Print Pascal's Triangle of height n: using iterators.
        :param height: height of the triangle to print
        :return: n-th line of Pascal's Triangle
        """
        if height == 1:
            self._print(self.ONE_LIST)
            return self.ONE_LIST
        elif height < 1:
            return []

        prev_line = self.print_pascal_triangle_iterators(height - 1)
        iterator = itertools.chain(self.ZERO_LIST, prev_line)
        ahead_iterator = itertools.chain(prev_line, self.ZERO_LIST)
        line = [x + y for x, y in itertools.izip(iterator, ahead_iterator)]
        self._print(line)
        return line

    def print_pascal_triangle_non_recursive(self, height):
        """
        Print Pascal's Triangle of height n: non-recursive.
        :param height: height of the triangle to print
        """
        line = []
        for x in xrange(height):
            line = self.ONE_LIST + line
            for i in xrange(1, len(line)):
                try:
                    line[i] += line[i + 1]
                except IndexError:
                    pass
            self._print(line)

    def print_pascal_triangle_non_recursive_deque(self, height):
        """
        Print Pascal's Triangle of height n: non-recursive deque.
        :param height: height of the triangle to print
        """
        line = collections.deque()
        for x in xrange(height):
            line.appendleft(1)
            for i in xrange(1, len(line)):
                try:
                    line[i] += line[i + 1]
                except IndexError:
                    pass
            self._print(list(line))

    def print_pascal_triangle_non_recursive_deque_c_like(self, height):
        """
        Print Pascal's Triangle of height n: non-recursive deque c-like style.
        :param height: height of the triangle to print
        """

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
            self._print(list(line))
            x += 1

    def print_pascal_triangle_non_recursive_even_more_c_like(self, height):
        """
        Print Pascal's Triangle of height n: non-recursive even more c-like style.
        :param height: height of the triangle to print
        """

        line = self.ZERO_LIST * height
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
            print_line = line[start:start + size]
            self._print(print_line)
            start -= 1
            size += 1

    def print_pascal_triangle_non_recursive_even_more_c_like_improved(self, height):
        """
        Print Pascal's Triangle of height n: non-recursive even more c-like style, improved.
        :param height: height of the triangle to print
        """

        line = self.ONE_LIST * height + self.ZERO_LIST
        start = height - 1
        size = 1
        while size <= height:
            index = start + 1
            while index < height:
                line[index] += line[index + 1]
                index += 1
            print_line = line[start:start + size]
            self._print(print_line)
            start -= 1
            size += 1

    def print_pascal_triangle_non_recursive_less_c_like(self, height):
        """
        Print Pascal's Triangle of height n: non-recursive less c-like style.
        :param height: height of the triangle to print
        """

        line = self.ONE_LIST * height + self.ZERO_LIST
        start = height - 1
        for size in xrange(1, height + 1):
            for index in xrange(start + 1, height):
                line[index] += line[index + 1]
            print_line = line[start:start + size]
            self._print(print_line)
            start -= 1

    def print_pascal_triangle_non_recursive_iterators(self, height):
        """
        Print Pascal's Triangle of height n: using iterators, non-recursive.
        :param height: height of the triangle to print
        """

        line = self.ONE_LIST
        self._print(line)
        for _ in xrange(height - 1):
            iterator = itertools.chain(self.ZERO_LIST, line)
            ahead_iterator = itertools.chain(line, self.ZERO_LIST)
            line = [x + y for x, y in itertools.izip(iterator, ahead_iterator)]
            self._print(line)


class CyPascalTriangle(object):

    def print_pascal_triangle_iterators(self, height):
        return cy_print_pascal_triangle_iterators(height)

    def print_pascal_triangle_non_recursive_iterators(self, height):
        cy_print_pascal_triangle_non_recursive_iterators(height)

    def print_pascal_triangle_non_recursive_even_more_c_like_improved(self, height):
        cy_print_pascal_triangle_non_recursive_even_more_c_like_improved(height)

    def print_pascal_triangle_non_recursive_less_c_like(self, height):
        cy_print_pascal_triangle_non_recursive_less_c_like(height)

    def print_pascal_triangle_c_types(self, height):
        cy_print_pascal_triangle_c_types(height)

    def print_pascal_triangle_c_types_ulong(self, height):
        cy_print_pascal_triangle_c_types_ulong(height)

    def print_pascal_triangle_non_recursive_even_more_c_like_improved_plus(self, height):
        cy_print_pascal_triangle_non_recursive_even_more_c_like_improved_plus(height)


class CPascalTriangle(object):

    def print_pascal_triangle(self, height):
        c_print_pascal_triangle(height)

    def print_pascal_triangle_ulong(self, height):
        c_print_pascal_triangle_ulong(height)

    def print_pascal_triangle_inline_asm(self, height):
        c_print_pascal_triangle_inline_asm(height)

    def print_pascal_triangle_full_asm_implementation(self, height):
        c_print_pascal_triangle_full_asm_implementation(height)
