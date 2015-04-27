import setuptools
from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(
    name='pascal_triangle',
    version='0.0.1',
    description='Print Pascal''s Triangle solutions',
    platforms='any',
    packages=setuptools.find_packages(),
    install_requires=('Cython==0.22', 'mock==1.0.1'),
    ext_modules=cythonize('./pascal_triangle/cypascal_triangle.pyx')
#    ext_modules=[Extension('cpascal_triangle', ['cpascal_triangle.c'])]
)
