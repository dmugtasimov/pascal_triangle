from .iterators import CyPascalTriangleIterators
from .constant_lists import CyPascalTriangleConstantLists
from .non_recursive import CyPascalTriangleNonRecursive
from .non_recursive_iterators import CyPascalTriangleNonRecursiveIterators
from .non_recursive_c_like_improved import CyPascalTriangleNonRecursiveCLikeImproved
from .non_recursive_c_like_more_improved import CyPascalTriangleNonRecursiveCLikeMoreImproved
from .non_recursive_less_c_like import CyPascalTriangleNonRecursiveLessCLike
from .c_types import CyPascalTriangleNonRecursiveCTypes
from .c_types_ulong import CyPascalTriangleNonRecursiveCTypesULong


CYTHON_IMPLEMENTATIONS = (CyPascalTriangleIterators, CyPascalTriangleConstantLists,
                          CyPascalTriangleNonRecursive, CyPascalTriangleNonRecursiveIterators,
                          CyPascalTriangleNonRecursiveCLikeImproved,
                          CyPascalTriangleNonRecursiveCLikeMoreImproved,
                          CyPascalTriangleNonRecursiveLessCLike,
                          CyPascalTriangleNonRecursiveCTypes,
                          CyPascalTriangleNonRecursiveCTypesULong)
