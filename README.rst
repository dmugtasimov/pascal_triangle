Installation
------------

#. Install prerequisites::

    sudo apt-get install python-pip
    pip install --user virtualenvwrapper

    cat << EOF >> ~/.bashrc
    export WORKON_HOME=$HOME/.virtualenvs
    source ~/.local/bin/virtualenvwrapper.sh
    EOF

    source ~/.bashrc
    mkvirtualenv pascal_triangle
    pip install --upgrade pip

    # to activate later:
    workon pascal_triangle

#. Install::

    git clone https://github.com/dmugtasimov/pascal_triangle.git
    cd pascal_triangle
    pip install -e .[cython,doc]

#. Install PyPy::

    wget https://bitbucket.org/pypy/pypy/downloads/pypy-4.0.1-linux64.tar.bz2
    tar -xf pypy-4.0.1-linux64.tar.bz2
    sudo mv pypy-4.0.1-linux64 /opt
    rm pypy-4.0.1-linux64.tar.bz2
    ln -s /opt/pypy-4.0.1-linux64/bin/pypy /usr/local/bin/pypy

#. Create virtualenv for PyPy::

    deactivate
    mkvirtualenv pascal_triangle_pypy -p /usr/local/bin/pypy
    pip install --upgrade pip

    # to activate later:
    workon pascal_triangle_pypy

#. Install into PyPy virtualenv::

    cd pascal_triangle
    pip install -e .

#. Create virtualenv for Python 3::

    deactivate
    mkvirtualenv pascal_triangle_py3 -p /usr/bin/python3
    pip install --upgrade pip

    # to activate later:
    workon pascal_triangle_py3

#. Install into PyPy virtualenv::

    cd pascal_triangle
    pip install -e .

#. Build pure C solution::

    ./build.sh

Running tests
-------------

#. Activate virtualenv::

    workon pascal_triangle

#. Run unit tests::

    python -m unittest -v pascal_triangle.tests.test_pascal_triangle

#. Run limitation tests::

    python -m pascal_triangle.tests.limitation_test

#. Set constant CPU frequency::

    seq 0 $(( `nproc` - 1 )) | xargs --verbose -I{} sudo cpufreq-set -c {} -g performance

#. Ensure that CPU frequency is set::

    cpufreq-info | grep 'decide'
    cpufreq-info | grep 'current CPU frequency is'

#. Run performance tests for CPython::

    python -m pascal_triangle.tests.performance_test
    python -m pascal_triangle.tests.performance_test --output-format=json > cpython_performance_test.json

#. Run performance tests for PyPy::

    workon pascal_triangle_pypy
    python -m pascal_triangle.tests.performance_test
    python -m pascal_triangle.tests.performance_test --output-format=json > pypy_performance_test.json

    workon pascal_triangle

#. Compare::

    python -m pascal_triangle.tests.compare cpython_performance_test.json pypy_performance_test.json

#. Run pure C implementations::

    ./ccpascal_triangle_normal 34 1000
    ./ccpascal_triangle_O2 34 1000
    ./ccpascal_triangle_O3 34 1000
    ./ccpascal_triangle_Ofast 34 1000

#. Set ondemand CPU frequency::

    seq 0 $(( `nproc` - 1 )) | xargs --verbose -I{} sudo cpufreq-set -c {} -g ondemand

Article
-------

For article generation run::

    workon pascal_triangle
    cd ./pascal_triangle/article
    source ./runtests.sh && make html

    firefox _build/html/index.html &
