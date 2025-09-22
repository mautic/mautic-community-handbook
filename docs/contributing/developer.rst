Developer
#########

Mautic development is open to all members of the Mautic community. The codebase is open source and publicly accessible.

There are various ways to contribute to Mautic as a developer, depending on your interests and how your skills align with current projects.

You might want to consider the following areas:

* Find and fix bugs
* Test bug fixes and features
* Review code for bug fixes and features
* Write and improve automated tests
* Work on Strategic Initiatives to bring new features to Mautic
* Join a Tiger Team to focus on a particular area of Mautic
* Create demo applications and plugins to encourage developers to work with Mautic
* Write and improve the :xref:`User Documentation` and :xref:`Developer Docs`
* Write technical articles for the Mautic Community :xref:`Mautic Community blog`

The following sections provide more information on contributing to Mautic as a developer.

----

Bugs and security vulnerabilities
*********************************

If you encounter a bug or find a security vulnerability, please report it to help improve Mautic for everyone.

Bugs
====

Reporting a bug
---------------

Before submitting a bug:

* Make sure there are no problems with your local installation, such as permission problems, outdated cache, etc. Please refer to Mautic's :xref:`Mautic troubleshooting` guide for assistance.
* If you're unsure whether the problem is a bug, please ask for help first in the :xref:`Mautic Community Forums`.

When you are confident that the problem is a bug, please create :xref:`GitHub create an issue` and provide as many details as possible, such as reproduction steps, Mautic/PHP versions, etc.

Providing step-by-step instructions for reproducing a bug is extremely important because the person who reviews your issue might not be a developer.

Fixing a bug
------------

If you're able to fix a bug, whether you discovered it or something reported by someone in the community, please make a pull request - PR - by following the instructions on the :ref:`Pull requests` section.

Reporting a security vulnerability
==================================

Please read the :xref:`Mautic security team` page for complete information about security issues and how to report them.

Pull requests
*************

It's highly appreciated when developers help Mautic by providing pull requests - PRs - against the Mautic code base. To make this process as smooth as possible for everyone, you must thoroughly follow the instructions.

.. contents::
  :local:
  :depth: 2

Step 1: review existing issues and PRs
======================================

Before working on a change, review the existing issues and PRs to see if someone else raised the same topic or maybe even started working on one by searching :xref:`Mautic open issues list` on GitHub. You can also ask in the :xref:`Mautic product team Slack`.

Step 2: review Mautic's roadmap & feature requests
==================================================

.. note::

   You can skip this section if you're not planning to build a new feature.

First, please keep in mind that many people are requesting new features. Therefore, the Core Team can only add a limited number of features to new releases.

If you'd like to propose a new feature, please review the :xref:`Mautic Roadmap` and the :xref:`Mautic Forums ideas and features request` topic category in the Mautic Forums to see if someone else has already suggested similar features and/or is already working on it. If you don't see any similar requested feature, you can suggest it in the Forums.

When there is enough interest, you can officially propose it on the :xref:`Mautic new features proposal` page so the Community can discuss them. You can then track if it's accepted or rejected on the :xref:`Mautic new features progress tracker` page.

Features that don't fit within the direction of the Mautic Core goals are more than welcome as third-party Plugins instead. 

Step 3: set up your local environment
=====================================

Get the Mautic source code
--------------------------

* Create a :xref:`GitHub signup` account and sign in
* Fork the Mautic repository by clicking the "Fork" button
* After the forking process has completed, clone your fork locally using the following command:

  .. code-block:: bash

      git clone https://github.com/USERNAME/mautic.git

  .. vale off

  Or, you can :xref:`install GitHub CLI` and run:

  .. vale on

  .. code-block:: bash

      gh repo clone mautic/mautic

  Cloning your fork creates a ``mautic`` directory in your local machine.

Install the software stack
--------------------------

Please see the instructions in the :ref:`Local environment setup` for installing the software stack.

Choose the right branch
-----------------------

Before working on a PR, you must determine the base branch for your work. Mautic follows :xref:`Semver`, best illustrated by the below example.

Assuming that:

``a`` = current major release - for example, ``4`` in ``4.4.5``

``b`` = current minor release - for example, ``4.4`` in ``4.4.5``

``c`` = future major release - for example, ``5`` in ``5.0``

.. vale off

