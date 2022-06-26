#!/bin/bash

ROOT="$(dirname $( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P ))"

docker run \
--rm --interactive \
ghcr.io/hadolint/hadolint < $ROOT/docker/Dockerfile
