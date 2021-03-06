import sys

import itertools
from array import array
from cpython cimport array as c_array

from .base import CyPascalTriangleBase


class CyPascalTriangleNonRecursiveCTypes(CyPascalTriangleBase):
    """
    Based on :py:class::`PyPascalTriangleNonRecursiveArray`.

    Difference:
        - Compiled with Cython
        - C type are used instead of Python types
    """

    max_height = 34

    def build(self, height, verbose=False):
        cdef c_array.array line = array('I', itertools.repeat(1, height + 1))
        cdef int start = height
        cdef int size = 0
        cdef int index
        cdef int i
        cdef int finish
        while size <= height:
            index = start + 1
            while index < height:
                line[index] += line[index + 1]
                index += 1

            i = start
            finish = start + size + 1
            while i < finish:
                if verbose:
                    sys.stdout.write(str(line[i]) + ' ')
                i += 1
            if verbose:
                print

            start -= 1
            size += 1
        return line  # return last line for testing purposes
