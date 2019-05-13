#!/usr/bin/env python
# Licensed under a 3-clause BSD style license, see LICENSE.

from __future__ import absolute_import
from __future__ import print_function

import sys
import os

from setuptools import setup
from setuptools import find_packages

# Only add pytest-runner if the setup.py call needs it
needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

def get_version():
    g = {}
    exec(open(os.path.join("hepunits", "_version.py")).read(), g)
    return g["__version__"]

setup(
    name = 'hepunits',
    author = 'Eduardo Rodrigues',
    author_email = 'eduardo.rodrigues@cern.ch',
    maintainer = 'Eduardo Rodrigues',
    maintainer_email = 'eduardo.rodrigues@cern.ch',
    version = get_version(),
    description = 'Units and constants in the HEP system of units',
    long_description = open('README.rst').read(),
    url = 'https://github.com/scikit-hep/hepunits',
    license = 'new BSD',
    packages = find_packages(),
    include_package_data = True,
    setup_requires = [] + pytest_runner,
    tests_require = ['pytest'],
    keywords = [
        'HEP', 'units', 'constants',
    ],
    classifiers = [
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Topic :: Scientific/Engineering',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 5 - Production/Stable',
    ],
    platforms = "Any",
)
