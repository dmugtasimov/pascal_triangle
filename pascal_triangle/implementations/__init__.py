import sys
import platform

from .python import *

ALL_IMPLEMENTATIONS = PYTHON_IMPLEMENTATIONS

python_implementation = platform.python_implementation()

if python_implementation == 'CPython' and sys.version_info[0] < 3:
    from .cython import *
    from .cextension import *
    ALL_IMPLEMENTATIONS += CYTHON_IMPLEMENTATIONS + CEXTENSION_IMPLEMENTATIONS

elif python_implementation == 'PyPy':
    from .cextension import *

    ALL_IMPLEMENTATIONS += CEXTENSION_IMPLEMENTATIONS
