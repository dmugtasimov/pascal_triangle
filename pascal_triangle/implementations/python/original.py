from .base import PyPascalTriangleBase


class PyPascalTriangleOriginal(PyPascalTriangleBase):
    """
    Modified original solution presented on interview.
    """

    original = True
    max_height = 900

    def build(self, height):
        if height <= 0:
            self._print([1])
            return [1]

        a = [0] + self.build(height - 1) + [0]
        b = [a[i] + a[i + 1] for i in xrange(len(a) - 1)]
        self._print(b)
        return b  # return last line for testing purposes
