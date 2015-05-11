import inspect

from pascal_triangle.pascal_triangle import PyPascalTriangle, CyPascalTriangle, CPascalTriangle

TEST_CLASSES = (PyPascalTriangle, CyPascalTriangle, CPascalTriangle)


def test_methods():
    for test_class in TEST_CLASSES:
        method_names = (name for name, method in
                        inspect.getmembers(test_class, predicate=inspect.ismethod)
                        if not name.startswith('_'))
        for method_name in method_names:
            yield test_class, method_name
