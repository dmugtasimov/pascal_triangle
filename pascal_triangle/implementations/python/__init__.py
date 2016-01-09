from .original import PyPascalTriangleOriginal
from .original_plus import PyPascalTriangleOriginalPlus
from .constant_lists import PyPascalTriangleConstantLists
from .constant_tuples import PyPascalTriangleConstantTuples
from .iterators import PyPascalTriangleIterators
from .non_recursive import PyPascalTriangleNonRecursive
from .non_recursive_c_like import PyPascalTriangleNonRecursiveCLike
from .non_recursive_c_like_improved import PyPascalTriangleNonRecursiveCLikeImproved
from .non_recursive_less_c_like import PyPascalTriangleNonRecursiveLessCLike
from .non_recursive_array import PyPascalTriangleNonRecursiveArray
from .non_recursive_iterators import PyPascalTriangleNonRecursiveIterators


PYTHON_IMPLEMENTATIONS = (PyPascalTriangleOriginal, PyPascalTriangleOriginalPlus,
                          PyPascalTriangleConstantLists, PyPascalTriangleConstantTuples,
                          PyPascalTriangleIterators, PyPascalTriangleNonRecursive,
                          PyPascalTriangleNonRecursiveCLike,
                          PyPascalTriangleNonRecursiveCLikeImproved,
                          PyPascalTriangleNonRecursiveLessCLike, PyPascalTriangleNonRecursiveArray,
                          PyPascalTriangleNonRecursiveIterators)
