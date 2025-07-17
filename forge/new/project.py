from pathlib import Path
from typing import Optional

import typer
from typing_extensions import Annotated

app = typer.Typer()

@app.command()
def project(
    name: Annotated[str, typer.Option(help="The name of the project to create.", show_default=False, prompt=True)],
    template: Annotated[str, typer.Option(help="The name of the template to use for creating the project.", show_default=False)] = "",
    dest: Annotated[Optional[Path], typer.Option(help="Where to create the new project.")] = "./",
    git: Annotated[bool, typer.Option(help="Whether or not to initialize a git repository in the project. Will initialize a repository by default.", show_default=False)] = True
    ):
    """
    Creates a new project structure for NAME, located at --dest/NAME.
    """
    print(f"Creating new project: {name}.")