# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

"""
Cookiecutter-Git Post Project Generation Hook Module.
"""
import base64
import errno
import getpass
import json
import os
import shlex
import shutil

from invoke import Responder, Result, run
import requests


class PostGenProjectHook(object):
    """
    Post Project Generation Class Hook.
    """

    bitbucket_repos_url_base = (
        "https://api.bitbucket.org/2.0/repositories/{}/{}"
    )
    create_remote_url = None
    github_repos_url = "https://api.github.com/user/repos"
    git_ignore_url_base = "https://www.gitignore.io/api/{}"
    headers = {}
    json_header = {"Content-Type": "application/json; charset=utf-8"}
    password_prompt_base = "Password for 'https://{}@{}': "
    remote_message_base = "Also see: https://{}/{}/{}"
    success_message_base = "\n\nSuccess! Your project was created here:\n{}\n{}\nThanks for using cookiecutter-git! :)\n\n"
    repo_dirpath = os.getcwd()
    cookiecutter_json_filepath = os.path.join(
        repo_dirpath, "cookiecutter.json"
    )
    raw_repo_slug_dirpath = os.path.join(
        repo_dirpath, "{% raw %}{{cookiecutter.repo_slug}}{% endraw %}"
    )
    git_ignore_filepath = os.path.join(repo_dirpath, ".gitignore")
    hooks_dirpath = os.path.join(repo_dirpath, "hooks")
    licenses_dirpath = os.path.join(repo_dirpath, "LICENSES")
    license_filepath = os.path.join(repo_dirpath, "LICENSE")
    notice_filepath = os.path.join(repo_dirpath, "NOTICE")

    def __init__(self, *args, **kwargs):
        """
        Initializes the class instance.
        """
        self.result = self._get_cookiecutter_result()
        self.copy_cookiecutter_git = self.result.get("copy_cookiecutter_git")
        self.copyright_holder = self.result.get("copyright_holder")
        self.copyright_license = self.result.get("copyright_license")
        self.git_email = self.result.get("git_email")
        self.git_ignore = self.result.get("git_ignore")
        self.git_name = self.result.get("git_name")
        self.make_dirs = self.result.get("make_dirs")
        self.remote_namespace = self.result.get("remote_namespace")
        self.remote_protocol = self.result.get("remote_protocol")
        self.remote_provider = str(self.result.get("remote_provider")).lower()
        self.remote_username = self.result.get("remote_username")
        self.repo_slug = self.result.get("repo_slug")
        self.repo_summary = self.result.get("repo_summary")
        self.repo_tagline = self.result.get("repo_tagline")
        self._testing = (
            True
            if str(self.result.get("_testing")).lower() == "true"
            else False
        )
        self.apache_license = self.copyright_license == "Apache-2.0"
        self.bitbucket_repos_url = self.bitbucket_repos_url_base.format(
            self.remote_namespace, self.repo_slug
        )
        self.copy_cookiecutter_git = self.copy_cookiecutter_git == "true"
        self.git_ignore_url = self.git_ignore_url_base.format(self.git_ignore)
        self.nested_license_filepath = os.path.join(
            self.licenses_dirpath, "{}.txt".format(self.copyright_license)
        )
        self.new_git_ignore = self.git_ignore != "windows,macos,linux,git"
        self.password_prompt = self.password_prompt_base.format(
            self.remote_username, self.remote_provider
        )
        self.project_dirpaths = [
            os.path.join(self.repo_dirpath, dirname.strip())
            for dirname in self.make_dirs.split(",")
            if dirname.strip()
        ]
        self.remote_data = {
            "name": self.repo_slug,
            "description": self.repo_tagline,
        }
        self.create_remote_url = self._get_create_remote_url()
        self.encoded_data = json.dumps(self.remote_data).encode()
        self.remote_password = None
        self.remote_repo = self.remote_provider != "none"
        self.remote_origin_url = self._get_remote_origin_url()
        self.remote_message = (
            self.remote_message_base.format(
                self.remote_provider, self.remote_namespace, self.repo_slug
            )
            if self.remote_repo
            else ""
        )
        self.success_message = self.success_message_base.format(
            self.repo_dirpath, self.remote_message
        )

    @staticmethod
    def format_basic_auth(username, password):
        """
        Formats HTTP Basic auth with base64 encoding.

        :param username:
        :param password:
        """
        auth_data = "{}:{}".format(username, password)
        return base64.b64encode(auth_data.encode())

    @staticmethod
    def parse_dotenv_password():
        """
        Parses the remote password from os environ.
        """
        return os.environ.get("REMOTE_PASSWORD", "").strip()

    @staticmethod
    def git_init():
        """
        Runs git init.
        """
        run("git init")

    @staticmethod
    def git_add():
        """
        Runs git add all.
        """
        # `git add -A`
        run("git add --all")

    @staticmethod
    def git_commit(message="Initial commit"):
        """
        Runs git commit with an initial message.

        :param message:
        """
        # `git commit -m "Initial commit"`
        run('git commit --message="{}"'.format(message))

    @staticmethod
    def _get_cookiecutter_result():
        """
        Removes as much jinja2 templating from the hook as possible.
        """
        # http://flask.pocoo.org/docs/latest/templating/#standard-filters
        try:
            result = json.loads("""{{ cookiecutter | tojson() }}""")
        # current temp hack around for `pipenv run pytest -s`
        except json.JSONDecodeError:
            result = {}
            repo_dirpath = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )
            json_filepath = os.path.join(repo_dirpath, "cookiecutter.json")
            with open(json_filepath) as f:
                for k, v in json.loads(f.read()).items():
                    result[k] = v
                    if isinstance(v, list):
                        result[k] = v[0]
        return result

    def _get_create_remote_url(self):
        """
        Gets the create remote URL.
        """
        create_remote_url = None
        if self.remote_username != self.remote_namespace:
            self.github_repos_url = "https://api.github.com/orgs/{}/repos".format(
                self.remote_namespace
            )
        if self.remote_provider == "bitbucket.org":
            create_remote_url = self.bitbucket_repos_url
            self.headers.update(self.json_header)
            self.remote_data.update({"has_issues": True, "is_private": True})
        elif self.remote_provider == "github.com":
            create_remote_url = self.github_repos_url
        return create_remote_url

    def _get_remote_origin_url(self):
        """
        Gets the remote origin URL.
        """
        remote_origin_url = "https://{}@{}/{}/{}.git".format(
            self.remote_username,
            self.remote_provider,
            self.remote_namespace,
            self.repo_slug,
        )
        if self.remote_protocol == "ssh":
            remote_origin_url = "git@{}:{}/{}.git".format(
                self.remote_provider, self.remote_namespace, self.repo_slug
            )
        return remote_origin_url

    def _git_push(self):
        """
        Pushes the git remote and sets as upstream.
        """
        if self._testing:
            print("_testing _git_push")
            r = Result(
                """Password for 'https://NathanUrwin@github.com':
Counting objects: 18, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (15/15), done.
Writing objects: 100% (18/18), 6.24 KiB | 0 bytes/s, done.
Total 18 (delta 0), reused 0 (delta 0)
To https://github.com/NathanUrwin/cookiecutter-git-demo.git
* [new branch]      master -> master
Branch master set up to track remote branch master from origin.""",
                command="git push --set-upstream origin master",
            )
            print(r.stdout)
            return r
        else:
            watchers = [
                Responder(
                    pattern=self.password_prompt,
                    response=self.remote_password + "\n",
                )
            ]
            # `git push -u origin master`
            run(
                "git push --set-upstream origin master",
                pty=True,
                watchers=watchers,
            )

    def _git_remote_add(self):
        """
        Adds the git remote origin with url.
        """
        run("git remote add origin {}".format(self.remote_origin_url))

    def _git_remote_repo(self):
        """
        Creates a remote repo if needed.
        """
        if self.remote_provider in ["bitbucket.org", "github.com"]:
            # http basic auth if needed
            auth_base64 = self.format_basic_auth(
                self.remote_username, self.remote_password
            )
            self.headers["Authorization"] = "Basic {}".format(
                auth_base64.decode()
            )
            # create remote POST request
            requests.post(
                self.create_remote_url,
                data=self.encoded_data,
                headers=self.headers,
            )

    def _set_remote_password(self):
        """
        Sets the remote password by parsing the dotenv or with getpass.
        """
        # current hack for tests. better work around ?
        self.remote_password = self.parse_dotenv_password()
        if not self.remote_password:
            # prompt CLI users for password
            self.remote_password = getpass.getpass(
                self.password_prompt
            ).strip()

    def _git_ignore(self):
        """
        Creates a new .gitignore if needed from gitignore.io.
        """
        if self.new_git_ignore:
            # gitignore.io/api -> {{cookiecutter.repo_slug}}/.gitignore
            response = requests.get(self.git_ignore_url)
            with open(self.git_ignore_filepath, "wb") as f:
                f.write(response.text)
            print("updated '{}'".format(self.git_ignore_filepath))

    def _git_repo(self):
        """
        Adds a .gitignore, initial commit, and remote repo.
        """
        self._git_ignore()
        self.git_init()
        self.git_add()
        self.git_commit()
        if self.remote_repo:
            self._set_remote_password()
            self._git_remote_repo()
            self._git_remote_add()
            self._git_push()

    def _make_dirs(self):
        """
        Makes dirs and adds .gitkeep files to them.
        """
        for dirpath in self.project_dirpaths:
            # equal to bash `mkdir -p $dirpath`
            try:
                os.makedirs(dirpath)
            except OSError as exc:
                if exc.errno == errno.EEXIST and os.path.isdir(dirpath):
                    pass
                else:
                    raise
            # equal to bash `touch $dirpath/.gitkeep`
            gitkeep = os.path.join(dirpath, ".gitkeep")
            with open(gitkeep, "a"):
                os.utime(gitkeep, None)

    def _copy_cookiecutter_git(self):
        """
        Removes cookiecutter-git features if not needed.
        """
        if not self.copy_cookiecutter_git:
            print("Removing '{}'...".format(self.cookiecutter_json_filepath))
            os.remove(self.cookiecutter_json_filepath)
            shutil.rmtree(self.hooks_dirpath, ignore_errors=True)
            shutil.rmtree(self.raw_repo_slug_dirpath, ignore_errors=True)

    def _copyright_license(self):
        """
        Adds the chosen LICENSE and removes the rest.
        """
        if not self.apache_license:
            print("Removing '{}'...".format(self.notice_filepath))
            os.remove(self.notice_filepath)
        shutil.move(self.nested_license_filepath, self.license_filepath)
        shutil.rmtree(self.licenses_dirpath, ignore_errors=True)

    def run(self):
        """
        Sets up the project license, dirs, and git repo.
        """
        self._copyright_license()
        self._copy_cookiecutter_git()
        self._make_dirs()
        self._git_repo()
        print(self.success_message)


def main():
    """
    Runs the post gen project hook main entry point.
    """
    PostGenProjectHook().run()


# This is required! Don't remove!!
if __name__ == "__main__":
    main()
