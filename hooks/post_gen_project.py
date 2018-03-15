#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement
"""Cookiecutter-Git Post-Generate Project Hook.
"""

import base64
import codecs
import errno
import json
import os
import shutil

import getpass
import subprocess
try:
    # python 2
    from urllib import urlencode
    from urllib2 import HTTPError, Request, urlopen
except ImportError:
    # python3
    from urllib.error import HTTPError
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen


def run(command, log=True):
    """A quick-and-dirty function that mimicks the fabric library local run.
    """
    try:
        output = codecs.decode(subprocess.check_output(command), 'utf-8')
    except subprocess.CalledProcessError as error:
        print('{}: {}\n{}'.format(error.returncode, error.cmd, error.output))
        raise error
    else:
        if output and log:
            print('{}\n{}'.format(' '.join(command), output))
        else:
            print(' '.join(command))
    return output


class requests(object):
    """ A class that mimicks the requests library using the built-in urllib.
    """

    @staticmethod
    def _request(url, headers, data, log):
        """A quick-and-dirty static method that wraps the urllib Request class.
        """
        try:
            req = Request(url, data=data, headers=headers)
            response = urlopen(req)
            content = response.read()
            response.close()
        except HTTPError as error:
            message = error.read()
            error.close()
            args = (error.code, error.reason, url, message)
            print('{} {}: {}\n{}'.format(*args))
            raise SystemExit
        else:
            if content and log:
                print('{}\n{}'.format(url, content))
            else:
                print(url)
        return content

    @classmethod
    def get(cls, url, headers={}, log=True):
        """A basic http GET request wrapper class method.
        """
        return cls._request(url, headers, None, log)

    @classmethod
    def post(cls, url, headers={}, data=None, log=True):
        """A basic http POST request wrapper class method.
        """
        return cls._request(url, headers, data, log)

# Constants
GITHUB_REPOS_URL = 'https://api.github.com/user/repos'
GITLAB_NAMESPACES_URL = 'https://gitlab.com/api/v3/namespaces'
GITLAB_PROJECTS_URL = 'https://gitlab.com/api/v3/projects'
JSON_HEADER = {'Content-Type': 'application/json; charset=utf-8'}

# Globals
REPO_PATH = os.getcwd()
APACHE_LICENSE = {% if cookiecutter.license == 'Apache-2.0' %}True{% else %}False{% endif %}
BITBUCKET_REPOS_URL = 'https://api.bitbucket.org/2.0/repositories/{{cookiecutter.repo_namespace}}/{{cookiecutter.repo_slug}}'
CREATE_REMOTE = {% if cookiecutter.create_remote == 'yes' %}True{% else %}False{% endif %}
GITIGNORE_PATH = os.path.join(REPO_PATH, '.gitignore')
{% if cookiecutter.git_username != cookiecutter.repo_namespace %}
GITHUB_REPOS_URL = 'https://api.github.com/orgs/{{cookiecutter.repo_namespace}}/repos'
{% endif %}
GITIGNORE_URL = 'https://www.gitignore.io/api/{{cookiecutter.gitignore}}'
GIT_USERNAME = '{{cookiecutter.git_username}}'
LICENSES_DIRPATH = os.path.join(REPO_PATH, 'LICENSES')
LICENSE_PATH = os.path.join(REPO_PATH, 'LICENSE')
LICENSE_TXT = os.path.join(LICENSES_DIRPATH, '{{cookiecutter.license}}.txt')
NEW_GITIGNORE = {% if cookiecutter.gitignore != 'windows,macos,linux,git' %}True{% else %}False{% endif %}
NOTICE_PATH = os.path.join(REPO_PATH, 'NOTICE')
PASSWORD_PROMPT = "Password for 'https://{{cookiecutter.git_username}}@{{cookiecutter.remote_provider}}': "
PROJECT_DIRS = [os.path.join(REPO_PATH, dirname) for dirname in '{{cookiecutter.make_dirs}}'.split(',')]
REMOTE_DATA = {'name': '{{cookiecutter.repo_slug}}', 'description': '{{cookiecutter.repo_description}}'}
REPO_NAMESPACE = '{{cookiecutter.repo_namespace}}'
REMOTE_ORIGIN_URL = 'https://{{cookiecutter.git_username}}@{{cookiecutter.remote_provider}}/{{cookiecutter.repo_namespace}}/{{cookiecutter.repo_slug}}.git'
REMOTE_PROVIDER = '{{cookiecutter.remote_provider}}'
SUCCESS_MESSAGE = '\n{{cookiecutter.repo_slug}} setup successfully!\n\n'


