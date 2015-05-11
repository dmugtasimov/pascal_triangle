import unittest
import inspect
from collections import deque

from mock import Mock, call

from pascal_triangle.pascal_triangle import PyPascalTriangle


_TEST_CLASS = PyPascalTriangle


def test_method_template(method_name):

    TRI_HEIGH = 4
    CALLS_5 = [call([1]), call([1, 1]), call([1, 2, 1]), call([1, 3, 3, 1]),
               call([1, 4, 6, 4, 1])]

    def test_method(self):
        method = getattr(self.pascal_triangle_testable, method_name)
        method(TRI_HEIGH)
        self.pascal_triangle_testable._test_print.assert_has_calls(CALLS_5)

    return test_method


class _TestPascalTriagnaleMeta(type):

    def __new__(cls, name, bases, attrs):
        method_names = (name for name, method in
                        inspect.getmembers(_TEST_CLASS, predicate=inspect.ismethod)
                        if not name.startswith('_'))
        for method_name in method_names:
            attrs['test_' + method_name] = test_method_template(method_name)

        return super(_TestPascalTriagnaleMeta, cls).__new__(cls, name, bases, attrs)


class TestPascalTriagnale(unittest.TestCase):

    __metaclass__ = _TestPascalTriagnaleMeta

    @classmethod
    def setUpClass(cls):
        cls.pascal_triangle_testable = _TEST_CLASS()

    def setUp(self):
        self.pascal_triangle_testable._test_print = Mock()

