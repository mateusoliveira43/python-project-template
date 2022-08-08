"""Test project version."""

from pathlib import Path

import pytest
import toml

import source

VERSION_LABELS = source.__version__.split(".", maxsplit=2)


def test_project_version() -> None:
    """
    Test if project's versions are the same.

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


@pytest.mark.parametrize(
    "label", VERSION_LABELS, ids=["major", "minor", "patch"]
)
def test_version_format(label: str) -> None:
    """
    Test if project's version is in the correct format.

    GIVEN one of `source.__version__` labels
    WHEN checked it's characters
    THEN they should be digits

    Parameters
    ----------
    label : str
        One of the labels of the project's version.

    """
    assert label.isdigit()
