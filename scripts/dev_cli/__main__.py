"""Development scripts CLI."""

from cly import config

from . import __version__
from .commands.doc import doc
from .commands.format_code import format_code
from .commands.lint import lint
from .commands.requirements import requirements
from .commands.scan import scan

CLI_CONFIG = {
    "name": "Development scripts",
    "description": "Development scripts for project.",
    "epilog": "",
    "version": __version__,
}

CLI = config.ConfiguredParser(CLI_CONFIG)

lint_command = CLI.create_command(lint)
lint_command.add_argument("--shell", action="store_true")
format_command = CLI.create_command(format_code, alias="format")
format_command.add_argument("--check", action="store_true")
scan_command = CLI.create_command(scan)
group = scan_command.add_mutually_exclusive_group(required=True)
group.add_argument(
    "--code",
    action="store_true",
)
group.add_argument(
    "--dependencies",
    action="store_true",
)
doc_command = CLI.create_command(doc)
doc_command.add_argument("--check", action="store_true")
CLI.create_command(requirements)
