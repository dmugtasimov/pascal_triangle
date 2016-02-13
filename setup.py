import sys
import setuptools
import platform

from distutils.core import setup, Extension


def get_ext_modules(with_cython_modules=True, with_cextensions=True):

    if with_cython_modules:
        from Cython.Build import cythonize
        ext_modules = cythonize((
            './pascal_triangle/cypascal_triangle.pyx',
            './pascal_triangle/implementations/cython/iterators.pyx',
            './pascal_triangle/implementations/cython/constant_lists.pyx',
            './pascal_triangle/implementations/cython/non_recursive.pyx',
            './pascal_triangle/implementations/cython/non_recursive_iterators.pyx',
            './pascal_triangle/implementations/cython/non_recursive_c_like_improved.pyx',
            './pascal_triangle/implementations/cython/non_recursive_c_like_more_improved.pyx',
            './pascal_triangle/implementations/cython/non_recursive_less_c_like.pyx',
            './pascal_triangle/implementations/cython/c_types.pyx',
            './pascal_triangle/implementations/cython/c_types_ulong.pyx',
        ))
    else:
        ext_modules = []

    if with_cextensions:
        cextensions = (
            Extension('pascal_triangle.implementations.cextension.cinitial',
                      ['./pascal_triangle/implementations/cextension/cinitial.c']),
            Extension('pascal_triangle.implementations.cextension.culong',
                      ['./pascal_triangle/implementations/cextension/culong.c']),
            Extension('pascal_triangle.implementations.cextension.cpartial_asm',
                      ['./pascal_triangle/implementations/cextension/cpartial_asm.c']),
            Extension('pascal_triangle.implementations.cextension.cfull_asm',
                      ['./pascal_triangle/implementations/cextension/cfull_asm.c']),
        )

        ext_modules.extend(cextensions)

    for ext_module in ext_modules:
        yield ext_module


class LazyList(list):

    def __init__(self, iterable, *args, **kwargs):
        super(LazyList, self).__init__(*args, **kwargs)
        self.iterable = iter(iterable)
        self.ready = False

    def __populate(self):
        if not self.ready:
            self.extend(self.iterable)
            self.ready = True

    def __iter__(self):
        self.__populate()
        return super(LazyList, self).__iter__()

    def __getitem__(self, index):
        self.__populate()
        return super(LazyList, self).__getitem__(index)

    def __len__(self):
        self.__populate()
        return super(LazyList, self).__len__()


CYTHON_REQUIRE = 'Cython==0.23.4'

python_implementation = platform.python_implementation()
if python_implementation == 'CPython':
    with_cython = sys.version_info[0] < 3
    with_cextension = sys.version_info[0] < 3
else:
    with_cython = False
    with_cextension = True


setup(
    name='pascal_triangle',
    version='0.0.1',
    description='Print Pascal''s Triangle solutions',
    platforms='any',
    packages=setuptools.find_packages(),
    # TODO(dmu) MEDIUM: Replace this dirty hack someday
    setup_requires=(CYTHON_REQUIRE,) if with_cython else (),
    install_requires=('terminaltables==2.1.0', 'mock==1.3.0',),
    extras_require={
        'cython': (CYTHON_REQUIRE,),
        'doc': ('Sphinx==1.3.5', 'sphinxcontrib-programoutput==0.8',),
    },
    ext_modules=LazyList(get_ext_modules(with_cython, with_cextension)),
)
