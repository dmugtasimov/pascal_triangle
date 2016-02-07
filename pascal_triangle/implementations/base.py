class PascalTriangleBase(object):

    language = NotImplemented
    original = False
    max_height = None

    EMPTY_LIST = []
    ZERO_LIST = [0]
    ONE_LIST = [1]

    EMPTY_TUPLE = ()
    ZERO_TUPLE = (0,)
    ONE_TUPLE = (1,)

    def __init__(self, verbose=False, return_list=False):
        self.verbose = verbose
        self.return_list = return_list

    def _test_print(self, arg):
        print arg

    def _print(self, arg):
        """
        Print Pascal's Triangle line
        :param arg: triangle line
        """
        if not self.verbose:
            return

        if not isinstance(arg, list):
            arg = list(arg)

        self._test_print(arg)

    def build(self, height):
        """Build Pascal's Triangle of given height.
        :param height: height of the triangle to print (zero-based)
        :return: last line of Pascal's Triangle
        """
        raise NotImplementedError()
