"""Security vulnerability scan for Image using SNYK https://snyk.io/."""

from cly.colors import print_flashy
from cly.utils import get_standard_output, run_command

from ..config import DOCKER_FILE, SERVICE_NAME
from ..errors import alert_error, check_docker
from .env_file import ENV_FILE, create_env_file, read_env_file
from .run import run


def scan_image() -> None:
    """
    Scan service's Image for security vulnerabilities.

    You need to have an account in https://snyk.io/ to execute the scan.

    """
    token = read_env_file()["SNYK_TOKEN"]
    if not token:
        alert_error(
            f"SNYK_TOKEN not set in {ENV_FILE}. Get it at "
            "https://app.snyk.io/account"
        )
    if SERVICE_NAME not in get_standard_output(  # type: ignore
        f"docker image ls {SERVICE_NAME}"
    ):
        run(["echo", "Image built"])
    print_flashy("Scanning Image")
    run_command(["docker", "scan", "--login", "--token", token])
    try:
        run_command(
            [
                "docker",
                "scan",
                "--severity",
                "medium",
                "--file",
                DOCKER_FILE.as_posix(),
                SERVICE_NAME,
            ]
        )
    finally:
        run_command(["rm", "~/.config/configstore/snyk.json"])


def scan() -> None:
    """Scan service's Image for security vulnerabilities."""
    create_env_file()
    check_docker()
    scan_image()
