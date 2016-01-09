from .original import PascalTriangleOriginal
from .original_plus import PascalTriangleOriginalPlus
from .constant_lists import PascalTriangleConstantLists
from .constant_tuples import PascalTriangleConstantTuples


ALL_IMPLEMENTATIONS = (PascalTriangleOriginal, PascalTriangleOriginalPlus,
                       PascalTriangleConstantLists, PascalTriangleConstantTuples)
