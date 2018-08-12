# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

"""
Cookiecutter-Git PostGenProjectHook Tests.
"""
import base64
from contextlib import contextmanager
import datetime
import json
import os
import shlex
import subprocess

from cookiecutter.utils import rmtree
from invoke import run
import pytest

from hooks.post_gen_project import git_disable_gpgsign, PostGenProjectHook


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests.

    https://github.com/audreyr/cookiecutter-pypackage/blob/master/tests/test_bake_project.py#L33

    :param cookies: pytest_cookies.Cookies, cookie to be baked and its temporal files will be removed
    """
    with git_disable_gpgsign():
        extra_context = kwargs.pop("extra_context", {})
        extra_context["_testing"] = True
        result = cookies.bake(*args, extra_context=extra_context, **kwargs)
        try:
            yield result
        finally:
            if result.project:
                rmtree(str(result.project))


def mock_request_with_remote_provider_as_bitbucket(mock):
    """
    Mocks the Bitbucket API POST request that creates the remote repo.

    :param mock: requests_mock.mocker.Mocker
    """
    bitbucket_repos_url = PostGenProjectHook.bitbucket_repos_url_base.format(
        "NathanUrwin", "cookiecutter-git-demo"
    )
    auth_base64 = PostGenProjectHook.format_basic_auth(
        "NathanUrwin", "notmypassword"
    )
    request_headers = {"Authorization": "Basic {}".format(auth_base64)}
    request_headers.update(PostGenProjectHook.json_header)
    mock.post(
        bitbucket_repos_url,
        json=json.dumps(
            {
                "name": "cookiecutter-git-demo",
                "description": "A cookiecutter-git demonstration :tada:",
                "has_issues": True,
                "is_private": True,
            }
        ).encode(),
        request_headers=request_headers,
    )


def mock_request_with_remote_provider_as_github(mock):
    """
    Mocks the GitHub API POST request that creates the remote repo.

    :param mock: requests_mock.mocker.Mocker
    """
    auth_base64 = PostGenProjectHook.format_basic_auth(
        "NathanUrwin", "notmypwd"
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


def test_cookiecutter_git(cookies, requests_mock):
    """
    Tests `$ cookiecutter gh:NathanUrwin/cookiecutter-git --no-input`.

    :param cookies: pytest_cookies.Cookies
    :param requests_mock: requests_mock.mocker.Mocker
    """
    mock_request_with_remote_provider_as_github(requests_mock)

    with bake_in_temp_dir(cookies) as result:

        # https://pytest-cookies.readthedocs.io/en/latest/getting_started/
        assert result.exception is None
        assert result.exit_code == 0
        assert result.project.basename == "cookiecutter-git-demo"
        assert result.project.isdir()

        # PostGenProjectHook._copyright_license
        assert not result.project.join("NOTICE").check()
        assert "MIT" in result.project.join("LICENSE").read()
        assert not result.project.join("LICENSES").check()

        # PostGenProjectHook._make_dirs
        assert result.project.join("docs", ".gitkeep").check()
        assert result.project.join("src", ".gitkeep").check()
        assert result.project.join("tests", ".gitkeep").check()

        # PostGenProjectHook._github_dir
        assert result.project.join(".github").check()

        # PostGenProjectHook._git_ignore
        assert (
            "windows,macos,linux,git"
            in result.project.join(".gitignore").read()
        )

        # PostGenProjectHook._git_init
        assert result.project.join(".git").check()


def test_cookiecutter_git_with_bitbucket(cookies, requests_mock):
    """
    Tests `$ cookiecutter gh:NathanUrwin/cookiecutter-git --no-input remote_provider=bitbucket.org`.

    :param cookies: pytest_cookies.Cookies
    :param requests_mock: requests_mock.mocker.Mocker
    """
    mock_request_with_remote_provider_as_bitbucket(requests_mock)

    with bake_in_temp_dir(
        cookies, extra_context={"remote_provider": "bitbucket.org"}
    ) as result:

        # https://pytest-cookies.readthedocs.io/en/latest/getting_started/
        assert result.exception is None
        assert result.exit_code == 0
        assert result.project.basename == "cookiecutter-git-demo"
        assert result.project.isdir()

        # PostGenProjectHook._copyright_license
        assert not result.project.join("NOTICE").check()
        assert "MIT" in result.project.join("LICENSE").read()
        assert not result.project.join("LICENSES").check()

        # PostGenProjectHook._make_dirs
        assert result.project.join("docs", ".gitkeep").check()
        assert result.project.join("src", ".gitkeep").check()
        assert result.project.join("tests", ".gitkeep").check()

        # PostGenProjectHook._github_dir
        assert not result.project.join(".github").check()

        # PostGenProjectHook._git_ignore
        assert (
            "windows,macos,linux,git"
            in result.project.join(".gitignore").read()
        )

        # PostGenProjectHook._git_init
        assert result.project.join(".git").check()


def test_cookiecutter_git_with_gitlab(cookies):
    """
    Tests `$ cookiecutter gh:NathanUrwin/cookiecutter-git --no-input remote_provider=gitlab.com`.

    :param cookies: pytest_cookies.Cookies
    """
    with bake_in_temp_dir(
        cookies, extra_context={"remote_provider": "gitlab.com"}
    ) as result:

        # https://pytest-cookies.readthedocs.io/en/latest/getting_started/
        assert result.exception is None
        assert result.exit_code == 0
        assert result.project.basename == "cookiecutter-git-demo"
        assert result.project.isdir()

        # PostGenProjectHook._copyright_license
        assert not result.project.join("NOTICE").check()
        assert "MIT" in result.project.join("LICENSE").read()
        assert not result.project.join("LICENSES").check()

        # PostGenProjectHook._make_dirs
        assert result.project.join("docs", ".gitkeep").check()
        assert result.project.join("src", ".gitkeep").check()
        assert result.project.join("tests", ".gitkeep").check()

        # PostGenProjectHook._github_dir
        assert not result.project.join(".github").check()

        # PostGenProjectHook._git_ignore
        assert (
            "windows,macos,linux,git"
            in result.project.join(".gitignore").read()
        )

        # PostGenProjectHook._git_init
        assert result.project.join(".git").check()
