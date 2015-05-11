from pascal_triangle.pascal_triangle import PyPascalTriangle
from pascal_triangle.cypascal_triangle import (cy_print_pascal_triangle_iterators,
    cy_print_pascal_triangle_non_recursive_iterators,
    cy_print_pascal_triangle_non_recursive_even_more_c_like_improved,
    cy_print_pascal_triangle_non_recursive_less_c_like,
    cy_print_pascal_triangle_c_types,
    cy_print_pascal_triangle_non_recursive_even_more_c_like_improved_plus)

from pascal_triangle.cpascal_triangle import (c_print_pascal_triangle, c_print_pascal_triangle_inline_asm,
                                              c_print_pascal_triangle_full_asm_implementation)

TRI_HEIGH = 4

printer = PyPascalTriangle()
print 'print_pascal_triangle_testable_fixed_better_naming:'
printer.print_pascal_triangle_testable_fixed_better_naming(TRI_HEIGH)
print 'print_pascal_triangle_non_recursive_even_more_c_like:'
printer.print_pascal_triangle_non_recursive_even_more_c_like(TRI_HEIGH)
print 'print_pascal_triangle_non_recursive_array:'
printer.print_pascal_triangle_non_recursive_array(TRI_HEIGH)
print 'cy_print_pascal_triangle_non_recursive_iterators:'
cy_print_pascal_triangle_non_recursive_iterators(TRI_HEIGH, True)
print 'cy_print_pascal_triangle_iterators:'
cy_print_pascal_triangle_iterators(TRI_HEIGH, True)
print 'cy_print_pascal_triangle_non_recursive_even_more_c_like_improved:'
cy_print_pascal_triangle_non_recursive_even_more_c_like_improved(TRI_HEIGH, True)
print 'cy_print_pascal_triangle_non_recursive_less_c_like:'
cy_print_pascal_triangle_non_recursive_less_c_like(TRI_HEIGH, True)
print 'cy_print_pascal_triangle_c_types:'
cy_print_pascal_triangle_c_types(TRI_HEIGH, True)
print 'cy_print_pascal_triangle_non_recursive_even_more_c_like_improved_plus:'
cy_print_pascal_triangle_non_recursive_even_more_c_like_improved_plus(TRI_HEIGH, True)
print 'c_print_pascal_triangle:'
c_print_pascal_triangle(TRI_HEIGH, True)
print 'c_print_pascal_triangle_inline_asm:'
c_print_pascal_triangle_inline_asm(TRI_HEIGH, True)
print 'c_print_pascal_triangle_full_asm_implementation:'
c_print_pascal_triangle_full_asm_implementation(TRI_HEIGH, True)
