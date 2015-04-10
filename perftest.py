import timeit

from pascal_triangle import (print_pascal_triangle, print_pascal_triangle_v2,
                             print_pascal_triangle_v3, print_pascal_triangle_v4,
                             print_pascal_triangle_v5, print_pascal_triangle_v6,
                             print_pascal_triangle_v7, print_pascal_triangle_v8,
                             print_pascal_triangle_v9, print_pascal_triangle_v10)
from cypascal_triangle import (cyprint_pascal_triangle_v1, cyprint_pascal_triangle_v2,
                               cyprint_pascal_triangle_v3)
from cpascal_triangle import (cprint_pascal_triangle_v1, casmprint_pascal_triangle_v2,
                              casmprint_pascal_triangle_v3)


FUNCS = (
    print_pascal_triangle,
    print_pascal_triangle_v2,
    print_pascal_triangle_v3,
    print_pascal_triangle_v4,
    print_pascal_triangle_v5,
    print_pascal_triangle_v6,
    print_pascal_triangle_v7,
    print_pascal_triangle_v8,
    print_pascal_triangle_v9,
    print_pascal_triangle_v10,
    cyprint_pascal_triangle_v1,
    cyprint_pascal_triangle_v2,
    cyprint_pascal_triangle_v3,
    cprint_pascal_triangle_v1,
    casmprint_pascal_triangle_v2,
    casmprint_pascal_triangle_v3,
)

CYCLES = 10000
HEIGHT = 20
for func in (f.__name__ for f in FUNCS):
    print '%s(%s) done for %s times in %s seconds' % (func, HEIGHT, CYCLES,
            timeit.timeit('%s(%s)' % (func, HEIGHT), setup='from __main__ import %s' % func,
                          number=CYCLES))
