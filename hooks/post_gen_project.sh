#!/usr/bin/env bash
{% if cookiecutter.license != 'Apache-2.0' %}
rm -rfv $PWD/NOTICE
{% endif %}{% if cookiecutter.gitignore != 'windows,osx,linux,git' %}
curl -fsSL https://www.gitignore.io/api/{{cookiecutter.gitignore}} > $PWD/.gitignore
echo "updated '$PWD/.gitignore'"
{% endif %}
echo
echo
echo '{{cookiecutter.repo_name}} setup successfully!'
echo
echo