* All PRs are made against the ``c.x`` branch in the first instance, for instance, ``5.x``.
* If the PR should be merged in an earlier release than the next major release of Mautic, duplicate the PR against the relevant ``a.b`` branch for bug fixes - for example, ``5.0`` - or ``a.x`` branch for features and enhancements - for example, ``5.x``.
* Backwards compatibility breaking changes can only be released in a major version, so they should only ever be made against the ``c.x`` branch, such as, ``5.x``.

The exception to this rule is if the last feature release - for example, ``5.4`` - has already been made, all features would be made against the ``c.x`` branch - for example, ``6.x`` rather than the ``5.x`` branch. This is usually made clear in release notes, but if you're unsure, please ask in :xref:`Mautic product team Slack`.

.. vale on

As an example, if Mautic just released a ``4.0.0`` version of Mautic, the following would apply:

.. list-table::
    :header-rows: 1

    * - Mautic version
      - Breaking changes/features allowed?
      - New features/enhancements allowed?
      - Bug fixes allowed?
    * - 4.0.1
      - ❌
      - ❌
      - ✅
    * - 4.1.0
      - ❌
      - ✅
      - ✅
    * - 5.0.0
      - ✅
      - ✅
      - ✅

The information below can help you determine which branch you need to choose as your base branch:

* ``4.4``, if you fix a bug and want your fix included in a ``4.4.x`` release of Mautic. You must also create a duplicate PR for the ``5.x`` branch.
* ``4.x``, if you add a new feature or enhance an existing one to include in a version of Mautic ``4``, the current major release.
* ``5.x``, if you add a new feature or enhance an existing one that breaks backward compatibility, to include in the next major version of Mautic, Mautic ``5``.

Create a topic branch
---------------------

A topic branch is a short-lived branch that you use when working on a single topic, such as a bug fix, a new feature, etc. Each time you want to work on a PR for a bug or on an enhancement, create a topic branch from the relevant base branch by running:

.. code-block:: bash

    git checkout -b BRANCH_NAME 5.x

Or, if you want to provide a bug fix for the ``5.0`` branch, first track the remote ``5.0`` branch locally:

.. code-block:: bash

    git checkout -t origin/5.0

Then, create a new branch from the ``5.0`` branch to work on the bug fix:

.. code-block:: bash

    git checkout -b BRANCH_NAME 5.0

.. vale off

.. tip::

   Use a descriptive name for your branch. For example, ``issue_XXX`` is a good convention for bug fixes. Replace the 'XXX' with the issue number.

.. vale on

The mentioned ``checkout`` command automatically brings you to the newly created branch. Don't forget to verify the branch you are working on with ``git branch``.

Step 4: work on changes
=======================

Work on the code as much as you want and commit as much as you want, but keep in mind the following:

.. vale off

* Mautic follows :xref:`Symfony coding standards` by implementing a pre-commit git hook that runs :xref:`PHP-cs-fixer`. When you install or update Mautic using Composer with the commands ``composer install`` and ``composer update``, it installs the git hook. This git hook automatically handles all code styling, so you don't need to worry about anything besides working on your code.
* Add unit tests to confirm the bug is fixed or the new feature works.

.. vale on

Backward compatibility breaks
-----------------------------

Try not to break backward compatibility - BC. If you must do so, please provide a compatibility layer to support the old way. PRs that break BC have less chance of acceptance, as they must wait for a major release.

.. vale off

What is BC break?
~~~~~~~~~~~~~~~~~

.. vale on

BC break is any change that may break a Plugin, either by using or extending a class. Given that Mautic has a Plugin ecosystem, it's important to consider the impact, even on code that may not be directly used.

Examples:

* Remove or rename a public or protected method in a non-final class. Create a new method instead and mark the old one :doc:`deprecated </governance/deprecation_policy>`.
* Change the signature of a private or public method in a non-final class. This means adding/removing method parameters or adding/changing parameters or return types. Create a new method instead and mark the old one :doc:`deprecated </governance/deprecation_policy>`.
* Change the behavior of a method so it does something differently.
* Add a new method to an existing interface. Create a new interface instead.
* Whenever you change a :xref:`Symfony Twig` template, think about the Themes that are overwriting this template. For instance, changing the template name can cause issues.

.. vale off

What is not considered a BC break?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. vale on

