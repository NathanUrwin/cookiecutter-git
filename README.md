# cookiecutter-git
**Git Cookiecutter**. Git Repository Project Template!

## Features
 - Bare project structure
 - License customization
 - [Gitignore customization](https://www.gitignore.io/)
 - Remote repository creation
  - [GitHub.com as provider](https://github.com/)
  - [GitLab.com as provider](https://gitlab.com/)
 - Cross-platform support

### Upcoming
 - More license choices
 - [github-changelog-generator](https://github.com/skywinder/github-changelog-generator)
 - [Bitbucket.org support](https://bitbucket.org/)
 - First major tag release
 - *AWS&reg; CodeCommit&reg;* support ?

## Requirements
 - [git](https://git-scm.com/downloads)
 - [python](https://www.python.org/downloads/)
 - [cookiecutter](https://github.com/audreyr/cookiecutter)

## Usage
    $ cookiecutter gh:webevllc/cookiecutter-git

### Example
    $ cookiecutter gh:webevllc/cookiecutter-git
    author_name [Nathan Urwin]:
    author_email [tuxredux2@gmail.com]:
    git_user [tuxredux]:
    repo_space [tuxredux]:
    repo_name [bare-repository]:
    pkg_name [bare_package]:
    Select create_remote:
    1 - yes
    2 - no
    Choose from 1, 2 [1]:
    Select remote_provider:
    1 - GitHub
    2 - GitLab
    Choose from 1, 2 [1]:
    Select github_org_repo_space:
    1 - no
    2 - yes
    Choose from 1, 2 [1]:
    gitlab_token []:
    gitignore [windows,osx,linux,git]:
    Select license:
    1 - Apache-2.0
    2 - MIT
    3 - BSD-3
    4 - GPLv3
    5 - Proprietary
    Choose from 1, 2, 3, 4, 5 [1]:
    copyright_holder [Webev LLC]:
    copyright_holder_short [WEBEV]:
    Initialized empty Git repository in /home/user/Projects/sandbox/bare-repository/.git/
    On branch master

    Initial commit

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

    	.gitignore
    	AUTHORS.md
    	CHANGELOG.md
    	CONTRIBUTING.md
    	LICENSE
    	NOTICE
    	README.md
    	bare_package/

    nothing added to commit but untracked files present (use "git add" to track)
    On branch master

    Initial commit

    Changes to be committed:
      (use "git rm --cached <file>..." to unstage)

    	new file:   .gitignore
    	new file:   AUTHORS.md
    	new file:   CHANGELOG.md
    	new file:   CONTRIBUTING.md
    	new file:   LICENSE
    	new file:   NOTICE
    	new file:   README.md
    	new file:   bare_package/.gitkeep

    [master (root-commit) d55acfb] Initial commit
     8 files changed, 350 insertions(+)
     create mode 100644 .gitignore
     create mode 100644 AUTHORS.md
     create mode 100644 CHANGELOG.md
     create mode 100644 CONTRIBUTING.md
     create mode 100644 LICENSE
     create mode 100644 NOTICE
     create mode 100644 README.md
     create mode 100644 bare_package/.gitkeep
    Enter host password for user 'tuxredux':
    {
      "id": 83353120,
      "name": "bare-repository",
      "full_name": "tuxredux/bare-repository",
      "owner": {
        "login": "tuxredux",
        "id": 13526277,
        "avatar_url": "https://avatars.githubusercontent.com/u/13526277?v=3",
        "gravatar_id": "",
        "url": "https://api.github.com/users/tuxredux",
        "html_url": "https://github.com/tuxredux",
        "followers_url": "https://api.github.com/users/tuxredux/followers",
        "following_url": "https://api.github.com/users/tuxredux/following{/other_user}",
        "gists_url": "https://api.github.com/users/tuxredux/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/tuxredux/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/tuxredux/subscriptions",
        "organizations_url": "https://api.github.com/users/tuxredux/orgs",
        "repos_url": "https://api.github.com/users/tuxredux/repos",
        "events_url": "https://api.github.com/users/tuxredux/events{/privacy}",
        "received_events_url": "https://api.github.com/users/tuxredux/received_events",
        "type": "User",
        "site_admin": false
      },
      "private": false,
      "html_url": "https://github.com/tuxredux/bare-repository",
      "description": null,
      "fork": false,
      "url": "https://api.github.com/repos/tuxredux/bare-repository",
      "forks_url": "https://api.github.com/repos/tuxredux/bare-repository/forks",
      "keys_url": "https://api.github.com/repos/tuxredux/bare-repository/keys{/key_id}",
      "collaborators_url": "https://api.github.com/repos/tuxredux/bare-repository/collaborators{/collaborator}",
      "teams_url": "https://api.github.com/repos/tuxredux/bare-repository/teams",
      "hooks_url": "https://api.github.com/repos/tuxredux/bare-repository/hooks",
      "issue_events_url": "https://api.github.com/repos/tuxredux/bare-repository/issues/events{/number}",
      "events_url": "https://api.github.com/repos/tuxredux/bare-repository/events",
      "assignees_url": "https://api.github.com/repos/tuxredux/bare-repository/assignees{/user}",
      "branches_url": "https://api.github.com/repos/tuxredux/bare-repository/branches{/branch}",
      "tags_url": "https://api.github.com/repos/tuxredux/bare-repository/tags",
      "blobs_url": "https://api.github.com/repos/tuxredux/bare-repository/git/blobs{/sha}",
      "git_tags_url": "https://api.github.com/repos/tuxredux/bare-repository/git/tags{/sha}",
      "git_refs_url": "https://api.github.com/repos/tuxredux/bare-repository/git/refs{/sha}",
      "trees_url": "https://api.github.com/repos/tuxredux/bare-repository/git/trees{/sha}",
      "statuses_url": "https://api.github.com/repos/tuxredux/bare-repository/statuses/{sha}",
      "languages_url": "https://api.github.com/repos/tuxredux/bare-repository/languages",
      "stargazers_url": "https://api.github.com/repos/tuxredux/bare-repository/stargazers",
      "contributors_url": "https://api.github.com/repos/tuxredux/bare-repository/contributors",
      "subscribers_url": "https://api.github.com/repos/tuxredux/bare-repository/subscribers",
      "subscription_url": "https://api.github.com/repos/tuxredux/bare-repository/subscription",
      "commits_url": "https://api.github.com/repos/tuxredux/bare-repository/commits{/sha}",
      "git_commits_url": "https://api.github.com/repos/tuxredux/bare-repository/git/commits{/sha}",
      "comments_url": "https://api.github.com/repos/tuxredux/bare-repository/comments{/number}",
      "issue_comment_url": "https://api.github.com/repos/tuxredux/bare-repository/issues/comments{/number}",
      "contents_url": "https://api.github.com/repos/tuxredux/bare-repository/contents/{+path}",
      "compare_url": "https://api.github.com/repos/tuxredux/bare-repository/compare/{base}...{head}",
      "merges_url": "https://api.github.com/repos/tuxredux/bare-repository/merges",
      "archive_url": "https://api.github.com/repos/tuxredux/bare-repository/{archive_format}{/ref}",
      "downloads_url": "https://api.github.com/repos/tuxredux/bare-repository/downloads",
      "issues_url": "https://api.github.com/repos/tuxredux/bare-repository/issues{/number}",
      "pulls_url": "https://api.github.com/repos/tuxredux/bare-repository/pulls{/number}",
      "milestones_url": "https://api.github.com/repos/tuxredux/bare-repository/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/tuxredux/bare-repository/notifications{?since,all,participating}",
      "labels_url": "https://api.github.com/repos/tuxredux/bare-repository/labels{/name}",
      "releases_url": "https://api.github.com/repos/tuxredux/bare-repository/releases{/id}",
      "deployments_url": "https://api.github.com/repos/tuxredux/bare-repository/deployments",
      "created_at": "2017-02-27T20:24:09Z",
      "updated_at": "2017-02-27T20:24:09Z",
      "pushed_at": "2017-02-27T20:24:10Z",
      "git_url": "git://github.com/tuxredux/bare-repository.git",
      "ssh_url": "git@github.com:tuxredux/bare-repository.git",
      "clone_url": "https://github.com/tuxredux/bare-repository.git",
      "svn_url": "https://github.com/tuxredux/bare-repository",
      "homepage": null,
      "size": 0,
      "stargazers_count": 0,
      "watchers_count": 0,
      "language": null,
      "has_issues": true,
      "has_downloads": true,
      "has_wiki": true,
      "has_pages": false,
      "forks_count": 0,
      "mirror_url": null,
      "open_issues_count": 0,
      "forks": 0,
      "open_issues": 0,
      "watchers": 0,
      "default_branch": "master",
      "permissions": {
        "admin": true,
        "push": true,
        "pull": true
      },
      "network_count": 0,
      "subscribers_count": 1
    }
    Password for 'https://tuxredux@github.com':
    Counting objects: 11, done.
    Delta compression using up to 8 threads.
    Compressing objects: 100% (8/8), done.
    Writing objects: 100% (11/11), 5.89 KiB | 0 bytes/s, done.
    Total 11 (delta 0), reused 0 (delta 0)
    To https://tuxredux@github.com/tuxredux/bare-repository.git
     * [new branch]      master -> master
    Branch master set up to track remote branch master from origin.


    bare-repository setup successfully!


    $ tree -a -L 1 bare-repository
    bare-repository
    ├── AUTHORS.md
    ├── bare_package
    ├── CHANGELOG.md
    ├── CONTRIBUTING.md
    ├── .git
    ├── .gitignore
    ├── LICENSE
    ├── NOTICE
    └── README.md

    2 directories, 7 files

## Development
See [CONTRIBUTING](CONTRIBUTING.md)

## History
See [CHANGELOG](CHANGELOG.md)

## Credits
See [AUTHORS](AUTHORS.md)

## License
See [LICENSE](LICENSE), [NOTICE](NOTICE)
