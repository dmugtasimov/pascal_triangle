Install::

    pip install -e .

Build pure C solution::

    gcc -fPIC -pthread -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -D_FORTIFY_SOURCE=2 -g -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security -o ccpascal_triangle ccpascal_triangle.c

Run unit tests::

    python -m unittest -v pascal_triangle.tests.test_pascal_triangle

Run functional manual tests (check expected results manually)::

    python -m pascal_triangle.tests.functional_manual_test

Run performance tests::

    python -m pascal_triangle.tests.performance_test

Run pure C solution::

    ./ccpascal_triangle
