#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

import os
import json
import shutil
import base64
import urllib
import urllib2
import getpass
import subprocess

REPO_PATH = os.getcwd()
LICENSES_DIRPATH = os.path.join(REPO_PATH, 'LICENSES')
LICENSE_TXT = os.path.join(LICENSES_DIRPATH, '{{cookiecutter.license}}.txt')
LICENSE_PATH = os.path.join(REPO_PATH, 'LICENSE')
NOTICE_PATH = os.path.join(REPO_PATH, 'NOTICE')
GITIGNORE_PATH = os.path.join(REPO_PATH, '.gitignore')
GITIGNORE_URL = 'https://www.gitignore.io/api/{{cookiecutter.gitignore}}'
JSON_HEADER = {'Content-Type': 'application/json; charset=utf-8'}

BITBUCKET_REPOS_URL = ('https://api.bitbucket.org/2.0/repositories/'
    '{{cookiecutter.repository_namespace}}/{{cookiecutter.repository_slug}}')

{% if cookiecutter.git_username == cookiecutter.repository_namespace %}
GITHUB_REPOS_URL = 'https://api.github.com/user/repos'
{% else %}
GITHUB_REPOS_URL = ('https://api.github.com/orgs/'
    '{{cookiecutter.repository_namespace}}/repos')
{% endif %}

{% if cookiecutter.remote_provider == 'gitlab.com' %}
GITLAB_TOKEN = getpass.getpass('gitlab_token: ').strip()
GITLAB_TOKEN_HEADER = {'PRIVATE-TOKEN': GITLAB_TOKEN}
{% endif %}
GITLAB_NAMESPACES_URL = 'https://gitlab.com/api/v3/namespaces'
GITLAB_PROJECTS_URL = 'https://gitlab.com/api/v3/projects'

REMOTE_REPO_URL = ('https://{{cookiecutter.git_username}}@'
    '{{cookiecutter.remote_provider}}/{{cookiecutter.repository_namespace}}/'
    '{{cookiecutter.repository_slug}}.git')
REMOTE_REPO_DATA = {
    'name': '{{cookiecutter.repository_slug}}',
    'description': '{{cookiecutter.repository_description}}'
    }


def run(command, log=True):
    try:
        output = subprocess.check_output(command)
    except subprocess.CalledProcessError as error:
        print('{}: {}\n{}'.format(error.returncode, error.cmd, error.output))
        raise error
    else:
        if output and log:
            print('{}\n{}'.format(' '.join(command), output))
        else:
            print(' '.join(command))
    return output


def _request(url, headers, data, log):
    try:
        req = urllib2.Request(url, data=data, headers=headers)
        response = urllib2.urlopen(req)
        content = response.read()
        response.close()
    except urllib2.HTTPError as error:
        message = error.read()
        error.close()
        print('{} {}: {}\n{}'.format(error.code, error.reason, url, message))
        raise SystemExit
    else:
        if content and log:
            print('{}\n{}'.format(url, content))
        else:
            print(url)
    return content


class requests(object):

    @staticmethod
    def get(url, headers={}, log=True):
        return _request(url, headers, None, log)

    @staticmethod
    def post(url, headers={}, data=None, log=True):
        return _request(url, headers, data, log)


def create_remote_repo():
    {% if cookiecutter.remote_provider == 'github.com' %}
    data = json.dumps(REMOTE_REPO_DATA)
    prompt = ("Password for 'https://{{cookiecutter.git_username}}@"
        "{{cookiecutter.remote_provider}}': ")
    auth_info = ('{{cookiecutter.git_username}}',
                 getpass.getpass(prompt).strip())
    auth_base = base64.b64encode('{}:{}'.format(*auth_info))
    headers = {'Authorization': 'Basic {}'.format(auth_base)}
    requests.post(GITHUB_REPOS_URL, data=data, headers=headers)

    {% elif cookiecutter.remote_provider == 'gitlab.com' %}
    search_param = {'search': '{{cookiecutter.repository_namespace}}'}
    search_url = GITLAB_NAMESPACES_URL + '?' + urllib.urlencode(search_param)
    search_results = requests.get(search_url, headers=GITLAB_TOKEN_HEADER)
    gitlab_namespaces = json.loads(search_results)
    for namespace in gitlab_namespaces:
        if namespace.get('name', '') == '{{cookiecutter.repository_namespace}}':
            namespace_id = namespace.get('id', '')
    if namespace_id:
        REMOTE_REPO_DATA.update({'namespace_id': namespace_id})
    data = unicode(urllib.urlencode(REMOTE_REPO_DATA))
    requests.post(GITLAB_PROJECTS_URL, data=data, headers=GITLAB_TOKEN_HEADER)

    {% elif cookiecutter.remote_provider == 'bitbucket.org' %}
    REMOTE_REPO_DATA.update({'has_issues': True, 'is_private': True})
    data = json.dumps(REMOTE_REPO_DATA)
    prompt = ("Password for 'https://{{cookiecutter.git_username}}@"
        "{{cookiecutter.remote_provider}}': ")
    auth_info = ('{{cookiecutter.git_username}}',
                 getpass.getpass(prompt).strip())
    auth_base = base64.b64encode('{}:{}'.format(*auth_info))
    JSON_HEADER['Authorization'] = 'Basic {}'.format(auth_base)
    requests.post(BITBUCKET_REPOS_URL, data=data, headers=JSON_HEADER)
    {% endif %}


def setup_license_file():
    {% if cookiecutter.license != 'Apache-2.0' %}
    print("Removing '{}'...".format(NOTICE_PATH))
    os.remove(NOTICE_PATH)
    {% endif %}
    shutil.move(LICENSE_TXT, LICENSE_PATH)
    shutil.rmtree(LICENSES_DIRPATH, ignore_errors=True)


def setup_git_repo():
    {% if cookiecutter.gitignore != 'windows,osx,linux,git' %}
    with open(GITIGNORE_PATH, 'wb') as f:
        f.write(requests.get(GITIGNORE_URL))
    print("updated '{}'".format(GITIGNORE_PATH))
    {% endif %}

    run(['git', 'init'])
    run(['git', 'status'])
    run(['git', 'add', '-A'])
    run(['git', 'status'])
    run(['git', 'commit', '-m', 'Initial commit'])

    {% if cookiecutter.create_remote == 'yes' %}
    create_remote_repo()
    run(['git', 'remote', 'add', 'origin', REMOTE_REPO_URL])
    run(['git', 'push', '-u', 'origin', 'master'])
    {% endif %}


def main():
    setup_license_file()
    setup_git_repo()
    print('\n{{cookiecutter.repository_slug}} setup successfully!\n\n')


if __name__ == '__main__':
    main()
