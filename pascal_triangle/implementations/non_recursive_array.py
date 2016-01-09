import itertools
import array

from pascal_triangle.base import PascalTriangleBase


class PascalTriangleNonRecursiveArray(PascalTriangleBase):
    """
    Based on :py:class::`PascalTriangleNonRecursiveLessCLike`.

    Difference:
        - array object are used instead of list
    """

    def build(self, height):
        line = array.array('I', itertools.repeat(1, height + 1))
        start = height
        for size in xrange(height + 1):
            for index in xrange(start + 1, height):
                line[index] += line[index + 1]
            print_line = line[start:]
            self._print(print_line)
            start -= 1

        return line  # return last line for testing purposes
