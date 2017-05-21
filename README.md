# cookiecutter-git
**Git Cookiecutter**. A git repository project template!

## Features
- [Bare project structure](https://github.com/tuxredux/cookiecutter-git-example)
  - For any programming language or codebase
  - Useful but not overruling organization
- [License customization](https://developer.github.com/v3/licenses/)
- [Gitignore customization](https://www.gitignore.io/)
- Remote repository creation
  - [GitHub.com as provider](https://developer.github.com/v3/repos/)
  - [GitLab.com as provider](https://docs.gitlab.com/ce/api/projects.html)
  - [Bitbucket.org as provider](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories)
- Cross-platform support

### Upcoming
- Add gitlab_token validation
- Add more secure auth methods
- Additional remote repo customization options
- Full coverage testing
- Continuous integration

## Requirements
- [git](https://git-scm.com/downloads)
- [python](https://www.python.org/downloads/)
- [cookiecutter](https://github.com/audreyr/cookiecutter)

## Usage
    $ cookiecutter gh:tuxredux/cookiecutter-git
    # OR
    $ cookiecutter https://github.com/tuxredux/cookiecutter-git

### Example
See [cookiecutter-git-example](https://github.com/tuxredux/cookiecutter-git-example)

    $ tree -a -I .git cookie-cookie-example
    cookiecutter-git-example
    ├── AUTHORS.md
    ├── CHANGELOG.md
    ├── CONTRIBUTING.md
    ├── .git
    ├── .gitignore
    ├── LICENSE
    ├── NOTICE
    ├── README.md
    └── example_package
        └── .gitkeep

    2 directories, 8 files

## Documentation
**cookiecutter.json** explained in-depth. See [cookiecutter.json](cookiecutter.json) for default values.

Prompt | Explanation
--- | ---
`author_name` | Your full name, including first and last names, titles, and possibly even your middle name. This will go under *Project Lead* in **AUTHORS.md**.
`author_email` | The email address you want associated with the repository. This will go under *Project Lead* in **AUTHORS.md**.
`git_username` | Your local git and `remote_provider` (see below) account username. This will be used for all git-based actions.
`repository_namespace` | The namespace where the repository will live, which can be a user or organization, group, or team (depending on the `remote_provider`). This will only be used if `create_remote` (see below) is `yes`.
`repository_slug` | The repository name which should only contain alphanumeric characters and dashes. This will be the local, top-level directory name, the remote endpoint, and the *H1* in the **README.md**.
`repository_description` | A short description about the repository. This will be the remote description setting, and the content under the *H1* in the **README.md**.
`package_name` | The child directory name. This will be dependent on your codebase. For example, the default value contains only alphanumeric characters and underscores suitable for [python development](https://www.python.org/dev/peps/pep-0008/).
`create_remote` | A `yes` or `no` choice on whether or not a remote repository is automatically created for you. This option is the main reason for *cookiecutter-git*, so the default choice is `yes`.
`remote_provider` | A choice between the three main, git, remote repository providers. This will only be used if `create_remote` is `yes`, and defaults to `github.com`.
`gitignore` | A comma-separated values list of preset templates of files for git to ignore. See the [gitignore.io docs](https://github.com/joeblau/gitignore.io#list) for a complete list of available values. This will be used to generate the **.gitignore** file.
`license` | The software license for the repository. This will be used to generate the **LICENSE** and **NOTICE** files, and determines how end users can ultimately use your source code.
`copyright_holder` | The individual or company that holds the intellectual property copyright. This will be used in the **LICENSE** file, rather than the `author_name`.

## Development
See [CONTRIBUTING](CONTRIBUTING.md)

## History
See [CHANGELOG](CHANGELOG.md)

## Credits
See [AUTHORS](AUTHORS.md)

## License
See [LICENSE](LICENSE), [NOTICE](NOTICE)
