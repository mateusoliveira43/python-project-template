"""Format and check Python code command."""

from cly.colors import print_flashy
from cly.utils import run_multiple_commands

from ..config import PROJECT_ROOT


def format_code(check: bool = False) -> None:
    """
    Format project's Python code.

    Parameters
    ----------
    check : bool, optional
        Only check if project's Python code format is correct, by default False

    """
    if check:
        print_flashy("Checking code format...")
        run_multiple_commands(
            [
                (f"black --check --diff {PROJECT_ROOT}", None),
                (f"isort --check --diff {PROJECT_ROOT}", None),
            ]
        )
    else:
        print_flashy("Formatting code...")
        run_multiple_commands(
            [
                (f"black {PROJECT_ROOT}", None),
                (f"isort {PROJECT_ROOT}", None),
            ]
        )
