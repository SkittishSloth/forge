from pathlib import Path
from typing import Optional

import os
import typer
import subprocess
from typing_extensions import Annotated

app = typer.Typer()

@app.command()
def project(
    name: Annotated[str, typer.Argument(help="The name of the project to create.", show_default=False)] = None,
    template: Annotated[str, typer.Option("-t", "--template", help="The name of the template to use for creating the project. If not specified, the default template will be used.", show_default=False)] = "",
    dest: Annotated[
        Optional[Path], 
        typer.Option(
            "-d", 
            "--dest", 
            file_okay=False,
            dir_okay=True,
            writable=True,
            readable=True,
            resolve_path=True,
            help="Where to create the new project."
        )
    ] = "./",
    git: Annotated[bool, typer.Option("--git/--no-git", "-g/-G", help="Whether or not to initialize a git repository in the project. Will initialize a repository by default.", show_default=False)] = True
    ):
    """
    Creates a new project structure.
    """
    project_path = dest / name
    print(f"Creating new project at: {project_path}")

#     # Create the project directory
#     os.makedirs(project_path, exist_ok=True)

#     # Create a simple README.md file
#     readme_path = project_path / "README.md"
#     readme_path.write_text(f"# {name}\n")

#     # Initialize git repository if requested
#     if git:
#         print("Initializing git repository...")
#         subprocess.run(["git", "init"], cwd=project_path, check=True)