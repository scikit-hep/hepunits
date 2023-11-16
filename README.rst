``hepunits``: units and constants in the HEP system of units
============================================================

|Scikit-HEP| |PyPI version| |Conda-forge version| |Zenodo DOI|

|GitHub Actions Status: CI| |Code Coverage|


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

This HEP system of units is in use in many software libraries such as GEANT4 and Gaudi.

Note that many units are now *exact*, such as the speed of light in vacuum.
The package is in agreement with the values in the 2020 Particle Data Group review.

.. _CLHEP: http://proj-clhep.web.cern.ch/proj-clhep/
.. _SI: http://www.physics.nist.gov/cuu/Units/index.html


Installation
------------

Install ``hepunits`` like any other Python package, typically:

.. code-block:: bash

    python -m pip install hepunits

The package is also available on `conda-forge`_, and installable with

.. code-block:: bash

    conda install -c conda-forge hepunits

.. _conda-forge: https://github.com/conda-forge/hepunits-feedstock


Getting started
---------------

The package contains 2 modules, ``constants`` and ``units``,
whose names are self-explanatory.
It may be more readable to import quantities explicitly from each of the modules
though everything is available from the top-level as ``from hepunits import ...``.

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

Fancier usage
~~~~~~~~~~~~~

When working with data the user should not need to know what units are used in their
internal representation (it makes sense, though, and *is important*, to be consistent throughout the "data storages"!).

These simple rules are enough - exemplified in the code below:

- Dimensioned quantities in the "data stores" abide to the HEP system of units.

- All definitions of dimensioned quantities are dimensioned by multiplying by the units,
  as in ``mass_window = 500 * keV``.

- All output of dimensioned quantities is converted to the required units
  by dividing by the units, as in ``energy_resolution() / GeV``.

For the sake of argument, let's consider below a function returning a dimensioned quantity.
the function below stores a dimensioned quantity defined in keV
(the actual value is represented in MeV, which is the standard unit) and the caller simply needs
to ensure an explicit conversion to the desired unit dividing by it (GeV in the example):

.. code-block:: python

    >>> from hepunits.units import keV, MeV, GeV
    >>> mass_window = 1 * GeV    # define a 1 GeV mass window
    >>> def energy_resolution():
    ...    # returns the energy resolution of 500 keV
    ...    return 500. * keV  # numerical value is 0.5
    ...
    >>> energy_resolution() / GeV # get the energy resolution in GeV
    0.0005



.. |Scikit-HEP| image:: https://scikit-hep.org/assets/images/Scikit--HEP-Project-blue.svg
   :target: https://scikit-hep.org

.. |PyPI version| image:: https://img.shields.io/pypi/v/hepunits.svg
   :target: https://pypi.org/project/hepunits/

.. |Conda-forge version| image:: https://img.shields.io/conda/vn/conda-forge/hepunits.svg
   :target: https://github.com/conda-forge/hepunits-feedstock

.. |Zenodo DOI| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.7244906.svg
   :target: https://doi.org/10.5281/zenodo.7244906

.. |GitHub Actions Status: CI| image:: https://github.com/scikit-hep/hepunits/workflows/CI/badge.svg
   :target: https://github.com/scikit-hep/hepunits/actions

.. |Code Coverage| image:: https://codecov.io/gh/scikit-hep/hepunits/graph/badge.svg?branch=master
   :target: https://codecov.io/gh/scikit-hep/hepunits?branch=master
