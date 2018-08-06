# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from invoke import task


@task
def changelog(x):
    """
    Generates a new Change Log.

    :param x: invoke.context.Context
    """
    x.run("github_changelog_generator -u NathanUrwin -p cookiecutter-git")


@task
def clean_build(x):
    """
    Removes build artifacts.

    :param x: invoke.context.Context
    """
    x.run("rm -frv build/")
    x.run("rm -frv dist/")
    x.run("rm -frv .eggs/")
    x.run("find . -name '*.egg-info' -exec rm -frv {} +")
    x.run("find . -name '*.egg' -exec rm -frv {} +")


@task
def clean_pyc(x):
    """
    Removes python file artifacts.

    :param x: invoke.context.Context
    """
    x.run("find . -name '*.pyc' -exec rm -frv {} +")
    x.run("find . -name '*.pyo' -exec rm -frv {} +")
    x.run("find . -name '__pycache__' -exec rm -frv {} +")
    x.run("find . -name '*~' -exec rm -frv {} +")


@task
def clean_test(x):
    """
    Removes test artifacts.

    :param x: invoke.context.Context
    """
    x.run("rm -fr .tox/")
    x.run("rm -f .coverage")
    x.run("rm -fr htmlcov/")


@task(clean_build, clean_pyc, clean_test)
def clean(x):
    """
    Removes all build artifacts.

    :param x: invoke.context.Context
    """
    x.run("find . -name '*~' -exec rm -frv {} +")


@task
def copy_cookie(x):
    """
    Copies the cookiecutter-git features into the to-be generated project dir.

    :param x: invoke.context.Context
    """
    x.run("cp -afrv cookiecutter.json '{{cookiecutter.repo_slug}}'")
    x.run("cp -afrv hooks '{{cookiecutter.repo_slug}}'")
    x.run("cp -afrv '{{cookiecutter.repo_slug}}' '{{cookiecutter.repo_slug}}'")


@task(name="format")
def format_python(x):
    """
    Formats the python source files using the uncompromising black.

    :param x: invoke.context.Context
    """
    x.run("black --line-length 79 .")
    x.run("git add --all")


@task
def tests(x):
    """
    Runs the py.test no-stdout-capture, entire-repo-coverage tests.

    :param x: invoke.context.Context
    """
    x.run(
        "pytest --capture=no --cov-report term:skip-covered --cov-report html --cov=. tests"
    )
