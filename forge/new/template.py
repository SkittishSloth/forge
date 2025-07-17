import typer

app = typer.Typer()

@app.command()
def new(
    name: str,
    dest: str = typer.Option(None, "--dest", help="Destination directory for the new template."),
    template: str = typer.Option(None, "--template", help="Template to base the new template on (optional)."),
):
    """
    Creates a new template structure.
    """
    print(f"Creating new template: {name}")
    print(f"Destination directory: {dest}")
    print(f"Base template: {template}")