Changing the constructor of a PHP service isn't considered a BC break. Services are autowired, so there is no harm in changing the dependencies.

.. vale off

Write your code with BC breaks in mind
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. vale on

Think about the BC breaks as you write a new code.

* Make new classes final by default. Only remove the final keyword if there is a good reason for it.
* Make a new method private by default. Make it public only if you need to use it outside of the class.
* Prefer composition over inheritance. This way, you can use final classes.
* A unit test isn't a good reason why a class shouldn't be final. For example, get the final service from the container instead of mocking it. You don't need to mock it if it's a final Data Transfer Object - DTO.

Step 5: are migrations needed?
==============================

Sometimes, a PR needs a migration. An example is when updating a country's regions. 

Say a region contains a typo, where ``Colmbra`` should be ``Coimbra``. What if the Mautic instance already has values in the database with the old value ``Colmbra``? 

That's where migrations come in handy because every time a User updates their Mautic instance, migrations run automatically.

.. note::

   You can skip the instructions below if you don't need migrations in your PR.

To create a migration, you can follow these steps:

#. Run ``bin/console doctrine:migrations:generate`` in your terminal. Doctrine generates a new migration file for you.

#. Open the file by following the path in your terminal after running the generate command. In this file, you should see two functions, ``preUp()`` and ``up()``:

   * ``preUp()`` allows you to define scenarios where the migration should or shouldn't run. For example, only when a certain database table exists.

   * ``up()`` runs the actual migration and allows you to make changes in Mautic's database. You can either take inspiration from other migrations in the ``app/migrations`` folder or learn more about migrations in the :xref:`Doctrine docs`.

#. When you're done, test your migrations by running ``migrations:execute --up VERSION``.

#. If all looks good, roll back your changes with ``migrations:execute --down VERSION``.

.. tip::

   You can find an example of migration scenario and code on :xref:`github_pr_8134`.

Step 6: prepare PR for submission
=================================

You're almost ready to submit your PR. There are three things you still need to look into:

#. Code standards
#. Developer documentation
#. Writing tests

To keep Mautic stable and easy to maintain, applying the appropriate code standards and writing automated tests is a hard requirement. Mautic can't accept features and/or enhancements without proper tests, as it would impact its stability. Why? When you try to build something in a specific part of Mautic, you might accidentally break another part of Mautic. With automated tests, which cover most aspects of Mautic, it's possible to prevent this as much as possible.

Code standards
--------------

Mautic follows Symfony's :xref:`Symfony coding standards` by implementing a pre-commit git hook that runs :xref:`PHP-cs-fixer`. When you install or update Mautic using Composer with the commands ``composer install`` and ``composer update``, it automatically installs the git hook. This git hook automatically deals with any code styling. You can format your code as you like, and then the git hook automatically converts it to Mautic's code style.

.. vale off

Developer Documentation
-----------------------

.. vale on

Each new feature should include a reference to a PR in the :xref:`Developer Docs GitHub`, if applicable. Any enhancements or bug fixes affecting the end-user or developer experience should have a PR mentioned in the description, which updates the relevant resources in the documentation.

Writing tests
-------------

.. vale off

All code contributions - especially enhancements/features - should include adequate and appropriate unit tests using :xref:`PHPUnit` and/or :xref:`Symfony functional tests`. The Core Team won't merge PRs without these tests. See the :ref:`Automated testing` section for more extensive information.

.. vale on

Step 7: submit a PR
===================

Update branch with rebase
-------------------------

Before submitting your PR, you need to update your branch:

.. code-block:: bash

    git checkout 4.x
    git fetch upstream
    git merge upstream/4.x
    git checkout BRANCH_NAME
    git rebase 4.x

.. attention::

     Replace ``4.x`` with the branch you selected previously. For example, ``4.4`` if you are fixing a bug.

When executing the ``rebase`` command, you might have to fix merge conflicts. Running ``git status`` can show you the un-merged files. Resolve all the conflicts, then continue the rebase:

.. code-block:: bash

    git add ... # add resolved files
    git rebase --continue

Check that all tests still pass and push your branch remotely:

.. code-block:: bash

    git push --force origin BRANCH_NAME

Sometimes, if there are a lot of merge conflicts, it can be easier to re-create your PR on an updated version of the branch, especially if you aren't confident in correctly resolving the conflicts. Please ask for help in :xref:`Mautic product team Slack` if you are struggling with PR rebase.

