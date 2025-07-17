import typer

from .project import app as project_app
from .template import app as template_app

app = typer.Typer()

app.add_typer(project_app)
app.add_typer(template_app)
