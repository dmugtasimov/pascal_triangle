from .base import CyPascalTriangleBase


class CyPascalTriangleNonRecursive(CyPascalTriangleBase):
    """
    Based on :py:class::`PyPascalTriangleNonRecursive`.

    Difference:
        - Compiled with Cython
    """

    def build(self, height):
        line = []
        for x in xrange(height + 1):
            line = self.ONE_LIST + line
            for i in xrange(1, x):
                line[i] += line[i + 1]
            self._print(line)

        return line
