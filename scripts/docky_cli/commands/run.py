"""Run commands in Docker's Container."""

from typing import List, Optional

from cly.colors import print_flashy
from cly.utils import run_command

from ..config import SERVICE_NAME
from ..errors import check_docker_and_compose
from . import COMMON_COMMAND
from .env_file import create_env_file


def run_command_in_container(command: List[Optional[str]]) -> None:
    """
    Run service's Container default command or run a custom command in it.

    Parameters
    ----------
    command : List[Optional[str]]
        Command to run instead of Container's default command.

    """
    print_flashy("Running command in Container")
    run_command(
        [
            *COMMON_COMMAND,
            "run",
            "--rm",
            SERVICE_NAME,
            *command,  # type: ignore
        ]
    )


def run(command: List[Optional[str]]) -> None:
    """
    Run service's Container default command or run a custom command in it.

    If images are not yet built, they are build before running the command.

    If no command is passed, runs the Container's default command. Otherwise,
    runs the passed commands in the Container and exits.

    Parameters
    ----------
    command : List[Optional[str]]
        Command to run instead of Container's default command.

    """
    create_env_file()
    check_docker_and_compose()
    run_command_in_container(command)
