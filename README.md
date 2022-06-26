# Python project template

[![Continuos Integration](https://github.com/mateusoliveira43/python-project-template/actions/workflows/ci.yml/badge.svg)](https://github.com/mateusoliveira43/python-project-template/actions)
[![Continuos Delivery](https://github.com/mateusoliveira43/python-project-template/actions/workflows/cd.yml/badge.svg)](https://github.com/mateusoliveira43/python-project-template/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

Template for a Python project. Check the project's documentation [here](https://mateusoliveira43.github.io/python-project-template/).

# Requirements

To run the project, it is necessary the following tools:

- [Poetry](https://python-poetry.org/docs/#installation)

Or

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

# Usage

Follow one of the next sections.

## Poetry

To install project dependencies and create a virtual environment, run
```
poetry install
```

To activate virtual environment, run
```
poetry shell
```

To deactivate virtual environment, run `CTRL+D` or `exit`.

## Docker

To connect to container's shell, run
```
docker/run.sh
```
and run `poetry shell` to activate virtual environment.

To exit the container's shell, run `CTRL+D` or `exit`.

To run Dockerfile linter, run
```
docker/lint.sh
```

To remove the project's containers, images, volumes and networks, run
```
docker/down.sh
```

To change Docker configuration, change the variables in `.env` file.

# Quality

Run the commands presented in this section with the project's virtual environment activated.

The quality metrics of the project are reproduced by the continuos integration (CI) pipeline of the project. CI configuration in [`.github/workflows/ci.yml`](.github/workflows/ci.yml) file.

## Tests

To run tests and coverage report, run
```
pytest
```

To see the html report, check `tests/coverage-results/htmlcov/index.html`.

Tests and coverage configuration in [`pyproject.toml`](pyproject.toml) file.

## Type checking

To run Python type checker, run
```
mypy .
```

Python type checker configuration in [`pyproject.toml`](pyproject.toml) file.

## Linter

To run Python linter, run
```
prospector
```

Python linter configuration in [`.prospector.yaml`](.prospector.yaml) file.

## Code formatters

To check Python code imports format, run
```
isort --check --diff .
```

To format Python code imports, run
```
isort .
```

To check Python code format, run
```
black --check --diff .
```

To format Python code, run
```
black .
```

isort and black configuration in [`pyproject.toml`](pyproject.toml) file.

To check all repository's files format, run
```
ec -verbose
```

File format configuration in [`.editorconfig`](.editorconfig) file.

## Security vulnerability scanners

To check common security issues in Python code, run
```
bandit --recursive scripts
```

To check known security vulnerabilities in Python dependencies, run
```
safety check --file requirements/prod.txt --full-report
safety check --file requirements/dev.txt --full-report
```

## Documentation

To check Python documentation generation, run
```
sphinx-apidoc --module-first --private --output-dir docs/modules source
sphinx-build -W -T -v -n docs public
```

To generate Python documentation, run
```
sphinx-apidoc --module-first --private --output-dir docs/modules source
sphinx-build -v -n docs public
```
To see the documentation , check `public/index.html`.

Sphinx configuration in [`docs/conf.py`](docs/conf.py) file.

## Pre-commit

To configure pre-commit automatically when cloning this repo, run
```
git config --global init.templateDir ~/.git-template
pre-commit init-templatedir --hook-type commit-msg --hook-type pre-commit ~/.git-template
```
pre-commit must be installed globally.

To configure pre-commit locally, run
```
pre-commit install --hook-type commit-msg --hook-type pre-commit
```

To test it, run
```
pre-commit run --all-files
```

pre-commit configuration in [`.pre-commit-config.yaml`](.pre-commit-config.yaml) file.

# Update requirements

To update requirements files, run
```
poetry export --format requirements.txt --output requirements/prod.txt
poetry export --format requirements.txt --output requirements/dev.txt --dev
```

# License

This repository is licensed under the terms of [MIT License](LICENSE).

