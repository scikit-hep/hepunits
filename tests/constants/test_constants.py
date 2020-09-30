#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license, see LICENSE.
"""
Tests for the hepunits.constants.constants module.
"""

from pytest import approx

from hepunits import eV, nanometer, s, THz
from hepunits import *


def test_constants():
    assert pi_sq == two_pi * half_pi
    assert Avogadro == 6.02214076e23
    assert c_light / (m / s) == 299792458
    assert hbarc_sq / c_light_sq == approx((h_Planck / two_pi) ** 2)
    assert hbar / (eV * s) == hbar / 1.0e3
    # wavelength of 555-ish nanometres (green light) has a frequency of 540 THz
    assert c_light / (555.17121851852 * nanometer) == approx(540 * THz)
