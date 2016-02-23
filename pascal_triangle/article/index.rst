.. Pascal's Triangle documentation master file, created by
   sphinx-quickstart on Sat Jan 23 00:27:52 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pascal's Triangle
=================

.. toctree::
   :hidden:

   limitation_test
   cpython_performance_test_34
   cpython_performance_test_67
   cpython_performance_test_900
   cpython_performance_test_3000
   pypy_performance_test_34
   pypy_performance_test_67
   pypy_performance_test_900
   pypy_performance_test_3000
   cpython_vs_cython_vs_pypy

Summary
-------

This article is about `Pascal's Triangle <http://en.wikipedia.org/wiki/Pascal%27s_triangle>`_
building algorithm implementations, their performance and limitations analysis. The article shows
some techniques for performance optimization that can be used for solving real life software
optimization problems.

Programming languages:

- Python (CPython and PyPy implementations)
- Cython
- C
- Assembler

Optimization techniques used:

- Microoptimizations
- Replace recursive algorithm with non-recursive
- Replace Python with other programming languages

Conclusions
-----------

- It is possible to improve performance for more than 200 times if you are ready to switch from CPython to C or Assembler
- You probably should not try to implement your algorithm in Assembler for better performance unless you are as proficient in Assembler as a C-compiler developer, otherwise just use compiler optimization options
- It was possible to improve CPython implementation by 40% by switching to non-recursive implementation and other language specific optimizations
- It is possible to improve performance by 20-50% by switching to Cython with no changes to source code
- It is possible to improve performance for 2-7 times by switching to PyPy with no changes to source code
- As expected from fastest to slowest: Assembler and C, PyPy, Cython, CPython
- You should always check if your performance optimization leads to improvement, because sometime unexpectedly they lead to performance degradation
- Faster implementations may have limitations that make them impractical. For example `CPascalTriangleFullAsm`_ has the best time performance, but limited to 34 height. Therefore it is more practical to cache or precalculate Pascal's Triangle of this height and return result from memory which would would run even faster than the Assembler implementation.

Implementation Notes
--------------------

- Complete source code can be found in `pascal_triangle <https://github.com/dmugtasimov/pascal_triangle>`_ github repository
- This article is automatically generated with `Sphinx <http://www.sphinx-doc.org/>`_
- Metaclasses are used for unit-testing variety of solutions of the same problem
- Specific property of Pascal's Triangle is used to test the solutions: sum of line's integers is equal to 2 to the power of line number
- cythonize() tries to compile \*.pyx files before Cython is installed according to setup_requires argument of setup(), so there is a need to have a LazyList() as work around
- Cython is incompatible with PyPy, so there is a need to check for python implementation being used
- It is important to set constant CPU frequency to get stable benchmark results

Full story
----------

The basic definition of Pascal's Triangle is the following:

*Pascal’s Triangle is a triangle formed of lines of integer numbers.
Each line has one more integer than the previous line and centered
with the previous line. First line has only one integer with value of 1.
Every integer in each line is a sum of two above integers.*

Example::

         1
       1   1
      1  2  1
     1 3   3 1
    1 4  6  4 1
   1 5 10 10 5 1

For more strict mathematical definition, please, see `Pascal’s Triangle <http://en.wikipedia.org/wiki/Pascal%27s_triangle>`_
wikipedia article.

Here is the code that I produced on a job interview when I was asked to code a program in Python
that prints Pascal's Triangle:

.. literalinclude:: ../implementations/original.py

For the purpose of this article I made small changes to my original implementation
(zero-based lines and function is converted to a class method):

.. literalinclude:: ../implementations/python/original.py

Limitations
~~~~~~~~~~~

When I started implementation of the Pascal's Triangle building algorithm it turned out that
different implementations have their own limitations. Therefore limitations should be described
first.

Here is the result of limitation test::

    $ python -m pascal_triangle.tests.limitation_test

.. include:: limitation_test.rst

As seen from the table there are several thresholds of triangle height limitation:

