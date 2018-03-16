# cookiecutter-git
A git repository project template!

### Table of Contents
- [Features](#features)
  - [Upcoming](#upcoming)
- [Requirements](#requirements)
- [Usage](#usage)
  - [Example](#example)
- [Documentation](#documentation)
- [Development](#development)
  - [Future](#future)
  - [History](#history)
- [Credits](#credits)
- [License](#license)

## Features
- [Bare project structure](https://github.com/nathanurwin/cookiecutter-git-demo)
  - For any programming language or codebase
  - Useful but not overruling organization
- [License customization](https://developer.github.com/v3/licenses/)
- [Gitignore customization](https://www.gitignore.io/)
- Remote repository creation
  - [Bitbucket.org](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories) using [Basic auth](https://developer.atlassian.com/bitbucket/api/2/reference/meta/authentication#basic-auth)
  - [GitHub.com](https://developer.github.com/v3/repos/#create) using [Basic auth](https://developer.github.com/v3/#basic-authentication)
  - [GitLab.com](https://docs.gitlab.com/ee/api/projects.html#create-project) using [Personal access tokens](https://docs.gitlab.com/ce/api/README.html#personal-access-tokens)
- Cross-platform support

### Upcoming
- Add gitlab_token validation
- Add more secure auth methods
- Additional remote repo customization
- Full coverage testing
- Continuous integration

## Requirements
- [git](https://git-scm.com/downloads)
- [python](https://www.python.org/downloads/)
- [cookiecutter](https://github.com/audreyr/cookiecutter)

## Usage
    $ cookiecutter gh:nathanurwin/cookiecutter-git

Which is an alias for:

    $ cookiecutter https://github.com/nathanurwin/cookiecutter-git

See generated [README.md]({{cookiecutter.repo_slug}}/README.md)

### Example
See [cookiecutter-git-demo](https://github.com/nathanurwin/cookiecutter-git-demo)

```
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
`repo_slug` | The repository name which should only contain alphanumeric characters and dashes. This will be the local, top-level directory name, the remote endpoint, and the *H1* in the **README.md**.
`repo_description` | A short description about the repository. This will be the remote description setting, and the content under the *H1* in the **README.md**.
`remote_repo` | A `yes` or `no` choice on whether or not a remote repository is automatically created for you. This option is the main reason for *cookiecutter-git*, so the default choice is `yes`.
`remote_provider` | A choice between the three main, git, remote repository providers. This will only be used if `remote_repo` is `yes`, and defaults to `github.com`.
`remote_protocol` | A choice between the HTTPS and SSH protocols. HTTPS is the default, since those using SSH qualify as power users and should be able to handle setting up a [cookiecutter user config](https://cookiecutter.readthedocs.io/en/latest/advanced/user_config.html).
`make_dirs` | A comma-separated values list of directory names. Directories will be made with a `.gitkeep` file, so they will be added to the initial commit.
`gitignore` | A comma-separated values list of preset templates of files for git to ignore. See the [gitignore.io docs](https://github.com/joeblau/gitignore.io#list) for a complete list of available values. This will be used to generate the **.gitignore** file.
`license` | The software license for the repository. This will be used to generate the **LICENSE** and **NOTICE** files, and determines how end users can ultimately use your source code.
`copyright_holder` | The individual or company that holds the intellectual property copyright. This will be used in the **LICENSE** file, rather than the `author_name`.

## Development
See [CONTRIBUTING](CONTRIBUTING.md)

### Future
See [ROADMAP](ROADMAP.md)

### History
See [CHANGELOG](CHANGELOG.md)

## Credits
See [AUTHORS](AUTHORS.md)

## License
See [LICENSE](LICENSE)
