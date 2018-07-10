# cookiecutter-git

[![GitHub release](https://img.shields.io/badge/release-v0.4.1-blue.svg)](https://github.com/NathanUrwin/cookiecutter-git/releases/tag/v0.4.1)
[![Development status](https://img.shields.io/badge/status-alpha-yellow.svg)](ROADMAP.md)
[![Build Status](https://img.shields.io/badge/build-unknown-lightgrey.svg)](https://travis-ci.com/NathanUrwin/cookiecutter-git)
[![codecov](https://img.shields.io/badge/codecov-0%25-lightgrey.svg)](https://codecov.io/gh/NathanUrwin/cookiecutter-git)

> Git repo project template :clipboard:

[![Cookiecutter-Git Logo](images/logo-256.png)](https://dylantyates.com/graphics)

This project is inspired by [cookiecutter-template by eviweb](https://github.com/eviweb/cookiecutter-template), and consists of a [cookiecutter](https://github.com/audreyr/cookiecutter#cookiecutter) (project template) that provides the necessary [markdown](https://guides.github.com/features/mastering-markdown/) docs and other files to pass [GitHub's recommended community standards](https://blog.github.com/2017-06-14-new-community-tools/) with an added bonus: remote repos are created for you [*automagically*](https://youtu.be/Z3qK8gT5LLg?t=9s)! :crystal_ball::zap::boom:

_**Note:** The [cookie-cookie](https://github.com/NathanUrwin/cookie-cookie) feature of creating a cookiecutter is **coming soon**!_

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Features](#features)
  - [Upcoming](#upcoming)
- [Requirements](#requirements)
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
  - [Useful but not overruling organization](#examples)
- [License customization](https://choosealicense.com/)
- [Git Ignore customization](https://www.gitignore.io/)
- [Remote repo creation](#resources)
  - [Bitbucket.org](https://bitbucket.org/) using HTTP Basic auth (2FA disabled only)
  - [GitHub.com](https://github.com/) using HTTP Basic auth (2FA support *coming soon*)
  - [GitLab.com](https://gitlab.com/) using `git push` (HTTP Basic auth or SSH)
- Cross-platform support
  - [Windows](https://www.microsoft.com/en-us/windows)
  - [macOS](https://www.apple.com/macos/high-sierra/)
  - [Linux](https://www.linux.org/)

### Upcoming

1. [Fix urllib2.URLError: <urlopen error](https://github.com/NathanUrwin/cookiecutter-git/issues/21)
2. [Fix GitLab.com as remote_provider](https://github.com/NathanUrwin/cookiecutter-git/issues/22)
3. [Remove duplicate password prompts](https://github.com/NathanUrwin/cookiecutter-git/issues/18)
4. [Full coverage testing](https://github.com/NathanUrwin/cookiecutter-git/issues/8)
5. [Continuous integration](https://github.com/NathanUrwin/cookiecutter-git/issues/9)
6. [Additional remote repo customization](https://github.com/NathanUrwin/cookiecutter-git/issues/12)
7. [Fix overwrite if exists option](https://github.com/NathanUrwin/cookiecutter-git/issues/19)
8. [Add example .cookiecutterrc](https://github.com/NathanUrwin/cookiecutter-git/issues/23)

## Requirements

- [Cookiecutter](https://github.com/audreyr/cookiecutter)
- [Git](https://git-scm.com/downloads)
- [Invoke](http://www.pyinvoke.org/)
- [Requests](http://docs.python-requests.org/en/master/)

### Recommended

- [ghi](https://github.com/stephencelis/ghi)
- [github-changelog-generator](https://github.com/github-changelog-generator/github-changelog-generator)

## Installation

### Command-line Users

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
remote: Counting objects: 535, done.
remote: Compressing objects: 100% (104/104), done.
remote: Total 535 (delta 74), reused 98 (delta 33), pack-reused 386
Receiving objects: 100% (535/535), 250.71 KiB | 0 bytes/s, done.
Resolving deltas: 100% (299/299), done.

$ cd cookiecutter-git
$ pipenv install
Installing dependencies from Pipfile.lock (e30ea1)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 17/17 — 00:00:01
To activate this project's virtualenv, run the following:
 $ pipenv shell
```

See [CONTRIBUTING](#contributing)

## Usage

```bash
$ mkdir -p ~/Projects/NathanUrwin
$ cd ~/Projects/NathanUrwin
$ cookiecutter gh:NathanUrwin/cookiecutter-git  # https://github.com/NathanUrwin/cookiecutter-git
You've cloned /home/user/.cookiecutters/cookiecutter-git before. Is it okay to delete and re-clone it? [yes]:
author_name [Nathan Urwin]:
author_email [nathan.e.urwin@gmail.com]: me@nathanurwin.com
git_username [nathanurwin]:
remote_namespace [nathanurwin]:
repo_slug [cookiecutter-git-demo]:
repo_description [A cookiecutter-git demonstration]: A cookiecutter-git demonstration :tada:
Select remote_repo:
1 - yes
2 - no
Choose from 1, 2 [1]:
Select remote_provider:
1 - github.com
2 - gitlab.com
3 - bitbucket.org
Choose from 1, 2, 3 [1]:
Select remote_protocol:
1 - https
2 - ssh
Choose from 1, 2 [1]:
make_dirs [docs,src,tests]:
gitignore [windows,macos,linux,git]:
Select license:
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
Removing '/home/user/Projects/NathanUrwin/cookiecutter-git-demo/NOTICE'...
git init
Initialized empty Git repository in /home/user/Projects/NathanUrwin/cookiecutter-git-demo/.git/

git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.editorconfig
	.github/
	.gitignore
	AUTHORS.md
	CHANGELOG.md
	CODE_OF_CONDUCT.md
	CONTRIBUTING.md
	LICENSE
	README.md
	ROADMAP.md
	docs/
	src/
	tests/

nothing added to commit but untracked files present (use "git add" to track)

git add -A
git status
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   .editorconfig
	new file:   .github/ISSUE_TEMPLATE/bug_report.md
	new file:   .github/ISSUE_TEMPLATE/feature_request.md
	new file:   .github/PULL_REQUEST_TEMPLATE.md
	new file:   .gitignore
	new file:   AUTHORS.md
	new file:   CHANGELOG.md
	new file:   CODE_OF_CONDUCT.md
	new file:   CONTRIBUTING.md
	new file:   LICENSE
	new file:   README.md
	new file:   ROADMAP.md
	new file:   docs/.gitkeep
	new file:   src/.gitkeep
	new file:   tests/.gitkeep



You need a passphrase to unlock the secret key for
user: "Nathan Urwin (Git key) <me@nathanurwin.com>"
4096-bit RSA key, ID 45F9BF10, created 2018-03-15

git commit -m Initial commit
[master (root-commit) 6e3e9cb] Initial commit
 15 files changed, 321 insertions(+)
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

Password for 'https://nathanurwin@github.com':
https://api.github.com/user/repos
{"id":137415126,"node_id":"MDEwOlJlcG9zaXRvcnkxMzc0MTUxMjY=","name":"cookiecutter-git-demo","full_name":"NathanUrwin/cookiecutter-git-demo","owner":{"login":"NathanUrwin","id":13526277,"node_id":"MDQ6VXNlcjEzNTI2Mjc3","avatar_url":"https://avatars2.githubusercontent.com/u/13526277?v=4","gravatar_id":"","url":"https://api.github.com/users/NathanUrwin","html_url":"https://github.com/NathanUrwin","followers_url":"https://api.github.com/users/NathanUrwin/followers","following_url":"https://api.github.com/users/NathanUrwin/following{/other_user}","gists_url":"https://api.github.com/users/NathanUrwin/gists{/gist_id}","starred_url":"https://api.github.com/users/NathanUrwin/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/NathanUrwin/subscriptions","organizations_url":"https://api.github.com/users/NathanUrwin/orgs","repos_url":"https://api.github.com/users/NathanUrwin/repos","events_url":"https://api.github.com/users/NathanUrwin/events{/privacy}","received_events_url":"https://api.github.com/users/NathanUrwin/received_events","type":"User","site_admin":false},"private":false,"html_url":"https://github.com/NathanUrwin/cookiecutter-git-demo","description":"A cookiecutter-git demonstration :tada:","fork":false,"url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo","forks_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/forks","keys_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/keys{/key_id}","collaborators_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/collaborators{/collaborator}","teams_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/teams","hooks_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/hooks","issue_events_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/issues/events{/number}","events_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/events","assignees_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/assignees{/user}","branches_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/branches{/branch}","tags_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/tags","blobs_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/git/blobs{/sha}","git_tags_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/git/tags{/sha}","git_refs_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/git/refs{/sha}","trees_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/git/trees{/sha}","statuses_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/statuses/{sha}","languages_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/languages","stargazers_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/stargazers","contributors_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/contributors","subscribers_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/subscribers","subscription_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/subscription","commits_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/commits{/sha}","git_commits_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/git/commits{/sha}","comments_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/comments{/number}","issue_comment_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/issues/comments{/number}","contents_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/contents/{+path}","compare_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/compare/{base}...{head}","merges_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/merges","archive_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/{archive_format}{/ref}","downloads_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/downloads","issues_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/issues{/number}","pulls_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/pulls{/number}","milestones_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/milestones{/number}","notifications_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/notifications{?since,all,participating}","labels_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/labels{/name}","releases_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/releases{/id}","deployments_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/deployments","created_at":"2018-06-14T22:23:37Z","updated_at":"2018-06-14T22:23:37Z","pushed_at":"2018-06-14T22:23:38Z","git_url":"git://github.com/NathanUrwin/cookiecutter-git-demo.git","ssh_url":"git@github.com:NathanUrwin/cookiecutter-git-demo.git","clone_url":"https://github.com/NathanUrwin/cookiecutter-git-demo.git","svn_url":"https://github.com/NathanUrwin/cookiecutter-git-demo","homepage":null,"size":0,"stargazers_count":0,"watchers_count":0,"language":null,"has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":0,"mirror_url":null,"archived":false,"open_issues_count":0,"license":null,"forks":0,"open_issues":0,"watchers":0,"default_branch":"master","permissions":{"admin":true,"push":true,"pull":true},"allow_squash_merge":true,"allow_merge_commit":true,"allow_rebase_merge":true,"network_count":0,"subscribers_count":1}
git remote add origin https://nathanurwin@github.com/nathanurwin/cookiecutter-git-demo.git
Password for 'https://nathanurwin@github.com':
Counting objects: 18, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (15/15), done.
Writing objects: 100% (18/18), 6.02 KiB | 0 bytes/s, done.
Total 18 (delta 0), reused 0 (delta 0)
To https://github.com/nathanurwin/cookiecutter-git-demo.git
 * [new branch]      master -> master
git push -u origin master
Branch master set up to track remote branch master from origin.


cookiecutter-git-demo setup successfully!


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
`git_name` | Your full name, including first and last names, titles, and possibly even your middle name. This will go under *Core Contributor* in **AUTHORS.md**. (`git config --global user.name`)
`git_email` | Your git user email address you want associated with the repository. This will go under *Core Contributor* in **AUTHORS.md**. (`git config --global user.email`)
`git_ignore` | A comma-separated values (csv) list of preset templates of paths for git to ignore. See the [gitignore.io README](https://github.com/joeblau/gitignore.io#list) for available values. This will be used to generate the **.gitignore** file.
`repo_slug` | The repository name containing only alphanumeric characters and dashes. This will be the local, top-level directory name, the remote repo endpoint, and the *H1* in the **README.md**.
`repo_tagline` | A short description about the repository in *50 words or less*. This will be the remote description setting, and the content under the *H1* in the **README.md**.
`repo_summary` | A long description about the repository in *50 words or more*. This will go after the `repo_tagline` with the content under the *H1* in the **README.md**.
`remote_provider` | A choice between `Bitbucket.org`, `GitHub.com`, `GitLab.com`, or `None`. This option creates a remote repository for you, and is this project's main feature so defaults to `GitHub.com`.
`remote_username` | Your git `remote_provider` account username. This will be used for all git remote-based actions. This is accompanied with a `remote_password` prompt that is never saved.
`remote_namespace` | Where the remote repository will live, which can be a user or organization, group, or team (depending on the `remote_provider`). Only used if `remote_provider` is not `None`.
`remote_protocol` | A choice between the `https` and `ssh` protocols. Defaults to `https`, since those using `ssh` qualify as power users and should be able to handle setting up a [cookiecutter user config](https://cookiecutter.readthedocs.io/en/latest/advanced/user_config.html).
`copyright_license` | The copyright license for the repository. This will be used to generate the **LICENSE** and **NOTICE** files, and determines how end users can ultimately use your source code.
`copyright_holder` | The individual or company that holds the intellectual property copyright. This will be used in the **LICENSE** file, rather than the `git_name`.
`make_dirs` | A comma-separated values (csv) list of directory names which are made with **.gitkeep** files. Nested dirs work if the system path separator is correct! (**tests/unit** or **tests\\\\unit**)
`copy_cookiecutter_git` | A `true` or `false` choice on whether or not *cookiecutter-git*'s features (being a cookiecutter) are copied into your new project. This adds the missing features from [cookie-cookie](https://github.com/NathanUrwin/cookie-cookie).

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
