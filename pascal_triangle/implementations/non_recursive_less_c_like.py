from pascal_triangle.base import PascalTriangleBase


class PascalTriangleNonRecursiveLessCLike(PascalTriangleBase):
    """
    Based on :py:class::`PascalTriangleNonRecursiveCLike`.

    Difference:
        - xrange objects are used
    """

    def build(self, height):
        line = self.ONE_LIST * (height + 1)
        start = height
        for size in xrange(height + 1):
            for index in xrange(start + 1, height):
                line[index] += line[index + 1]
            print_line = line[start:]
            self._print(print_line)
            start -= 1

        return line
