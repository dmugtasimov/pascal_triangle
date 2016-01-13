from .base import CPascalTriangleBase
from .cinitial import c_pascal_triangle_initial


class CPascalTriangleInitial(CPascalTriangleBase):
    """
    Based on :py:class::`CyPascalTriangleNonRecursiveCTypes`.

    Difference:
        - C implementation
    """

    def build(self, height):
        c_pascal_triangle_initial(height)
