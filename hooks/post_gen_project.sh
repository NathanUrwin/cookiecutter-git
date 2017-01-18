#!/usr/bin/env bash

{% if cookiecutter.license != 'Apache-2.0' %}
rm -rfv "${PWD}/NOTICE"
{% endif %}

{% if cookiecutter.gitignore != 'windows,osx,linux,git' %}
curl -fsSL 'https://www.gitignore.io/api/{{cookiecutter.gitignore}}' > "${PWD}/.gitignore"
echo "updated '$PWD/.gitignore'"
{% endif %}

git init
git status
git add -A
git status
git commit -m "Initial commit"

{% if cookiecutter.create_remote == 'yes' %}

{% if cookiecutter.remote_provider == 'GitHub' %}
{% if cookiecutter.github_org_repo_space == 'no' %}
github_api_endpoint=https://api.github.com/user/repos
{% else %}
github_api_endpoint='https://api.github.com/orgs/{{cookiecutter.repo_space}}/repos'
{% endif %}
curl -fsSL -u '{{cookiecutter.git_user}}' "$github_api_endpoint" -d '{"name":"{{cookiecutter.repo_name}}"}'
git remote add origin 'https://{{cookiecutter.git_user}}@github.com/{{cookiecutter.repo_space}}/{{cookiecutter.repo_name}}.git'

{% elif cookiecutter.remote_provider == 'GitLab' %}
namespaces="$(curl -fsSL -H "PRIVATE-TOKEN: {{cookiecutter.gitlab_token}}" 'https://gitlab.com/api/v3/namespaces?search={{cookiecutter.repo_space}}')"
repo_space="$(echo "$namespaces" | sed -n -e 's/.*"id":\(.*\),"path":"{{cookiecutter.repo_space}}".*/\1/p')"
if [ ! -z "$repo_space" ]; then
  repo_space="&namespace=${repo_space}"
fi
curl -fsSL -X POST -H "PRIVATE-TOKEN: {{cookiecutter.gitlab_token}}" "https://gitlab.com/api/v3/projects?name={{cookiecutter.repo_name}}${repo_space}"
git remote add origin 'https://{{cookiecutter.git_user}}@gitlab.com/{{cookiecutter.repo_space}}/{{cookiecutter.repo_name}}.git'

{% endif %}
git push -u origin master
{% endif %}

echo
echo
echo '{{cookiecutter.repo_name}} setup successfully!'
echo
echo
