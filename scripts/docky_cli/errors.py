"""Error related functionalities."""

import shutil

from cly.colors import color_text


def alert_error(message: str) -> None:
    """
    Alert error to user.

    Parameters
    ----------
    message : str
        Error message.

    Raises
    ------
    SystemExit
        Exit with error code 1.

    """
    print(color_text(f"ERROR: {message}", "red"))
    raise SystemExit(1)


def check_docker() -> None:
    """
    Check if Docker is installed and in the path.

    Check if Docker ('docker' executable) is installed and in the path. If not,
    exits with error and message.

    """
    if shutil.which("docker") is None:
        alert_error("Docker is not installed or in the path.")


def check_compose() -> None:
    """
    Check if Docker Compose is installed and in the path.

    Check if Docker Compose ('docker-compose' executable) is installed and in
    the path. If not, exits with error and message.

    """
    if shutil.which("docker-compose") is None:
        alert_error("Docker Compose is not installed or in the path.")


def check_docker_and_compose() -> None:
    """
    Check if Docker and Docker Compose are installed and in the path.

    Check if Docker ('docker' executable) is installed and in the path. If not,
    exits with error and message.
    Check if Docker Compose ('docker-compose' executable) is installed and in
    the path. If not, exits with error and message.

    """
    check_docker()
    check_compose()
