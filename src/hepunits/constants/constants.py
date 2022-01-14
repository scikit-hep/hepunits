# Licensed under a 3-clause BSD style license, see LICENSE.
"""
Physical and other handy constants
==================================

This module `hepunits.constants` contains 2 sorts of constants:

  * Physical constants.
  * Common and/or handy constants.

All constants are computed in the HEP System of Units
as defined in the `hepunits.units` module.

Typical use case::

    >>> from hepunits.constants import c_light
    >>> from hepunits.units     import picosecond, micrometer
    >>> tau_Bs = 1.5 * picosecond    # a particle lifetime, say the Bs meson's
    >>> ctau_Bs = c_light * tau_Bs   # ctau of the particle, ~450 microns
    >>> print ctau_Bs                # result in HEP units, so mm ;-)
    0.449688687
    >>> print ctau_Bs / micrometer   # result in micrometers
    449.688687

"""

# -----------------------------------------------------------------------------
# Import statements
# -----------------------------------------------------------------------------

from math import pi
from typing import List

from ..units.units import eplus, joule, kelvin, m, mole, s

__all__ = (
    "m",
    "s",
    "eplus",
    "mole",
    "joule",
    "kelvin",
    "c_light",
    "c_light_sq",
    "pi",
    "two_pi",
    "half_pi",
    "pi_sq",
    "eminus",
    "e_sq",
    "Avogadro",
    "h_Planck",
    "hbar_Planck",
    "hbar",
    "hbarc",
    "hbarc_sq",
    "k_Boltzmann",
)


# -----------------------------------------------------------------------------
# Mathematical constants
# -----------------------------------------------------------------------------

two_pi = 2 * pi
half_pi = pi / 2
pi_sq = pi * pi

# -----------------------------------------------------------------------------
# Physical constants
# -----------------------------------------------------------------------------

# Speed of light in vacuum (exact value, taken from PDG 2020)
c_light = 299792458 * m / s
c_light_sq = c_light * c_light

# Electron charge
eminus = -eplus  # electron charge
e_sq = eplus * eplus

# Avogadro constant (exact value, taken from PDG 2020)
Avogadro = 6.02214076e23 / mole

# Planck constant (exact value, taken from PDG 2020)
h_Planck = 6.62607015e-34 * joule * s

hbar_Planck = h_Planck / two_pi
hbar = hbar_Planck

hbarc = hbar_Planck * c_light

hbarc_sq = hbarc * hbarc

# Boltzmann constant (exact value, taken from PDG 2020)
k_Boltzmann = 1.380649e-23 * joule / kelvin


def __dir__() -> List[str]:
    return list(__all__)
