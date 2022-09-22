"""Docky commands."""

from ..config import COMPOSE_FILE, PROJECT_ROOT

COMMON_COMMAND = [
    "docker-compose",
    "--file",
    COMPOSE_FILE.as_posix(),
    "--project-directory",
    PROJECT_ROOT.as_posix(),
]
