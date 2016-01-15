from .base import CPascalTriangleBase
from .culong import c_pascal_triangle_ulong


class CPascalTriangleULong(CPascalTriangleBase):
    """
    Based on :py:class::`CPascalTriangleInitial`.

    Difference:
        - Unsigned long is used instead of unsigned int
    """

    def build(self, height):
        return c_pascal_triangle_ulong(height, 0, self.return_list)
