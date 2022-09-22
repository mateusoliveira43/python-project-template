"""Testing environment for CLY?! object."""

import sys
from contextlib import redirect_stderr, redirect_stdout
from tempfile import TemporaryFile
from typing import List, Tuple
from unittest.mock import patch

from .config import ConfiguredParser


def run_cli(
    cli: ConfiguredParser, arguments: List[str]
) -> Tuple[int, str, str]:
    """
    Run CLY?! object with desired arguments and capturing output.

    Parameters
    ----------
    cli : ConfiguredParser
        CLY?! object.
    arguments : List[str]
        Arguments to pass to CLY?! object.

    Returns
    -------
    Tuple[int, str, str]
        Tuple with the following elements, in this order

        - Exit code
        - Standard output (stdout)
        - Standard error (stderr)

        from CLI?! object execution

    """
    with TemporaryFile(mode="w+", encoding="utf-8") as stdout:
        with TemporaryFile(mode="w+", encoding="utf-8") as stderr:
            with patch.object(sys, "argv", ["file_name", *arguments]):
                with redirect_stdout(stdout):
                    with redirect_stderr(stderr):
                        try:
                            cli()
                            exit_code = 0
                        except SystemExit as sys_exit:  # NOSONAR
                            exit_code = sys_exit.code
            stderr.seek(0, 0)
            standard_error = stderr.read()
        stdout.seek(0, 0)
        standard_output = stdout.read()
    return exit_code, standard_output, standard_error
