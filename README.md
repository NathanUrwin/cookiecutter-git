# cookiecutter-git

[![GitHub release](https://img.shields.io/badge/release-v0.4.1-blue.svg)](https://github.com/NathanUrwin/cookiecutter-git/releases/tag/v0.4.1)
[![Development status](https://img.shields.io/badge/status-alpha-yellow.svg)](ROADMAP.md)
[![Build Status](https://img.shields.io/badge/build-unknown-lightgrey.svg)](https://travis-ci.com/NathanUrwin/cookiecutter-git)
[![codecov](https://img.shields.io/badge/codecov-0%25-lightgrey.svg)](https://codecov.io/gh/NathanUrwin/cookiecutter-git)

> Git cookiecutter template :clipboard:

[![Cookiecutter-Git Logo](images/logo-256.png)](https://dylantyates.com/graphics)

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
- [Gitignore customization](https://www.gitignore.io/)
- [Remote repository creation](#resources)
  - [Bitbucket.org](https://bitbucket.org/) using Basic auth
  - [GitHub.com](https://github.com/) using Basic auth
  - [GitLab.com](https://gitlab.com/) using Personal access tokens
- Cross-platform support
  - [Windows](https://www.microsoft.com/en-us/windows)
  - [macOS](https://www.apple.com/macos/high-sierra/)
  - [Linux](https://www.linux.org/)

### Upcoming

- [Add gitlab_token validation](https://github.com/NathanUrwin/cookiecutter-git/issues/7)
- [Full coverage testing](https://github.com/NathanUrwin/cookiecutter-git/issues/8)
- [Continuous integration](https://github.com/NathanUrwin/cookiecutter-git/issues/9)
- [Add more secure auth methods](https://github.com/NathanUrwin/cookiecutter-git/issues/11)
- [Additional remote repo customization](https://github.com/NathanUrwin/cookiecutter-git/issues/12)

## Requirements

- [Cookiecutter](https://github.com/audreyr/cookiecutter)
- [Git](https://git-scm.com/downloads)

## Usage

    $ cookiecutter gh:NathanUrwin/cookiecutter-git  # https://github.com/NathanUrwin/cookiecutter-git
    You've cloned /home/user/.cookiecutters/cookiecutter-git before. Is it okay to delete and re-clone it? [yes]:
    author_name [Nathan Urwin]:
    author_email [nathan.e.urwin@gmail.com]: me@nathanurwin.com
    git_username [nathanurwin]:
    repo_namespace [nathanurwin]:
    repo_slug [cookiecutter-git-demo]:
    repo_description [A cookiecutter-git demonstration]:
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
    Removing '/home/user/Git/NathanUrwin/sandbox/.sandbox/cookiecutter-git-demo/NOTICE'...
    git init
    Initialized empty Git repository in /home/user/Git/NathanUrwin/sandbox/.sandbox/cookiecutter-git-demo/.git/

    git status
    On branch master

    Initial commit

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

      .editorconfig
      .gitignore
      AUTHORS.md
      CHANGELOG.md
      CONTRIBUTING.md
      LICENSE
      README.md
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
      new file:   .gitignore
      new file:   AUTHORS.md
      new file:   CHANGELOG.md
      new file:   CONTRIBUTING.md
      new file:   LICENSE
      new file:   README.md
      new file:   docs/.gitkeep
      new file:   src/.gitkeep
      new file:   tests/.gitkeep



    You need a passphrase to unlock the secret key for
    user: "Nathan Urwin <nathan.e.urwin@gmail.com>"
    4096-bit RSA key, ID 45F9BF10, created 2018-03-15

    git commit -m Initial commit
    [master (root-commit) 2e8431e] Initial commit
    10 files changed, 148 insertions(+)
    create mode 100644 .editorconfig
    create mode 100644 .gitignore
    create mode 100644 AUTHORS.md
    create mode 100644 CHANGELOG.md
    create mode 100644 CONTRIBUTING.md
    create mode 100644 LICENSE
    create mode 100644 README.md
    create mode 100644 docs/.gitkeep
    create mode 100644 src/.gitkeep
    create mode 100644 tests/.gitkeep

    Password for 'https://nathanurwin@github.com':
    https://api.github.com/user/repos
    {"id":136241061,"node_id":"MDEwOlJlcG9zaXRvcnkxMzYyNDEwNjE=","name":"cookiecutter-git-demo","full_name":"NathanUrwin/cookiecutter-git-demo","owner":{"login":"NathanUrwin","id":13526277,"node_id":"MDQ6VXNlcjEzNTI2Mjc3","avatar_url":"https://avatars2.githubusercontent.com/u/13526277?v=4","gravatar_id":"","url":"https://api.github.com/users/NathanUrwin","html_url":"https://github.com/NathanUrwin","followers_url":"https://api.github.com/users/NathanUrwin/followers","following_url":"https://api.github.com/users/NathanUrwin/following{/other_user}","gists_url":"https://api.github.com/users/NathanUrwin/gists{/gist_id}","starred_url":"https://api.github.com/users/NathanUrwin/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/NathanUrwin/subscriptions","organizations_url":"https://api.github.com/users/NathanUrwin/orgs","repos_url":"https://api.github.com/users/NathanUrwin/repos","events_url":"https://api.github.com/users/NathanUrwin/events{/privacy}","received_events_url":"https://api.github.com/users/NathanUrwin/received_events","type":"User","site_admin":false},"private":false,"html_url":"https://github.com/NathanUrwin/cookiecutter-git-demo","description":"A cookiecutter-git demonstration","fork":false,"url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo","forks_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/forks","keys_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/keys{/key_id}","collaborators_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/collaborators{/collaborator}","teams_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/teams","hooks_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/hooks","issue_events_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/issues/events{/number}","events_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/events","assignees_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/assignees{/user}","branches_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/branches{/branch}","tags_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/tags","blobs_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/git/blobs{/sha}","git_tags_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/git/tags{/sha}","git_refs_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/git/refs{/sha}","trees_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/git/trees{/sha}","statuses_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/statuses/{sha}","languages_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/languages","stargazers_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/stargazers","contributors_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/contributors","subscribers_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/subscribers","subscription_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/subscription","commits_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/commits{/sha}","git_commits_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/git/commits{/sha}","comments_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/comments{/number}","issue_comment_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/issues/comments{/number}","contents_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/contents/{+path}","compare_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/compare/{base}...{head}","merges_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/merges","archive_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/{archive_format}{/ref}","downloads_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/downloads","issues_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/issues{/number}","pulls_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/pulls{/number}","milestones_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/milestones{/number}","notifications_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/notifications{?since,all,participating}","labels_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/labels{/name}","releases_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/releases{/id}","deployments_url":"https://api.github.com/repos/NathanUrwin/cookiecutter-git-demo/deployments","created_at":"2018-06-05T22:20:32Z","updated_at":"2018-06-05T22:20:32Z","pushed_at":"2018-06-05T22:20:33Z","git_url":"git://github.com/NathanUrwin/cookiecutter-git-demo.git","ssh_url":"git@github.com:NathanUrwin/cookiecutter-git-demo.git","clone_url":"https://github.com/NathanUrwin/cookiecutter-git-demo.git","svn_url":"https://github.com/NathanUrwin/cookiecutter-git-demo","homepage":null,"size":0,"stargazers_count":0,"watchers_count":0,"language":null,"has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":0,"mirror_url":null,"archived":false,"open_issues_count":0,"license":null,"forks":0,"open_issues":0,"watchers":0,"default_branch":"master","permissions":{"admin":true,"push":true,"pull":true},"allow_squash_merge":true,"allow_merge_commit":true,"allow_rebase_merge":true,"network_count":0,"subscribers_count":1}
    git remote add origin https://nathanurwin@github.com/nathanurwin/cookiecutter-git-demo.git
    Password for 'https://nathanurwin@github.com':
    Counting objects: 11, done.
    Delta compression using up to 8 threads.
    Compressing objects: 100% (8/8), done.
    Writing objects: 100% (11/11), 3.22 KiB | 0 bytes/s, done.
    Total 11 (delta 0), reused 0 (delta 0)
    To https://github.com/nathanurwin/cookiecutter-git-demo.git
    * [new branch]      master -> master
    git push -u origin master
    Branch master set up to track remote branch master from origin.


    cookiecutter-git-demo setup successfully!

See generated [README.md]({{cookiecutter.repo_slug}}/README.md)

### Examples

See [cookiecutter-git-demo](https://github.com/NathanUrwin/cookiecutter-git-demo)

```bash
$ tree -a -I .git cookiecutter-git-demo
cookiecutter-git-demo
├── AUTHORS.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── docs
│   └── .gitkeep
├── .editorconfig
├── .gitignore
├── LICENSE
├── README.md
├── src
│   └── .gitkeep
└── tests
    └── .gitkeep

3 directories, 10 files
```

## Documentation

**cookiecutter.json** explained in-depth. See [cookiecutter.json](cookiecutter.json) for default values.

Prompt | Explanation
--- | ---
`author_name` | Your full name, including first and last names, titles, and possibly even your middle name. This will go under *Project Lead* in **AUTHORS.md**.
`author_email` | The email address you want associated with the repository. This will go under *Project Lead* in **AUTHORS.md**.
`git_username` | Your local git and `remote_provider` (see below) account username. This will be used for all git-based actions.
`repo_namespace` | The namespace where the repository will live, which can be a user or organization, group, or team (depending on the `remote_provider`). This will only be used if `remote_repo` (see below) is `yes`.
`repo_slug` | The repository name which should only contain alphanumeric characters and dashes. This will be the local, top-level directory name, the remote repo endpoint, and the *H1* in the **README.md**.
`repo_description` | A short description about the repository. This will be the remote description setting, and the content under the *H1* in the **README.md**.
`remote_repo` | A `yes` or `no` choice on whether or not a remote repository is automatically created for you. This option is the main reason for *cookiecutter-git*, so the default choice is `yes`.
`remote_provider` | A choice between `bitbucket.org`, `github.com`, and `gitlab.com`. This will only be used if `remote_repo` is `yes`, and defaults to `github.com`.
`remote_protocol` | A choice between the `https` and `ssh` protocols. `https` is the default, since those using `ssh` qualify as power users and should be able to handle setting up a [cookiecutter user config](https://cookiecutter.readthedocs.io/en/latest/advanced/user_config.html).
`make_dirs` | A comma-separated values list of directory names. Directories will be made with a **.gitkeep** file, so they will be added to the initial commit. Nested dirs work if the system path separator is correct!
`gitignore` | A comma-separated values list of preset templates of files for git to ignore. See the [gitignore.io README](https://github.com/joeblau/gitignore.io#list) for a complete list of available values. This will be used to generate the **.gitignore** file.
`license` | The software license for the repository. This will be used to generate the **LICENSE** and **NOTICE** files, and determines how end users can ultimately use your source code.
`copyright_holder` | The individual or company that holds the intellectual property copyright. This will be used in the **LICENSE** file, rather than the `author_name`.

## Resources

- [Creating a Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/first_steps.html)
- [Using Pre/Post-Generate Hooks](https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html)
- [Python Subprocess management](https://docs.python.org/3/library/subprocess.html)
- [Python URL handling modules](https://docs.python.org/3/library/urllib.html)
- [Python Future urllib](http://python-future.org/compatible_idioms.html#urllib-module)
- [GitHub Developer Licenses](https://developer.github.com/v3/licenses/)
- [mkdir -p functionality in python](https://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python)
- [Create empty file using python](https://stackoverflow.com/questions/12654772/create-empty-file-using-python)
- [Git Ignore DotIO Docs](https://www.gitignore.io/docs)
- [Bitbucket API Basic auth](https://developer.atlassian.com/bitbucket/api/2/reference/meta/authentication#basic-auth)
- [Bitbucket API repositories](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Busername%7D/%7Brepo_slug%7D#post)
- [GitHub API Basic authentication](https://developer.github.com/v3/#basic-authentication)
- [GitHub API Create repositories](https://developer.github.com/v3/repos/#create)
- [GitLab API Personal access tokens](https://docs.gitlab.com/ce/api/#personal-access-tokens)
- [GitLab API Namespaces](https://docs.gitlab.com/ce/api/namespaces.html)
- [GitLab API Create project](https://docs.gitlab.com/ce/api/projects.html#create-project)

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
