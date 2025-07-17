import typer

from .new import app as new_app

app = typer.Typer()

app.add_typer(new_app, name="new")

if __name__ == "__main__":
    app()