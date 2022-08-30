"""Remove Docker dependencies management command."""

from cly.colors import print_flashy
from cly.utils import run_command

from ..config import COMMON_COMMAND
from ..errors import check_docker_and_compose
from .env_file import create_env_file


def remove_dependencies() -> None:
    """
    Remove all Containers, Networks, Images and Volumes in compose file.

    Reads project's compose file, and removes all of it's dependencies from
    host machine.
    """
    print_flashy("Removing Containers, Networks, Images and Volumes")
    run_command(
        [
            *COMMON_COMMAND,
            "down",
            "--volumes",
            "--rmi",
            "'all'",
        ]
    )


def down() -> None:
    """Remove all Containers, Networks, Images and Volumes in compose file."""
    create_env_file()
    check_docker_and_compose()
    remove_dependencies()
