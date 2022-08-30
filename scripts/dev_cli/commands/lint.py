from scripts.cly.colors import print_flashy
from scripts.cly.utils import run_command


def lint() -> None:
    """Lint project source code and tests."""
    print_flashy("Linting source code...")
    # TODO run commands in selected directory
    run_command("prospector")
    print_flashy("Linting tests...")
    run_command("prospector --profile tests/.prospector.yaml tests")
