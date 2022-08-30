"""Lint Dockerfile using hadolint https://github.com/hadolint/hadolint."""

from cly.colors import print_flashy
from cly.utils import run_command

from ..config import DOCKER_FILE
from ..errors import check_docker


def lint() -> None:
    """Lint Dockerfile."""
    check_docker()
    print_flashy("Linting Dockerfile")
    run_command(
        [
            "docker",
            "run",
            "--rm",
            "--interactive",
            "ghcr.io/hadolint/hadolint",
            "<",
            DOCKER_FILE.as_posix(),
        ]
    )