.. vale off

Make a PR
---------

.. vale on

You can now make a PR on the :xref:`Mautic GitHub repository`.

.. note::

   Take care to point your PR towards ``mautic:4.0`` if you want the Core Team to pull a bug fix based on the ``4.0`` branch.

To ease the Core Team work, always include what you have modified in your PR message and provide steps to test your fix or feature. Keep in mind that not all testers have a thorough knowledge of Mautic's features, nor are they all likely to be developers. Therefore, clear testing steps are crucial.

Step 8: receiving feedback
==========================

All contributors need to follow some best practices to ensure a constructive feedback process.

If you think someone fails to keep this advice in mind and want another perspective, please request a review of the feedback in the ``#dev`` channel on :xref:`Mautic Community Slack`.

The :xref:`Mautic Product Team` decides which PRs get merged, so their feedback is the most relevant. Please don't feel pressured to refactor your code immediately when someone provides feedback and wait for the Product Team to review it.

.. vale off

Rework PR
---------

.. vale on

Based on the feedback on your PR, you might need to make some changes. Before re-submitting the PR, rebase with ``upstream/4.x`` or ``upstream/4.4`` as appropriate - but *don't merge* - and force the push to the origin:

.. code-block:: bash

    git rebase -f upstream/4.x
    git push --force origin BRANCH_NAME

.. caution::

   If you want to do a ``push --force``, don't forget to **specify the branch name explicitly** to avoid breaking other branches. Always use the option ``--force`` with caution as it overwrites the remote history and can lead to data loss.

Step 9: testing
===============

.. vale off

PR testing
----------

.. vale on

If you want to test a PR from other developers, see the :ref:`PR review process` section. All PRs require testing by others in the Community and must have the code reviewed by a member of the Core Team. Read more information in the :doc:`/governance/code_governance` section.

Automated testing
-----------------

Mautic uses :xref:`PHPUnit`, :xref:`Selenium`, and :xref:`Codeception` as the suite of testing tools.

PHPUnit
~~~~~~~

Before executing unit tests, copy the ``.env.dist`` file to ``.env`` then update to reflect your local environment configuration.

.. warning::

   Running functional tests without setting the ``.env`` file with a different database results in the configured database being overwritten.

To run the entire test suite:

.. code-block:: bash

    bin/phpunit --bootstrap vendor/autoload.php --configuration app/phpunit.xml.dist

To run tests for a specific bundle:

.. code-block:: bash

    bin/phpunit --bootstrap vendor/autoload.php --configuration app/phpunit.xml.dist --filter EmailBundle

To run a specific test:

.. code-block:: bash

    bin/phpunit --bootstrap vendor/autoload.php --configuration app/phpunit.xml.dist --filter "/::testVariantEmailWeightsAreAppropriateForMultipleContacts( .*)?$/" Mautic\EmailBundle\Tests\EmailModelTest app/bundles/EmailBundle/Tests/Model/EmailModelTest.php

Codeception
~~~~~~~~~~~

Before executing the end to end test suite:

#. Build test dependencies:

   .. code-block:: bash

      bin/codecept build

#. Edit ``.env.local`` to set the environment to test mode:

   .. code-block:: php

      # .env.local
      APP_ENV=test
      APP_DEBUG=1

#. Run the test:

   * To run the entire test suite:

     .. code-block:: bash

         bin/codecept run acceptance

   * To run tests for a specific bundle:

     .. code-block:: bash

         bin/codecept run acceptance ContactManagementCest

   * To run a specific test:

     .. code-block:: bash

         bin/codecept run acceptance ContactManagementCest:createContactFromForm

For more detailed steps on writing and running tests, please refer to the Mautic's :xref:`Mautic e2e test suite` documentation.

Static analysis
---------------

Mautic uses :xref:`PHPSTAN` for some of its parts during continuous integration tests. To test your specific contribution locally, install PHPSTAN globally with ``composer global require phpstan/phpstan-shim``.

Mautic can't have PHPSTAN as its devDependency because it requires PHP7+. To execute analysis on a specific bundle, run ``~/.composer/vendor/phpstan/phpstan-shim/phpstan.phar analyse app/bundles/*Bundle``.

