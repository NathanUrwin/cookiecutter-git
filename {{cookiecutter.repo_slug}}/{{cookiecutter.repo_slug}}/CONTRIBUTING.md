# Contributing

Contributions are welcome, and they are greatly appreciated!

Every little bit helps, and credit will always be given.

## Types of Contributions

### Bug Reports, Feature Requests, and Feedback

Create a [new project issue][issue-link]! Try to be as descriptive as possible.

### Bug Fixes, New Features and Documentation

Create a [new merge/pull request][merge-link]! Make sure to follow the guidelines.

## Merge/Pull Request Guidelines

Make sure to have atomic commits and contextual commit messages!

["How to Write a Git Commit Message" by Chris Beams.][chris-beams]

[issue-link]: {% if cookiecutter.remote_provider == "None" %}mailto:{{cookiecutter.git_email}}{% else %}https://{{cookiecutter.remote_provider|lower()}}/{{cookiecutter.remote_namespace}}/{{cookiecutter.repo_slug}}/issues/new{% endif %}
[merge-link]: {% if cookiecutter.remote_provider == "None" %}mailto:{{cookiecutter.git_email}}{% else %}https://{{cookiecutter.remote_provider|lower()}}/{{cookiecutter.remote_namespace}}/{{cookiecutter.repo_slug}}/{% if cookiecutter.remote_provider == 'GitHub.com' %}compare{% elif cookiecutter.remote_provider == 'GitLab.com' %}merge_requests/new{% elif cookiecutter.remote_provider == 'Bitbucket.org' %}pull-requests/new{% endif %}{% endif %}
[chris-beams]: http://chris.beams.io/posts/git-commit/
