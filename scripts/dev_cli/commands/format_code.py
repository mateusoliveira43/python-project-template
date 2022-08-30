from cly.colors import print_flashy
from cly.utils import run_command


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
        run_command("black --check --diff .")
        run_command("isort --check --diff .")
        # TODO run both and exit status code of sum
    else:
        print_flashy("Formatting code...")
        run_command("black .")
        run_command("isort .")
