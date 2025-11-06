# Licensed under a 3-clause BSD style license, see LICENSE.

"""
Units in the HEP system of units
================================

This module `hepunits.units` contains 2 submodules for:

  * Basic physical units and derived units (`hepunits.units.units`).
  * Commonly-used unit prefixes (`hepunits.units.prefixes`).

All units are provided in the HEP System of Units as defined below.

In HEP the System of Units consists of the basic units originally defined by
the [CLHEP]_ project:

    ===================   ================== ====
    Quantity              Name               Unit
    ===================   ================== ====
    Length                millimeter         mm
    Time                  nanosecond         ns
    Energy                Mega electron Volt MeV
    Positron charge       eplus
    Temperature           kelvin             K
    Amount of substance   mole               mol
    Luminous intensity    candela            cd
    Plane angle           radian             rad
    Solid angle           steradian          sr
    ===================   ================== ====

It is largely based on the international system of units ([SI]_)

    ===================   ========   ====
    Quantity              Name       Unit
    ===================   ========   ====
    Length                meter      m
    Time                  second     s
    Mass                  kilogram   kg
    Electric current      ampere     A
    Temperature           kelvin     K
    Amount of substance   mole       mol
    Luminous intensity    candela    cd
    ===================   ========   ====

but augments it with handy definitions, changing the basic length and time
units.

Typical use cases::

    >>> # add two quantities with length units and get the result in meters
    >>> from hepunits import units as u
    >>> (1 * u.meter + 5 * u.cm) / u.meter
    1.05
    >>> from hepunits.units import MeV, GeV
    >>> massWindow = 100 * MeV    # define a 100 MeV mass window
    >>> def energy_resolution():
    ...    # returns the energy resolution of 100 MeV
    ...    return 100 * MeV
    ...
    >>> energy_resolution() / GeV # get the energy resolution in GeV
    0.1

**References**

.. [CLHEP] http://proj-clhep.web.cern.ch/proj-clhep/.
.. [SI] http://www.physics.nist.gov/cuu/Units/index.html.
"""

from math import pi as _pi

from . import prefixes as _pre

# --------------------------------------------------------------------
# Units of length
# ---------------
millimeter = 1.0
millimeter2 = millimeter * millimeter
millimeter3 = millimeter * millimeter * millimeter

mm = millimeter
mm2 = millimeter2
mm3 = millimeter3

meter = _pre.kilo * millimeter
meter2 = meter * meter
meter3 = meter * meter * meter

m = meter
m2 = meter2
m3 = meter3

centimeter = _pre.centi * meter
centimeter2 = centimeter * centimeter
centimeter3 = centimeter * centimeter * centimeter

cm = centimeter
cm2 = centimeter2
cm3 = centimeter3

kilometer = _pre.kilo * meter
kilometer2 = kilometer * kilometer
kilometer3 = kilometer * kilometer * kilometer

km = kilometer
km2 = kilometer2
km3 = kilometer3

micrometer = _pre.micro * meter
micron = micrometer

nanometer = _pre.nano * meter

angstrom = 1e-10 * meter

femtometer = _pre.femto * meter
fermi = femtometer

fm = femtometer
fm2 = femtometer * femtometer
fm3 = femtometer * femtometer * femtometer

barn = 1.0e-28 * meter2

millibarn = _pre.milli * barn
microbarn = _pre.micro * barn
nanobarn = _pre.nano * barn
picobarn = _pre.pico * barn
femtobarn = _pre.femto * barn
attobarn = _pre.atto * barn

mb = millibarn
ub = microbarn
nb = nanobarn
pb = picobarn
fb = femtobarn
ab = attobarn

invmb = 1.0 / millibarn
invub = 1.0 / microbarn
invnb = 1.0 / nanobarn
invpb = 1.0 / picobarn
invfb = 1.0 / femtobarn
invab = 1.0 / attobarn

# --------------------------------------------------------------------
# Units of time
# --------------------------------------------------------------------
nanosecond = 1.0

ns = nanosecond

second = _pre.giga * nanosecond
millisecond = _pre.milli * second
microsecond = _pre.micro * second
picosecond = _pre.pico * second
femtosecond = _pre.femto * second
attosecond = _pre.atto * second
zeptosecond = _pre.zepto * second
yoctosecond = _pre.yocto * second

s = second
ms = millisecond
us = microsecond
ps = picosecond
fs = femtosecond
# shortcut "as = attosecond" not possible since "as" is a reserved word ;-)
zs = zeptosecond
ys = yoctosecond

minute = 60 * second
hour = 60 * minute
day = 24 * hour
year = 365.25 * day

h = hour
d = day
y = year

hertz = 1.0 / second

kilohertz = _pre.kilo * hertz
megahertz = _pre.mega * hertz
gigahertz = _pre.giga * hertz
terahertz = _pre.tera * hertz

Hz = hertz

kHz = kilohertz
MHz = megahertz
GHz = gigahertz
THz = terahertz

# --------------------------------------------------------------------
# Units of energy
# --------------------------------------------------------------------
megaelectronvolt = 1.0

