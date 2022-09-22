"""Start application with Docker's Containers."""

from cly.colors import print_flashy
from cly.utils import run_command

from ..errors import check_docker_and_compose
from . import COMMON_COMMAND
from .env_file import create_env_file


def start_all() -> None:
    """Start all services in compose file."""
    create_env_file()
    check_docker_and_compose()
    print_flashy("Starting application")
    run_command([*COMMON_COMMAND, "up"])
