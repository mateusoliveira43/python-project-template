"""Configuration file for Sphinx."""

# -- Path setup --------------------------------------------------------------

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1].as_posix()

sys.path.append(PROJECT_ROOT)


# -- Project information -----------------------------------------------------

project = "Python project template"
copyright = "2022, Mateus Oliveira"
author = "Mateus Oliveira"


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_rtd_theme",
    "sphinx.ext.napoleon",
    "sphinx.ext.githubpages",
]


# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
