import timeit
import collections

def print_pascal_triangle_v7(height):
    line = collections.deque()
    for x in xrange(height):
        line.appendleft(1)
        for i in xrange(1, len(line)):
            try:
                line[i] += line[i + 1]
            except IndexError:
                pass
        #print line


CYCLES = 10000
HEIGHT = 20
func = 'print_pascal_triangle_v7'
print '%s(%s) done for %s times in %s seconds' % (func, HEIGHT, CYCLES,
        timeit.timeit('%s(%s)' % (func, HEIGHT), setup='from cpascal_triangle import %s' % func,
                      number=CYCLES))