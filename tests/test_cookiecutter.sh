#!/bin/bash
set -x
echo PATH is $PATH
cookiecutter gh:NathanUrwin/cookiecutter-git --no-input <<< yes
set +x
