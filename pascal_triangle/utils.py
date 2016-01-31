import terminaltables


class RSTTable(terminaltables.AsciiTable):

    def __init__(self, *args, **kwargs):
        super(RSTTable, self).__init__(*args, **kwargs)
        self.inner_row_border = True
