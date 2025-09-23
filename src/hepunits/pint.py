"""Conversion routines between CLHEP and Pint units

CLHEP adopts the approach where all the quantities are stored in the base unit
system, effectively dimensionless. Pint offers to store both the magnitude and
the dimensionality of the unit, which is helpful in deducing and/or validating
the resulting unit of formulas. This module offers conversion routines between
Pint's default base unit system and CLHEP.
"""

from __future__ import annotations

try:
    import pint
except ImportError as exc:
    msg = "pint is required to use hepunits.pint"
    raise ImportError(msg) from exc

# TODO: support more unit conversions
_clhep_base_units = {
    "[length]": "millimeter",
    "[time]": "nanosecond",
    "[mass]": "MeV * millimeter**-2 * nanosecond**2",
    "[current]": "elementary_charge / nanosecond",
}


def _unit_from(val: pint.Quantity | pint.Unit) -> pint.Unit:
    """Extract the dimensionality from a Pint Quantity or Unit"""
    # Grabbing the type is a quick way to be in the correct unit registry
    # see e.g. https://github.com/hgrecco/pint/issues/2207
    unit = type(val.units) if isinstance(val, pint.Quantity) else type(val)
    out = unit("dimensionless")
    for dim, exponent in val.dimensionality.items():
        if dim not in _clhep_base_units:
            msg = f"Unsupported dimension {dim} in {val}"
            raise ValueError(msg)
        out *= unit(_clhep_base_units[dim]) ** exponent

    return out


def to_clhep(val: pint.Quantity | pint.Unit) -> float:
    """Convert a Pint Quantity or Unit to CLHEP base units

    Parameters
    ----------
    val : pint.Quantity or pint.Unit
        The value to convert

    Returns
    -------
    float
        The value in CLHEP base units (dimensionless)
    """
    clhep_unit = _unit_from(val)
    q = pint.Quantity(1.0, val) if isinstance(val, pint.Unit) else val
    return q.to(clhep_unit).magnitude  # type: ignore[no-any-return]


def from_clhep(val: float, unit: pint.Unit) -> pint.Quantity:
    """Convert a value in CLHEP base units to a Pint Quantity

    Parameters
    ----------
    val : float
        The value in CLHEP base units (dimensionless)
    unit : pint.Unit
        The desired output unit

    Returns
    -------
    pint.Quantity
        The value in the desired unit
    """
    clhep_unit = _unit_from(unit)
    return pint.Quantity(val, clhep_unit).to(unit)
