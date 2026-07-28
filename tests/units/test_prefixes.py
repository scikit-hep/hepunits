# Licensed under a 3-clause BSD style license, see LICENSE.
"""
Tests for the hepunits.units.prefixes module.
"""

from math import log2

from pytest import approx

from hepunits import kibi, mega, micro, tebi, yocto, yotta


def test_prefixes_e6():
    assert 4 * mega == 1.0 / 0.25 / micro


def test_prefixes_e24():
    assert yotta * yocto == approx(1.0)


def test_prefixes_binary():
    assert log2(kibi) == 10
    assert log2(tebi) == 40
