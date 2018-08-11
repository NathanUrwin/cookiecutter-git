# cookiecutter-git

[![Tagged Release](https://img.shields.io/badge/release-v0.6.1-blue.svg?longCache=true)](https://github.com/NathanUrwin/cookiecutter-git/releases/tag/v0.6.1)
[![Development Status](https://img.shields.io/badge/status-beta-brightgreen.svg?longCache=true)](ROADMAP.md)
[![Build Status](https://travis-ci.org/NathanUrwin/cookiecutter-git.svg?branch=master)](https://travis-ci.org/NathanUrwin/cookiecutter-git)
[![Build Status](https://ci.appveyor.com/api/projects/status/3q0aik8sgmndwibp/branch/master?svg=true)](https://ci.appveyor.com/project/NathanUrwin/cookiecutter-git/branch/master)
[![codecov](https://codecov.io/gh/NathanUrwin/cookiecutter-git/branch/master/graph/badge.svg)](https://codecov.io/gh/NathanUrwin/cookiecutter-git)
[![python](https://img.shields.io/badge/python-2.7%2C%203.4%2C%203.5%2C%203.6%2C%203.7-blue.svg?longCache=true)](https://www.python.org/downloads/)

> Git repo project template using Cookiecutter :cookie:

[![Cookiecutter-Git Logo](images/logo-256.png)](https://dylantyates.com/graphics)

This project is inspired by [cookiecutter-template by eviweb](https://github.com/eviweb/cookiecutter-template), and consists of a [cookiecutter](https://github.com/audreyr/cookiecutter#cookiecutter) (project template) that provides the necessary [markdown](https://guides.github.com/features/mastering-markdown/) docs and other files to pass [GitHub's recommended community standards](https://blog.github.com/2017-06-14-new-community-tools/) with an added bonus: remote repos are created for you [*automagically*](https://youtu.be/Z3qK8gT5LLg?t=24s)! :crystal_ball::zap::boom:

_**Note:** The [Beta release](https://github.com/NathanUrwin/cookiecutter-git/releases/tag/v0.5.0) introduces [breaking changes](https://github.com/NathanUrwin/cookiecutter-git/compare/v0.4.1...v0.5.0)! [Invoke](http://docs.pyinvoke.org/en/1.1/) and [Requests](http://docs.python-requests.org/en/master/) are **now required** and [the prompts](#documentation) have changed!_

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Requirements](#requirements)
  - [Recommended](#recommended)
- [Installation](#installation)
  - [Users](#users)
  - [Contributors](#contributors)
- [Usage](#usage)
  - [Examples](#examples)
- [Documentation](#documentation)
- [Resources](#resources)
- [Development](#development)
  - [Future](#future)
  - [History](#history)
  - [Community](#community)
- [Credits](#credits)
- [License](#license)

## Features

- [Bare project structure](https://github.com/nathanurwin/cookiecutter-git-demo)
  - For any programming language or codebase
  - Useful but not overruling organization
- [License customization](https://choosealicense.com/)
- Code of Conduct customization
- [Git Ignore customization](https://www.gitignore.io/)
- Remote repo creation
  - [Bitbucket.org](https://bitbucket.org/) using HTTP Basic auth (2FA disabled only)
  - [GitHub.com](https://github.com/) using HTTP Basic auth (2FA support *coming soon*)
  - [GitLab.com](https://gitlab.com/) using `git push` (HTTP Basic auth or SSH)
- Cross-platform support
  - [Windows](https://www.microsoft.com/en-us/windows)
  - [macOS](https://www.apple.com/macos/high-sierra/)
  - [Linux](https://www.linux.org/)

## Requirements

- [Cookiecutter](https://github.com/audreyr/cookiecutter)
- [Invoke](http://www.pyinvoke.org/)
- [Requests](http://docs.python-requests.org/en/master/)

_**Note:** Cookiecutter **should be** installed with [pip](https://pip.pypa.io/en/stable/installing/), or else `invoke` and `requests` may not be in `$PATH` and/or `$PYTHONPATH`!_

### Recommended

- [ghi](https://github.com/stephencelis/ghi)
- [github-changelog-generator](https://github.com/github-changelog-generator/github-changelog-generator)

## Installation

### Users

```bash
$ pip install --user cookiecutter invoke requests
Collecting cookiecutter
  Using cached https://files.pythonhosted.org/packages/16/99/1ca3a75978270288354f419e9166666801cf7e7d8df984de44a7d5d8b8d0/cookiecutter-1.6.0-py2.py3-none-any.whl
Collecting invoke
  Using cached https://files.pythonhosted.org/packages/6c/66/9e232c59e61f0a0b6552d68419a5c5a5dba368e105fdbfd2b6c74c402234/invoke-1.0.0-py3-none-any.whl
Collecting requests
  Cache entry deserialization failed, entry ignored
  Using cached https://files.pythonhosted.org/packages/65/47/7e02164a2a3db50ed6d8a6ab1d6d60b69c4c3fdf57a284257925dfc12bda/requests-2.19.1-py2.py3-none-any.whl
Collecting binaryornot>=0.2.0 (from cookiecutter)
  Using cached https://files.pythonhosted.org/packages/24/7e/f7b6f453e6481d1e233540262ccbfcf89adcd43606f44a028d7f5fae5eb2/binaryornot-0.4.4-py2.py3-none-any.whl
Collecting poyo>=0.1.0 (from cookiecutter)
  Using cached https://files.pythonhosted.org/packages/ea/6c/62c76c12015f6a1849446fb73da59be1229312c54d6d05068275e52bf29f/poyo-0.4.1-py2.py3-none-any.whl
Collecting future>=0.15.2 (from cookiecutter)
Collecting jinja2-time>=0.1.0 (from cookiecutter)
  Using cached https://files.pythonhosted.org/packages/6a/a1/d44fa38306ffa34a7e1af09632b158e13ec89670ce491f8a15af3ebcb4e4/jinja2_time-0.2.0-py2.py3-none-any.whl
Collecting whichcraft>=0.4.0 (from cookiecutter)
  Using cached https://files.pythonhosted.org/packages/60/8a/5c52e30e11672f7e3aa61f348ddae443d122bcd96bc8b785ac76dbae944b/whichcraft-0.4.1-py2.py3-none-any.whl
Collecting jinja2>=2.7 (from cookiecutter)
  Using cached https://files.pythonhosted.org/packages/7f/ff/ae64bacdfc95f27a016a7bed8e8686763ba4d277a78ca76f32659220a731/Jinja2-2.10-py2.py3-none-any.whl
Collecting click>=5.0 (from cookiecutter)
  Using cached https://files.pythonhosted.org/packages/34/c1/8806f99713ddb993c5366c362b2f908f18269f8d792aff1abfd700775a77/click-6.7-py2.py3-none-any.whl
Collecting certifi>=2017.4.17 (from requests)
  Cache entry deserialization failed, entry ignored
  Using cached https://files.pythonhosted.org/packages/7c/e6/92ad559b7192d846975fc916b65f667c7b8c3a32bea7372340bfe9a15fa5/certifi-2018.4.16-py2.py3-none-any.whl
Collecting chardet<3.1.0,>=3.0.2 (from requests)
  Using cached https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl
Collecting urllib3<1.24,>=1.21.1 (from requests)
  Cache entry deserialization failed, entry ignored
  Using cached https://files.pythonhosted.org/packages/bd/c9/6fdd990019071a4a32a5e7cb78a1d92c53851ef4f56f62a3486e6a7d8ffb/urllib3-1.23-py2.py3-none-any.whl
Collecting idna<2.8,>=2.5 (from requests)
  Cache entry deserialization failed, entry ignored
  Using cached https://files.pythonhosted.org/packages/4b/2a/0276479a4b3caeb8a8c1af2f8e4355746a97fab05a372e4a2c6a6b876165/idna-2.7-py2.py3-none-any.whl
Collecting arrow (from jinja2-time>=0.1.0->cookiecutter)
Collecting MarkupSafe>=0.23 (from jinja2>=2.7->cookiecutter)
Collecting python-dateutil (from arrow->jinja2-time>=0.1.0->cookiecutter)
  Cache entry deserialization failed, entry ignored
  Using cached https://files.pythonhosted.org/packages/cf/f5/af2b09c957ace60dcfac112b669c45c8c97e32f94aa8b56da4c6d1682825/python_dateutil-2.7.3-py2.py3-none-any.whl
Collecting six>=1.5 (from python-dateutil->arrow->jinja2-time>=0.1.0->cookiecutter)
  Using cached https://files.pythonhosted.org/packages/67/4b/141a581104b1f6397bfa78ac9d43d8ad29a7ca43ea90a2d863fe3056e86a/six-1.11.0-py2.py3-none-any.whl
Installing collected packages: chardet, binaryornot, poyo, future, six, python-dateutil, arrow, MarkupSafe, jinja2, jinja2-time, whichcraft, certifi, urllib3, idna, requests, click, cookiecutter, invoke
Successfully installed MarkupSafe-1.0 arrow-0.12.1 binaryornot-0.4.4 certifi-2018.4.16 chardet-3.0.4 click-6.7 cookiecutter-1.6.0 future-0.16.0 idna-2.7 invoke-1.0.0 jinja2-2.10 jinja2-time-0.2.0 poyo-0.4.1 python-dateutil-2.7.3 requests-2.19.1 six-1.11.0 urllib3-1.23 whichcraft-0.4.1
```

See [Usage](#usage)

### Contributors

```bash
$ git clone https://github.com/NathanUrwin/cookiecutter-git
Cloning into 'cookiecutter-git'...
remote: Counting objects: 757, done.
remote: Compressing objects: 100% (80/80), done.
remote: Total 757 (delta 63), reused 73 (delta 32), pack-reused 645
Receiving objects: 100% (757/757), 337.48 KiB | 0 bytes/s, done.
Resolving deltas: 100% (432/432), done.
$ cd cookiecutter-git
$ pipenv install --dev --pre
Creating a virtualenv for this project…
Using /home/user/.pyenv/versions/3.6.6/bin/python3.6m to create virtualenv…
⠋Running virtualenv with interpreter /home/user/.pyenv/versions/3.6.6/bin/python3.6m
Using base prefix '/home/user/.pyenv/versions/3.6.6'
New python executable in /home/user/.local/share/virtualenvs/cookiecutter-git-Jx1W2Sde/bin/python3.6m
Also creating executable in /home/user/.local/share/virtualenvs/cookiecutter-git-Jx1W2Sde/bin/python
Installing setuptools, pip, wheel...done.

Virtualenv location: /home/user/.local/share/virtualenvs/cookiecutter-git-Jx1W2Sde
Installing dependencies from Pipfile.lock (25c20f)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 58/58 — 00:00:07
To activate this project's virtualenv, run the following:
 $ pipenv shell
$ pipenv run invoke tests
# before running tests you may have to run:
$ pipenv run pip install -r requirements.txt
```

See [CONTRIBUTING](#contributing)

## Usage

```bash
$ mkdir -p ~/Projects/NathanUrwin
$ cd ~/Projects/NathanUrwin
$ cookiecutter gh:NathanUrwin/cookiecutter-git
You've downloaded /home/user/.cookiecutters/cookiecutter-git before. Is it okay to delete and re-download it? [yes]:
git_name [Nathan Urwin]:
git_email [me@nathanurwin.com]:
git_ignore [windows,macos,linux,git]:
repo_slug [cookiecutter-git-demo]:
repo_tagline [A cookiecutter-git demonstration :tada:]:
repo_summary [This project ...]:
Select remote_provider:
1 - github.com
2 - gitlab.com
3 - bitbucket.org
4 - none
Choose from 1, 2, 3, 4 [1]:
remote_username [NathanUrwin]:
remote_namespace [NathanUrwin]:
Select remote_protocol:
1 - https
2 - ssh
Choose from 1, 2 [1]:
Select code_of_conduct:
1 - contributor_covenant
2 - citizen_code_of_conduct
Choose from 1, 2 [1]:
Select copyright_license:
1 - MIT
2 - Apache-2.0
3 - BSD-2-Clause
4 - BSD-3-Clause
5 - GPL-2.0
6 - GPL-3.0
7 - AGPL-3.0
8 - LGPL-2.1
9 - LGPL-3.0
10 - EPL-1.0
11 - MPL-2.0
12 - Unlicense
Choose from 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 [1]:
copyright_holder [Nathan Urwin]:
make_dirs [docs,src,tests]:
Password for 'https://NathanUrwin@github.com':
Initialized empty Git repository in /home/user/Projects/NathanUrwin/cookiecutter-git-demo/.git/
[master (root-commit) 5bdaa5c] Initial commit
 15 files changed, 350 insertions(+)
 create mode 100644 .editorconfig
 create mode 100644 .github/ISSUE_TEMPLATE/bug_report.md
 create mode 100644 .github/ISSUE_TEMPLATE/feature_request.md
 create mode 100644 .github/PULL_REQUEST_TEMPLATE.md
 create mode 100644 .gitignore
 create mode 100644 AUTHORS.md
 create mode 100644 CHANGELOG.md
 create mode 100644 CODE_OF_CONDUCT.md
 create mode 100644 CONTRIBUTING.md
 create mode 100644 LICENSE
 create mode 100644 README.md
 create mode 100644 ROADMAP.md
 create mode 100644 docs/.gitkeep
 create mode 100644 src/.gitkeep
 create mode 100644 tests/.gitkeep
To https://github.com/NathanUrwin/cookiecutter-git-demo.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.


Success! Your project was created here:
/home/user/Projects/NathanUrwin/cookiecutter-git-demo
Also see: https://github.com/NathanUrwin/cookiecutter-git-demo
Thanks for using cookiecutter-git! :)


```

See generated [README.md](https://github.com/NathanUrwin/cookiecutter-git-demo/blob/master/README.md)

### Examples

See [cookiecutter-git-demo](https://github.com/NathanUrwin/cookiecutter-git-demo)

```bash
$ tree -a -I .git cookiecutter-git-demo
cookiecutter-git-demo
├── AUTHORS.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── docs
│   └── .gitkeep
├── .editorconfig
├── .github
│   ├── ISSUE_TEMPLATE
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── .gitignore
├── LICENSE
├── README.md
├── ROADMAP.md
├── src
│   └── .gitkeep
└── tests
    └── .gitkeep

5 directories, 15 files
```

## Documentation

Cookiecutter prompts explained in-depth. See [cookiecutter.json](cookiecutter.json) for default values.

Prompt | Explanation
--- | ---
`git_name` | Your full name, including first and last names, titles, and possibly even your middle name. This will go under *Core Contributor* in **AUTHORS.md**. See `git config --global user.name`
`git_email` | Your git user email address you want associated with the repository. This will go under *Core Contributor* in **AUTHORS.md**. See `git config --global user.email`
`git_ignore` | A comma-separated values (csv) list of preset templates of paths for git to ignore. See the [gitignore.io README](https://github.com/joeblau/gitignore.io#list) for available values. This will be used to generate the **.gitignore** file.
`repo_slug` | The repository name containing only alphanumeric characters and dashes. This will be the local, top-level directory name, the remote repo endpoint, and the *H1* in the **README.md**.
`repo_tagline` | A short description about the repository in *50 words or less*. This will be the remote description setting, and the content under the *H1* in the **README.md**.
`repo_summary` | A long description about the repository in *50 words or more*. This will go after the `repo_tagline` with the content under the *H1* in the **README.md**.
`remote_provider` | A choice between `bitbucket.org`, `github.com`, `gitlab.com`, or `None`. This option creates a remote repository for you, and is this project's main feature so defaults to `github.com`.
`remote_username` | Your git `remote_provider` account username. This will be used for all git remote-based actions. This is accompanied with a `remote_password` prompt that is never saved.
`remote_namespace` | Where the remote repository will live, which can be a user or organization, group, or team (depending on the `remote_provider`). Only used if `remote_provider` is not `None`.
`remote_protocol` | A choice between the `https` and `ssh` protocols. Defaults to `https`, since those using `ssh` qualify as power users and should be able to handle setting up a [cookiecutter user config](https://cookiecutter.readthedocs.io/en/latest/advanced/user_config.html).
`code_of_conduct` | Adopt a code of conduct to define community standards, signal a welcoming and inclusive project, and outline procedures for handling abuse. A choice between the [Contributor Covenant](https://www.contributor-covenant.org/) or [Citizen Code of Conduct](http://citizencodeofconduct.org/).
`copyright_license` | The copyright license for the repository. This will be used to generate the **LICENSE** and **NOTICE** files, and determines how end users can ultimately use your source code.
`copyright_holder` | The individual or company that holds the intellectual property copyright. This will be used in the **LICENSE** file, rather than the `git_name`.
`make_dirs` | A comma-separated values (csv) list of directory names which are made with **.gitkeep** files. Nested dirs work if the system path separator is correct! (**tests/unit** or **tests\\\\unit**)

## Resources

- [Creating a Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/first_steps.html)
- [Using Pre/Post-Generate Hooks](https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html)
- [GitHub Developer Licenses](https://developer.github.com/v3/licenses/)
- [mkdir -p functionality in python](https://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python)
- [Create empty file using python](https://stackoverflow.com/questions/12654772/create-empty-file-using-python)
- [Git Ignore Dot IO Docs](https://www.gitignore.io/docs)
- [Bitbucket API Basic auth](https://developer.atlassian.com/bitbucket/api/2/reference/meta/authentication#basic-auth)
- [Bitbucket API repos](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Busername%7D/%7Brepo_slug%7D#post)
- [GitHub API Basic auth](https://developer.github.com/v3/#basic-authentication)
- [GitHub API Create repos](https://developer.github.com/v3/repos/#create)
- [GitLab Push to create a new project](https://docs.gitlab.com/ce/gitlab-basics/create-project.html#push-to-create-a-new-project)

## Development

See [CONTRIBUTING](CONTRIBUTING.md)

### Future

See [ROADMAP](ROADMAP.md)

### History

See [CHANGELOG](CHANGELOG.md)

### Community

See [CODE OF CONDUCT](CODE_OF_CONDUCT.md)

## Credits

See [AUTHORS](AUTHORS.md)

## License

See [LICENSE](LICENSE)
