from .original import PascalTriangleOriginal
from .original_plus import PascalTriangleOriginalPlus
from .constant_lists import PascalTriangleConstantLists
from .constant_tuples import PascalTriangleConstantTuples
from .iterators import PascalTriangleIterators
from .non_recursive import PascalTriangleNonRecursive
from .non_recursive_c_like import PascalTriangleNonRecursiveCLike
from .non_recursive_c_like_improved import PascalTriangleNonRecursiveCLikeImproved
from .non_recursive_less_c_like import PascalTriangleNonRecursiveLessCLike
from .non_recursive_array import PascalTriangleNonRecursiveArray
from .non_recursive_iterators import PascalTriangleNonRecursiveIterators


ALL_IMPLEMENTATIONS = (PascalTriangleOriginal, PascalTriangleOriginalPlus,
                       PascalTriangleConstantLists, PascalTriangleConstantTuples,
                       PascalTriangleIterators, PascalTriangleNonRecursive,
                       PascalTriangleNonRecursiveCLike, PascalTriangleNonRecursiveCLikeImproved,
                       PascalTriangleNonRecursiveLessCLike, PascalTriangleNonRecursiveArray,
                       PascalTriangleNonRecursiveIterators)
