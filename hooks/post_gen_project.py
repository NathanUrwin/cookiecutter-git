#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import base64
import urllib
import urllib2
import getpass
import subprocess

REPO_PATH = os.getcwd()
NOTICE_PATH = os.path.join(REPO_PATH, u'NOTICE')
GITIGNORE_PATH = os.path.join(REPO_PATH, u'.gitignore')
GITIGNORE_URL = u'https://www.gitignore.io/api/{{cookiecutter.gitignore}}'

{% if cookiecutter.github_org_repo_space == 'no' %}
GITHUB_REPOS_URL = u'https://api.github.com/user/repos'
{% else %}
GITHUB_REPOS_URL = u'https://api.github.com/orgs/{{cookiecutter.repo_space}}/repos'
{% endif %}

GITLAB_TOKEN_HEADER = {u'PRIVATE-TOKEN': u'{{cookiecutter.gitlab_token}}'}
GITLAB_NAMESPACES_URL = u'https://gitlab.com/api/v3/namespaces'
GITLAB_PROJECTS_URL = u'https://gitlab.com/api/v3/projects'
REPO_REMOTE_URL = (u'https://{{cookiecutter.git_user}}@'
    u'{{cookiecutter.remote_provider|lower}}.com/'
    u'{{cookiecutter.repo_space}}/{{cookiecutter.repo_name}}.git')
REPO_NAME_DATA = {u'name': u'{{cookiecutter.repo_name}}'}


def run(command, log=True):
    try:
        output = subprocess.check_output(command)
    except subprocess.CalledProcessError as error:
        print u'%s: %s\n%s' % (error.returncode, error.cmd, error.output)
        raise error
    else:
        if output and log:
            print u'%s\n%s' % (u' '.join(command), output)
        else:
            print u' '.join(command)
    return output


def request(url, headers=None, data=None, log=True):
    try:
        req = urllib2.Request(url, data=data, headers=headers)
        response = urllib2.urlopen(req)
        content = response.read()
        response.close()
    except urllib2.HTTPError as error:
        message = error.read()
        error.close()
        print u'%s %s: %s\n%s' % (error.code, error.reason, url, message)
        raise error
    else:
        if content and log:
            print u'%s\n%s' % (url, content)
        else:
            print url
    return content


def create_github_repo():
    data = json.dumps(REPO_NAME_DATA)
    prompt = (u"Password for 'https://{{cookiecutter.git_user}}@"
        u"{{cookiecutter.remote_provider|lower}}.com': ")
    auth_info = (u'{{cookiecutter.git_user}}', getpass.getpass(prompt).strip())
    auth_base = base64.b64encode(u'%s:%s' % auth_info)
    headers = {u'Authorization': u'Basic %s' % auth_base}
    request(GITHUB_REPOS_URL, data=data, headers=headers)


def create_gitlab_repo():
    search_param = {u'search': u'{{cookiecutter.repo_space}}'}
    search_url = GITLAB_NAMESPACES_URL + u'?' + urllib.urlencode(search_param)
    search_results = request(search_url, headers=GITLAB_TOKEN_HEADER)
    gitlab_namespaces = json.loads(search_results)
    for namespace in gitlab_namespaces:
        if namespace.get(u'name', u'') == u'{{cookiecutter.repo_space}}':
            namespace_id = namespace.get(u'id', u'')
    if namespace_id:
        REPO_NAME_DATA.update({u'namespace_id': namespace_id})
    data = unicode(urllib.urlencode(REPO_NAME_DATA))
    request(GITLAB_PROJECTS_URL, data=data, headers=GITLAB_TOKEN_HEADER)

{% if cookiecutter.license != 'Apache-2.0' %}
print u"Removing '%s'..." % NOTICE_PATH
os.remove(NOTICE_PATH)
{% endif %}

{% if cookiecutter.gitignore != 'windows,osx,linux,git' %}
with open(GITIGNORE_PATH, u'wb') as f:
    f.write(request(GITIGNORE_URL))
print u"updated '%s'" % GITIGNORE_PATH
{% endif %}

run([u'git', u'init'])
run([u'git', u'status'])
run([u'git', u'add', u'-A'])
run([u'git', u'status'])
run([u'git', u'commit', u'-m', u'"Initial commit"'])

{% if cookiecutter.create_remote == 'yes' %}

{% if cookiecutter.remote_provider == 'GitHub' %}
create_github_repo()
{% elif cookiecutter.remote_provider == 'GitLab' %}
create_gitlab_repo()
{% endif %}

run([u'git', u'remote', u'add', u'origin', REPO_REMOTE_URL])
run([u'git', u'push', u'-u', u'origin', u'master'])

{% endif %}

print
print
print u'{{cookiecutter.repo_name}} setup successfully!'
print
print
