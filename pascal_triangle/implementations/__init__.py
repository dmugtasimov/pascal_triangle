import platform

from .python import *

ALL_IMPLEMENTATIONS = PYTHON_IMPLEMENTATIONS

if platform.python_implementation() == 'CPython':
    from .cython import *
    from .cextension import *

    ALL_IMPLEMENTATIONS += CYTHON_IMPLEMENTATIONS + CEXTENSION_IMPLEMENTATIONS
