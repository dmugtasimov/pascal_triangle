from pascal_triangle.base import PascalTriangleBase


class PascalTriangleNonRecursive(PascalTriangleBase):
    """
    A non recursive implementation of Pascal Triangle printing algorithm.
    """

    def build(self, height):
        line = []
        for x in xrange(height + 1):
            line = self.ONE_LIST + line
            for i in xrange(1, x):
                line[i] += line[i + 1]
            self._print(line)

        return line
