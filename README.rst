Build cypascal_triangle:
python setup.py build_ext --inplace

Build cpascal_triangle:
gcc -dynamiclib -I/usr/include/python2.7/ -lpython2.7 -o cpascal_triangle.so cpascal_triangle.c