* 34 is a height limit for all algorithms that use unsigned 32-bit integers to store resulting lines.
* 67 is a height limit for all algorithms that use unsigned 64-bit integers to store resulting lines.
* A just below 1000 height limit is valid for all recursive algorithms in Python since the default recursion limit in python is 1000 frames.
* The other implementations are virtually limited by the time required for calculation (1 second).

From practical point of view limit of 34 and 67 height makes corresponding algorithms
useless since lines Pascal's Triangle of 67 height can be precomputed and stored in
memory with any other algorithm. It would take just (height + 2) * (height + 1) / 2 * 8 =
(67 + 2) * (67 + 1) / 2 * 8 = 18 768 bytes for 64-bit implementation.

So all optimizations that are limited by 64-height make only scientific interest.

Another conclusion from limitation test is that we can only compare implementations for particular
heights. There will be 4 benchmarks of different heights: 34, 67, 900, 3000.

Performance
~~~~~~~~~~~

CPython
```````

- The best implementation is Assembler x86 implementation
- Non-recursive implementations do better than recursive implementations
- Cython implementations do better than Python implementations
- C implementations do better than Cython implementations
- Assembler x86 implementation does better than C implementations
- Best implementation is about 100 times faster than the original implementation
- Best C implementation is about 50 times faster than the original implementation
- Best Cython implementation is about 90% faster than the original implementation
- Best Python implementation is about 40% faster than the original implementation
- `PyPascalTriangleNonRecursive`_, `PyPascalTriangleNonRecursiveLessCLike`_ and `PyPascalTriangleNonRecursiveCLikeImproved`_ are three best Python implementations
- Cython implementation that used C type is not the best Cython implementation
- 32-bit vs 64-bit integers do not make notable difference
- Sometimes more optimized Python implementation can do better than less optimized Cython implementation
- Some "optimizations" lead to up to 30% performance loss

.. include:: cpython_performance_test_34.rst
.. include:: cpython_performance_test_67.rst
.. include:: cpython_performance_test_900.rst
.. include:: cpython_performance_test_3000.rst

PyPy
````

- C-like Python implementations interpreted with PyPy do better than interpreted with CPython
- `PyPascalTriangleNonRecursiveCLike`_, `PyPascalTriangleNonRecursiveLessCLike`_ and `PyPascalTriangleNonRecursive`_  are three best Python implementations interpreted with PyPy
- Best Python implementation is about 300% faster than the original implementation with PyPy
- It is easier to gain higher performance increase for Python with PyPy than with CPython

.. include:: pypy_performance_test_34.rst
.. include:: pypy_performance_test_67.rst
.. include:: pypy_performance_test_900.rst
.. include:: pypy_performance_test_3000.rst

CPython vs Cython vs PyPy
`````````````````````````

- PyPy is faster than Cython
- Cython is faster than CPython
- Cython increases performance for tens of percents
- PyPy increase performance in several times
- CPython, Cython and PyPy do their best at different implementations
- `PyPascalTriangleNonRecursive`_ is the best for CPython
- `PyPascalTriangleNonRecursiveLessCLike`_ is the best for Cython
- `PyPascalTriangleNonRecursiveCLike`_ is the best for PyPy

.. include:: cpython_vs_cython_vs_pypy.rst

Pure C implementations
``````````````````````

- Most optimal version is more than 200 times faster than original CPython version
- Compiler-optimized (-O3 and -Ofast options) C code runs faster than Assembler code
- Python types conversion required for C extensions come with up to 10% overhead on function call
- gcc optimization options may improve run time up to 3 times

Compilation script:

.. literalinclude:: ../../build.sh

Output of :code:`$ ./ccpascal_triangle_normal`

.. literalinclude:: ccpascal_triangle_normal.txt

Output of :code:`$ ./ccpascal_triangle_O2`

.. literalinclude:: ccpascal_triangle_O2.txt

Output of :code:`$ ./ccpascal_triangle_O3`

.. literalinclude:: ccpascal_triangle_O3.txt

Output of :code:`$ ./ccpascal_triangle_Ofast`

