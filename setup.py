import setuptools
from distutils.core import setup, Extension
from Cython.Build import cythonize

ext_modules = cythonize('./pascal_triangle/cypascal_triangle.pyx')
ext_modules.append(Extension('pascal_triangle.cpascal_triangle',
                             ['./pascal_triangle/cpascal_triangle.c']))

setup(
    name='pascal_triangle',
    version='0.0.1',
    description='Print Pascal''s Triangle solutions',
    platforms='any',
    packages=setuptools.find_packages(),
    setup_requires=('Cython==0.22',),
    install_requires=('mock==1.0.1',),
    ext_modules=ext_modules
)
