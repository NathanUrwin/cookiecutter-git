# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

"""Cookiecutter-Git Post-Generate Project Hook.
"""

import base64
import codecs
import errno
import getpass
import json
import os
import shlex
import shutil
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
        output = codecs.decode(
            subprocess.check_output(shlex.split(command)), "utf-8"
        )
    except subprocess.CalledProcessError as error:
        print("> {}: {}\n{}".format(error.returncode, error.cmd, error.output))
        raise error
    else:
        if output and log:
            print("> {}\n{}".format(command, output))
        else:
            print("> {}".format(command))
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
            print("> {} {}: {}\n{}".format(*args))
            raise SystemExit
        else:
            if content and log:
                print("> {}\n{}".format(url, content))
            else:
                print("> {}".format(url))
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
GITHUB_REPOS_URL = "https://api.github.com/user/repos"
GITLAB_NAMESPACES_URL = "https://gitlab.com/api/v3/namespaces"
GITLAB_PROJECTS_URL = "https://gitlab.com/api/v3/projects"
JSON_HEADER = {"Content-Type": "application/json; charset=utf-8"}

# Globals
try:
    RESULTS = json.loads("""{{ cookiecutter | tojson() }}""")
except json.JSONDecodeError:
    RESULTS = {}
    repo_dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_filepath = os.path.join(repo_dirpath, "cookiecutter.json")
    with open(json_filepath) as f:
        for k, v in json.loads(f.read()).items():
            RESULTS[k] = v
            if isinstance(v, list):
                RESULTS[k] = v[0]

COPY_COOKIECUTTER_GIT = RESULTS["copy_cookiecutter_git"]
COPYRIGHT_HOLDER = RESULTS["copyright_holder"]
COPYRIGHT_LICENSE = RESULTS["copyright_license"]
GIT_EMAIL = RESULTS["git_email"]
GIT_IGNORE = RESULTS["git_ignore"]
GIT_NAME = RESULTS["git_name"]
MAKE_DIRS = RESULTS["make_dirs"]
REMOTE_NAMESPACE = RESULTS["remote_namespace"]
REMOTE_PROTOCOL = RESULTS["remote_protocol"]
REMOTE_PROVIDER = RESULTS["remote_provider"].lower()
REMOTE_USERNAME = RESULTS["remote_username"]
REPO_DESCRIPTION = RESULTS["repo_description"]
REPO_SLUG = RESULTS["repo_slug"]

REPO_DIRPATH = os.getcwd()
APACHE_LICENSE = True if COPYRIGHT_LICENSE == "Apache-2.0" else False
BITBUCKET_REPOS_URL = "https://api.bitbucket.org/2.0/repositories/{}/{}".format(
    REMOTE_NAMESPACE, REPO_SLUG
)
COOKIECUTTER_JSON_FILEPATH = os.path.join(REPO_DIRPATH, "cookiecutter.json")
COPY_COOKIECUTTER_GIT = True if COPY_COOKIECUTTER_GIT == "true" else False
CREATE_REMOTE_URL = ""
RAW_REPO_SLUG_DIRPATH = os.path.join(
    REPO_DIRPATH, "{% raw %}{{cookiecutter.repo_slug}}{% endraw %}"
)
if REMOTE_USERNAME != REMOTE_NAMESPACE:
    GITHUB_REPOS_URL = "https://api.github.com/orgs/{}/repos".format(
        REMOTE_NAMESPACE
    )
GITIGNORE_PATH = os.path.join(REPO_DIRPATH, ".gitignore")
GITIGNORE_URL = "https://www.gitignore.io/api/{}".format(GIT_IGNORE)
HOOKS_DIRPATH = os.path.join(REPO_DIRPATH, "hooks")
LICENSES_DIRPATH = os.path.join(REPO_DIRPATH, "LICENSES")
LICENSE_PATH = os.path.join(REPO_DIRPATH, "LICENSE")
LICENSE_TXT = os.path.join(
    LICENSES_DIRPATH, "{}.txt".format(COPYRIGHT_LICENSE)
)
NEW_GITIGNORE = True if GIT_IGNORE != "windows,macos,linux,git" else False
NOTICE_FILEPATH = os.path.join(REPO_DIRPATH, "NOTICE")
PASSWORD_PROMPT = "Password for 'https://{}@{}': ".format(
    REMOTE_USERNAME, REMOTE_PROVIDER
)
PROJECT_DIRPATHS = [
    os.path.join(REPO_DIRPATH, dirname.strip())
    for dirname in MAKE_DIRS.split(",")
    if dirname.strip()
]
REMOTE_DATA = {"name": REPO_SLUG, "description": REPO_DESCRIPTION}
REMOTE_REPO = True if REMOTE_PROVIDER != "none" else False
if REMOTE_PROTOCOL == "https":
    REMOTE_ORIGIN_URL = "https://{}@{}/{}/{}.git".format(
        REMOTE_USERNAME, REMOTE_PROVIDER, REMOTE_NAMESPACE, REPO_SLUG
    )
