"""Docky CLI."""

from cly import config

from . import __version__
from .commands.down import down
from .commands.env_file import env
from .commands.lint import lint
from .commands.list_docker_objects import list_docker_objects
from .commands.run import run
from .commands.scan import scan
from .commands.up import start_all

CLI_CONFIG = {
    "name": "Docky",
    "description": (
        "Docky: Run Docker commands with Python. "
        f"Script configuration in {config.__file__}."
    ),
    "epilog": "Docker\N{whale} + Python\N{snake}",
    "version": __version__,
}

CLI = config.ConfiguredParser(CLI_CONFIG)

env_command = CLI.create_command(env)
env_command.add_argument("-s", "--show", action="store_true")
CLI.create_command(start_all, alias="up")
run_command = CLI.create_command(run)
run_command.add_argument(dest="command", nargs="*")
list_command = CLI.create_command(list_docker_objects, alias="ls")
list_command.add_argument("-a", "--all", dest="show_all", action="store_true")
CLI.create_command(lint)
CLI.create_command(scan)
CLI.create_command(down)
