from pathlib import Path
from typing import List
from unittest import TestCase

import pytest
import toml
from cly.utils import get_standard_output

import source

PROJECT_ROOT = Path(__file__).resolve().parent.parent
VERSION_LABELS = source.__version__.split(".", maxsplit=2)


def read_variable_from_file(variable_name: str, file_path: Path) -> str:
    """
    Read a variable from a file.
    Parameters
    ----------
    variable_name : str
        Name of the variable in the file.
    file_path : Path
        Path of the file to be read.
    Returns
    -------
    str
        Variable value, if it exists in the file; empty string otherwise.
    """
    with open(file_path, mode="r", encoding="utf-8") as file:
        for line in file:
            if line.strip().startswith(variable_name):
                return line.strip().split("=", maxsplit=1)[1].strip()
        return ""


def test_pyproject_version() -> None:
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


class TestSemanticVersioning(TestCase):
    """Test semantic versioning as described in https://semver.org/."""

    previous_version_labels: List[str]

    @classmethod
    def setUpClass(cls) -> None:
        previous_version = get_standard_output("git describe --tag --abbrev=0")
        if isinstance(previous_version, list):
            cls.previous_version_labels = previous_version[0].split(
                ".", maxsplit=2
            )
        else:
            pytest.skip(reason="No previous version")

    @staticmethod
    def alert_increment(label: str) -> str:
        return f"{label} version MUST be incremented."

    @staticmethod
    def alert_reset(label: str, change: str) -> str:
        return (
            f"{label} version MUST be reset to 0 when "
            f"{change} version is incremented."
        )

    def test_major(self) -> None:
        assert int(VERSION_LABELS[0]) >= int(
            self.previous_version_labels[0]
        ), self.alert_increment("Major")

    def test_minor(self) -> None:
        if int(VERSION_LABELS[0]) > int(self.previous_version_labels[0]):
            assert int(VERSION_LABELS[1]) == 0, self.alert_reset(
                "Minor", "Major"
            )
        else:
            assert int(VERSION_LABELS[1]) >= int(
                self.previous_version_labels[1]
            ), self.alert_increment("Minor")

    def test_patch(self) -> None:
        if int(VERSION_LABELS[0]) > int(self.previous_version_labels[0]):
            assert int(VERSION_LABELS[2]) == 0, self.alert_reset(
                "Patch", "Major"
            )
        elif int(VERSION_LABELS[1]) > int(self.previous_version_labels[1]):
            assert int(VERSION_LABELS[2]) == 0, self.alert_reset(
                "Patch", "Minor"
            )
        else:
            assert int(VERSION_LABELS[2]) >= int(
                self.previous_version_labels[2]
            ), self.alert_increment("Patch")
