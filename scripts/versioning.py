#!/usr/bin/env python3

import json

versioning = {
    "isVersionNew": False,
    "version": "1.0.0",
    "releaseBody": "## 1.0.0\n\nTeste teste teste\n",
}
print(json.dumps(versioning))
