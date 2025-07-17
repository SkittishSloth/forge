from pathlib import Path
from typing import Optional

import os
import typer
import yaml
from typing_extensions import Annotated

app = typer.Typer()

@app.command()
def template(
    name: Annotated[str, typer.Argument(help="The name of the template to create.", show_default=False)] = "",
    template: Annotated[
        str,
        typer.Option(
            "-t",
            "--template",
            help="The name of the template to base the new template on (optional).",
            show_default=False,
        ),
    ] = "",
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
            help="Where to create the new template.",
        ),
    ] = "./",
):
    """
    Creates a new template structure.
    """
    if not name:
        name = typer.prompt("Please enter the template name")

    # # Determine the full path for the new template
    # # Assuming dest is where the user wants the .forge/templates directory to be
    # template_set_dir = Path(dest) / ".forge" / "templates"
    # new_template_dir = template_set_dir / name

    print(f"Creating new template skeleton: {name}")

    # # Create the necessary directories
    # os.makedirs(new_template_dir, exist_ok=True)

    # # Create a placeholder forge.meta.yaml file
    # (new_template_dir / "forge.meta.yaml").write_text(yaml.dump({"name": name}))

    # # Create a simple example template file
    # (new_template_dir / "template.txt").write_text(f"This is a template file for {name}.")