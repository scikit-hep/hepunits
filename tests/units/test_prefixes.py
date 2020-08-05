#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license, see LICENSE.
"""
Tests for the hepunits.units.prefixes module.
"""

from pytest import approx

from math import log

from hepunits import mega, micro, yotta, yocto, kibi, tebi


def test_prefixes_e6():
    assert 4 * mega == 1.0 / 0.25 / micro


def test_prefixes_e24():
    assert yotta * yocto == approx(1.0)


def test_prefixes_binary():
    assert log(kibi, 2) == 10
    assert log(tebi, 2) == 40
