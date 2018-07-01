# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from contextlib import contextmanager
import datetime
import os
import shlex
import subprocess

from cookiecutter.utils import rmtree

from hooks.post_gen_project import run


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests.

    https://github.com/audreyr/cookiecutter-pypackage/blob/master/tests/test_bake_project.py#L33

    :param cookies: pytest_cookies.Cookies, cookie to be baked and its temporal files will be removed
    """
    with git_disable_gpgsign():
        result = cookies.bake(*args, **kwargs)
        try:
            yield result
        finally:
            rmtree(str(result.project))


@contextmanager
def git_disable_gpgsign():
    """Temporarily disables git commit GPG signing.
    """
    gpgsign = run("git config --global --get commit.gpgsign")
    if gpgsign and gpgsign.strip() == "true":
        # turn off gpgsigning commits
        try:
            run("git config --global --unset commit.gpgsign")
            yield
        # turn gpgsigning back on
        finally:
            run("git config --global --bool commit.gpgsign true")


def test_bake_project(cookies):
    """Tests `cookiecutter gh:NathanUrwin/cookiecutter-git --no-input` equivalence.

    :param cookies: pytest_cookies.Cookies
    """
    with bake_in_temp_dir(cookies) as result:
        assert result.exception is None
        assert result.exit_code == 0
        assert result.project.isdir()


def test_year_compute_in_license_file(cookies):
    """Tests `{% now 'utc', '%Y' %}` template tag in LICENSE file.

    :param cookies: pytest_cookies.Cookies
    """
    with bake_in_temp_dir(cookies) as result:
        license = result.project.join("LICENSE")

        now = datetime.datetime.now()
        assert str(now.year) in license.read()
