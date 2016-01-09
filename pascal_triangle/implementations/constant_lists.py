from pascal_triangle.base import PascalTriangleBase


class PascalTriangleConstantLists(PascalTriangleBase):
    """
    Based on :py:class::`PascalTriangleOriginalPlus`.

    Improvements:
        - Constant lists replaced with named constants
    """

    def build(self, height):
        if height == 0:
            self._print(self.ONE_LIST)
            return self.ONE_LIST
        elif height < 0:
            return self.EMPTY_LIST

        prev_line = self.ZERO_LIST + self.build(height - 1) + self.ZERO_LIST
        line = [prev_line[i] + prev_line[i + 1] for i in xrange(len(prev_line) - 1)]
        self._print(line)
        return line
