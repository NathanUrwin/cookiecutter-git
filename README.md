# cookiecutter-git
**Git Cookiecutter**. Git Repository Project Template!

## Features
- [Bare project structure](https://github.com/webevllc/cookiecutter-git-example)
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
    $ cookiecutter gh:webevllc/cookiecutter-git

### Example
See [cookiecutter-git-example](https://github.com/webevllc/cookiecutter-git-example)

    $ tree -a cookiecutter-git-example
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

## Development
See [CONTRIBUTING](CONTRIBUTING.md)

## History
See [CHANGELOG](CHANGELOG.md)

## Credits
See [AUTHORS](AUTHORS.md)

## License
See [LICENSE](LICENSE), [NOTICE](NOTICE)
