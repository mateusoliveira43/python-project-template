"""Security vulnerability scan for Python code and dependencies."""

from cly.colors import print_flashy
from cly.utils import run_command


def scan(code: bool = False, dependencies: bool = False) -> None:
    """
    Security vulnerability scan.

    Parameters
    ----------
    code : bool, optional
        Scan Python code, by default False
    dependencies : bool, optional
        Scan Python dependencies, by default False

    """
    if code:
        print_flashy("Scanning Python code...")
        run_command("bandit --exclude ./tests,./.venv --recursive .")
    if dependencies:
        print_flashy("Scanning Python dependencies...")
        run_command("safety check --full-report --file requirements/prod.txt")
        run_command("safety check --full-report --file requirements/dev.txt")
