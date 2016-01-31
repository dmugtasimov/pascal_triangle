from .base import PyPascalTriangleBase


class PyPascalTriangleOriginalPlus(PyPascalTriangleBase):
    """
    Based on :py:class::`PascalTriangleOriginal`.

    Difference:
        - Better naming of local variables
        - Fixed corner cases
    """

    max_height = 900

    def build(self, height):
        if height == 0:
            self._print([1])
            return [1]
        elif height < 0:
            return []

        prev_line = [0] + self.build(height - 1) + [0]
        line = [prev_line[i] + prev_line[i + 1] for i in xrange(len(prev_line) - 1)]
        self._print(line)
        return line
