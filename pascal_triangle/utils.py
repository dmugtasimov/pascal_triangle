import terminaltables


def format_float_safe(v):
    return '{0:.06f}'.format(v) if isinstance(v, float) else v


class RSTTable(terminaltables.AsciiTable):

    def __init__(self, *args, **kwargs):
        super(RSTTable, self).__init__(*args, **kwargs)
        self.inner_row_border = True
