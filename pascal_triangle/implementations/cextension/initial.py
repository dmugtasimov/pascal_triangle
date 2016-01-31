from .base import CPascalTriangleBase
from .cinitial import c_pascal_triangle_initial


class CPascalTriangleInitial(CPascalTriangleBase):
    """
    Based on :py:class::`CyPascalTriangleNonRecursiveCTypes`.

    Difference:
        - C implementation
    """

    max_height = 34

    def build(self, height):
        return c_pascal_triangle_initial(height, 0, self.return_list)
