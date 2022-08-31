"""Utils functions for calling shell."""

# Scripts that manipulate the shell must always be careful with possible
# security implications.
import subprocess  # nosec
from typing import List, Optional, Union

from .colors import color_text

SPACE = " "


def parse_arguments(arguments: Union[str, List[str]]) -> str:
    """
    Parse arguments into a string.

    Parameters
    ----------
    arguments : Union[str, List[str]]
        A string, or list of strings, containing the commands and arguments.

    Returns
    -------
    str
        Parsed arguments.

    """
    if isinstance(arguments, list):
        return SPACE.join(arguments)
    return arguments


def get_output(
    arguments: Union[str, List[str]]
) -> subprocess.CompletedProcess:
    """
    Get the output information of the shell command.

    **Be careful about security implications when manipulating the shell!**

    Parameters
    ----------
    arguments : Union[str, List[str]]
        A string, or list of strings, containing the commands and arguments.

    Returns
    -------
    subprocess.CompletedProcess
        Command's output information.

    """
    command = parse_arguments(arguments)
    return subprocess.run(
        command,
        shell=True,  # nosec
        check=False,
        capture_output=True,
        encoding="utf-8",
    )


def get_returncode(arguments: Union[str, List[str]]) -> int:
    """
    Get the returncode of the shell command.

    **Be careful about security implications when manipulating the shell!**

    Parameters
    ----------
    arguments : Union[str, List[str]]
        A string, or list of strings, containing the commands and arguments.

    Returns
    -------
    int
        Command's returncode.

    """
    output = get_output(arguments)
    return output.returncode


def get_standard_output(
    arguments: Union[str, List[str]], lines: bool = False
) -> Optional[List[str]]:
    """
    Get the standard output of the shell command.

    **Be careful about security implications when manipulating the shell!**

    Parameters
    ----------
    arguments : Union[str, List[str]]
        A string, or list of strings, containing the commands and arguments.
    lines : bool
        Separate output in lines instead of separating in words, by default
        False.

    Returns
    -------
    output : Optional[List[str]]
        A list of strings containing the output's words or lines; else, None.

    """
    output = get_output(arguments).stdout
    if output:
        if lines:
            return [line for line in output.split("\n") if line]
        return [
            word for word in output.replace("\n", SPACE).split(SPACE) if word
        ]
    return None


def run_command(
    arguments: Union[str, List[str]]
) -> subprocess.CompletedProcess:
    """
    Run the shell command.

    **Be careful about security implications when manipulating the shell!**

    Parameters
    ----------
    arguments : Union[str, List[str]]
        A string, or list of strings, containing the commands and arguments.

    Returns
    -------
    subprocess.CompletedProcess
        Executes the command.

    Raises
    ------
    SystemExit
        If command fails.

    """
    command = parse_arguments(arguments)
    try:
        return subprocess.run(
            command, shell=True, check=True, encoding="utf-8"  # nosec
        )
    except subprocess.CalledProcessError as error:
        print(color_text(f"ERROR: {error}", "red"))
        raise SystemExit(error.returncode) from error
