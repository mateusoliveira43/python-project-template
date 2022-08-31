"""Format and check Python code command."""

from cly.colors import print_flashy
from cly.utils import run_command

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
        # TODO run both and exit status code of sum
        run_command(f"black --check --diff {PROJECT_ROOT}")
        run_command(f"isort --check --diff {PROJECT_ROOT}")
    else:
        print_flashy("Formatting code...")
        run_command(f"black {PROJECT_ROOT}")
        run_command(f"isort {PROJECT_ROOT}")
