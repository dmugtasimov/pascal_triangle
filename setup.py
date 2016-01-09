import setuptools
from distutils.core import setup, Extension


def get_ext_modules():
    from Cython.Build import cythonize
    ext_modules = cythonize('./pascal_triangle/cypascal_triangle.pyx')
    ext_modules.append(Extension('pascal_triangle.cpascal_triangle',
                                 ['./pascal_triangle/cpascal_triangle.c']))

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


setup(
    name='pascal_triangle',
    version='0.0.1',
    description='Print Pascal''s Triangle solutions',
    platforms='any',
    packages=setuptools.find_packages(),
    setup_requires=('Cython==0.23.4',),
    install_requires=('Cython==0.23.4', 'mock==1.3.0',),
    ext_modules=LazyList(get_ext_modules()),
)