.. literalinclude:: ccpascal_triangle_Ofast.txt

Environment
~~~~~~~~~~~

.. program-output:: lscpu

.. program-output:: cpufreq-info | grep 'current CPU'
    :shell:

.. program-output:: uname -srvmpio

.. program-output:: cat /etc/issue

.. program-output:: python -V

.. program-output:: cython -V

.. literalinclude:: pypy_version.txt

.. program-output:: gcc --version

Source code
~~~~~~~~~~~

Please, see class's docstring and diff to review the difference with base implementation.

PascalTriangleBase
``````````````````

.. literalinclude:: ../implementations/base.py

PyPascalTriangleBase
````````````````````

.. literalinclude:: ../implementations/python/base.py

PyPascalTriangleOriginal
````````````````````````

.. literalinclude:: ../implementations/python/original.py

PyPascalTriangleOriginalPlus
````````````````````````````

.. literalinclude:: ../implementations/python/original_plus.py

Diff
++++

.. literalinclude:: ../implementations/python/original_plus.py
    :diff: ../implementations/python/original.py

PyPascalTriangleConstantLists
`````````````````````````````

.. literalinclude:: ../implementations/python/constant_lists.py

Diff
++++

.. literalinclude:: ../implementations/python/constant_lists.py
    :diff: ../implementations/python/original_plus.py

PyPascalTriangleConstantTuples
``````````````````````````````

.. literalinclude:: ../implementations/python/constant_tuples.py

Diff
++++

.. literalinclude:: ../implementations/python/constant_tuples.py
    :diff: ../implementations/python/constant_lists.py

PyPascalTriangleIterators
`````````````````````````

.. literalinclude:: ../implementations/python/iterators.py

Diff
++++

.. literalinclude:: ../implementations/python/iterators.py
    :diff: ../implementations/python/constant_lists.py

PyPascalTriangleNonRecursive
````````````````````````````

.. literalinclude:: ../implementations/python/non_recursive.py

PyPascalTriangleNonRecursiveIterators
`````````````````````````````````````

.. literalinclude:: ../implementations/python/non_recursive_iterators.py

Diff
++++

.. literalinclude:: ../implementations/python/non_recursive_iterators.py
    :diff: ../implementations/python/non_recursive.py

PyPascalTriangleNonRecursiveCLike
`````````````````````````````````

.. literalinclude:: ../implementations/python/non_recursive_c_like.py

Diff
++++

.. literalinclude:: ../implementations/python/non_recursive_c_like.py
    :diff: ../implementations/python/non_recursive.py

PyPascalTriangleNonRecursiveCLikeImproved
`````````````````````````````````````````

.. literalinclude:: ../implementations/python/non_recursive_c_like_improved.py

Diff
++++

.. literalinclude:: ../implementations/python/non_recursive_c_like_improved.py
    :diff: ../implementations/python/non_recursive_c_like.py

PyPascalTriangleNonRecursiveLessCLike
`````````````````````````````````````

.. literalinclude:: ../implementations/python/non_recursive_less_c_like.py

Diff
++++

.. literalinclude:: ../implementations/python/non_recursive_less_c_like.py
    :diff: ../implementations/python/non_recursive_c_like.py

PyPascalTriangleNonRecursiveArray
`````````````````````````````````

.. literalinclude:: ../implementations/python/non_recursive_array.py

Diff
++++

.. literalinclude:: ../implementations/python/non_recursive_array.py
    :diff: ../implementations/python/non_recursive_less_c_like.py

CyPascalTriangleBase
````````````````````

.. literalinclude:: ../implementations/cython/base.py

CyPascalTriangleConstantLists
`````````````````````````````

.. literalinclude:: ../implementations/cython/constant_lists.pyx

Diff
++++

.. literalinclude:: ../implementations/cython/constant_lists.pyx
    :diff: ../implementations/python/constant_lists.py

