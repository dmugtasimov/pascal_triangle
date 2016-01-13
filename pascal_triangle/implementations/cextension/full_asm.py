from .base import CPascalTriangleBase
from .cfull_asm import c_pascal_triangle_full_asm


class CPascalTriangleFullAsm(CPascalTriangleBase):
    """
    Based on :py:class::`CPascalTrianglePartialAsm`.

    Difference:
        - The algorithm is implemented in Assembler completely
    """

    language = 'C/Assembler'

    def build(self, height):
        c_pascal_triangle_full_asm(height)