def setup_git_repo():
    """A function that adds a .gitignore, initial commit, and remote repo.
    """
    if NEW_GITIGNORE:
        response = requests.get(GITIGNORE_URL)
        with open(GITIGNORE_PATH, 'wb') as f:
            f.write(response)
        print("updated '{}'".format(GITIGNORE_PATH))

    run(['git', 'init'])
    run(['git', 'status'])
    run(['git', 'add', '-A'])
    run(['git', 'status'])
    run(['git', 'commit', '-m', 'Initial commit'])

    if CREATE_REMOTE:
        auth_info = (GIT_USERNAME, getpass.getpass(PASSWORD_PROMPT).strip())
        auth_base = base64.b64encode('{}:{}'.format(*auth_info))

        if REMOTE_PROVIDER == 'github.com':
            create_remote_url = GITHUB_REPOS_URL
            data = json.dumps(REMOTE_DATA)
            headers = {'Authorization': 'Basic {}'.format(auth_base)}

        elif REMOTE_PROVIDER == 'gitlab.com':
            gitlab_token = getpass.getpass('gitlab_token: ').strip()
            token_header = {'PRIVATE-TOKEN': gitlab_token}
            search_param = {'search': REPO_NAMESPACE}
            search_url = GITLAB_NAMESPACES_URL + '?' + urlencode(search_param)
            search_results = requests.get(search_url, headers=token_header)
            gitlab_namespaces = json.loads(search_results)
            for namespace in gitlab_namespaces:
                if namespace.get('path', '') == REPO_NAMESPACE:
                    namespace_id = namespace.get('id', '')
                    if namespace_id:
                        REMOTE_DATA.update({'namespace_id': namespace_id})

            create_remote_url = GITLAB_PROJECTS_URL
            data = urlencode(REMOTE_DATA)
            headers = token_header

        elif REMOTE_PROVIDER == 'bitbucket.org':
            REMOTE_DATA.update({'has_issues': True, 'is_private': True})
            JSON_HEADER['Authorization'] = 'Basic {}'.format(auth_base)

            create_remote_url = BITBUCKET_REPOS_URL
            data = json.dumps(REMOTE_DATA)
            headers = JSON_HEADER

        requests.post(create_remote_url, data=data, headers=headers)
        run(['git', 'remote', 'add', 'origin', REMOTE_ORIGIN_URL])
        run(['git', 'push', '-u', 'origin', 'master'])


def setup_project_dirs():
    """A function that makes dirs and adds .gitkeep files to them.
    """
    for dirpath in PROJECT_DIRS:
        try:
            os.makedirs(dirpath)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(dirpath):
                pass
            else:
                raise
        gitkeep = os.path.join(dirpath, '.gitkeep')
        with open(gitkeep, 'a'):
            os.utime(gitkeep, None)


def setup_license_file():
    """A simple function that adds the chosen LICENSE and removes the rest.
    """
    if not APACHE_LICENSE:
        print("Removing '{}'...".format(NOTICE_PATH))
        os.remove(NOTICE_PATH)

    shutil.move(LICENSE_TXT, LICENSE_PATH)
    shutil.rmtree(LICENSES_DIRPATH, ignore_errors=True)


def main():
    """The main entry point for the post-generate project hook.
    """
    setup_license_file()
    setup_project_dirs()
    setup_git_repo()
    print(SUCCESS_MESSAGE)

# This is required! Don't remove!!
if __name__ == '__main__':
    main()
