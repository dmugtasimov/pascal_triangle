#!/usr/bin/env bash

set -x

gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -D_FORTIFY_SOURCE=2 -g -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security -o ccpascal_triangle_normal ./pascal_triangle/ccpascal_triangle.c
chmod a+x ./ccpascal_triangle_normal

gcc -O2 -o ccpascal_triangle_O2 ./pascal_triangle/ccpascal_triangle.c
chmod a+x ./ccpascal_triangle_O2

gcc -O3 -o ccpascal_triangle_O3 ./pascal_triangle/ccpascal_triangle.c
chmod a+x ./ccpascal_triangle_O3

gcc -Ofast -o ccpascal_triangle_Ofast ./pascal_triangle/ccpascal_triangle.c
chmod a+x ./ccpascal_triangle_Ofast
