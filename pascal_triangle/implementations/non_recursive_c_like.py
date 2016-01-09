from pascal_triangle.base import PascalTriangleBase


class PascalTriangleNonRecursiveCLike(PascalTriangleBase):
    """
    Based on :py:class::`PascalTriangleNonRecursive`.

    Difference:
        - All required memory is allocated at once
        - List concatenations are replaced with value assignment by index
    """

    def build(self, height):
        line = self.ZERO_LIST * (height + 1)
        start = height
        size = 0
        while size <= height:
            line[start] = 1
            i = 1
            while i < size:
                index = start + i
                line[index] += line[index + 1]
                i += 1
            print_line = line[start:start + size + 1]
            self._print(print_line)
            start -= 1
            size += 1

        return line
