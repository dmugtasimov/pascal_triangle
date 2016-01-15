import unittest

from pascal_triangle.implementations import ALL_IMPLEMENTATIONS


def test_method_template(implementation_class):

    TRI_HEIGHT = 5
    TRI_HEIGHT_SUM = 2 ** TRI_HEIGHT

    def test_method(self):
        result = implementation_class(return_list=True).build(TRI_HEIGHT)
        self.assertEquals(sum(result), TRI_HEIGHT_SUM)

    return test_method


class _TestPascalTriangleMeta(type):

    def __new__(mcs, name, bases, attrs):
        for implementation in ALL_IMPLEMENTATIONS:
            attrs['test_' + implementation.__name__] = test_method_template(implementation)

        return super(_TestPascalTriangleMeta, mcs).__new__(mcs, name, bases, attrs)


class TestPascalTriangle(unittest.TestCase):

    __metaclass__ = _TestPascalTriangleMeta
