"""Project's tests."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_FOLDER = PROJECT_ROOT / "scripts"
if SCRIPTS_FOLDER.exists():
    # Since scripts is not a Python package, this is needed
    sys.path.append(SCRIPTS_FOLDER.as_posix())