electronvolt = _pre.micro * megaelectronvolt

zettaelectronvolt = _pre.zetta * electronvolt
exaelectronvolt = _pre.exa * electronvolt
petaelectronvolt = _pre.peta * electronvolt
teraelectronvolt = _pre.tera * electronvolt
gigaelectronvolt = _pre.giga * electronvolt
kiloelectronvolt = _pre.kilo * electronvolt

ZeV = zettaelectronvolt
EeV = exaelectronvolt
PeV = petaelectronvolt
TeV = teraelectronvolt
GeV = gigaelectronvolt
MeV = megaelectronvolt
keV = kiloelectronvolt
eV = electronvolt

electronvolt2 = electronvolt * electronvolt

eV2 = electronvolt2

# --------------------------------------------------------------------
# Units of electric charge
# --------------------------------------------------------------------
eplus = 1.0  # positron charge

# --------------------------------------------------------------------
# Units of temperature
# --------------------------------------------------------------------
kelvin = 1.0

K = kelvin

# --------------------------------------------------------------------
# Units of amount of substance
# --------------------------------------------------------------------
mole = 1.0

mol = mole

# --------------------------------------------------------------------
# Units of luminous intensity
# --------------------------------------------------------------------
candela = 1.0

cd = candela

# --------------------------------------------------------------------
# Units of angles
# --------------------------------------------------------------------
radian = 1.0  # plane angle
steradian = 1.0  # solid angle

rad = radian
sr = steradian

milliradian = _pre.milli * radian
mrad = milliradian

degree = (_pi / 180.0) * radian

deg = degree

# --------------------------------------------------------------------
# Derived units
# --------------------------------------------------------------------

# Positron charge
e_SI = 1.602176634e-19  # exact value, taken from PDG 2022


# Electric charge
# --------------------------------------------------------------------
coulomb = eplus / e_SI

C = coulomb

# Electric current
ampere = coulomb / second

milliampere = _pre.milli * ampere
microampere = _pre.micro * ampere
nanoampere = _pre.nano * ampere

A = ampere

mA = milliampere
uA = microampere
nA = nanoampere

# Energy
joule = electronvolt / e_SI  # joule = 6.24151e+12 * MeV

gigajoule = _pre.giga * joule
megajoule = _pre.mega * joule
kilojoule = _pre.kilo * joule

J = joule

GJ = gigajoule
MJ = megajoule
kJ = kilojoule

erg = 1.0e-7 * joule

# Power
watt = joule / second

gigawatt = _pre.giga * watt
megawatt = _pre.mega * watt
kilowatt = _pre.kilo * watt

W = watt

GW = gigawatt
MW = megawatt
kW = kilowatt

# Force
newton = joule / meter

N = newton

dyne = 1.0e-5 * newton

# Pressure
pascal = newton / meter2

Pa = pascal

bar = 1.0e5 * pascal

millibar = _pre.milli * bar

mbar = millibar

atmosphere = 101325.0 * pascal

atm = atmosphere

# Mass [E][T^2][L^-2]
kilogram = joule * second * second / meter2
gram = _pre.milli * kilogram

quettagram = _pre.quetta * gram
ronnagram = _pre.ronna * gram
milligram = _pre.milli * gram
rontogram = _pre.ronto * gram

Qg = quettagram
Rg = ronnagram
kg = kilogram
g = gram
mg = milligram
rg = rontogram

# Electric potential
megavolt = megaelectronvolt / eplus
volt = _pre.micro * megavolt
kilovolt = _pre.kilo * volt

MV = megavolt
kV = kilovolt
V = volt

# Electric capacitance
farad = coulomb / volt

millifarad = _pre.milli * farad
microfarad = _pre.micro * farad
nanofarad = _pre.nano * farad
picofarad = _pre.pico * farad

F = farad
mF = millifarad
uF = microfarad
nF = nanofarad
pF = picofarad

# Electric resistance
ohm = volt / ampere

# Magnetic Field
tesla = volt * second / meter2

T = tesla

gauss = 1.0e-4 * tesla

kilogauss = _pre.kilo * gauss

G = gauss
Gs = gauss
kG = kilogauss
kGs = kilogauss

# Magnetic Flux
weber = volt * second

milliweber = _pre.milli * weber
microweber = _pre.micro * weber
nanoweber = _pre.nano * weber

Wb = weber

mWb = milliweber
uWb = microweber
nWb = nanoweber

# Inductance
henry = weber / ampere

H = henry

# --------------------------------------------------------------------
# Units derived from luminous intensity
# --------------------------------------------------------------------

# Luminous flux
lumen = candela * steradian

lm = lumen

# Illuminance, i.e. amount of luminous flux per unit area
lux = lumen / meter2

lx = lux

# --------------------------------------------------------------------
# Units for radiation
# --------------------------------------------------------------------

# Activity
becquerel = 1.0 / second

kilobecquerel = _pre.kilo * becquerel
megabecquerel = _pre.mega * becquerel
gigabecquerel = _pre.giga * becquerel

