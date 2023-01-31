"""Lint Python code command."""

from cly.colors import print_flashy
from cly.utils import run_command

from ..config import PROJECT_ROOT, PROSPECTOR_DIRECTORIES


def lint(shell: bool = False) -> None:
    """
    Lint project Python and Shell script code.

    Parameters
    ----------
    shell : bool, optional
        Lint project's Shell script code if True; Otherwise, lint project's
        Python code, by default False

    """
    if shell:
        shell_files = [
            file.as_posix()
            for file in PROJECT_ROOT.glob("**/*.sh")
            if all(ignore not in file.as_posix() for ignore in [".venv/"])
        ]
        names = " ".join(shell_files)
        print_flashy(f"Linting shell file(s)...")
        run_command(f"shellcheck {names}")
    else:
        for directory in PROSPECTOR_DIRECTORIES:
            print_flashy(f"Linting {directory}...")
            run_command("prospector", directory)
