"""Lint Python code command."""

from cly.colors import print_flashy
from cly.utils import run_command

from ..config import PROSPECTOR_DIRECTORIES


def lint() -> None:
    """Lint project source code and tests."""
    for directory in PROSPECTOR_DIRECTORIES:
        print_flashy(f"Linting {directory}...")
        run_command("prospector", directory)
