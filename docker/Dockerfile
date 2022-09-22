FROM mateusoliveira43/poetry:1.2-python3.10-slim

ARG GROUP_ID=1000
ARG USER_ID=1000
ARG USER_NAME=develop
ARG WORK_DIR=/home/$USER_NAME/PROJECT

RUN apt-get update && apt-get install --yes --no-install-recommends \
    git=1:2.30.* \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd --gid $GROUP_ID $USER_NAME \
    && useradd --uid $USER_ID --gid $GROUP_ID --create-home $USER_NAME \
    && runuser --user $USER_NAME -- mkdir --parents $WORK_DIR/.venv
USER $USER_NAME
WORKDIR $WORK_DIR
