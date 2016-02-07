from .base import PyPascalTriangleBase


class PyPascalTriangleNonRecursiveLessCLike(PyPascalTriangleBase):
    """
    Based on :py:class::`PascalTriangleNonRecursiveCLike`.

    Difference:
        - xrange objects are used instead of while-loops
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

        return line  # return last line for testing purposes
