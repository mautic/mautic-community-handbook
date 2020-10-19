---
title: Pull requests
slug: pull-requests
taxonomy:
    category:
        - docs
---

## Pull requests
---

We highly appreciate it when developers help us by providing Pull Requests against the Mautic code base. In order to make this process as smooth as possible for everyone, we kindly ask you to follow this process step by step. 

## Table of contents

<!--
Use this site to generate the TOC list elements:

- https://ecotrust-canada.github.io/markdown-toc/

remove the first two lines
-->

  - [Step 1: Check existing Issues and Pull Requests](#step-1-check-existing-issues-and-pull-requests)
  - [Step 2: Feature? Check the roadmap & Feature Requests](#step-2-feature-check-the-roadmap-feature-requests)
  - [Step 3: Sign the Mautic Contributor Agreement](#step-3-sign-the-mautic-contributor-agreement)
  - [Step 4: Setup your environment](#step-4-setup-your-environment)
    - [Install the software stack](#install-the-software-stack)
    - [Get the Mautic source code](#get-the-mautic-source-code)
  - [Step 5: Work on your Pull Request](#step-5-work-on-your-pull-request)
    - [Choose the right branch](#choose-the-right-branch)
    - [Install Mautic](#install-mautic)
    - [Create a Topic Branch](#create-a-topic-branch)
    - [Work on your Pull Request](#work-on-your-pull-request)
  - [Step 6: Migrations needed?](#step-6-migrations-needed)
  - [Step 7: Prepare your Pull Request for Submission](#step-7-prepare-your-pull-request-for-submission)
    - [Code Standards](#code-standards)
    - [Documentation](#documentation)
    - [Writing tests](#writing-tests)
  - [Step 8: Submit your Pull Request](#step-8-submit-your-pull-request)
    - [Rebase your Pull Request](#rebase-your-pull-request)
    - [Make a Pull Request](#make-a-pull-request)
  - [Step 9: Receiving feedback](#step-9-receiving-feedback)
    - [Rework your Pull Request](#rework-your-pull-request)
  - [Testing](#testing)
    - [Pull Request Testing](#pull-request-testing)
    - [Automated Testing](#automated-testing)
      - [PHPUnit](#phpunit)
      - [Codeception/Selenium](#codeceptionselenium)
        - [Mac OS](#mac-os)
        - [Other Platforms](#other-platforms)
        - [Executing Tests](#executing-tests)
    - [Static Analysis](#static-analysis)

## Step 1: Check existing Issues and Pull Requests

Before working on a change, check to see if someone else also raised the topic or maybe even started working on a PR by [searching on GitHub][open-issues-github].

## Step 2: Feature? Check the roadmap & Feature Requests

_Skip this section if you're not planning to build a new feature_.

Do you want to add a new feature to Mautic? Keep in mind that there are many people requesting new features, so we can only add a limited amount of features in new releases.

Please check our [Roadmap][roadmap] and existing [Feature Requests][feature-requests] to see if someone else has already suggested similiar functionality and/or is already working on it. If not, we kindly ask you to first [create a new Feature Request][create-feature-request] in the appropriate section in the Community Forums, so that it can be discussed by the community prior to development work being done.

Features that are determined not to fit within the direction of the Mautic Core goals are more than welcome to be created as plugins instead. 

## Step 3: Sign the Mautic Contributor Agreement
You will need to sign the [Mautic Contributors Agreement][contributor-agreement] in order to contribute code to Mautic (which can be done online).

## Step 4: Setup your environment

### Install the software stack 

For installing the software stack, please see the [Local environment setup][local-environment-setup] instructions.

### Get the Mautic source code

- Create a [GitHub][github-join] account and sign in
- Fork the Mautic repository (click on the "Fork" button)
- After the "forking action" has completed, clone your fork locally (this will create a `mautic` directory):

```
git clone https://github.com/USERNAME/mautic.git
```

## Step 5: Work on your Pull Request

### Choose the right branch

Before working on a PR, you must determine on which branch you need to work. Mautic follows [Semantic Versioning][semver], which is best illustrated by an example. Let's say we just released a 3.0.0 version of Mautic, the following would apply:

|Mautic version|Breaking changes/features allowed?|New features/enhancements allowed?|Bug fixes allowed?|
|---|---|---|---|
|3.0.1|❌|❌|✅|
|3.1.0|❌|✅|✅|
|4.0.0|✅|✅|✅|

You can determine on which branch to work as follows:

- `3.0` (for example), if you are fixing a bug for an existing version of Mautic
- `staging`, if you are adding a new feature

### Install Mautic

- Go into your Mautic folder and install the PHP Composer dependencies:

```
cd mautic
composer install
```

- Open Mautic in your browser, for example by going to `http://localhost/mautic` or `https://mautic.ddev.site` depending on your environment, and follow the steps to install Mautic locally.

### Create a Topic Branch

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

### Work on your Pull Request

Work on the code as much as you want and commit as much as you want; but keep in mind the following:
- Mautic follows [Symfony's coding standards][symfony-coding-standards] by implementing a pre-commit git hook running [php-cs-fixer][php-cs-fixer], which is installed and updated with composer install/composer update. All code styling is handled automatically by the aforementioned git hook.
- Add unit tests to prove that the bug is fixed or that the new feature actually works (see below).
- Try hard to not break backward compatibility (if you must do so, try to provide a compatibility layer to support the old way) -- PRs that break backward compatibility have less chance to be merged.

## Step 6: Migrations needed?

Sometimes, a PR needs a migration. A simple example is when a country's regions are updated. Let's say a region contains a typo, `Colmbra` should be `Coimbra`. What if the Mautic instance already has values in the database with the old value (`Colmbra` in this case)? That's where migrations come in handy. **Every time a user updates their Mautic instance, migrations run automatically.**

>>>  You can skip this step if you believe you don't need migrations in your PR.

An example migration scenario + code can be found [here][example-migration].

In order to create a migration, you can follow these steps:

1. Run `bin/console doctrine:migrations:generate` in your terminal. A new migration file will now be prepared for you:

```bash
$ bin/console doctrine:migrations:generate 
Generated new migration class to "/var/www/html/app/migrations/Version20201017195540.php"
```

2. Open the file that was just created. You will see it has two functions, `preUp()` and `up()`.
  - `preUp()` allows you to define scenarios where the migration should or should not run (e.g. only when a certain database table exists).
  - `up()` runs the actual migration and allows you to do changes in Mautic's database. You can either take inspiration from other migrations in the `app/migrations` folder or learn more about migrations in [Doctrine's documentation](doctrine-migrations-docs).

3. When you're done, test your migration(s) by running `migrations:execute --up VERSION`. If all looks good, you can roll back your changes with `migrations:execute --down VERSION`.

## Step 7: Prepare your Pull Request for Submission

You're almost ready to submit your pull request! There's three things we still need to look into:

1. Code Standards
2. End-user documentation
3. Writing tests

In order to keep Mautic stable and easy to maintain, we have a hard requirement to apply the appropriate Code Standards and to write automated tests. We can't accept features and/or enhancements without appropriate tests, as it would put the stability of Mautic in danger. Why? When you try to build something in a specific part of the application, you might accidentally break another feature. With automated tests, which go through most aspects of the application, we prevent this as much as possible. 

### Code Standards

Mautic follows [Symfony's coding standards][symfony-coding-standards] by implementing pre-commit git hook running [php-cs-fixer][php-cs-fixer], which is installed and updated with `composer install`/`composer update`.

All code styling is handled automatically by the aforementioned git hook. If you setup git hook correctly (which is true if you ever run `composer install`/`composer update` before creating a pull request), you can format your code as you like - it will be converted to Mautic code style automatically.

### Documentation 

Each new feature should include a reference to a pull request in our [End User Documentation][mautic-docs] repository or [Developer Documentation][developer-docs] repository if applicable.  Any enhancements or bugfixes affecting the end-user or developer experience should also be accompanied by a PR updating the relevant resources in the Documentation.

### Writing tests

All code contributions (especially enhancements/features) should include adequate and appropriate unit tests using [PHPUnit][php-unit] and/or [Symfony functional tests][symfony-functional-tests]. Pull Requests without these tests will not be merged. See below for more extensive information on Automated Tests.

## Step 8: Submit your Pull Request

### Rebase your Pull Request

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

### Make a Pull Request

You can now make a pull request on the `mautic/mautic` GitHub repository.

! Take care to point your pull request towards `mautic:3.0` if you want the core team to pull a bug fix based on the `3.0` branch.

To ease the core team work, always include the modified components in your pull request message and provide steps how to test your fix/feature. Keep in mind that not all testers have a thorough knowledge of all of Mautic's features, therefore clear testing steps are crucial!

## Step 9: Receiving feedback

We ask all contributors to follow some best practices (TODO LINK) to ensure a constructive feedback process.

If you think someone fails to keep this advice in mind and you want another perspective, please join the #dev channel on Mautic Slack.

The [product team][product-team] is responsible for deciding which PRs get merged, so their feedback is the most relevant. So do not feel pressured to refactor your code immediately when someone provides feedback.

### Rework your Pull Request

Based on the feedback on the pull request, you might need to rework your PR. Before re-submitting the PR, rebase with `upstream/staging` or `upstream/3.0`, don't merge; and force the push to the origin:

```
git rebase -f upstream/staging
git push --force origin BRANCH_NAME
```

! When doing a push --force, always specify the branch name explicitly to avoid messing other branches in the repository (--force tells Git that you really want to mess with things so do it carefully).

## Testing

### Pull Request Testing

If you want to test Pull Request from other developers, see [Testing Pull Requests](/contributing/developer/testing-pull-requests).

### Automated Testing

Mautic uses [Codeception][codeception], [PHPUnit][php-unit], and [Selenium][selenium] as our suite of testing tools. 

#### PHPUnit

Before executing unit tests, copy the `.env.dist` file to `.env` then update to reflect your local environment
configuration.

**Running functional tests without setting the .env file with a different database will result in the configured database being overwritten.**

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

#### Codeception/Selenium

If you plan on running the acceptance test suite, you'll need to have the Selenium Server Standalone installed and the Chrome WebDriver available locally.

##### Mac OS

If you're on a Mac and you use [Homebrew][homebrew], you can install Selenium by running `brew install selenium-server-standalone`.

You'll also need to download the latest [Chrome WebDriver][chrome-web-driver] which can also be installed with:

`brew cask install chromedriver`

If installing manually, Unzip and move the `chromedriver` file to `/usr/local/Cellar/selenium-server-standalone/drivers/chromedriver`.

Once you have Selenium installed and the WebDriver available at the specified location, open and modify the plist file found at `/usr/local/Cellar/selenium-server-standalone/3.5.3/homebrew.mxcl.selenium-server-standalone.plist`.

In the `<dict><array>` block under `ProgramArguments`, add the following after the line containing `<string>-jar</string>`"

```xml
...
<string>-Dwebdriver.chrome.driver=/usr/local/Cellar/selenium-server-standalone/drivers/chromedriver</string>
...
```

> If installing via Homebrew, the path to use will be: /usr/local/bin/chromedriver

With that completed, you may now start the Selenium server using `brew services start selenium-server-standalone`.

##### Other Platforms

Follow the standard installation procedure for Selenium server standalone. Ensure that you have the chrome driver
available, and startup the server with the following command:

```sh
java -jar -Dwebdriver.chrome.driver=/path/to/chromedriver /full/path/to/selenium-server-standalone.3.x.x.jar
```

##### Executing Tests

All test suites can be executed by running `bin/codecept run` from the project root. Optionally, you can specify running just the `acceptance`, `functional`, or `unit` test suites by adding one of those words after the `run` command.

### Static Analysis

Mautic uses [PHPSTAN][phpstan] for some of its parts during continuous integration tests. If you want to test your specific contribution locally, install PHPSTAN globally with `composer global require phpstan/phpstan-shim`. 

Mautic cannot have PHPSTAN as its dev dependency, because it requires PHP7+. To run analysis on a specific bundle, run `~/.composer/vendor/phpstan/phpstan-shim/phpstan.phar analyse app/bundles/*Bundle`

[mautic-contributors-agreement]: <https://www.mautic.org/contributor-agreement>

[symfony-coding-standards]: <http://symfony.com/doc/current/contributing/code/standards.html>
[php-cs-fixer]: <https://github.com/friendsofphp/php-cs-fixer>
[php-unit]: <https://phpunit.de/manual/5.7/en/index.html>
[symfony-functional-tests]: <https://symfony.com/doc/2.8/testing.html>
[mautic-docs]: <https://github.com/mautic/documentation>
[developer-docs]: <https://developer.mautic.org/>
[codeception]: <https://codeception.com>
[selenium]: <http://www.seleniumhq.org>
[homebrew]: <https://brew.sh>
[chrome-web-driver]: <https://sites.google.com/a/chromium.org/chromedriver/downloads>
[phpstan]: <https://github.com/phpstan/phpstan>
[open-issues-github]: <https://github.com/mautic/mautic/issues?q=is%3Aopen+>
[roadmap]: <https://forum.mautic.org/t/mautic-roadmap-discussion/13760>
[feature-requests]: <https://forum.mautic.org/c/ideas/14/l/latest?order=votes>
[create-feature-request]: <https://forum.mautic.org/c/ideas/14/l/latest?order=votes>
[contributor-agreement]: <https://www.mautic.org/contributor-agreement>
[local-environment-setup]: </contributing-to-mautic/developer/local-environment-setup>
[github-join]: <https://github.com/join>
[symfony-coding-standards]: <http://symfony.com/doc/current/contributing/code/standards.html>
[semver]: <https://semver.org/>
[product-team]: <https://contribute.mautic.org/product-team>
[example-migration]: <https://github.com/mautic/mautic/pull/8134/files>
[doctrine-migrations-docs]: <https://www.doctrine-project.org/projects/doctrine-migrations/en/2.1/index.html>
