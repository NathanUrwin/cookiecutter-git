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
    """A quick-and-dirty function that mimicks the invoke local run.
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
        elif log:
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


class PostGenProjectHook(object):
    """
    """
    github_repos_url = "https://api.github.com/user/repos"
    json_header = {"Content-Type": "application/json; charset=utf-8"}

    def __init__(self, *args, **kwargs):
        self.results = self._get_cookiecutter_results()
        self.copy_cookiecutter_git = self.results.get("copy_cookiecutter_git")
        self.copyright_holder = self.results.get("copyright_holder")
        self.copyright_license = self.results.get("copyright_license")
        self.git_email = self.results.get("git_email")
        self.git_ignore = self.results.get("git_ignore")
        self.git_name = self.results.get("git_name")
        self.make_dirs = self.results.get("make_dirs")
        self.remote_namespace = self.results.get("remote_namespace")
        self.remote_protocol = self.results.get("remote_protocol")
        self.remote_provider = self.results.get("remote_provider", "").lower()
        self.remote_username = self.results.get("remote_username")
        self.repo_description = self.results.get("repo_description")
        self.repo_slug = self.results.get("repo_slug")

        self.repo_dirpath = os.getcwd()
        self.apache_license = (
            True if self.copyright_license == "Apache-2.0" else False
        )
        self.bitbucket_repos_url = "https://api.bitbucket.org/2.0/repositories/{}/{}".format(
            self.remote_namespace, self.repo_slug
        )
        self.cookiecutter_json_filepath = os.path.join(
            self.repo_dirpath, "cookiecutter.json"
        )
        self.copy_cookiecutter_git = (
            True if self.copy_cookiecutter_git == "true" else False
        )
        self.create_remote_url = None
        self.raw_repo_slug_dirpath = os.path.join(
            self.repo_dirpath,
            "{% raw %}{{cookiecutter.repo_slug}}{% endraw %}",
        )
        if self.remote_username != self.remote_namespace:
            self.github_repos_url = "https://api.github.com/orgs/{}/repos".format(
                self.remote_namespace
            )
        self.git_ignore_filepath = os.path.join(
            self.repo_dirpath, ".gitignore"
        )
        self.git_ignore_url = "https://www.gitignore.io/api/{}".format(
            self.git_ignore
        )
        self.headers = {}
        self.hooks_dirpath = os.path.join(self.repo_dirpath, "hooks")
        self.licenses_dirpath = os.path.join(self.repo_dirpath, "LICENSES")
        self.license_filepath = os.path.join(self.repo_dirpath, "LICENSE")
        self.nested_license_filepath = os.path.join(
            self.licenses_dirpath, "{}.txt".format(self.copyright_license)
        )
        self.new_git_ignore = (
            True if self.git_ignore != "windows,macos,linux,git" else False
        )
        self.notice_filepath = os.path.join(self.repo_dirpath, "NOTICE")
        self.password_prompt = "Password for 'https://{}@{}': ".format(
            self.remote_username, self.remote_provider
        )
        self.project_dirpaths = [
            os.path.join(self.repo_dirpath, dirname.strip())
            for dirname in self.make_dirs.split(",")
            if dirname.strip()
        ]
        self.remote_data = {
            "name": self.repo_slug,
            "description": self.repo_description,
        }
        if self.remote_provider == "bitbucket.org":
            self.create_remote_url = self.bitbucket_repos_url
            self.headers.update(self.json_header)
            self.remote_data.update({"has_issues": True, "is_private": True})
        elif self.remote_provider == "github.com":
            self.create_remote_url = self.github_repos_url
        self.encoded_data = json.dumps(self.remote_data).encode()
        self.remote_password = None
        self.remote_repo = True if self.remote_provider != "none" else False
        self.remote_origin_url = "https://{}@{}/{}/{}.git".format(
            self.remote_username,
            self.remote_provider,
            self.remote_namespace,
            self.repo_slug,
        )
        if self.remote_protocol == "ssh":
            self.remote_origin_url = "git@{}:{}/{}.git".format(
                self.remote_provider, self.remote_namespace, self.repo_slug
            )
        self.remote_message = (
            "\n\nCheck out the remote here: https://{}/{}/{}".format(
                self.remote_provider, self.remote_namespace, self.repo_slug
            )
            if self.remote_repo
            else ""
        )
        self.success_message = "\n\n{} setup successfully!{}\n\n".format(
            self.repo_slug, self.remote_message
        )

    def _get_cookiecutter_results(self):
        """
        """
        # remove as much jinja2 templating from this file as possible
        try:
            results = json.loads("""{{ cookiecutter | tojson() }}""")

        # this is temporary hack around for `pipenv run pytest`
        except json.JSONDecodeError:
            results = {}
            repo_dirpath = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )
            json_filepath = os.path.join(repo_dirpath, "cookiecutter.json")
            with open(json_filepath) as f:
                for k, v in json.loads(f.read()).items():
                    results[k] = v
                    if isinstance(v, list):
                        results[k] = v[0]
        return results

    def _git_push_origin(self):
        """Creates a remote repo if needed and pushes to origin.
        """
        if self.remote_provider != "none":
            # temp hack for `pytest-dotenv`. need to mock requests
            self.remote_password = (
                base64.b64decode(os.environ.get("REMOTE_PASSWORD", "").strip())
                .strip()
                .decode()
            )
            if not self.remote_password:
                self.remote_password = getpass.getpass(
                    self.password_prompt
                ).strip()

        if self.remote_provider in ["bitbucket.org", "github.com"]:
            # http basic auth if needed
            auth_info = (self.remote_username, self.remote_password)
            auth_data = "{}:{}".format(*auth_info)
            auth_base = base64.b64encode(auth_data.encode())
            self.headers["Authorization"] = "Basic {}".format(
                auth_base.decode()
            )

            # create remote POST request
            requests.post(
                self.create_remote_url,
                data=self.encoded_data,
                headers=self.headers,
            )

        # git push
        run("git remote add origin {}".format(self.remote_origin_url))
        run(
            "git push -u origin <<< {}".format(self.remote_password), log=False
        )
        print("> git push -u origin")

    def _git_init_commit(self):
        """Creates a git repo with the first (initial) commit.
        """
        run("git init")
        run("git status")
        run("git add -A")
        run("git status")
        run('git commit -m "Initial commit"')

    def _git_ignore(self):
        """Creates a new .gitignore if needed from gitignore.io.
        """
        if self.new_git_ignore:
            # gitignore.io/api -> .gitignore
            response = requests.get(self.git_ignore_url)
            with open(self.git_ignore_filepath, "wb") as f:
                f.write(response)
            print("updated '{}'".format(self.git_ignore_filepath))

    def _git_repo(self):
        """Adds a .gitignore, initial commit, and remote repo.
        """
        self._git_ignore()
        self._git_init_commit()
        if self.remote_repo:
            self._git_push_origin()

    def _make_dirs(self):
        """Makes dirs and adds .gitkeep files to them.
        """
        for dirpath in self.project_dirpaths:
            # equal to bash `mkdir -p`
            try:
                os.makedirs(dirpath)
            except OSError as exc:
                if exc.errno == errno.EEXIST and os.path.isdir(dirpath):
                    pass
                else:
                    raise

            gitkeep = os.path.join(dirpath, ".gitkeep")
            # equal to bash `touch`
            with open(gitkeep, "a"):
                os.utime(gitkeep, None)

    def _copy_cookiecutter_git(self):
        """Removes cookiecutter-git features if not needed.
        """
        if not self.copy_cookiecutter_git:
            print("Removing '{}'...".format(self.cookiecutter_json_filepath))
            os.remove(self.cookiecutter_json_filepath)

            shutil.rmtree(self.hooks_dirpath, ignore_errors=True)
            shutil.rmtree(self.raw_repo_slug_dirpath, ignore_errors=True)

    def _copyright_license(self):
        """Adds the chosen LICENSE and removes the rest.
        """
        if not self.apache_license:
            print("Removing '{}'...".format(self.notice_filepath))
            os.remove(self.notice_filepath)

        shutil.move(self.nested_license_filepath, self.license_filepath)
        shutil.rmtree(self.licenses_dirpath, ignore_errors=True)

    def run(self):
        """
        """
        self._copyright_license()
        self._copy_cookiecutter_git()
        self._make_dirs()
        self._git_repo()
        print(self.success_message)


def main():
    """Post-generate project hook main entry point.
    """
    PostGenProjectHook().run()


# This is required! Don't remove!!
if __name__ == "__main__":
    main()