else:
    REMOTE_ORIGIN_URL = "git@{}:{}/{}.git".format(
        REMOTE_PROVIDER, REMOTE_NAMESPACE, REPO_SLUG
    )
SUCCESS_MESSAGE = "\n{} setup successfully!\n\n".format(REPO_SLUG)


def setup_git_ignore():
    if NEW_GITIGNORE:
        response = requests.get(GITIGNORE_URL)
        with open(GITIGNORE_PATH, "wb") as f:
            f.write(response)
        print("updated '{}'".format(GITIGNORE_PATH))


def setup_git_commit():
    run("git init")
    run("git status")
    run("git add -A")
    run("git status")
    run('git commit -m "Initial Commit"')


def setup_git_remote():
    if REMOTE_PROVIDER in ["bitbucket.org", "github.com"]:
        auth_info = (REMOTE_USERNAME, getpass.getpass(PASSWORD_PROMPT).strip())
        auth_data = "{}:{}".format(*auth_info)
        auth_base = base64.b64encode(auth_data.encode())

    if REMOTE_PROVIDER == "bitbucket.org":
        REMOTE_DATA.update({"has_issues": True, "is_private": True})
        JSON_HEADER["Authorization"] = "Basic {}".format(auth_base.decode())

        CREATE_REMOTE_URL = BITBUCKET_REPOS_URL
        data = json.dumps(REMOTE_DATA).encode()
        headers = JSON_HEADER

    elif REMOTE_PROVIDER == "github.com":
        CREATE_REMOTE_URL = GITHUB_REPOS_URL
        data = json.dumps(REMOTE_DATA).encode()
        headers = {"Authorization": "Basic {}".format(auth_base.decode())}

    elif REMOTE_PROVIDER == "gitlab.com":
        gitlab_token = getpass.getpass("gitlab_token: ").strip()
        token_header = {"PRIVATE-TOKEN": gitlab_token}
        search_param = {"search": REMOTE_NAMESPACE}
        search_url = GITLAB_NAMESPACES_URL + "?" + urlencode(search_param)
        search_results = requests.get(search_url, headers=token_header)
        gitlab_namespaces = json.loads(search_results)
        for namespace in gitlab_namespaces:
            if namespace.get("path", "") == REMOTE_NAMESPACE:
                namespace_id = namespace.get("id", "")
                if namespace_id:
                    REMOTE_DATA.update({"namespace_id": namespace_id})

        CREATE_REMOTE_URL = GITLAB_PROJECTS_URL
        data = bytearray(urlencode(REMOTE_DATA), "utf-8")
        headers = token_header

    requests.post(CREATE_REMOTE_URL, data=data, headers=headers)
    run("git remote add origin {}".format(REMOTE_ORIGIN_URL))
    run("git push -u origin")


def setup_git_repo():
    """A function that adds a .gitignore, initial commit, and remote repo.
    """
    setup_git_ignore()

    setup_git_commit()

    if REMOTE_REPO:
        setup_git_remote()


def setup_cookiecutter_git():
    """A simple function that removes cookiecutter-git features if not needed.
    """
    if not COPY_COOKIECUTTER_GIT:
        print("Removing '{}'...".format(COOKIECUTTER_JSON_FILEPATH))
        os.remove(COOKIECUTTER_JSON_FILEPATH)

        shutil.rmtree(HOOKS_DIRPATH, ignore_errors=True)
        shutil.rmtree(RAW_REPO_SLUG_DIRPATH, ignore_errors=True)


def setup_project_dirs():
    """A function that makes dirs and adds .gitkeep files to them.
    """
    for dirpath in PROJECT_DIRPATHS:
        try:
            os.makedirs(dirpath)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(dirpath):
                pass
            else:
                raise
        gitkeep = os.path.join(dirpath, ".gitkeep")
        with open(gitkeep, "a"):
            os.utime(gitkeep, None)


def setup_license_file():
    """A simple function that adds the chosen LICENSE and removes the rest.
    """
    if not APACHE_LICENSE:
        print("Removing '{}'...".format(NOTICE_FILEPATH))
        os.remove(NOTICE_FILEPATH)

    shutil.move(LICENSE_TXT, LICENSE_PATH)
    shutil.rmtree(LICENSES_DIRPATH, ignore_errors=True)


def main():
    """The main entry point for the post-generate project hook.
    """
    setup_license_file()
    setup_project_dirs()
    setup_cookiecutter_git()
    setup_git_repo()

    print(SUCCESS_MESSAGE)


# This is required! Don't remove!!
if __name__ == "__main__":
    main()
