import argparse
from typing import Any, Callable, Dict, Optional

from _typeshed import Incomplete

from .colors import color_text as color_text
from .docstring import get_help_from_docstring as get_help_from_docstring
from .docstring import (
    get_param_help_from_docstring as get_param_help_from_docstring,
)

USAGE_PREFIX: str
POSITIONALS_TITLE: str
OPTIONALS_TITLE: str
HELP_MESSAGE: str
VERSION_MESSAGE: str
MAJOR_VERSION: int
MINOR_VERSION: int
PYTHON_MINIMUM_VERSION: Incomplete

def check_python_minimum_version() -> None: ...
def decorate_kwargs(func: Callable[..., Any]) -> Callable[..., Any]: ...

class CustomFormatter(argparse.HelpFormatter):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class ConfiguredParser:
    name: str
    description: str
    epilog: str
    version: str
    add_help: bool
    parser: argparse.ArgumentParser
    subparser: Optional[argparse._SubParsersAction]  # type: ignore
    commands: Optional[Dict[str, Callable[..., Any]]]
    def __init__(
        self, config: Dict[str, str], add_help: bool = ...
    ) -> None: ...
    def create_parser(self) -> argparse.ArgumentParser: ...
    def create_subparser(
        self,
    ) -> argparse._SubParsersAction: ...  # type: ignore
    def create_command(
        self,
        command: Callable[..., Any],
        alias: Optional[str] = ...,
        help_message: Optional[str] = ...,
    ) -> argparse.ArgumentParser: ...
    def get_arguments(self) -> argparse.Namespace: ...
    def __call__(self) -> None: ...
