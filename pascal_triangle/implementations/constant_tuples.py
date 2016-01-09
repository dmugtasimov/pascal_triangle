from pascal_triangle.base import PascalTriangleBase


class PascalTriangleConstantTuples(PascalTriangleBase):
    """
    Based on :py:class::`PascalTriangleConstantLists`.

    Improvements:
        - Lists replaced with tuples
    """

    def build(self, height):
        if height == 0:
            self._print(self.ONE_TUPLE)
            return self.ONE_TUPLE
        elif height < 0:
            return self.EMPTY_TUPLE

        prev_line = self.ZERO_TUPLE + self.build(height - 1) + self.ZERO_TUPLE
        line = tuple(prev_line[i] + prev_line[i + 1] for i in xrange(len(prev_line) - 1))
        self._print(line)
        return line
