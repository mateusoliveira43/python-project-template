#!/bin/bash

ROOT="$(dirname $( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P ))"
$ROOT/docker/env.sh

docker-compose \
--file $ROOT/docker/docker-compose.yaml \
--project-directory $ROOT \
down --volumes --rmi 'all'