Bq = becquerel

kBq = kilobecquerel
MBq = megabecquerel
GBq = gigabecquerel

curie = 3.7e10 * becquerel

millicurie = _pre.milli * curie
microcurie = _pre.micro * curie
nanocurie = _pre.nano * curie

Ci = curie

mCi = millicurie
uCi = microcurie
nCi = nanocurie

# Absorbed dose
gray = joule / kilogram

megagray = _pre.mega * gray
kilogray = _pre.kilo * gray
milligray = _pre.milli * gray
microgray = _pre.micro * gray

Gy = gray

MGy = megagray
kGy = kilogray
mGy = milligray
uGy = microgray

# Dose equivalent
sievert = joule / kilogram

Sv = sievert

__all__ = (
    "GJ",
    "GW",
    "MJ",
    "MV",
    "MW",
    "MW",
    "A",
    "Bq",
    "C",
    "Ci",
    "EeV",
    "F",
    "G",
    "GBq",
    "GHz",
    "GeV",
    "Gs",
    "Gy",
    "H",
    "Hz",
    "J",
    "K",
    "MBq",
    "MGy",
    "MHz",
    "MeV",
    "N",
    "Pa",
    "PeV",
    "Qg",
    "Rg",
    "Sv",
    "T",
    "THz",
    "TeV",
    "V",
    "W",
    "Wb",
    "ZeV",
    "ab",
    "ampere",
    "angstrom",
    "atm",
    "atmosphere",
    "attobarn",
    "attosecond",
    "bar",
    "barn",
    "becquerel",
    "candela",
    "cd",
    "centimeter",
    "centimeter2",
    "centimeter3",
    "cm",
    "cm2",
    "cm3",
    "coulomb",
    "curie",
    "d",
    "day",
    "deg",
    "degree",
    "dyne",
    "eV",
    "eV2",
    "e_SI",
    "electronvolt",
    "electronvolt2",
    "eplus",
    "erg",
    "exaelectronvolt",
    "farad",
    "fb",
    "femtobarn",
    "femtometer",
    "femtosecond",
    "fermi",
    "fm",
    "fm2",
    "fm3",
    "fs",
    "g",
    "gauss",
    "gigabecquerel",
    "gigaelectronvolt",
    "gigahertz",
    "gigajoule",
    "gigawatt",
    "gram",
    "gray",
    "h",
    "henry",
    "hertz",
    "hour",
    "invab",
    "invfb",
    "invmb",
    "invnb",
    "invpb",
    "invub",
    "joule",
    "kBq",
    "kG",
    "kGs",
    "kGy",
    "kHz",
    "kJ",
    "kV",
    "kW",
    "keV",
    "kelvin",
    "kg",
    "kilobecquerel",
    "kiloelectronvolt",
    "kilogauss",
    "kilogram",
    "kilogray",
    "kilohertz",
    "kilojoule",
    "kilometer",
    "kilometer2",
    "kilometer3",
    "kilovolt",
    "kilowatt",
    "km",
    "km2",
    "km3",
    "lm",
    "lumen",
    "lux",
    "lx",
    "m",
    "m2",
    "m3",
    "mA",
    "mCi",
    "mF",
    "mGy",
    "mWb",
    "mb",
    "mbar",
    "megabecquerel",
    "megaelectronvolt",
    "megagray",
    "megahertz",
    "megajoule",
    "megavolt",
    "megawatt",
    "meter",
    "meter2",
    "meter3",
    "mg",
    "microampere",
    "microbarn",
    "microcurie",
    "microfarad",
    "microgray",
    "micrometer",
    "micron",
    "microsecond",
    "microweber",
    "milliampere",
    "millibar",
    "millibarn",
    "millicurie",
    "millifarad",
    "milligram",
    "milligray",
    "millimeter",
    "millimeter2",
    "millimeter3",
    "milliradian",
    "millisecond",
    "milliweber",
    "minute",
    "mm",
    "mm2",
    "mm3",
    "mol",
    "mole",
    "mrad",
    "ms",
    "nA",
    "nCi",
    "nF",
    "nWb",
    "nanoampere",
    "nanobarn",
    "nanocurie",
    "nanofarad",
    "nanometer",
    "nanosecond",
    "nanoweber",
    "nb",
    "newton",
    "ns",
    "ohm",
    "pF",
    "pascal",
    "pb",
    "petaelectronvolt",
    "picobarn",
    "picofarad",
    "picosecond",
    "ps",
    "quettagram",
    "rad",
    "radian",
    "rg",
    "ronnagram",
    "rontogram",
    "s",
    "second",
    "sievert",
    "sr",
    "steradian",
    "teraelectronvolt",
    "terahertz",
    "tesla",
    "uA",
    "uCi",
    "uF",
    "uGy",
    "uWb",
    "ub",
    "us",
    "volt",
    "watt",
    "weber",
    "y",
    "year",
    "yoctosecond",
    "ys",
    "zeptosecond",
    "zettaelectronvolt",
    "zs",
)


def __dir__() -> list[str]:
    return list(__all__)
