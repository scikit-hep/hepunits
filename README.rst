hepunits: units and constants in the HEP system of units
========================================================

.. image:: https://dev.azure.com/scikit-hep/HepUnits/_apis/build/status/scikit-hep.hepunits?branchName=master
  :alt: Build Status
  :target: https://dev.azure.com/scikit-hep/hepunits/_build/latest?definitionId=5?branchName=master

.. image:: https://img.shields.io/azure-devops/coverage/scikit-hep/HepUnits/5.svg
  :alt: Coverage
  :target: https://dev.azure.com/scikit-hep/HepUnits/_build/latest?definitionId=5?branchName=master

.. image:: https://img.shields.io/azure-devops/tests/scikit-hep/HepUnits/5.svg
   :alt: Tests
   :target: https://dev.azure.com/scikit-hep/HepUnits/_build/latest?definitionId=5?branchName=master


``hepunits`` collects the most commonly used units and constants in the
HEP System of Units, as derived from the basic units originally defined by the `CLHEP`_ project,
which are *not* the same as the SI system of units:

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


It is largely based on the international system of units (`SI`_)

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

but augments it with handy definitions, changing the basic length and time units.

.. _CLHEP: http://proj-clhep.web.cern.ch/proj-clhep/
.. _SI: http://www.physics.nist.gov/cuu/Units/index.html


Installation
------------

Install ``hepunits`` like any other Python package:

.. code-block:: bash

    pip install hepunits

or similar (use ``--user``, ``virtualenv``, etc. if you wish).


Getting started
---------------

The module ``hepunits.constants`` contains 2 sorts of constants:
physical constants and commonly used constants.

The typical usage is the following:

.. code-block:: python

    >>> from hepunits.constants import c_light
    >>> from hepunits.units     import picosecond, micrometer
    >>> tau_Bs = 1.5 * picosecond    # a particle lifetime, say the Bs meson's
    >>> ctau_Bs = c_light * tau_Bs   # ctau of the particle, ~450 microns
    >>> print ctau_Bs                # result in HEP units, so mm
    0.449688687
    >>> print ctau_Bs / micrometer   # result in micrometers
    449.688687

Typical usage of the ``hepunits.units`` module:

.. code-block:: python

    >>> # add two quantities with length units and get the result in meters
    >>> from hepunits import units as u
    >>> (1 * u.meter + 5 * u.cm) / u.meter
    1.05
    >>> # the default result is, of course, in HEP units, so mm
    >>> 1 * u.meter + 5 * u.cm
    1050.0

.. code-block:: python

    >>> from hepunits.units import MeV, GeV
    >>> massWindow = 100 * MeV    # define a 100 MeV mass window
    >>> def energy_resolution():
    ...    # returns the energy resolution of 100 MeV
    ...    return 100 * MeV
    ...
    >>> energy_resolution() / GeV # get the energy resolution in GeV
    0.1
