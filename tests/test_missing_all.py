import sys

import pytest

import hepunits


def filter_module(item: str) -> bool:
    if item == "__version__":
        return True
    if item.startswith("_"):
        return False
    if item in {"List"}:
        return False
    return True


@pytest.mark.skipif(
    sys.version_info < (3, 7), reason="Python 3.7+ added __dir__ support"
)
@pytest.mark.parametrize(
    "module",
    (
        hepunits,
        hepunits.units,
        hepunits.constants,
        hepunits.constants.constants,
        hepunits.units.prefixes,
        hepunits.units.units,
    ),
)
def test_missing_all(module):
    assert set(dir(module)) == set(module.__all__)

    full_module = {it for it in module.__dict__ if filter_module(it)}
    assert full_module == set(module.__all__)


def test_exported():
    expr = set(hepunits.units.__all__) - (set(hepunits.__all__) | {"prefixes"})
    assert not expr

    expr = set(hepunits.constants.__all__) - set(hepunits.__all__)
    assert not expr

    expr = set(hepunits.constants.constants.__all__) - set(hepunits.constants.__all__)
    assert not expr

    expr = set(hepunits.units.prefixes.__all__) - set(hepunits.units.__all__)
    assert not expr

    expr = set(hepunits.units.units.__all__) - set(hepunits.units.__all__)
    assert not expr
