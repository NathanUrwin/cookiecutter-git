#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

import os
import json
import base64
import urllib
import urllib2
import getpass
import subprocess

REPO_PATH = os.getcwd()
NOTICE_PATH = os.path.join(REPO_PATH, 'NOTICE')
GITIGNORE_PATH = os.path.join(REPO_PATH, '.gitignore')
GITIGNORE_URL = 'https://www.gitignore.io/api/{{cookiecutter.gitignore}}'

{% if cookiecutter.git_user == cookiecutter.repo_space %}
GITHUB_REPOS_URL = 'https://api.github.com/user/repos'
{% else %}
GITHUB_REPOS_URL = 'https://api.github.com/orgs/{{cookiecutter.repo_space}}/repos'
{% endif %}

{% if cookiecutter.remote_provider == 'GitLab' %}
GITLAB_TOKEN = getpass.getpass('gitlab_token: ').strip()
GITLAB_TOKEN_HEADER = {'PRIVATE-TOKEN': GITLAB_TOKEN}
{% endif %}
GITLAB_NAMESPACES_URL = 'https://gitlab.com/api/v3/namespaces'
GITLAB_PROJECTS_URL = 'https://gitlab.com/api/v3/projects'
REPO_REMOTE_URL = ('https://{{cookiecutter.git_user}}@'
    '{{cookiecutter.remote_provider|lower}}.com/'
    '{{cookiecutter.repo_space}}/{{cookiecutter.repo_name}}.git')
REPO_NAME_DATA = {'name': '{{cookiecutter.repo_name}}'}


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


def create_github_repo():
    data = json.dumps(REPO_NAME_DATA)
    prompt = ("Password for 'https://{{cookiecutter.git_user}}@"
        "{{cookiecutter.remote_provider|lower}}.com': ")
    auth_info = ('{{cookiecutter.git_user}}', getpass.getpass(prompt).strip())
    auth_base = base64.b64encode('{}:{}'.format(*auth_info))
    headers = {'Authorization': 'Basic {}'.format(auth_base)}
    requests.post(GITHUB_REPOS_URL, data=data, headers=headers)


def create_gitlab_repo():
    search_param = {'search': '{{cookiecutter.repo_space}}'}
    search_url = GITLAB_NAMESPACES_URL + '?' + urllib.urlencode(search_param)
    search_results = requests.get(search_url, headers=GITLAB_TOKEN_HEADER)
    gitlab_namespaces = json.loads(search_results)
    for namespace in gitlab_namespaces:
        if namespace.get('name', '') == '{{cookiecutter.repo_space}}':
            namespace_id = namespace.get('id', '')
    if namespace_id:
        REPO_NAME_DATA.update({'namespace_id': namespace_id})
    data = unicode(urllib.urlencode(REPO_NAME_DATA))
    requests.post(GITLAB_PROJECTS_URL, data=data, headers=GITLAB_TOKEN_HEADER)

{% if cookiecutter.license != 'Apache-2.0' %}
print("Removing '{}'...".format(NOTICE_PATH))
os.remove(NOTICE_PATH)
{% endif %}

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

{% if cookiecutter.remote_provider == 'GitHub' %}
create_github_repo()
{% elif cookiecutter.remote_provider == 'GitLab' %}
create_gitlab_repo()
{% endif %}

run(['git', 'remote', 'add', 'origin', REPO_REMOTE_URL])
run(['git', 'push', '-u', 'origin', 'master'])

{% endif %}

print()
print('{{cookiecutter.repo_name}} setup successfully!')
print()
print()
