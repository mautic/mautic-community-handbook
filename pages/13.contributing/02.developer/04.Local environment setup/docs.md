---
title: Local environment setup
slug: local-environment-setup
taxonomy:
    category:
        - docs
---

## Setting up your local environment
---

This page will guide you through setting up your local environment to use and develop for Mautic.

## Development / build process requirements

>>>>>> We recommend working with [DDEV][mautic-ddev] since it includes almost all required software out of the box (PHP, Composer, MySQL) and has some handy features like MailHog, PHPMyAdmin, dynamic PHP version switching and much more. Mautic-specific installation instructions for DDEV can be found [here][mautic-ddev].

1. Mautic uses Git as a version control system. Download and install git for your OS from [https://git-scm.com/][git].
2. Install a server, PHP and MySql to be able to run Mautic locally. You can use [DDEV][mautic-ddev] (recommended) or an [AMP package for your OS][amp-packages].
3. Install [Composer][composer], the dependency manager for PHP.
4. Install [NPM][npm].
5. Install [Grunt][grunt].
6. Install [GitHub CLI][github-cli]

## Mautic requirements

1. See [Mautic requirements][mautic-requirements].
2. PHP modules (already included in DDEV and most AMP packages):
	- required: `zip`, `xml`, `mcrypt`, `imap`, `mailparse`
	- recommended: `openssl`, `opcache` / `apcu` / `memcached`
	- recommended for development: `xdebug`
3. Recommended memory limit: minimally 256 MB for testing, 512 MB and more for production.
4. Recommended MySQL defaults can be set by running the queries `SET GLOBAL innodb_default_row_format=DYNAMIC; SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));`

## Installation

1. Open a Terminal/Console window.
2. Change directory to the server root (i.e. `cd /var/www` if your local server root is at /var/www).
3. Clone the repository (`gh repo clone mautic/mautic`)
4. The **mautic** directory should appear in the server root. Change directory to mautic directory (`cd mautic`).
5. Install dependencies (`composer install`) if you are not using DDEV. If you're using DDEV, type `ddev start`.
6. Visit Mautic in a browser (probably at http://localhost/mautic site) and follow installation steps.
7. If you're using DDEV, allow Mautic to be set up by the installer, then access the instance at https://mautic.ddev.

## Keeping Up-To-Date

### Source Files

Each time you update Mautic's source after the initial setup/installation via a new checkout, download, git pull, etc; you will need to clear the cache. To do so, run the following command:
```bash
	$ cd /your/mautic/directory

	$ php bin/console cache:clear
```
(Note that if you are accessing Mautic through the dev environment (via index_dev.php), you would need to add `--env=dev` to the command).

### Vendors

Run `composer install` to ensure new vendors are installed and/or existing upgraded.

### Database Schema

Before running these commands, please make a backup of your database.

If updating from [a tagged release][tagged-releases] to a tagged release, schema changes will be included in a migrations file. To apply the changes, run

    $ php bin/console doctrine:migrations:migrate

If you are updating to the latest source (remember this is alpha), first run

    $ php bin/console doctrine:schema:update --dump-sql

This will list out the queries Doctrine wants to execute in order to get the schema up-to-date (no queries are actually executed). Review the queries to ensure there is nothing detrimental to your data. 

If you're satisfied with the queries, execute them with

    $ php bin/console doctrine:schema:update --force

Your schema should now be up-to-date with the source.

## Development environment

Mautic downloaded from GitHub has the development environment. You can access it by adding `index_dev.php` after the Mautic URL. Eg. `http://localhost/mautic/index_dev.php/s/`. Or in case of CLI commands, add `--env=dev` attribute to it.

This development environment will display the PHP errors, warnings and notices directly as the output, so you don't have to open the log to see them. It will also load, for example, translations without cache, so every change you make will be visible without clearing it. The only changes which require clearing the cache are in the `config.php` files.

In case of assets like JS, CSS, the source files are loaded instead of concatenated, minified files. This way the changes in those files will be directly visible on refresh. If you'd wanted to see the change in the production environment, you'd have to have run the `bin/console mautic:assets:generate` command.

In many cases, the CSS files are built from LESS files. To compile the changes in the LESS files, run `grunt compile-less` command.

[mautic-requirements]: <https://www.mautic.org/download/requirements>
[amp-packages]: <https://en.wikipedia.org/wiki/List_of_Apache%E2%80%93MySQL%E2%80%93PHP_packages>
[composer]: <https://getcomposer.org/>
[npm]: <https://www.npmjs.com/>
[grunt]: <http://gruntjs.com/>
[tagged-releases]: <https://github.com/mautic/mautic/releases>
[mautic-ddev]: <https://www.mautic.org/blog/developer/local-mautic-development-with-ddev>
[git]: <https://git-scm.com/>
[github-cli]: <https://cli.github.com>