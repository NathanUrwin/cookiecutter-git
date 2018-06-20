from __future__ import absolute_import, division, print_function, with_statement

from contextlib import contextmanager
import datetime
import os
import shlex
import subprocess

from cookiecutter.utils import rmtree


def run(command):
    return subprocess.check_output(shlex.split(command))


@contextmanager
def cookiecutter_bake(cookies, *args, **kwargs):
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


@contextmanager
def git_disable_gpgsign():

    gpgsign = run('git config --global --get commit.gpgsign')
    if gpgsign and gpgsign.strip() == 'true':

        try:
            run('git config --global --unset commit.gpgsign')
            yield

        finally:
            run('git config --global --bool commit.gpgsign true')


def test_year_compute_in_license_file(cookies):

    with git_disable_gpgsign():

        with cookiecutter_bake(cookies) as result:
            license = result.project.join('LICENSE')

            now = datetime.datetime.now()
            assert str(now.year) in license.read()
