import itertools

from pascal_triangle.base import PascalTriangleBase


class PascalTriangleIterators(PascalTriangleBase):
    """
    Based on :py:class::`PascalTriangleConstantLists`.

    Difference:
        - Iterators are used instead of lists where it is possible
    """

    def build(self, height):
        if height == 0:
            self._print(self.ONE_LIST)
            return self.ONE_LIST
        elif height < 0:
            return self.EMPTY_LIST

        prev_line = self.build(height - 1)
        iterator = itertools.chain(self.ZERO_LIST, prev_line)
        ahead_iterator = itertools.chain(prev_line, self.ZERO_LIST)
        line = [x + y for x, y in itertools.izip(iterator, ahead_iterator)]
        self._print(line)
        return line
