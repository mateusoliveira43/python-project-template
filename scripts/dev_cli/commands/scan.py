from scripts.cly.colors import print_flashy
from scripts.cly.utils import run_command


def scan(code: bool = False, dependencies: bool = False) -> None:
    """Security vulnerability scan."""
    if code:
        print_flashy("Scanning Python code...")
        run_command("bandit --exclude ./tests,./.venv --recursive .")
    if dependencies:
        print_flashy("Scanning Python dependencies...")
        run_command("safety check --full-report --file requirements/prod.txt")
        run_command("safety check --full-report --file requirements/dev.txt")
