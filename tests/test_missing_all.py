import pytest

import hepunits


def filter_module(item: str) -> bool:
    if item == "__version__":
        return True
    if item.startswith("_"):
        return False
    return item not in {"List"}


@pytest.mark.parametrize(
    "module",
    [
        hepunits.units,
        hepunits.constants,
        hepunits.constants.constants,
        hepunits.units.prefixes,
        hepunits.units.units,
    ],
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
