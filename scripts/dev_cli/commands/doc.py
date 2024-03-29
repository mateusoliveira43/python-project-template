"""Generate and check project documentation command."""

from tempfile import TemporaryDirectory

from cly.colors import print_flashy
from cly.utils import run_command

from ..config import (
    DOCUMENTATION_FOLDER,
    DOCUMENTATION_OUTPUT_FOLDER,
    SOURCE_FOLDER,
)


def doc(check: bool = False) -> None:
    """
    Generate project documentation.

    Parameters
    ----------
    check : bool, optional
        Check if project documentation is ok, by default False

    """
    run_command(
        [
            "sphinx-apidoc",
            "--force",
            "-q",
            "--module-first",
            "--private",
            "--output-dir",
            (DOCUMENTATION_FOLDER / "modules").as_posix(),
            SOURCE_FOLDER.as_posix(),
        ]
    )
    if check:
        print_flashy("Checking documentation...")
        with TemporaryDirectory() as temporary_directory:
            run_command(
                "sphinx-build -WTvna "
                f"{DOCUMENTATION_FOLDER} {temporary_directory}"
            )
    else:
        print_flashy("Generating documentation...")
        run_command(
            f"sphinx-build -vna {DOCUMENTATION_FOLDER} "
            f"{DOCUMENTATION_OUTPUT_FOLDER}"
        )
