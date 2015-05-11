import types
import time

from .utils import test_methods

from pascal_triangle.pascal_triangle import CPascalTriangle

MAX_HEIGHT = 4096
MAX_TIME_SECONDS = 1


def _print(self, arg):
    self._print_last_call = list(arg)


def run_limitation_test():
    powers_of_2 = tuple(2 ** p for p in xrange(MAX_HEIGHT + 1))

    for test_class, method_name in test_methods():
        class_name = test_class.__name__
        if issubclass(test_class, CPascalTriangle):
            printer = test_class(return_list=True)
        else:
            printer = test_class()
        printer._print_last_call = None
        printer._print = types.MethodType(_print, printer)
        method = getattr(printer, method_name)

        lower = 0
        upper = 1
        last_error = None
        print '%s.%s(...):' % (class_name, method_name)
        while lower < upper <= MAX_HEIGHT:
            start = time.time()
            try:
                result = method(upper)
            except Exception as e:
                last_error = 'EXCEPTION: %s.%s(%s): %r' % (class_name, method_name, upper, e)
                upper = (lower + upper) / 2
                continue
            finish = time.time()
            duration = finish - start

            if result is not None:
                result = list(result)
                total_sum = sum(result)
                if total_sum != powers_of_2[upper]:
                    last_error = 'OVERFLOW:  %s.%s(%s)' % (class_name, method_name, upper)
                    upper = (lower + upper) / 2
                    continue

            if duration > MAX_TIME_SECONDS:
                print 'TIMEOUT:   %s.%s(%s): %.06f seconds' % (class_name, method_name, upper, duration)
                break
            lower = upper
            upper *= 2
        else:
            if last_error:
                print last_error
            print 'DONE:      %s.%s(%s): %.06f seconds' % (class_name, method_name, upper, duration)

        print


if __name__ == '__main__':
    run_limitation_test()
