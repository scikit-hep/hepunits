# Licensed under a 3-clause BSD style license, see LICENSE.
"""
Common unit prefixes
====================

There are 2 types of prefixes:

  * SI prefixes [SI_prefixes]_.
  * Binary prefixes [Binary_prefixes]_.

**References**

.. [SI_prefixes] https://en.wikipedia.org/wiki/International_System_of_Units#Prefixes.
.. [Binary_prefixes] https://en.wikipedia.org/wiki/Unit_prefix#Binary_prefixes.
"""

__all__ = (
    "atto",
    "centi",
    "deca",
    "deci",
    "exa",
    "exbi",
    "femto",
    "gibi",
    "giga",
    "googol",
    "hecto",
    "kibi",
    "kilo",
    "mebi",
    "mega",
    "micro",
    "milli",
    "nano",
    "pebi",
    "peta",
    "pico",
    "tebi",
    "tera",
    "yobi",
    "yocto",
    "yotta",
    "zebi",
    "zepto",
    "zetta",
)


# -----------------------------------------------------------------------------
# SI prefixes
# -----------------------------------------------------------------------------
from typing import List

yotta = 1.0e24
zetta = 1.0e21
exa = 1.0e18
peta = 1.0e15
tera = 1.0e12
giga = 1.0e9
mega = 1.0e6
kilo = 1.0e3
hecto = 1.0e2
deca = 1.0e1
deci = 1.0e-1
centi = 1.0e-2
milli = 1.0e-3
micro = 1.0e-6
nano = 1.0e-9
pico = 1.0e-12
femto = 1.0e-15
atto = 1.0e-18
zepto = 1.0e-21
yocto = 1.0e-24

# -----------------------------------------------------------------------------
# Binary prefixes
# -----------------------------------------------------------------------------
kibi = 2.0**10
mebi = 2.0**20
gibi = 2.0**30
tebi = 2.0**40
pebi = 2.0**50
exbi = 2.0**60
zebi = 2.0**70
yobi = 2.0**80

# -----------------------------------------------------------------------------
# Miscellaneous prefixes
# -----------------------------------------------------------------------------
googol = 1.0e100


def __dir__() -> List[str]:
    return list(__all__)
