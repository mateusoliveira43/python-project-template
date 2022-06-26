"""Test project version."""

from pathlib import Path

import toml

import source


def test_project_version() -> None:
    """
    Test if project version is correct.

    GIVEN `pyproject.toml:version` and `source.__version__`
    WHEN compared
    THEN they should be the same
    """
    with open(
        Path(source.__file__).resolve().parents[1] / "pyproject.toml",
        encoding="utf-8",
    ) as pyproject_file:
        pyproject = toml.loads(pyproject_file.read())

    pyproject_version = pyproject["tool"]["poetry"]["version"]

    assert source.__version__ == pyproject_version
