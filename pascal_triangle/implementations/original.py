def print_pascal_triangle_original(n):
    """
    Print Pascal's Triangle of height n: original interview solution.
    :param n: height of the triangle to print
    :return: n-th line of Pascal's Triangle
    """
    if n <= 1:
        print [1]
        return [1]

    a = [0] + print_pascal_triangle_original(n - 1) + [0]
    b = [a[i] + a[i + 1] for i in xrange(len(a) - 1)]
    print b
    return b