.. attention::

   If you've added a new feature or changed any UI to Mautic, please add it to the :xref:`Developer Docs` and/or :xref:`User Documentation`.

   Read the :doc:`/contributing/contributing_docs_rst` section to work with all documentation.

.. vale off

Issues and PRs review
*********************

.. vale on

Issues and PRs reviewers are the backbone of Mautic's success. Anyone familiar with Mautic and PHP is welcome to triage bug reports and review PRs. You don't need to be an expert to help.

If you don't feel ready to contribute code or patches, reviewing issues and PRs can be a great start to getting involved and giving back.

Why reviewing is important
==========================

There are significantly more PRs and bug reports than members of the Mautic Core Team available to review, fix, and merge them. Community reviews are essential to ensure that reported bugs are happening and that new features and fixes are working as expected and not introducing new problems.

Things to pay attention to when you triage an issue or review a PR:

* **Bug Reports**: ensure the accuracy and completeness of the issue. Can you reproduce the bug? Is any important information missing?
* **PRs**: ensure that the bug fixes or new enhancements are implemented correctly and covered by test cases - that new bugs aren't introduced and that backward compatibility is maintained.

.. note::

   Before you start, remember that you are reviewing the results of someone's hard work. A good review comment should express appreciation for the contributor's effort, acknowledge what they did well, point out areas for improvement, and suggest a next step.

Review processes
================

.. important::

   Mautic uses :xref:`GitHub` to manage bug reports and PRs. You must have an account and log in to do reviews.

Bug report review process
-------------------------

If you'd like to help triage an issue, explore the :xref:`Mautic open issues list` in the Mautic repository to find new issues.

Here are the steps to triage a bug report:

#. **Is the report complete?**

   Good bug reports contain enough information, such as a detailed description of the bug, how to reproduce it, and environment details, for example, Mautic version, operation system - OS, etc. It may sometimes include code samples and screenshots or screen recordings.

   Issue forms ensure the basic information set, but sometimes, this may not be enough to reproduce the issue. If you aren't sure, ask for clarification.

#. **Reproduce the bug**

   You can :ref:`set up your local environment<Local environment setup>` and test whether you can reproduce the bug on your system. If the reporter didn't provide enough information, ask for clarification.

#. **Leave a comment**

   At last, add a comment to the bug report. Thank the reporter for reporting the bug. Here is an example:

   ::

    Thank you for creating this bug report, @mautibot. I could reproduce the bug on my end.
    Please let me know if you'd like to work on it.

.. vale off

PR review process
-----------------

.. vale on

Every change to Mautic happens via PRs. Every PR must have a number of successful tests and code reviews to be merged to the core and released in the next version - the number required depends on the :doc:`tier of the PR </governance/code_governance>`. Testing a PR is a great way to move Mautic forward and personally improve its quality and stability.

Here are the steps to review a PR:

.. vale off

#. :ref:`Set up your local environment<Local environment setup>` to test PRs locally.
#. Find a :xref:`Mautic PRs` to test. You can also seek PRs with the label :xref:`Mautic ready-to-test issue label`.
#. Read the description and steps to test. If it's a bug fix, follow the steps to ensure you can recreate the issue.
#. Pull the PR to your local machine to use the development environment for testing.

   To do this, follow the instructions at the :xref:`Checking out pull requests locally` section on GitHub Docs or, if you're using GitHub CLI, run the ``gh pr checkout <number>`` command.

#. Clear cache for the development environment by running the ``rm -rf var/cache/*`` or ``bin/console cache:clear -e dev`` command.
#. Follow the steps from the PR description again to see if the result is exactly as described.
#. Submit a review in the PR - see :xref:`Submitting your review` section on GitHub Docs. If there is a problem, provide as much information as possible, including error log messages.

.. vale on

.. note::

   The Education Team plans to provide more thorough guidelines about bug reports triage and PRs review in the near future.

Local environment setup
***********************

This page guides you through setting up your local environment to use and develop Mautic.

.. contents::
  :local:
  :depth: 2

Development/build process requirements
======================================

.. tip::

   Working with :xref:`DDEV` is recommended, since it includes almost all required software out of the box - PHP, Composer, MySQL - and has some handy features like MailHog, PHPMyAdmin, dynamic PHP version switching, and much more.

   You can find Mautic-specific installation instructions for DDEV in the :xref:`Local Mautic development with DDEV` blog post.

