from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(
    #ext_modules=cythonize('cypascal_triangle.pyx')
    ext_modules=[Extension('cpascal_triangle', ['cpascal_triangle.c'])]
)
