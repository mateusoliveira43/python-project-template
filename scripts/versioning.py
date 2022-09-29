#!/usr/bin/env python3

import json
from pathlib import Path

from scripts.cly.utils import get_standard_output
from source import __version__

previous_version = get_standard_output("git describe --tag --abbrev=0")


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
        Path(__file__).parent.parent / "docs/changelog.rst"
    ) as changelog:
        for line in changelog:
            if line.strip() == previous_version[0]:
                break
            if line.strip() == __version__:
                append = True
            if append:
                text += line

    if not text:
        raise SystemExit(1)

    return text


versioning = {
    "isVersionNew": previous_version[0] != __version__,
    "version": __version__,
    "releaseBody": get_release_body(),
}
print(json.dumps(versioning))
