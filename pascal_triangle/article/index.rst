.. Pascal's Triangle documentation master file, created by
   sphinx-quickstart on Sat Jan 23 00:27:52 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pascal's Triangle
=================

.. toctree::
   :hidden:

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

* Python
* Cython
* ?PyPy
* C
* Assembler

Optimization techniques used:

* Microoptimizations
* Replace recursive algorithm with non-recursive
* Replace Python with other programming languages

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
