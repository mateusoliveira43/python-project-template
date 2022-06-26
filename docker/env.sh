#!/bin/bash

ROOT="$(dirname $( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P ))"
FILE="$ROOT/.env"
PROJECT_NAME='python-project-template'

if ! test -f $FILE; then
    echo "USER_ID=$(id -u)" >> $FILE
    echo "GROUP_ID=$(id -g)" >> $FILE
    echo "PROJECT_NAME=$PROJECT_NAME" >> $FILE
    echo "WORK_DIR=/home/$PROJECT_NAME/$PROJECT_NAME" >> $FILE
    echo ".env file created in project's root"
fi
