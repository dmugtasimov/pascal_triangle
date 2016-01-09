def print_pascal_triangle_real_original(n):
    """
    Print Pascal's Triangle of height n: original interview solution.
    :param n: height of the triangle to print
    :return: n-th line of Pascal's Triangle
    """
    if n <= 1:
        print [1]
        return [1]

    a = [0] + print_pascal_triangle_real_original(n - 1) + [0]
    b = [a[i] + a[i + 1] for i in xrange(len(a) - 1)]
    print b
    return b


class PascalTriangleBase(object):

    EMPTY_LIST = []
    ZERO_LIST = [0]
    ONE_LIST = [1]

    EMPTY_TUPLE = ()
    ZERO_TUPLE = (0,)
    ONE_TUPLE = (1,)

    def _test_print(self, arg):
        print arg

    def _print(self, arg):
        """
        Print Pascal's Triangle line
        :param arg: triangle line
        """
        if not isinstance(arg, list):
            arg = list(arg)

        self._test_print(arg)

    def build(self, height):
        """Build Pascal's Triangle of given height.
        :param height: height of the triangle to print (zero-based)
        :return: last line of Pascal's Triangle
        """
        raise NotImplementedError()
