Install::

    pip install Cython
    pip install -e .

Build pure C solution::

    # With ~ the same options as setup.py does
    gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -D_FORTIFY_SOURCE=2 -g -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security -o ccpascal_triangle ccpascal_triangle.c
    # With moderate optimization
    gcc -O2 -o ccpascal_triangle ccpascal_triangle.c
    # Set execution bit
    chmod a+x ./ccpascal_triangle

Run unit tests::

    python -m unittest -v pascal_triangle.tests.test_pascal_triangle

Run functional manual tests (check expected results manually)::

    python -m pascal_triangle.tests.functional_manual_test

Set constant CPU frequency::

    sudo cpufreq-set -c 0 -g performance
    sudo cpufreq-set -c 1 -g performance
    ...
    sudo cpufreq-set -c n -g performance

Run performance tests::

    python -m pascal_triangle.tests.performance_test

Run pure C solution::

    ./ccpascal_triangle

See gcc compilation options::

    import distutils.sysconfig
    import distutils.ccompiler
    compiler = distutils.ccompiler.new_compiler()
    distutils.sysconfig.customize_compiler(compiler)
    print 'preprocessor:', compiler.preprocessor
    print 'compiler:', compiler.compiler
    print 'compiler_so:', compiler.compiler_so
    print 'compiler_cxx:', compiler.compiler_cxx
    print 'linker_so:', compiler.linker_so
    print 'linker_exe:', compiler.linker_exe
    print 'archiver:', compiler.archiver
