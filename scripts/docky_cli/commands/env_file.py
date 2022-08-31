""".env file management command."""

from typing import Dict

from cly.colors import color_text, print_flashy
from cly.utils import get_standard_output

from ..config import PROJECT_ROOT, SERVICE_NAME, USER_NAME, __file__
from ..errors import alert_error

ENV_FILE = PROJECT_ROOT / ".env"


def create_env_file() -> None:
    """Create .env file in project's root, if it does not already exists."""
    if not ENV_FILE.exists():
        if not SERVICE_NAME:
            alert_error(f"SERVICE_NAME is not set in {__file__}")
        if SERVICE_NAME != SERVICE_NAME.lower():
            alert_error(f"SERVICE_NAME is not lowercase in {__file__}")
        with open(ENV_FILE, mode="w", encoding="utf-8") as env_file:
            env_file.write(
                f"GROUP_ID={get_standard_output('id -g')[0]}\n"  # type: ignore
            )
            env_file.write(
                f"USER_ID={get_standard_output('id -u')[0]}\n"  # type: ignore
            )
            env_file.write(f"USER_NAME={USER_NAME}\n")
            env_file.write(f"SERVICE_NAME={SERVICE_NAME}\n")
            env_file.write(f"WORK_DIR=/home/{USER_NAME}/{SERVICE_NAME}\n")
            env_file.write("SNYK_TOKEN=\n")
        print_flashy(f".env file created in {PROJECT_ROOT}")


def read_env_file() -> Dict[str, str]:
    """
    Read variables in .env file.

    Returns
    -------
    Dict[str, str]
        Dict with keys being .env file's variable names and values being it's
        values.

    """
    with open(ENV_FILE, mode="r", encoding="utf-8") as env_file:
        variables = [
            line.split("=", maxsplit=1)
            for line in env_file.read().splitlines()
        ]
        return dict(variables)


def env(show: bool = False) -> None:
    """
    Create .env file in project's root, if it does not already exists.

    Parameters
    ----------
    show : bool
        Show variables in .env file, by default False

    """
    create_env_file()
    if show:
        variables = read_env_file()
        spacing = len(color_text(max(variables.keys(), key=len), "green"))
        for key, value in variables.items():
            key_name = color_text(key, "green" if value else "red").ljust(
                spacing
            )
            print(f"{key_name} = {value}")
