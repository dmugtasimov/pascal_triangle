from pascal_triangle.base import PascalTriangleBase


class CPascalTriangleBase(PascalTriangleBase):

    language = 'C'

    def __init__(self, return_list=False):
        self.return_list = return_list
