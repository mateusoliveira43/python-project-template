"""List all Docker objects management command."""

from cly.colors import print_flashy
from cly.utils import run_command

from ..config import SERVICE_NAME
from ..errors import check_docker
from .env_file import create_env_file


def list_docker_objects(show_all: bool = False) -> None:
    """
    List all Containers, Networks, Images and Volumes in compose file.

    Parameters
    ----------
    show_all : bool
        List all Containers, Networks, Images and Volumes in host machine
        , by default False

    """
    create_env_file()
    check_docker()

    service_filter = "" if show_all else f" --filter name={SERVICE_NAME}"
    print_flashy("Listing Containers")
    run_command(f"docker container ls --all{service_filter}")
    print_flashy("Listing Networks")
    run_command(f"docker network ls {service_filter}")
    print_flashy("Listing Images")
    run_command(
        f"docker image ls --all{''if show_all else f' {SERVICE_NAME}'}"
    )
    print_flashy("Listing Volumes")
    run_command(f"docker volume ls{service_filter}")
