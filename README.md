# cookiecutter-git
**Git Cookiecutter**. Git Repository Project Template!

## Features
- [Bare project structure](https://github.com/webevllc/cookiecutter-git-example)
- [License customization](https://developer.github.com/v3/licenses/)
- [Gitignore customization](https://www.gitignore.io/)
- Remote repository creation
  - [GitHub.com as provider](https://developer.github.com/v3/repos/)
  - [GitLab.com as provider](https://docs.gitlab.com/ce/api/projects.html)
- Cross-platform support

### Upcoming
- [Bitbucket.org support](https://bitbucket.org/)
- Full coverage testing
- Continuous integration
- [CodeCommit support](https://aws.amazon.com/codecommit/) ?

## Requirements
- [git](https://git-scm.com/downloads)
- [python](https://www.python.org/downloads/)
- [cookiecutter](https://github.com/audreyr/cookiecutter)

## Usage
    $ cookiecutter gh:webevllc/cookiecutter-git

### Example
See [cookiecutter-git-example](https://github.com/webevllc/cookiecutter-git-example)

    $ tree -a test-repo
    test-repo
    ├── AUTHORS.md
    ├── CHANGELOG.md
    ├── CONTRIBUTING.md
    ├── .git
    ├── .gitignore
    ├── LICENSE
    ├── NOTICE
    ├── README.md
    └── test_pkg
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
