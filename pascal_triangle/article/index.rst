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
building algorithm implementations, their performance and limitation analysis. The article shows
some techniques for performance optimization that can be used for solving real life software
optimization problems.

Algorithms:

* Recursive
* Non-recursive

Programming languages:

* Python (CPython and PyPy implementations)
* Cython
* C
* Assembler

Optimization techniques used:

* Microoptimizations
* Replace recursive algorithm with non-recursive
* Replace Python with other programming languages

Conclusions
-----------

* Faster implementations may have limitations that make them impractical. For example `CPascalTriangleFullAsm`_ has the best time performance, but limited to 34 height. Therefore practially it is easier to cache or precalculate Pascal's Triangle of this height.

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
(made lines zero-based and converted the function into a class method):

.. literalinclude:: ../implementations/python/original.py

Limitations
~~~~~~~~~~~

When I started implementation of the Pascal's Triangle building algorithm it turned out that
different implementations have their own limitations. Therefore I should describe the limitations
first.

Here is the result of limitation test::

    $ python -m pascal_triangle.tests.limitation_test

.. include:: limitation_test.rst

As seen from the table there are several thresholds of triangle height limitations:

* 34 is a height limit for all algorithms that use unsigned 32-bit integers for calculation.
* 67 is a height limit for all algorithms that use unsigned 64-bit integers for calculation.
* Just below 1000 is a height limit for all recursive algorithms in Python since the default recursion limit in python is 1000 frames.
* The other implementations are virtually limited by the time required for calculation once it exceeds 1 second.

From practical point of view limit of 34 and 67 height makes corresponding algorithms
useless since lines Pascal's Triangle of 67 height can be precomputed and stored in
memory with any other even slow algorithms. It would take only (height + 2) * (height + 1) / 2 =
(67 + 2) * (67 + 1) / 2 * 8 = 18768 bytes.

So all optimizations that were made for original implementation have only scientific interest.

Another conclusion from limitation test is that we can only compare implementations for particular
heights. Performance of all implementations can be benchmarked for 34 height and there should be
a benchmark for 67 height group, 1000 height group and over 1000 height group.

Performance
~~~~~~~~~~~

CPython
```````

.. include:: cpython_performance_test_34.rst
.. include:: cpython_performance_test_67.rst
.. include:: cpython_performance_test_900.rst
.. include:: cpython_performance_test_3000.rst

PyPy
````

.. include:: pypy_performance_test_34.rst
.. include:: pypy_performance_test_67.rst
.. include:: pypy_performance_test_900.rst
.. include:: pypy_performance_test_3000.rst

CPython vs Cython vs PyPy
`````````````````````````

.. include:: cpython_vs_cython_vs_pypy.rst

C implementations
`````````````````

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

Source code
~~~~~~~~~~~

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
