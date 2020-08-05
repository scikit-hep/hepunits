#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license, see LICENSE.

from setuptools import setup

# Setup will not be able to find the version if these packages are missing
#
# > Remember, setup.py does not run when installing from a wheel, so only
# > required to make one

import setuptools_scm  # noqa: F401
import toml  # noqa: F401

setup()
