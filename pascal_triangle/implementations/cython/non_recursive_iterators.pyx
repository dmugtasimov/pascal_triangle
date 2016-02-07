import itertools

from .base import CyPascalTriangleBase


class CyPascalTriangleNonRecursiveIterators(CyPascalTriangleBase):
    """
    Based on :py:class::`PyPascalTriangleNonRecursiveIterators`.

    Difference:
        - Compiled with Cython
    """

    def build(self, height):
        if height < 0:
            return self.EMPTY_LIST

        line = self.ONE_LIST
        self._print(line)
        for _ in xrange(height):
            iterator = itertools.chain(self.ZERO_LIST, line)
            ahead_iterator = itertools.chain(line, self.ZERO_LIST)
            line = [x + y for x, y in itertools.izip(iterator, ahead_iterator)]
            self._print(line)

        return line  # return last line for testing purposes
