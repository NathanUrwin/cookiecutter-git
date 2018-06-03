#!/bin/bash
apt-cache policy python-cookiecutter
/usr/local/bin/cookiecutter gh:NathanUrwin/cookiecutter-git --no-input <<< yes
