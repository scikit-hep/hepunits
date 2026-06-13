# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## Commands

```bash
uv run pytest                       # run the test suite
uv run pytest tests/units           # run a single directory
uv run pytest tests/test_pint.py::test_name   # run a single test
nox -s tests                        # tests in an isolated env (installs .[test])
nox -s lint                         # runs pre-commit across all files
prek -a --quiet                     # lint directly (ruff, mypy, etc.)
```

`pytest` is configured with `filterwarnings = ["error"]` and `xfail_strict`, so any
warning fails the suite. Pint is an optional test dependency pinned `<0.25.1`.

## Architecture

`hepunits` defines units and constants in the **HEP System of Units** (the CLHEP
convention used by GEANT4/Gaudi), *not* SI. The base units are: length=mm, time=ns,
energy=MeV, charge=eplus. Everything else is derived as a plain `float` relative to
these bases — there is no quantity/dimension type. A "value with units" is just a
number; you attach units by multiplying (`500 * keV`) and read them back by dividing
(`x / GeV`).

Dependency order of the core modules (each imports only from those above it):

1. `units/prefixes.py` — SI and binary prefixes (`kilo`, `milli`, `mebi`, ...) as floats.
2. `units/units.py` — base units set to `1.0`, then every other unit derived
   arithmetically from them and from prefixes (imported as `_pre`). This is the root of
   truth for numeric values; e.g. `meter = _pre.kilo * millimeter`,
   `kilogram = joule * second**2 / meter2`.
3. `constants/constants.py` — physical constants (`c_light`, `hbar`, `Avogadro`, ...)
   computed from the units. Imports `from ..units.units import ...`.
4. Top-level `__init__.py` re-exports everything flat, so `from hepunits import GeV` and
   `from hepunits.units import GeV` both work.

The `units/__init__.py` and `constants/__init__.py` re-export from their submodules; the
`.units`/`.constants` subpackage `__init__` files exist mainly to provide these flat
namespaces.

`pint.py` is the only module with logic beyond definitions: optional Pint interop via
`to_clhep` / `from_clhep`. It maps Pint base dimensions to CLHEP base-unit strings in
`_clhep_base_units`. Importing it without Pint installed raises `ImportError`.

## The `__all__` invariant

Every public module maintains an explicit `__all__` and a `__dir__` returning it.
`tests/test_missing_all.py` enforces two things mechanically:

- **`test_missing_all`**: a module's `__all__` must exactly equal its public namespace
  (every non-underscore name defined or imported in the module).
- **`test_exported`**: every name in a submodule's `__all__` must also appear in its
  parent's `__all__`, all the way up to the top-level `hepunits.__all__`.

**When you add or rename any unit, constant, or prefix, you must update `__all__` (and the
matching import lists) in every module up the chain** — the defining module, its package
`__init__`, and the top-level `__init__.py`. The lists are kept alphabetically sorted
(ruff `RUF022` style). Skipping a level fails the test suite.

## Conventions

- Python 3.9+; mypy runs in `strict` mode over `src` (targeting 3.13). Keep things typed.
- Ruff enforces a broad rule set including no `print` (`T20`) and `pathlib` over `os.path`.
- Version is derived from VCS tags via `hatch-vcs` into `src/hepunits/_version.py` (do
  not edit that file).
- Numeric values follow the PDG review (currently 2020/2022); cite the source in a comment
  when adding a constant, matching the existing `# exact value, taken from PDG 2022` style.
