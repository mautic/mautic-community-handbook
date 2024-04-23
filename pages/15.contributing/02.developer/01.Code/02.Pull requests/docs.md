---
title: Pull requests
slug: pull-requests
taxonomy:
    category:
        - docs
---

## Pull requests
---

It's highly appreciated when developers help Mautic by providing Pull Requests against the Mautic code base. In order to make this process as smooth as possible for everyone, it's asked that you follow this process step by step. 

## Table of contents

<!--
Use this site to generate the TOC list elements:

- https://ecotrust-canada.github.io/markdown-toc/

remove the first two lines
-->

  - [Step 1: Check existing Issues and Pull Requests](#step-1-review-existing-issues-and-pull-requests)
  - [Step 2: Feature? Check the roadmap & Feature Requests](#step-2-new-feature-review-the-roadmap-feature-requests)
  - [Step 3: Setup your environment](#step-3-set-up-your-environment-or-use-gitpod)
    - [Install the software stack](#install-the-software-stack)
    - [Get the Mautic source code](#get-the-mautic-source-code)
  - [Step 4: Work on your Pull Request](#step-4-work-on-your-pull-request)
    - [Choose the right branch](#choose-the-right-branch)
    - [Install Mautic](#install-mautic)
    - [Create a Topic Branch](#create-a-topic-branch)
    - [Work on your Pull Request](#work-on-your-pull-request)
  - [Step 5: Migrations needed?](#step-5-migrations-needed)
  - [Step 6: Prepare your Pull Request for Submission](#step-6-prepare-your-pull-request-for-submission)
    - [Code Standards](#code-standards)
    - [Documentation](#documentation)
    - [Writing tests](#writing-tests)
  - [Step 7: Submit your Pull Request](#step-7-submit-your-pull-request)
    - [Rebase your Pull Request](#rebase-your-pull-request)
    - [Make a Pull Request](#make-a-pull-request)
  - [Step 8: Receiving feedback](#step-8-receiving-feedback)
    - [Rework your Pull Request](#rework-your-pull-request)
  - [Step 9: Testing](#step-9-testing)
    - [Pull Request Testing](#pull-request-testing)
    - [Automated Testing](#automated-testing)
      -[PHPUnit](#phpunit)
    - [Static Analysis](#static-analysis)

## Step 1: review existing issues and pull requests

Before working on a change, review the existing issues and pull requests to see if someone else also raised the topic or maybe even started working on a PR by [searching on GitHub][open-issues-github].  You can also ask in the Product Team [Slack][mautic-slack] channel, #t-product.

## Step 2: new feature? Review the roadmap & feature requests

_Skip this section if you're not planning to build a new feature_.

Do you want to add a new feature to Mautic? Keep in mind that there are many people requesting new features, so the Core Team can only add a limited amount of features in new releases.

Please review the [Roadmap][roadmap] and existing [Feature Requests][feature-requests] to see if someone else has already suggested similar features and/or is already working on it. If not, please first [create a new Feature Request][create-feature-request] in the appropriate section in the Community Forums, so that the Community can discuss prior to development work commencing.

Features that don't to fit within the direction of the Mautic Core goals are more than welcome as third-party Plugins instead. 

## Step 3: set up your environment (or use Gitpod)

### Install the software stack 

For installing the software stack, please see the [Local environment setup][local-environment-setup] instructions.

### Get the Mautic source code

- Create a [GitHub][github-join] account and sign in
- Fork the Mautic repository by clicking the "Fork" button
- After the "forking action" has completed, clone your fork locally - this will create a `mautic` directory - using the following command:

```
git clone https://github.com/USERNAME/mautic.git
```

or, if you use the [GitHub CLI][github-cli], use 

```
gh repo clone mautic/mautic
```

## Step 4: work on your pull request

### Choose the right branch

Before working on a PR, you must determine on which branch you need to work. Mautic follows [Semantic Versioning][semver], which is best illustrated by an example. 

Assuming that:

a = current major release (e.g. 4 in 4.4.5)
b = current minor release (e.g. 4.4 in 4.4.5)
c = future major release (e.g. 5 in 5.0)

* All PRs are made against the c.x branch in the first instance (e.g. 5.x)
* If the PR should be merged in an earlier release than the next major release of Mautic, duplicate the PR against the relevant a.b branch for bug fixes (e.g. 5.0), or a.x branch for features and enhancements (e.g. 5.x).
* Backwards compatibility breaking changes can only be released in a major version, so they should only ever be made against the c.x branch (e.g. 5.x)

The exception to this rule is if the last feature release (e.g. 5.4) has already been made, then all features would be made against the c.x branch (e.g. 6.x), rather than the 5.x branch. This is usually made clear in release notes, but if you're not sure, please ask in #t-product on Slack.

As an example, if Mautic just released a 4.0.0 version of Mautic, the following would apply:

|Mautic version|Breaking changes/features allowed?|New features/enhancements allowed?|Bug fixes allowed?|
|---|---|---|---|
|4.0.1|❌|❌|✅|
|4.1.0|❌|✅|✅|
|5.0.0|✅|✅|✅|

You can determine on which branch to work as follows:

- `4.4`, if you are fixing a bug and you want your bug included in a 4.4.x releases of Mautic - you must also create a duplicate PR for the 5.x branch as well.
- `4.x`, if you are adding a new feature or enhancing an existing feature to include in a version of Mautic 4, which is the current major release.
- `5.x`, if you are adding a new feature or enhancing an existing feature which breaks backwards compatibility, to include in the next major version of Mautic, Mautic 5.

### Install Mautic

If you are using DDEV, type:

`ddev start`

and the installer takes care of the rest - the Mautic installation process happens at the command line automatically. Just wait for it to complete!

If you aren't using DDEV:

- Go into your Mautic folder and install the PHP Composer dependencies:

```
cd mautic
composer install
```

- Open Mautic in your browser, for example by going to `http://localhost/mautic` depending on your environment, if you want to install in the UI. Follow the steps to [install Mautic][install-mautic] locally.

### Create a topic branch

Each time you want to work on a PR for a bug or on an enhancement, create a topic branch from the relevant base branch:

```
git checkout -b BRANCH_NAME 5.x
```

Or, if you want to provide a bug fix for the `5.0` branch, first track the remote `5.0` branch locally:

```
git checkout -t origin/5.0
```

Then create a new branch off the `5.0` branch to work on the bug fix:

```
git checkout -b BRANCH_NAME 5.0
```

>>>>>> Use a descriptive name for your branch - for example issue_XXX where XXX is the issue number is a good convention for bug fixes.

The mentioned checkout commands automatically switch the code to the newly created branch - verify the branch you are working on with `git branch`.

### Work on your pull request

Work on the code as much as you want and commit as much as you want, but keep in mind the following:

- Mautic follows [Symfony's coding standards][symfony-coding-standards] by implementing a pre-commit git hook running [php-cs-fixer][php-cs-fixer]. Mautic installs and updates this with composer install/composer update. This handles all code styling automatically.
- Add unit tests to prove that the fixing of the bug or that the new feature actually works - see below.

### Backward compatibility  breaks

Try hard to not break backward compatibility (BC) - if you must do so, try to provide a compatibility layer to support the old way. PRs that break backward compatibility have less chance of acceptance, as they have to wait for release in a major release.

#### What is BC break?

Any change that may break a plugin either using or extending a class. As Mautic has the Plugin ecosystem, we must be considerate of the impact, even on code we might not be using ourselves.

Examples:
- Removing or renaming a public or protected method in a non-final class. Create a new method instead and mark the old one [deprecated](https://contribute.mautic.org/governance/code-governance/deprecation-policy).
- Changing the signature of a private or public method in a non-final class. Meaning adding, removing method parameters or adding or changing param or return types. Create a new method instead and mark the old one deprecated.
- Changing behavior of a method so it does something differently.
- Adding a new method to an existing interface. Create a new interface instead.
- Every time you change a TWIG template then think about the Themes that are overwriting this template. For example, changing the template name will cause issues.

#### What is not considered a BC break?

On the other hand, there are some changes you can do that are not considered a BC break:
- Changing constructor of a PHP service. Services are autowired so there is no harm in changing the dependencies.

#### Write your code with BC breaks in mind

Think about the BC breaks as you write a new code.

- Make new classes final by default. Only remove the final keyword if there is a good reason for it.
- Make a new method private by default. Make it public only if you need to use it outside of the class.
- Prefer composition over inheritance. This way you can use final classes.
- A unit test is not a good reason why a class shouldn't be final. For example, get the final service from the container instead of mocking it. If it's a final DTO object then you don't need to mock it at all.

## Step 5: migrations needed?

Sometimes a PR needs a migration. An example is when updating a country's regions. 

If a region contains a typo, `Colmbra` should be `Coimbra`, what if the Mautic instance already has values in the database with the old value - `Colmbra` in this case? 

That's where migrations come in handy. **Every time a User updates their Mautic instance, migrations run automatically.**

>>>  You can skip this step if you believe you don't need migrations in your PR.

Find an example migration scenario + code [here][example-migration].

In order to create a migration, you can follow these steps:

1. Run `bin/console doctrine:migrations:generate` in your terminal. Doctrine creates a new migration file for you:

```bash
$ bin/console doctrine:migrations:generate 
Generated new migration class to "/var/www/html/app/migrations/Version20201017195540.php"
```

2. Open the file that was just created. It has two functions, `preUp()` and `up()`.

  - `preUp()` allows you to define scenarios where the migration should or shouldn't run - for example only when a certain database table exists.

  - `up()` runs the actual migration and allows you to do changes in Mautic's database. You can either take inspiration from other migrations in the `app/migrations` folder or learn more about migrations in [Doctrine's documentation][doctrine-migrations-docs].

3. When you're done, test your migration/s by running `migrations:execute --up VERSION`. If all looks good, you can roll back your changes with `migrations:execute --down VERSION`.

## Step 6: prepare your pull request for submission

You're almost ready to submit your pull request. There's three things you still need to look into:

1. Code Standards
2. End-user documentation
3. Writing tests

In order to keep Mautic stable and easy to maintain, there is a hard requirement to apply the appropriate Code Standards and to write automated tests. Mautic can't accept features and/or enhancements without appropriate tests, as it would impact the stability of Mautic. Why? When you try to build something in a specific part of Mautic, you might accidentally break another part of Mautic. With automated tests, which cover most aspects of Mautic, it's possible to prevent this as much as possible. 

### Code standards

Mautic follows [Symfony's coding standards][symfony-coding-standards] by implementing pre-commit git hook running [php-cs-fixer][php-cs-fixer]. `composer install`/`composer update` installs and updates this automatically.

The aforementioned git hook automatically deals with any code styling. If you setup git hook correctly - which is the case if you ever run `composer install`/`composer update` before creating a pull request - you can format your code as you like - the git hook converts it to Mautic's code style automatically.

### Documentation 

Each new feature should include a reference to a pull request in the [End User Documentation][mautic-docs] repository and/or [Developer Documentation][developer-docs] repository if applicable. Any enhancements or bug fixes affecting the end-user or developer experience should have a PR mentioned in the description which updates the relevant resources in the Documentation.

### Writing tests

All code contributions - especially enhancements/features - should include adequate and appropriate unit tests using [PHPUnit][php-unit] and/or [Symfony functional tests][symfony-functional-tests]. The Core Team won't merge pull requests without these tests. See below for more extensive information on Automated Tests.

## Step 7: submit your pull request

### Rebase your pull request

Before submitting your PR, update your branch - especially if it takes you a while to finish your changes:

```
git checkout 4.x
git fetch upstream
git merge upstream/4.x
git checkout BRANCH_NAME
git rebase 4.x
```

! Replace `4.x` with the branch you selected previously - for example `4.4` - if you are working on a bug fix.

When doing the rebase command, you might have to fix merge conflicts. `git status` shows you the un-merged files. Resolve all the conflicts, then continue the rebase:

```
git add ... # add resolved files
git rebase --continue
```

Check that all tests still pass and push your branch remotely:

```
git push --force origin BRANCH_NAME
```

Sometimes if there are a lot of merge conflicts, it can be easier to re-create your PR on an updated version of the branch, especially if you aren't confident in correctly resolving the conflicts. Please ask for help in #t-product if you are struggling with the rebase of your PR.

### Make a pull request

You can now make a pull request on the `mautic/mautic` GitHub repository.

>>>>> Take care to point your pull request towards `mautic:4.0` if you want the core team to pull a bug fix based on the `4.0` branch.

To ease the core team work, always include what you have modified in your pull request message and provide steps how to test your fix/feature. Keep in mind that not all testers have a thorough knowledge of all of Mautic's features, nor are they all likely to be developers, therefore clear testing steps are crucial.

## Step 8: receiving feedback

It's asked of all contributors to follow some best practices to ensure a constructive feedback process.

If you think someone fails to keep this advice in mind and you want another perspective, please request a review of the feedback in the #dev channel on [Mautic Slack][mautic-slack].

The [Product Team][product-team] is responsible for deciding which PRs get merged, so their feedback is the most relevant. So, don't feel pressured to refactor your code immediately when someone provides feedback, wait for the Product Team to review.

### Rework your pull request

Based on the feedback on the pull request, you might need to rework your PR. Before re-submitting the PR, rebase with `upstream/4.x` or `upstream/4.4` as appropriate - don't merge - and force the push to the origin:

```
git rebase -f upstream/4.x
git push --force origin BRANCH_NAME
```

>>>>>> When doing a push --force, **always** specify the branch name explicitly to avoid messing up other branches in the repository. `--force` tells Git that you **really** want to mess with things, so do it carefully.

## Step 9: Testing

### Pull request testing

If you want to test a pull request from other developers, see [Testing Pull Requests][testing-prs].  All pull requests have a requirement for testing by others in the community, and must have the code reviewed by a member of the core team. Read more about this in the [code governance][code-governance] information.

### Automated testing

Mautic uses [PHPUnit][php-unit] and [Selenium][selenium] as the suite of testing tools. 

#### PHPUnit

**PHPUnit version:** Mautic 4.x requires [PHPUnit v5.7](https://phpunit.de/manual/5.7/en/installation.html), and Mautic 5.x requires [PHPUnit v9+](https://phpunit.de/announcements/phpunit-9.html). Make sure to install the right version of PHPUnit for the version of Mautic you are testing.

**Mautic 4.x:** Before executing unit tests, copy the `.env.dist` file to `.env` then update to reflect your local environment configuration. Mautic 5.x includes an 'env.test' file which is used for unit tests - edit this with your database information if needed.

**Running functional tests without setting the .env file with a different database results in the configured database being overwritten.**

To run the entire test suite: 

```bash
bin/phpunit --bootstrap vendor/autoload.php --configuration app/phpunit.xml.dist
```

To run tests for a specific bundle:

```bash
bin/phpunit --bootstrap vendor/autoload.php --configuration app/phpunit.xml.dist --filter EmailBundle
```

To run a specific test:

```bash
bin/phpunit --bootstrap vendor/autoload.php --configuration app/phpunit.xml.dist --filter "/::testVariantEmailWeightsAreAppropriateForMultipleContacts( .*)?$/" Mautic\EmailBundle\Tests\EmailModelTest app/bundles/EmailBundle/Tests/Model/EmailModelTest.php
```

### Static analysis

Mautic uses [PHPSTAN][phpstan] for some of its parts during continuous integration tests. If you want to test your specific contribution locally, install PHPSTAN globally with `composer global require phpstan/phpstan-shim`. 

Mautic can't have PHPSTAN as its dev dependency, because it requires PHP7+. To run analysis on a specific bundle, run `~/.composer/vendor/phpstan/phpstan-shim/phpstan.phar analyse app/bundles/*Bundle`

[mautic-contributors-agreement]: <https://www.mautic.org/contributor-agreement>
[symfony-coding-standards]: <http://symfony.com/doc/current/contributing/code/standards.html>
[php-cs-fixer]: <https://github.com/friendsofphp/php-cs-fixer>
[php-unit]: <https://phpunit.de/getting-started/phpunit-10.html>
[symfony-functional-tests]: <https://symfony.com/doc/2.8/testing.html>
[mautic-docs]: <https://github.com/mautic/documentation>
[developer-docs]: <https://developer.mautic.org/>
[testing-prs]: </contributing-to-mautic/developer/community-reviews#the-pull-request-review-process>
[phpstan]: <https://github.com/phpstan/phpstan>
[open-issues-github]: <https://github.com/mautic/mautic/issues?q=is%3Aopen+>
[roadmap]: <>
[feature-requests]: <https://forum.mautic.org/c/ideas/14/l/latest?order=votes>
[create-feature-request]: <https://forum.mautic.org/c/ideas/14/l/latest?order=votes>
[contributor-agreement]: <https://www.mautic.org/contributor-agreement>
[local-environment-setup]: </contributing-to-mautic/developer/local-environment-setup>
[github-join]: <https://github.com/join>
[symfony-coding-standards]: <http://symfony.com/doc/current/contributing/code/standards.html>
[semver]: <https://semver.org/>
[product-team]: <https://contribute.mautic.org/product-team>
[example-migration]: <https://github.com/mautic/mautic/pull/8134/files>
[doctrine-migrations-docs]: <https://symfony.com/bundles/DoctrineMigrationsBundle/current/index.html>
[mautic-slack]: <https://mautic.org/slack>
[install-mautic]: <https://docs.mautic.org/en/setup/how-to-install-mautic>
[code-governance]: </community-structure/governance/code-governance>
[github-cli]: <https://cli.github.com>
