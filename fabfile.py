# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement

from fabric.api import execute, local, task


@task
def clean():
    execute(clean_build)
    execute(clean_pyc)
    execute(clean_test)
    local('find . -name "*~" -exec rm -f {} +')


@task
def clean_build():
    local('rm -fr build/')
    local('rm -fr dist/')
    local('rm -fr .eggs/')
    local('find . -name "*.egg-info" -exec rm -fr {} +')
    local('find . -name "*.egg" -exec rm -f {} +')


@task
def clean_pyc():
    local('find . -name "*.pyc" -exec rm -f {} +')
    local('find . -name "*.pyo" -exec rm -f {} +')
    local('find . -name "__pycache__" -exec rm -fr {} +')
    local('find . -name "*~" -exec rm -f {} +')


@task
def clean_test():
    local('rm -fr .tox/')
    local('rm -f .coverage')
    local('rm -fr htmlcov/')


@task
def help():
    print()
    print('clean         - remove all build artifacts')
    print('clean-build   - remove build artifacts')
    print('clean-pyc     - remove Python file artifacts')
    print()
