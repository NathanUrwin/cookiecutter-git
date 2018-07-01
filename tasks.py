# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from invoke import task

from hooks.post_gen_project import requests


@task
def clean_build(x):
    """remove build artifacts"""
    x.run("rm -frv build/")
    x.run("rm -frv dist/")
    x.run("rm -frv .eggs/")
    x.run('find . -name "*.egg-info" -exec rm -frv {} +')
    x.run('find . -name "*.egg" -exec rm -frv {} +')


@task
def clean_pyc(x):
    """remove Python file artifacts"""
    x.run('find . -name "*.pyc" -exec rm -frv {} +')
    x.run('find . -name "*.pyo" -exec rm -frv {} +')
    x.run('find . -name "__pycache__" -exec rm -frv {} +')
    x.run('find . -name "*~" -exec rm -frv {} +')


@task
def clean_test(x):
    """remove test artifacts"""
    x.run("rm -fr .tox/")
    x.run("rm -f .coverage")
    x.run("rm -fr htmlcov/")


@task(clean_build, clean_pyc, clean_test)
def clean(x):
    """remove all build artifacts"""
    x.run('find . -name "*~" -exec rm -frv {} +')


@task
def copy_cookie(x):
    x.run('cp -afrv cookiecutter.json "{{cookiecutter.repo_slug}}"')
    x.run('cp -afrv hooks "{{cookiecutter.repo_slug}}"')
    x.run('cp -afrv "{{cookiecutter.repo_slug}}" "{{cookiecutter.repo_slug}}"')


@task
def deploy_demo(x):
    pass


@task
def format_py(x):
    """format Python source files"""
    x.run('find . -name "*.py" -exec pipenv run black -l 79 {} +')
