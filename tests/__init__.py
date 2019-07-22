#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pathlib import Path

import auger
#from cookiecutter.main import cookiecutter

sys.path.append(str(Path(__file__).resolve().parents[1]))
from hooks.post_gen_project import main, PostGenProjectHook


if __name__ == "__main__":
    with auger.magic([PostGenProjectHook]):
        #cookiecutter_git_path = str(Path(__file__).resolve().parents[1])
        #cookiecutter(cookiecutter_git_path)
        main()
