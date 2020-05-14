"""
    Invoke Tasks
"""
import os
from invoke import task


@task
def lint(ctx):
    """
        Task to run PyLint over all python files within the project.
    """
    print('Invoking :: PyLint :')
    py_files = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                py_files.append(file_path)
    ctx.run('python -m pylint ' + ' '.join(py_files))


@task
def check_flake(ctx):
    """
        Task to run Flak8 over all python files within the project.
    """
    print('Invoking :: Check Flake :')
    py_files = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                py_files.append(file_path)
    print('Checking : ' + ' '.join(py_files))
    ctx.run('python -m flake8 ' + ' '.join(py_files))


@task
def check_style(ctx):
    """
        Task to run PEP8 over all the python files within the project.
    """
    print('Invoking :: Check Style :')
    py_files = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                py_files.append(file_path)
    print('Checking : ' + ' '.join(py_files))
    ctx.run('python -m pycodestyle ' + ' '.join(py_files))


@task
def check_json(ctx):
    """
        Task to run python json.tools over each json file within the project.
    """
    print('Invoking :: Check JSON :')
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                print('Checking : ' + file_path)
                ctx.run('python -m json.tool ' + file_path)


@task
def check_yaml(_):
    """
        Task to check that all YAML within the project is valid.
    """
    print('Invoking :: Check YAML :')


@task(check_json, check_yaml, check_style, check_flake, lint)
def check(_):
    """
        Task to preform all check Tasks.
    """
    print('Invoking :: Check :')