.. vale off

#. Mautic uses Git as a version control system. Download and install :xref:`Git` for your OS
#. Install a server, PHP, and MySQL to run Mautic locally. Read :xref:`Local Mautic development with DDEV` blog post to use DDEV or use :xref:`AMP software bundle` packages for your OS
#. Install :xref:`Composer`, the dependency manager for PHP
#. Install :xref:`npm`
#. Install :xref:`Grunt`
#. Install :xref:`GitHub CLI`

.. vale on

Mautic requirements
===================

#. See the :xref:`Mautic requirements` page for details of the required PHP version, PHP extensions, database, and web servers
#. PHP modules - already included in DDEV and most AMP packages:

   * required: ``zip``, ``xml``, ``mcrypt``, ``imap``, ``mailparse``
   * recommended: ``openssl``, ``opcache`` / ``apcu`` / ``memcached``
   * recommended for development: ``xdebug``

#. Recommended memory limit: minimal 256 MB for testing and 512 MB or more for production
#. Recommended MySQL defaults. Set it by running: 

   .. code-block:: bash

      SET GLOBAL innodb_default_row_format=DYNAMIC; SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));


Installation
============

#. Open a terminal/console window
#. Change directory to the server root. For example, ``cd /var/www`` if your local server root is at ``/var/www``
#. Clone the repository by running ``gh repo clone mautic/mautic``
#. Change directory to ``mautic`` by running ``cd mautic``
#. Install dependencies with ``composer install``. If you're using DDEV, run ``ddev start``
#. Open Mautic in a browser - probably at ``http://localhost/mautic`` - and follow the installation steps. If you're using DDEV, the installer sets up Mautic for you. Then you can access the instance at ``https://mautic.ddev``

Keeping up-to-date
==================

Source files
------------

Each time you update Mautic's source after the initial setup/installation via a new checkout, download, git pull, etc., you need to clear the cache. To do so, run the following command:

 .. code-block:: bash

	$ cd /your/mautic/directory

	$ php bin/console cache:clear

.. note::

   If you're accessing Mautic through the development environment via ``index_dev.php``, you must add ``--env=dev`` to the PHP command above.

Vendors
-------

Run ``composer install`` to install new vendors and upgrade the existing ones.

.. vale off

Database Schema
---------------

.. vale on

.. important::

   Before running these commands, please make a backup of your database.

Updating from a :xref:`Mautic tagged releases` to a tagged release includes Schema changes in a migrations file. To apply the changes, run:

.. code-block:: php

	$ php bin/console doctrine:migrations:migrate

If you are updating to the latest source - remember, this is alpha - first run:

.. code-block:: php

    $ php bin/console doctrine:schema:update --dump-sql

This list out the queries Doctrine wants to execute to get the schema up-to-date. No queries are actually executed. Review the queries to ensure there is nothing detrimental to your data.

If you're satisfied with the queries, execute them with:

.. code-block:: php

    $ php bin/console doctrine:schema:update --force

Your schema should now be up-to-date with the source.

Development environment
=======================

Mautic downloaded from GitHub has the development environment. You can access it by adding ``index_dev.php`` after the Mautic URL. For example, ``http://localhost/mautic/index_dev.php/s/``. In case of CLI commands, add ``--env=dev`` attribute to it.

This development environment displays the PHP errors, warnings, and notices directly as the output, so you don't have to open the log to see them. It also loads translations without a cache, so every change you make is visible without clearing it. The only changes which require clearing the cache are in the ``config.php`` files.

.. vale off

Regarding assets like JavaScript and CSS, the source files are loaded instead of concatenated, minified files. This way, the changes in those files will be directly visible when refreshed. If you want to see the change in the production environment, run this command:

.. vale on

.. code-block:: bash

  bin/console mautic:assets:generate

In many cases, LESS files builds the CSS files. Mautic uses Grunt to compile the changes in the LESS files. Follow the below steps:

.. vale off

#. Install the Grunt CLI globally, by running:

   .. code-block:: bash

     npm install -g grunt-cli

#. Go to the Mautic root directory and run:

   .. code-block:: bash

     npm install
     
#. Compile the changes in the LESS files by running: 

   .. code-block:: bash

     grunt compile-less

.. vale on