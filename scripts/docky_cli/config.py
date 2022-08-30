"""Config file for Docky."""

from pathlib import Path

USER_NAME: str = "develop"
SERVICE_NAME: str = "python-project-template"
PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent.parent
COMPOSE_FILE: Path = PROJECT_ROOT / "docker/docker-compose.yaml"
DOCKER_FILE: Path = PROJECT_ROOT / "docker/Dockerfile"

COMMON_COMMAND = [
    "docker-compose",
    "--file",
    COMPOSE_FILE.as_posix(),
    "--project-directory",
    PROJECT_ROOT.as_posix(),
]
