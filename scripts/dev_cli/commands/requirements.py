"""Update Python requirements files."""

from cly.colors import print_flashy
from cly.utils import run_command

from ..config import PROJECT_ROOT


def requirements() -> None:
    """
    Update Python requirements files.

    Runs Poetry export command inside a Docker container to update Python
    requirements files.

    """
    base_command = (
        f"docker container run -ti -w /tests -v {PROJECT_ROOT}:/tests --rm "
        "mateusoliveira43/poetry poetry export --format requirements.txt "
        "--output"
    )
    print_flashy("Checking Python requirements file(s)...")
    run_command(f"{base_command} requirements/prod.txt")
    run_command(f"{base_command} requirements/dev.txt --with dev")
