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
    pip install -e .

#. Build pure C solution::

    gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -D_FORTIFY_SOURCE=2 -g -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security -o ccpascal_triangle_normal ccpascal_triangle.c
    chmod a+x ./ccpascal_triangle_normal

    gcc -O2 -o ccpascal_triangle_O2 ccpascal_triangle.c
    chmod a+x ./ccpascal_triangle_O2

    gcc -O3 -o ccpascal_triangle_O3 ccpascal_triangle.c
    chmod a+x ./ccpascal_triangle_O3

    gcc -Ofast -o ccpascal_triangle_Ofast ccpascal_triangle.c
    chmod a+x ./ccpascal_triangle_Ofast

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

#. Run performance tests::

    python -m pascal_triangle.tests.performance_test

#. Run pure C implementations::

    ./ccpascal_triangle_normal
    ./ccpascal_triangle_O2
    ./ccpascal_triangle_O3
    ./ccpascal_triangle_Ofast

#. Set ondemand CPU frequency::

    seq 0 $(( `nproc` - 1 )) | xargs --verbose -I{} sudo cpufreq-set -c {} -g ondemand

Article
-------

For article generation run::

    workon pascal_triangle
    cd ./pascal_triangle/article
    make html

    firefox _build/html/index.html &
