Contributing
============

Here, you can find out how (**and why**) the project is structured to best
understand it and be able to help us improve the project even further.

Versioning
----------

The project follows the `Semantic Versioning <https://semver.org/>`_ to assign
and increment the project version. This is enforced through the following:

- Tests: the tests in ``tests/test_version.py`` file enforces the correct use of
  Semantic Versioning (which are reproduced) by the CI pipeline of the project.
- Automation:

  - tagging and releasing: through the ``scripts/versioning.py`` which collects
    the necessary information to the CD pipeline of the project. For this, a
    pull request only changing the project version (and the releases notes, if
    necessary), must be opened and closed.
  - update of released notes: through the pull request title, the CD pipeline
    of the project updates the releases notes in the documentation after each
    pull request is closed. It is **very important to write good pull request
    titles** because of this.

  The automation options are mutually exclusive, i.e. only one of them is
  triggered by the CD pipeline at a time.

For the first release, the end of the CD pipeline file,
``.github/workflows/cd.yml``, must be uncommented during the tagging and
releasing pull request.
