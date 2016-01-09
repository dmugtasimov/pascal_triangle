from .base import PyPascalTriangleBase


class PyPascalTriangleNonRecursiveCLikeImproved(PyPascalTriangleBase):
    """
    Based on :py:class::`PascalTriangleNonRecursiveCLike`.

    Difference:
        - Removed some unneeded computations
    """

    def build(self, height):
        line = self.ONE_LIST * (height + 1)
        start = height
        size = 0
        while size <= height:
            index = start + 1
            while index < height:
                line[index] += line[index + 1]
                index += 1
            print_line = line[start:start + size + 1]
            self._print(print_line)
            start -= 1
            size += 1

        return line
