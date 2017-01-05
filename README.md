# cookiecutter-bare
**Cookiecutter** for a **Bare** Project!

## Features
 - Bare project structure
 - License customization
 - Gitignore customization

## Upcoming
 - Gitlab support
 - Remote repository automatic initialization
 - [github-changelog-generator](https://github.com/skywinder/github-changelog-generator)
 - First major tag release

## Requirements
 - [bash](https://www.gnu.org/software/bash/bash.html)
 - [python](https://www.python.org/downloads/)
 - [cookiecutter](https://github.com/audreyr/cookiecutter)

## Usage
    $ cookiecutter gh:webevllc/cookiecutter-bare

## Example
    $ cookiecutter gh:webevllc/cookiecutter-bare
    Cloning into 'cookiecutter-bare'...
    remote: Counting objects: 52, done.
    remote: Compressing objects: 100% (33/33), done.
    remote: Total 52 (delta 25), reused 41 (delta 14), pack-reused 0
    Unpacking objects: 100% (52/52), done.
    Checking connectivity... done.
    author_name [My Name]: Nathan Urwin
    author_email [myemail@example.com]: tuxredux2@gmail.com
    github_user [myusernameismyusernameis]: tuxredux
    repo_space [myusernameorgroup]: webevllc
    repo_name [my-repo-name]: cc-bare-test
    pkg_name [mypkgname]: ccbaretest
    gitignore [windows,osx,linux,git]: windows,osx,linux,git,python
    Select license:
    1 - Apache-2.0
    2 - MIT
    3 - BSD-3
    4 - GPLv3
    5 - Proprietary
    Choose from 1, 2, 3, 4, 5 [1]:
    copyright_holder [My Company, Inc.]: WEBEV LLC
    copyright_holder_short [MY COMPANY]: WEBEV
    updated '/home/user/Projects/webevllc/cc-bare-test/.gitignore'


    cc-bare-test setup successfully!


    $ tree -a cc-bare-test
    cc-bare-test
    ├── AUTHORS.md
    ├── ccbaretest
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
