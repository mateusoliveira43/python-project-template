#!/usr/bin/env python3
"""
Get versioning information for CD pipeline of the project in JSON format.
Gets the following information in JSON format:
- if version is new (isVersionNew key).
- the version (version key).
- the text for the release (releaseBody key).
This information is used by the Continuous Delivery pipeline of the project to
automatically create a tag and release for the project, or, add latest changes
to Release Notes (changelog) in the documentation.
"""

import json
import sys
from pathlib import Path

from cly import __version__
from cly.colors import color_text
from cly.utils import get_standard_output

previous_git_version = get_standard_output("git describe --tag --abbrev=0")
previous_version = (
    previous_git_version[0]
    if isinstance(previous_git_version, list)
    else "None"
)


def get_release_body() -> str:
    """
    Get text for GitHub Release.
    Gets text between new version and previous version from docs/changelog.rst
    file.
    Returns
    -------
    str
        Text between new version and previous version.
    """
    text = ""
    append = False
    with open(
        Path(__file__).parent.parent / "docs/changelog.rst",
        encoding="utf-8",
    ) as changelog:
        for line in changelog:
            if line.strip() == previous_version:
                break
            if line.strip() == __version__:
                append = True
            if append:
                text += line

    return text


release_body = get_release_body()
is_version_new = previous_version != __version__
if is_version_new and not release_body:
    print(
        color_text("ERROR: No release body provided for release.", "red"),
        file=sys.stderr,
    )
    raise SystemExit(1)

versioning = {
    "isVersionNew": is_version_new,
    "version": __version__,
    "releaseBody": release_body,
}
print(json.dumps(versioning))
