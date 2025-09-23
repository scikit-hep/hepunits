import pint
from pytest import approx
import pytest

import hepunits
from hepunits.pint import from_clhep, to_clhep


def test_pint_constants():
    ureg = pint.UnitRegistry()

    # These three constants set the relationship between mass, length, time, and charge
    # TODO: check all 7 SI defining constants (hence also supporting more unit conversions)
    pint_c = to_clhep(1 * ureg.speed_of_light)
    assert pint_c == approx(hepunits.c_light, rel=1e-15)
    pint_h = to_clhep(1 * ureg.planck_constant)
    assert pint_h == approx(hepunits.h_Planck, rel=1e-15)
    pint_e = to_clhep(1 * ureg.elementary_charge)
    assert pint_e == approx(1.0, rel=1e-15)


def test_pint_roundtrip():
    ureg = pint.UnitRegistry()

    assert to_clhep(3 * ureg.mm) == approx(3.0)
    assert to_clhep(3 * ureg.cm) == approx(30.0)
    assert to_clhep(2 * ureg.ohm) == approx(2.0 * hepunits.ohm)
    assert to_clhep(ureg.coulomb) == approx(hepunits.coulomb)

    assert (
        from_clhep(hepunits.c_light, ureg.meter / ureg.second).m
        == (1.0 * ureg.c).to(ureg.meter / ureg.second).m
    )
    assert from_clhep(hepunits.tesla, ureg.tesla).m == (1 * ureg.tesla).m

def test_unsupported_dimension():
    ureg = pint.UnitRegistry()
    with pytest.raises(ValueError, match="Unsupported dimension"):
        to_clhep(1 * ureg.kelvin)