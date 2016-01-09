import sys

from .base import CyPascalTriangleBase


class CyPascalTriangleNonRecursiveCLikeMoreImproved(CyPascalTriangleBase):
    """
    Based on :py:class::`CyPascalTriangleNonRecursiveCLikeImproved`.

    Difference:
        - List slicing replaced with character by character output
    """

    def build(self, height, verbose=False):
        line = self.ONE_LIST * (height + 1)
        start = height
        size = 0
        while size <= height:
            index = start + 1
            while index < height:
                line[index] += line[index + 1]
                index += 1

            i = start
            finish = start + size + 1
            while i < finish:
                if verbose:
                    sys.stdout.write(str(line[i]) + " ")
                i += 1
            if verbose:
                print

            start -= 1
            size += 1
        return line
