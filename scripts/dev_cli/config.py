"""Config file for development scripts."""

from pathlib import Path
from typing import List

PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent.parent
VIRTUAL_ENVIRONMENT: Path = PROJECT_ROOT / ".venv"
REQUIREMENTS_FOLDER: Path = PROJECT_ROOT / "requirements"
SOURCE_FOLDER = PROJECT_ROOT / "source"
TESTS_FOLDER: Path = PROJECT_ROOT / "tests"
DOCUMENTATION_FOLDER = PROJECT_ROOT / "docs"
DOCUMENTATION_OUTPUT_FOLDER = PROJECT_ROOT / "public"

PROSPECTOR_DIRECTORIES: List[Path] = [PROJECT_ROOT, TESTS_FOLDER]
