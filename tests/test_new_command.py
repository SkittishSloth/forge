import os
import pytest
from typer.testing import CliRunner
from forge.new.project import app  # Assuming your typer app is named 'app' in forge/new/project.py

runner = CliRunner()

def test_new_project_basic(tmp_path):
    """
    Test the basic functionality of forge new project command.
    """
    project_name = "my-test-project"
    result = runner.invoke(app, [project_name, "--dest", str(tmp_path)])

    # Assert that the command exited successfully
    assert result.exit_code == 0

    # Assert that the project directory was created
    project_path = tmp_path / project_name
    assert project_path.is_dir()

    # Assert that the README.md file was created
    readme_path = project_path / "README.md"
    assert readme_path.is_file()

    # Assert the content of the README.md file
    with open(readme_path, "r") as f:
        content = f.read()
    assert content == f"# {project_name}\n"

def test_new_project_git_init_default(tmp_path):
    """
    Test that git initialization happens by default.
    """
    project_name = "my-git-project-default"
    result = runner.invoke(app, [project_name, "--dest", str(tmp_path)])

    assert result.exit_code == 0

    project_path = tmp_path / project_name
    git_path = project_path / ".git"
    assert git_path.is_dir()

def test_new_project_git_init_disabled(tmp_path):
    """
    Test that git initialization is disabled with --no-git.
    """
    project_name = "my-git-project-disabled"
    result = runner.invoke(app, [project_name, "--dest", str(tmp_path), "--no-git"])

    assert result.exit_code == 0

    project_path = tmp_path / project_name
    git_path = project_path / ".git"
    assert not git_path.is_dir()