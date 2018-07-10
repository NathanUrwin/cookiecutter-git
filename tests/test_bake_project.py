# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

"""
Cookiecutter-Git Tests with pytest, pytest-cookies, pytest-dotenv, and requests-mock.
"""
import base64
from contextlib import contextmanager
import datetime
import json
import os
import shlex
import subprocess

from cookiecutter.utils import rmtree
from invoke import Result, run
import pytest

from hooks.post_gen_project import PostGenProjectHook


@contextmanager
def git_disable_gpgsign():
    """
    Disables git commit GPG signing temporarily.
    """
    result = run("git config --global --get commit.gpgSign")
    if result.stdout.strip() == "true":
        # turn off gpg signing commits
        try:
            run("git config --global --unset commit.gpgSign")
            yield
        # turn gpg signing back on
        except KeyboardInterrupt:
            run("git config --global --bool commit.gpgSign true")
        finally:
            run("git config --global --bool commit.gpgSign true")


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests.

    https://github.com/audreyr/cookiecutter-pypackage/blob/master/tests/test_bake_project.py#L33

    :param cookies: pytest_cookies.Cookies, cookie to be baked and its temporal files will be removed
    """
    with git_disable_gpgsign():
        result = cookies.bake(
            *args, extra_context={"_testing": True}, **kwargs
        )
        try:
            yield result
        finally:
            if result.project:
                rmtree(str(result.project))


def mock_request_with_remote_provider_as_github(mock):
    """
    Mocks the GitHub API POST request that creates the remote repo.

    :param mock: requests_mock.mocker.Mocker
    """
    remote_password = PostGenProjectHook.parse_dotenv_password()
    auth_base64 = PostGenProjectHook.format_basic_auth(
        "NathanUrwin", remote_password
    )
    mock.post(
        PostGenProjectHook.github_repos_url,
        json=json.dumps(
            {
                "name": "cookiecutter-git-demo",
                "description": "A cookiecutter-git demonstration :tada:",
            }
        ).encode(),
        request_headers={"Authorization": "Basic {}".format(auth_base64)},
    )


def test_bake_project(cookies, requests_mock):
    """
    Tests `cookiecutter gh:NathanUrwin/cookiecutter-git --no-input` CLI equivalence.

    :param cookies: pytest_cookies.Cookies
    :param requests_mock: requests_mock.mocker.Mocker
    """
    mock_request_with_remote_provider_as_github(requests_mock)

    with bake_in_temp_dir(cookies) as result:

        # https://pytest-cookies.readthedocs.io/en/latest/features/
        assert result.exception is None
        assert result.exit_code == 0

        # https://py.readthedocs.io/en/latest/path.html#py._path.local.LocalPath
        assert result.project.basename == "cookiecutter-git-demo"
        assert result.project.isdir()
