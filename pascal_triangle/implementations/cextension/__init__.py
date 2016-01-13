from .initial import CPascalTriangleInitial
from .ulong import CPascalTriangleULong
from .partial_asm import CPascalTrianglePartialAsm
from .full_asm import CPascalTriangleFullAsm


CEXTENSION_IMPLEMENTATIONS = (CPascalTriangleInitial, CPascalTriangleULong,
                              CPascalTrianglePartialAsm, CPascalTriangleFullAsm)
