#!/bin/bash

if ! test -d '.venv/bin'; then
    poetry install
fi
exec poetry run $@