CyPascalTriangleIterators
`````````````````````````

.. literalinclude:: ../implementations/cython/iterators.pyx

Diff
++++

.. literalinclude:: ../implementations/cython/iterators.pyx
    :diff: ../implementations/python/iterators.py

CyPascalTriangleNonRecursive
````````````````````````````

.. literalinclude:: ../implementations/cython/non_recursive.pyx

Diff
++++

.. literalinclude:: ../implementations/cython/non_recursive.pyx
    :diff: ../implementations/python/non_recursive.py

CyPascalTriangleNonRecursiveIterators
`````````````````````````````````````

.. literalinclude:: ../implementations/cython/non_recursive_iterators.pyx

Diff
++++

.. literalinclude:: ../implementations/cython/non_recursive_iterators.pyx
    :diff: ../implementations/python/non_recursive_iterators.py

CyPascalTriangleNonRecursiveCLikeImproved
`````````````````````````````````````````

.. literalinclude:: ../implementations/cython/non_recursive_c_like_improved.pyx

Diff
++++

.. literalinclude:: ../implementations/cython/non_recursive_c_like_improved.pyx
    :diff: ../implementations/python/non_recursive_c_like_improved.py

CyPascalTriangleNonRecursiveCLikeMoreImproved
`````````````````````````````````````````````

.. literalinclude:: ../implementations/cython/non_recursive_c_like_more_improved.pyx

Diff
++++

.. literalinclude:: ../implementations/cython/non_recursive_c_like_more_improved.pyx
    :diff: ../implementations/cython/non_recursive_c_like_improved.pyx

CyPascalTriangleNonRecursiveLessCLike
`````````````````````````````````````

.. literalinclude:: ../implementations/cython/non_recursive_less_c_like.pyx

Diff
++++

.. literalinclude:: ../implementations/cython/non_recursive_less_c_like.pyx
    :diff: ../implementations/python/non_recursive_less_c_like.py

CyPascalTriangleNonRecursiveCTypes
``````````````````````````````````

.. literalinclude:: ../implementations/cython/c_types.pyx

Diff
++++

.. literalinclude:: ../implementations/cython/c_types.pyx
    :diff: ../implementations/python/non_recursive_array.py

CyPascalTriangleNonRecursiveCTypesULong
```````````````````````````````````````

.. literalinclude:: ../implementations/cython/c_types_ulong.pyx

Diff
++++

.. literalinclude:: ../implementations/cython/c_types_ulong.pyx
    :diff: ../implementations/cython/c_types.pyx

CPascalTriangleInitial
``````````````````````

.. literalinclude:: ../implementations/cextension/initial.py
.. literalinclude:: ../implementations/cextension/cinitial.c
    :language: c

CPascalTriangleULong
````````````````````

.. literalinclude:: ../implementations/cextension/ulong.py
.. literalinclude:: ../implementations/cextension/culong.c
    :language: c

Diff
++++

.. literalinclude:: ../implementations/cextension/ulong.py
    :diff: ../implementations/cextension/initial.py

.. literalinclude:: ../implementations/cextension/culong.c
    :diff: ../implementations/cextension/cinitial.c

CPascalTrianglePartialAsm
`````````````````````````

.. literalinclude:: ../implementations/cextension/partial_asm.py
.. literalinclude:: ../implementations/cextension/cpartial_asm.c
    :language: c

Diff
++++

.. literalinclude:: ../implementations/cextension/partial_asm.py
    :diff: ../implementations/cextension/initial.py

.. literalinclude:: ../implementations/cextension/cpartial_asm.c
    :diff: ../implementations/cextension/cinitial.c

CPascalTriangleFullAsm
``````````````````````

.. literalinclude:: ../implementations/cextension/full_asm.py
.. literalinclude:: ../implementations/cextension/cfull_asm.c
    :language: c

Diff
++++

.. literalinclude:: ../implementations/cextension/full_asm.py
    :diff: ../implementations/cextension/partial_asm.py

.. literalinclude:: ../implementations/cextension/cfull_asm.c
    :diff: ../implementations/cextension/cpartial_asm.c

TODO
----

- Provide Assembler x86 implementation for 64-bit integer values
- Support Python 3.x (port Python, Cython and C extensions code)
