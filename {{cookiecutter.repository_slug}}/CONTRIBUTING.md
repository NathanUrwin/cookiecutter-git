# Contributing
Contributions are welcome, and they are greatly appreciated!

Every little bit helps, and credit will always be given.

## Types of Contributions

### Bug Reports, Feature Requests, and Feedback
Create a [new project issue][1]! Try to be as descriptive as possible.

### Bug Fixes, New Features and Documentation
Create a [new merge/pull request][2]! Make sure to follow the guidelines.

## Merge/Pull Request Guidelines
Make sure to have atomic commits and contextual commit messages!

[Check out this awesome blog post by Chris Beams for more information.][3]

[1]: https://{{cookiecutter.remote_provider}}/{{cookiecutter.repository_namespace}}/{{cookiecutter.repository_slug}}/issues/new
[2]: https://github.com/{{cookiecutter.repository_namespace}}/{{cookiecutter.repository_slug}}/{% if cookiecutter.remote_provider == 'github.com' %}compare{% elif cookiecutter.remote_provider == 'gitlab.com' %}merge_requests/new{% elif cookiecutter.remote_provider == 'bitbucket.org' %}pull-requests/new{% endif %}
[3]: http://chris.beams.io/posts/git-commit/
