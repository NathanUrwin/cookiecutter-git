#!/usr/bin/env bash

{% if cookiecutter.license != 'Apache-2.0' %}
rm -rfv $PWD/NOTICE
{% endif %}

{% if cookiecutter.gitignore != 'windows,osx,linux,git' %}
curl -fsSL https://www.gitignore.io/api/{{cookiecutter.gitignore}} > $PWD/.gitignore
echo "updated '$PWD/.gitignore'"
{% endif %}

git init
git status
git add -A
git status
git commit -m "Initial commit"

{% if cookiecutter.create_remote == 'y' %}

{% if cookiecutter.repo_space_is_org == 'n' %}
github_api_endpoint=https://api.github.com/user/repos
{% else %}
github_api_endpoint=https://api.github.com/orgs/{{cookiecutter.repo_space}}/repos
{% endif %}

curl -fsSL -u '{{cookiecutter.github_user}}' $github_api_endpoint -d '{"name":"{{cookiecutter.repo_name}}"}'
git remote add origin https://{{cookiecutter.github_user}}@github.com/{{cookiecutter.repo_space}}/{{cookiecutter.repo_name}}.git
git push -u origin master
{% endif %}

echo
echo
echo '{{cookiecutter.repo_name}} setup successfully!'
echo
echo
