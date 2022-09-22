"""Docky Command Line Interface (CLI) package."""

import sys
from pathlib import Path

sys.path.append(Path(__file__).resolve().parent.parent.as_posix())

# https://github.com/mateusoliveira43/docky
__version__ = "1.1.1"  # major.minor.patch
