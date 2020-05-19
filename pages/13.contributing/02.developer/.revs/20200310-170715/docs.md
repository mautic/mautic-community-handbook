---
title: Developer
---

---
## Contributing Code

Development is open and available to any member of the Mautic community. All fixes and improvements are done through pull requests to the code. This code is open source and publicly available. 

## Reporting Security Vulnerabilities

If you think that you have found a security vulnerability, please email [security@mautic.org](mailto:security@mautic.org) with as much detail as possible. The core team will review the vulnerability and if found applicable, will create the patch in a private repository. The vulnerability will be disclosed once the patch has been included into a release. 

## Developer Documentation

Developer documentation is available at [https://developer.mautic.org](https://developer.mautic.org).  To add additions or corrects to the documentation, submit Issues or Pull Requests against [https://github.com/mautic/developer-documentation](https://github.com/mautic/developer-documentation).

## Core Feature Development Procedures

Pull Requests with additional features should be created with the Mautic Product Roadmap goals in consideration. Any features that are created for core that don’t follow the overall goals of the project may not be included. 

In addition to following the general direction of the development goals, the pull request code must be well-formed following coding standards and guidelines. If you wish to target a specific release version number for the feature, its best to make the pull request early so any feedback from the core team can be implemented and adequate testing can be performed. 

Features that are determined not to fit within the direction of the Mautic Core goals are more than welcome to be created as plugins instead. 

## Code Contribution Requirements

### Code Standards

Mautic follows [Symfony's coding standards](http://symfony.com/doc/current/contributing/code/standards.html) by implementing pre-commit git hook running [php-cs-fixer](https://github.com/friendsofphp/php-cs-fixer), which is installed and updated with `composer install`/`composer update`.

All code styling is handled automatically by the aforementioned git hook. If you setup git hook correctly (which is true if you ever run `composer install`/`composer update` before creating a pull request), you can format your code as you like - it will be converted to Mautic code style automatically.

### Automated Tests

All code contributions should include adequate and appropriate unit tests using [PHPUnit](https://phpunit.de/manual/5.7/en/index.html) and/or Symfony functional tests ([https://symfony.com/doc/2.8/testing.html](https://symfony.com/doc/2.8/testing.html)). Pull Requests without these tests will not be merged. See below for more extensive information on Automated Tests.

### Pull Request Description 

When creating a new Pull Request, the description template should be filled appropriately in detail. Any Pull Request that does not have an appropriate description will not be considered for merge. 

### Documentation 

Each new feature should include a reference to a pull request in our [End User Documentation](https://github.com/mautic/documentation) repository or [Developer Documentation](https://github.com/mautic/developer-documentation) repository if applicable.  Any enhancements or bugfixes affecting the end-user or developer experience should also be accompanied by a PR updating the relevant resources in the Documentation.

## Development / Build process requirements

1. Mautic uses Git as a version control system. Download and install git for your OS from https://git-scm.com/.
2. Install a server, PHP and MySql to be able to run Mautic locally. A quick way to get set up is [AMP package for your OS](https://en.wikipedia.org/wiki/List_of_Apache%E2%80%93MySQL%E2%80%93PHP_packages).
3. Install [Composer](https://getcomposer.org/), the dependency manager for PHP.
4. Install [NPM](https://www.npmjs.com/).
5. Install [Grunt](http://gruntjs.com/).

## Mautic requirements

1. See [Mautic requirements](https://www.mautic.org/download/requirements).
2. PHP modules:
	- required: `zip`, `xml`, `mcrypt`, `imap`, `mailparse`
	- recommended: `openssl`, `opcache` / `apcu` / `memcached`
	- recommended for development: `xdebug`
3. Recommended memory limit: minimally 256 MB for testing, 512 MB and more for production.
4. Recommended MySQL defaults can be set by running the queries `SET GLOBAL innodb_default_row_format=DYNAMIC; SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));`

## Installation

1. Open a Terminal/Console window.
2. Change directory to the server root (i.e. `cd /var/www` if your local server root is at /var/www).
3. Clone the repository (`git clone https://github.com/mautic/mautic.git`)
4. The **mautic** directory should appear in the server root. Change directory to mautic directory (`cd mautic`).
5. Install dependencies (`composer install`).
6. Visit Mautic in a browser (probably at http://localhost/mautic) and follow installation steps.

## Keeping Up-To-Date

### Source Files

Each time you update Mautic's source after the initial setup/installation via a new checkout, download, git pull, etc; you will need to clear the cache. To do so, run the following command:

	$ cd /your/mautic/directory

	$ php app/console cache:clear

(Note that if you are accessing Mautic through the dev environment (via index_dev.php), you would need to add `--env=dev` to the command).

### Vendors

Run `composer install` to ensure new vendors are installed and/or existing upgraded.

### Database Schema

Before running these commands, please make a backup of your database.

If updating from <a href="https://github.com/mautic/mautic/releases">a tagged release</a> to <a href="https://github.com/mautic/mautic/releases">a tagged release</a>, schema changes will be included in a migrations file. To apply the changes, run

    $ php app/console doctrine:migrations:migrate

If you are updating to the latest source (remember this is alpha), first run

    $ php app/console doctrine:schema:update --dump-sql

This will list out the queries Doctrine wants to execute in order to get the schema up-to-date (no queries are actually executed). Review the queries to ensure there is nothing detrimental to your data. If you have doubts about a query, submit an issue here and we'll verify it.

If you're satisfied with the queries, execute them with

    $ php app/console doctrine:schema:update --force

Your schema should now be up-to-date with the source.

## Development environment

Mautic downloaded from GitHub has the development environment. You can access it by adding `index_dev.php` after the Mautic URL. Eg. `http://localhost/mautic/index_dev.php/s/`. Or in case of CLI commands, add `--env=dev` attribute to it.

This development environment will display the PHP errors, warnings and notices directly as the output so you don't have to open the log to see them. It will also load for example translations without cache, so every change you make will be visible without clearing it. The only changes which require clearing the cache are in the `config.php` files.

In case of assets like JS, CSS, the source files are loaded instead of concatenated, minified files. This way the changes in those files will be directly visible on refresh. If you'd wanted to see the change in the production environment, you'd have to have run the `app/console mautic:assets:generate` command.

In many cases, the CSS files are built from LESS files. To compile the changes in the LESS files, run `grunt compile-less` command.

## Testing

### Pull Request Testing

Everyone can test submitted features and bug fixes. No programming skills are required. All you have to do is to follow the steps below.

Every change to Mautic core happens via PRs. Every PR must have 2 successful tests to be merged to the core and released in the next version. Testing a PR is a great way to move Mautic forward and personally improve its quality and stability.

1. [Select a PR](https://github.com/mautic/mautic/pulls) to test.
2. Read the description and steps to test. If it's a bug fix, follow the steps to ensure you can recreate the issue.
3. Use the development environment (above) for testing.
3. [Apply the PR](https://help.github.com/articles/checking-out-pull-requests-locally/#modifying-an-inactive-pull-request-locally)
4. Clear cache for development environment (`rm -rf app/cache/*` or `app/console cache:clear -e dev`).
5. Follow the steps from the PR description again to see if the result is as described.
6. Write a comment about how the test went. If there is a problem, provide as much information as possible including error log messages.

### Automated Testing

Mautic uses [Codeception](https://codeception.com), [PHPUnit](https://phpunit.de), and [Selenium](http://www.seleniumhq.org)
as our suite of testing tools. 

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

If you're on a Mac and you use [Homebrew](https://brew.sh), you can install Selenium by running `brew install selenium-server-standalone`.

You'll also need to download the latest [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).

Unzip and move the `chromedriver` file to `/usr/local/Cellar/selenium-server-standalone/drivers/chromedriver`.

Once you have Selenium installed and the WebDriver available at the specified location, open and modify the plist file found at `/usr/local/Cellar/selenium-server-standalone/3.5.3/homebrew.mxcl.selenium-server-standalone.plist`.

In the `<dict><array>` block under `ProgramArguments`, add the following after the line containing `<string>-jar</string>`"

```xml
...
<string>-Dwebdriver.chrome.driver=/usr/local/Cellar/selenium-server-standalone/drivers/chromedriver</string>
...
```

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

Mautic uses [PHPSTAN](https://github.com/phpstan/phpstan) for some of its parts during continuous integration tests. If you want to test your specific contribution locally, install PHPSTAN globally with `composer global require phpstan/phpstan-shim`. 

Mautic cannot have PHPSTAN as its dev dependency, because it requires PHP7+. To run analysis on a specific bundle, run `~/.composer/vendor/phpstan/phpstan-shim/phpstan.phar analyse app/bundles/*Bundle`