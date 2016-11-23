# cookiecutter-docs-md
Cookiecutter for **Markdown Documentation**!

## Features
 - Markdown documentation
 - Simple project structure
 - License customization
 - Gitignore customization

## Upcoming
 - Gitlab support
 - Remote repo init
 - [github-changelog-generator][1]

## Requirements
 - [bash][2]
 - [python][3]
 - [cookiecutter][4]

## Usage
    $ cookiecutter gh:webevllc/cookiecutter-docs-md

## Example
    $ cookiecutter gh:webevllc/cookiecutter-docs-md
    Cloning into 'cookiecutter-docs-md'...
    remote: Counting objects: 42, done.
    remote: Compressing objects: 100% (27/27), done.
    remote: Total 42 (delta 18), reused 35 (delta 11), pack-reused 0
    Unpacking objects: 100% (42/42), done.
    Checking connectivity... done.
    author_name [My Name]: Nathan Urwin
    author_email [myemail@example.com]: tuxredux2@gmail.com
    github_user [myusernameismyusernameis]: tuxredux
    repo_space [myusernameorgroup]: tuxredux
    repo_name [my-repo-name]: cc-docs-md-test
    pkg_name [mypkgname]: ccdocsmdtest

    $ tree -a cc-docs-md-test
    cc-docs-md-test
    ├── AUTHORS.md
    ├── ccdocsmdtest
    │   └── .gitkeep
    ├── CHANGELOG.md
    ├── CONTRIBUTING.md
    ├── .gitignore
    ├── LICENSE
    ├── NOTICE
    └── README.md

    1 directory, 8 files

## Development
See [CONTRIBUTING](CONTRIBUTING.md)

## History
See [CHANGELOG](CHANGELOG.md)

## Credits
See [AUTHORS](AUTHORS.md)

## License
See [LICENSE](LICENSE), [NOTICE](NOTICE)

[1]: https://github.com/skywinder/github-changelog-generator
[2]: https://www.gnu.org/software/bash/bash.html
[3]: https://www.python.org/downloads/
[4]: https://github.com/audreyr/cookiecutter
