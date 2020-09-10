# cookiecutter-git

[![Tagged Release](https://img.shields.io/badge/release-v0.6.1-blue.svg?longCache=true)](https://github.com/NathanUrwin/cookiecutter-git/releases/tag/v0.6.1)
[![Development Status](https://img.shields.io/badge/status-beta-brightgreen.svg?longCache=true)](ROADMAP.md)
[![Build Status](https://travis-ci.org/NathanUrwin/cookiecutter-git.svg?branch=master)](https://travis-ci.org/NathanUrwin/cookiecutter-git)
[![Build Status](https://ci.appveyor.com/api/projects/status/3q0aik8sgmndwibp/branch/master?svg=true)](https://ci.appveyor.com/project/NathanUrwin/cookiecutter-git/branch/master)
[![codecov](https://codecov.io/gh/NathanUrwin/cookiecutter-git/branch/master/graph/badge.svg)](https://codecov.io/gh/NathanUrwin/cookiecutter-git)
[![python](https://img.shields.io/badge/python-2.7%2C%203.4%2C%203.5%2C%203.6%2C%203.7-blue.svg?longCache=true)](https://www.python.org/downloads/)

> Git repo project template using Cookiecutter :cookie:

[![Cookiecutter-Git Logo](images/logo-256.png)](https://dylantyates.com/graphics)

This project is inspired by [cookiecutter-template by eviweb](https://github.com/eviweb/cookiecutter-template), and consists of a [cookiecutter](https://github.com/audreyr/cookiecutter#cookiecutter) (project template) that provides the necessary [markdown](https://guides.github.com/features/mastering-markdown/) docs and other files to pass [GitHub's open source guidelines](https://opensource.guide/) with an added bonus: remote repos are created for you [*automagically*](https://youtu.be/Z3qK8gT5LLg?t=24s)! :crystal_ball::zap::boom:

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
  - [Example](#example)
- [Documentation](#documentation)
- [Resources](#resources)
- [Development](#development)
  - [Future](#future)
  - [History](#history)
  - [Community](#community)
- [Credits](#credits)
- [License](#license)

## Features

- Creates new project directory
- [Bare project structure](https://github.com/nathanurwin/cookiecutter-git-demo)
  - For any programming language or codebase
  - Useful but not overruling organization
- [License customization](https://choosealicense.com/)
- Code of Conduct customization
- [Git Ignore customization](https://www.gitignore.io/)
- Git repo initialization
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
- [pyenv](https://github.com/pyenv/pyenv) ([conda](https://github.com/conda/conda) on Windows)

## Installation

### Users

```bash
$ pip install --user cookiecutter invoke requests
```

See [Usage](#usage)

### Contributors

```bash
$ git clone https://github.com/NathanUrwin/cookiecutter-git
$ cd cookiecutter-git
$ pipenv install --dev --pre
# before running tests you may have to run:
$ pipenv run pip install -r requirements.txt
$ pipenv run invoke tests
```

See [CONTRIBUTING](#contributing)

## Usage

```bash
$ mkdir -p ~/Projects/NathanUrwin
$ cd ~/Projects/NathanUrwin
$ cookiecutter gh:NathanUrwin/cookiecutter-git
```

See generated [README.md](https://github.com/NathanUrwin/cookiecutter-git-demo/blob/master/README.md)

### Example

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
`remote_provider` | A choice between `bitbucket.org`, `github.com`, `gitlab.com`, or `none`. This option creates a remote repository for you, and is this project's main feature so defaults to `github.com`.
`remote_username` | Your git `remote_provider` account username. This will be used for all git remote-based actions. This is accompanied with a `remote_password` prompt that is never saved.
`remote_namespace` | Where the remote repository will live, which can be a user or organization, group, or team (depending on the `remote_provider`). Only used if `remote_provider` is not `none`.
`remote_protocol` | A choice between the `https` and `ssh` protocols. Defaults to `https`, since those using `ssh` qualify as power users and should be able to handle setting up a [cookiecutter user config](https://cookiecutter.readthedocs.io/en/latest/advanced/user_config.html).
`code_of_conduct` | Adopt a code of conduct to define community standards, signal a welcoming and inclusive project, and outline procedures for handling abuse. A choice between the [Contributor Covenant](https://www.contributor-covenant.org/) or [Citizen Code of Conduct](http://citizencodeofconduct.org/).
`copyright_license` | The copyright license for the repository. This will be used to generate the **LICENSE** and **NOTICE** files, and determines how end users can ultimately use your source code.
`copyright_holder` | The individual or company that holds the intellectual property copyright. This will be used in the **LICENSE** file, rather than the `git_name`.
`make_dirs` | A comma-separated values (csv) list of directory names which are made with **.gitkeep** files. Nested dirs work if the system path separator is correct! (For example: **tests/unit** for Mac/Linux or **tests\\\\unit** for Windows)

## Resources

- [GitHub's recommended community standards](https://blog.github.com/2017-06-14-new-community-tools/)
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
