import subprocess
from typing import List, Optional, Union

from .colors import color_text as color_text

SPACE: str

def parse_arguments(arguments: Union[str, List[str]]) -> str: ...
def get_output(
    arguments: Union[str, List[str]],
) -> subprocess.CompletedProcess: ...  # type: ignore
def get_returncode(arguments: Union[str, List[str]]) -> int: ...
def get_standard_output(
    arguments: Union[str, List[str]], lines: bool = ...
) -> Optional[List[str]]: ...
def run_command(
    arguments: Union[str, List[str]],
) -> subprocess.CompletedProcess: ...  # type: ignore
