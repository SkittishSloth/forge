import os
import pytest
from typer.testing import CliRunner  # Assuming your typer app is named 'app' in forge/new/project.py
from forge.__main__ import app

runner = CliRunner()

def test_new_project_basic(tmp_path):
    """
    Test the basic functionality of forge new project command.
    """
    project_name = "my-test-project"
    result = runner.invoke(app, ["project", project_name])

    if result.exit_code != 0:
        print(result.stderr_bytes)
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
    assert content == f"# {project_name}\\n"
def test_new_project_git_init_default(tmp_path):
    """
    Test that git initialization happens by default.
    """
    project_name = "my-git-project-default"
    result = runner.invoke(app, ["project", project_name])
    assert result.exit_code == 0

    project_path = tmp_path / project_name
    git_path = project_path / ".git"
    assert git_path.is_dir()

def test_new_project_git_init_disabled(tmp_path):
    """
    Test that git initialization is disabled with --no-git.
    """
    project_name = "my-git-project-disabled"
    result = runner.invoke(app, ["project", project_name, "--no-git"])
    assert result.exit_code == 0
    project_path = tmp_path / project_name
    git_path = project_path / ".git"
    assert not git_path.is_dir()

def test_new_template_basic(tmp_path):
    """
    Test the basic functionality of forge new template command.
    """
    template_name = "my-test-template"
    result = runner.invoke(app, ["template", template_name])

    if result.exit_code != 0:
        print(result.stderr_bytes)
    # Assert that the command exited successfully
    assert result.exit_code == 0

    # Assert that the template directory structure was created
    template_set_path = tmp_path / ".forge" / "templates"
    template_path = template_set_path / template_name
    assert template_path.is_dir()

    # Assert that the forge.meta.yaml file was created
    meta_path = template_path / "forge.meta.yaml"
    assert meta_path.is_file()

    # Assert that the example template file was created
    example_template_path = template_path / "template.txt"
    assert example_template_path.is_file()
    assert result.exit_code == 0