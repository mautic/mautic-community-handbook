---
title: Pull requests
taxonomy:
    category:
        - docs
---

## Pull requests
---

We highly appreciate it when developers help us by providing Pull Requests against the Mautic code base. In order to make this process as smooth as possible for everyone, we kindly ask you to follow this process step by step. 

<!-- ## Table of Contents -->

<!--
Use this site to generate the TOC list elements:

- https://ecotrust-canada.github.io/markdown-toc/

remove the first two lines
-->

  - [Step 1: Check existing Issues and Pull Requests](#step-1-check-existing-issues-and-pull-requests)
  - [Step 2: Feature? Check the roadmap & Feature Requests](#step-2-feature-check-the-roadmap--feature-requests)
  - [Step 3: Setup your environment](#step-3-setup-your-environment)
    - [Install the software stack](#install-the-software-stack)
    - [Get the Mautic source code](#get-the-mautic-source-code)
  - [Step 4: Work on your Pull Request](#step-4-work-on-your-pull-request)
    - [Choose the right branch](#choose-the-right-branch)
    - [Install Mautic](#install-mautic)
    - [Create a Topic Branch](#create-a-topic-branch)
    - [Work on your Pull Request](#work-on-your-pull-request)
    - [Prepare your Pull Request for Submission](#prepare-your-pull-request-for-submission)
  - [Step 5: Submit your Pull Requests](#step-5-submit-your-pull-requests)
    - [Rebase your Pull Request](#rebase-your-pull-request)
    - [Make a Pull Request](#make-a-pull-request)
  - [Step 6: Receiving feedback](#step-6-receiving-feedback)
    - [Rework your Pull Request](#rework-your-pull-request)

### Step 1: Check existing Issues and Pull Requests

Before working on a change, check to see if someone else also raised the topic or maybe even started working on a PR by [searching on GitHub](https://github.com/mautic/mautic/issues?q=is%3Aopen+).

### Step 2: Feature? Check the roadmap & Feature Requests

_Skip this section if you're not planning to build a new feature_.

Do you want to add a new feature to Mautic? Keep in mind that there are many people requesting new features, so we can only add a limited amount of features in new releases.

Please check our [Roadmap](https://forum.mautic.org/t/mautic-roadmap-discussion/13760) and existing [Feature Requests](https://forum.mautic.org/c/ideas/14/l/latest?order=votes) to see if someone else has already suggested similiar functionality and/or is already working on it. If not, we kindly ask you to first [create a new Feature Request](https://forum.mautic.org/c/ideas/14/l/latest?order=votes) in the appropriate section in the Community Forums, so that it can be discussed by the community prior to development work being done.

### Step 3: Setup your environment

#### Install the software stack

! We recommend working with DDEV since it includes all required software out of the box and has some handy features like dynamic PHP version switching and much more. Mautic-specific installation instructions for DDEV can be found [here](https://www.mautic.org/blog/developer/local-mautic-development-with-ddev). 

Before working on Mautic, make sure you have an environment with the following software:

- Git
- PHP version 7.1+ with Composer
- MySQL 5.7+

Refer to Mautic's [requirements](https://www.mautic.org/download/requirements) for an up-to-date list of required software.

#### Get the Mautic source code

- Create a [GitHub](https://github.com/join) account and sign in
- Fork the Mautic repository (click on the "Fork" button)
- After the "forking action" has completed, clone your fork locally (this will create a `mautic` directory):

```
git clone https://github.com/USERNAME/mautic.git
```

### Step 4: Work on your Pull Request

#### Choose the right branch

Before working on a PR, you must determine on which branch you need to work. Mautic follows [Semantic Versioning](https://semver.org/), which is best illustrated by an example. Let's say we just released a 3.0.0 version of Mautic, the following would apply:

|Mautic version|Breaking changes/features allowed?|New features/enhancements allowed?|Bug fixes allowed?|
|---|---|---|---|
|3.0.1|❌|❌|✅|
|3.1.0|❌|✅|✅|
|4.0.0|✅|✅|✅|

You can determine on which branch to work as follows:

- `3.0` (for example), if you are fixing a bug for an existing version of Mautic
- `staging`, if you are adding a new feature

#### Install Mautic

- Go into your Mautic folder and install the PHP Composer dependencies:

```
cd mautic
composer install
```

- Open Mautic in your browser, for example by going to `http://localhost/mautic` or `https://mautic.ddev.site` depending on your environment, and follow the steps to install Mautic locally.

#### Create a Topic Branch

Each time you want to work on a PR for a bug or on an enhancement, create a topic branch:

```
git checkout -b BRANCH_NAME staging
```

Or, if you want to provide a bug fix for the `3.0` branch, first track the remote `3.0` branch locally:

```
git checkout -t origin/3.0
```

Then create a new branch off the `3.0` branch to work on the bug fix:

```
git checkout -b BRANCH_NAME 3.0
```

! Use a descriptive name for your branch (issue_XXX where XXX is the issue number is a good convention for bug fixes).

The above checkout commands automatically switch the code to the newly created branch (check the branch you are working on with `git branch`).

#### Work on your Pull Request

Work on the code as much as you want and commit as much as you want; but keep in mind the following:
- Mautic follows [Symfony's coding standards](http://symfony.com/doc/current/contributing/code/standards.html) by implementing a pre-commit git hook running [php-cs-fixer](https://github.com/friendsofphp/php-cs-fixer), which is installed and updated with composer install/composer update. All code styling is handled automatically by the aforementioned git hook.
- Add unit tests to prove that the bug is fixed or that the new feature actually works.
- Try hard to not break backward compatibility (if you must do so, try to provide a compatibility layer to support the old way) -- PRs that break backward compatibility have less chance to be merged.


#### Prepare your Pull Request for Submission

When your PR is not about a bug fix (when you add a new feature or change an existing one for instance), it must also include the following:

- Ensure all tests pass (TODO add details)

### Step 5: Submit your Pull Requests

#### Rebase your Pull Request

Before submitting your PR, update your branch (needed if it takes you a while to finish your changes):

```
git checkout staging
git fetch upstream
git merge upstream/staging
git checkout BRANCH_NAME
git rebase staging
```

! Replace `staging` with the branch you selected previously (e.g. `3.0`) if you are working on a bug fix.

When doing the rebase command, you might have to fix merge conflicts. git status will show you the unmerged files. Resolve all the conflicts, then continue the rebase:

```
git add ... # add resolved files
git rebase --continue
```

Check that all tests still pass and push your branch remotely:

```
git push --force origin BRANCH_NAME
```

#### Make a Pull Request

You can now make a pull request on the `mautic/mautic` GitHub repository.

! Take care to point your pull request towards `mautic:3.0` if you want the core team to pull a bug fix based on the `3.0` branch.

To ease the core team work, always include the modified components in your pull request message and provide steps how to test your fix/feature. Keep in mind that not all testers have a thorough knowledge of all of Mautic's features, therefore clear testing steps are crucial!

### Step 6: Receiving feedback

We ask all contributors to follow some best practices (TODO LINK) to ensure a constructive feedback process.

If you think someone fails to keep this advice in mind and you want another perspective, please join the #dev channel on Mautic Slack.

The [product team](https://contribute.mautic.org/product-team) is responsible for deciding which PRs get merged, so their feedback is the most relevant. So do not feel pressured to refactor your code immediately when someone provides feedback.

#### Rework your Pull Request

Based on the feedback on the pull request, you might need to rework your PR. Before re-submitting the PR, rebase with `upstream/staging` or `upstream/3.0`, don't merge; and force the push to the origin:

```
git rebase -f upstream/staging
git push --force origin BRANCH_NAME
```

! When doing a push --force, always specify the branch name explicitly to avoid messing other branches in the repository (--force tells Git that you really want to mess with things so do it carefully).