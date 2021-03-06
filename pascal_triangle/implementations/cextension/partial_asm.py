from .base import CPascalTriangleBase
from .cpartial_asm import c_pascal_triangle_partial_asm


class CPascalTrianglePartialAsm(CPascalTriangleBase):
    """
    Based on :py:class::`CPascalTriangleInitial`.

    Difference:
        - Array initialization is implemented in Assembler
    """

    language = 'C/Assembler'
    max_height = 34

    def build(self, height):
        return c_pascal_triangle_partial_asm(height, 0, self.return_list)
