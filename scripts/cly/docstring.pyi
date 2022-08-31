from typing import Any, Callable, List, Tuple

from _typeshed import Incomplete

NUMPY: str
GOOGLE: str
SPHINX: str
NUMPY_PARAMS: str
GOOGLE_PARAMS: str
SPHINX_PARAM: str
SPHINX_RETURNS: str
SPHINX_RAISES: str
DOCSTRING_SECTIONS: Incomplete
DOCSTRING_STYLES_PARAMS: Incomplete

def get_help_from_docstring(command: Callable[..., Any]) -> str: ...
def get_index_of_sphinx_param_section(
    docstring_lines: List[str],
) -> Tuple[int, str]: ...
def get_param_help_from_numpy_docstring(
    docstring_lines: List[str], index_param_section: int, param_name: str
) -> str: ...
def get_param_help_from_google_docstring(
    docstring_lines: List[str], index_param_section: int, param_name: str
) -> str: ...
def get_param_help_from_sphinx_docstring(
    docstring_lines: List[str], index_param_section: int, param_name: str
) -> str: ...
def get_param_help_from_docstring(
    param_name: str, command: Callable[..., Any]
) -> str: ...
