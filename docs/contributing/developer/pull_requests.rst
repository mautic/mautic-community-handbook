Pull requests
#############

Creating pull requests
**********************

It's highly appreciated when developers help Mautic by providing pull requests - PRs - against the Mautic code base. To make this process as smooth as possible for everyone, you must thoroughly follow the instructions.

Table of contents
*****************

* :ref:`Step 1: review existing issues and pull requests`
* :ref:`Step 2: new feature? Review the roadmap & feature requests`
* :ref:`Step 3: set up your environment (or use Gitpod)`
  
  * :ref:`Install the software stack`
  * :ref:`Get the Mautic source code`

* :ref:`Step 4: work on your pull request`
  
  * :ref:`Choose the right branch`
  * :ref:`Install Mautic`
  * :ref:`Create a topic branch`
  * :ref:`Work on your pull request`

* :ref:`Step 5: migrations needed?`
* :ref:`Step 6: prepare your pull request for submission`
  
  * :ref:`Code standards`
  * :ref:`Documentation`
  * :ref:`Writing tests`

* :ref:`Step 7: submit your pull request`
  
  .. vale off

  * :ref:`Rebase your pull request`
  * :ref:`Make a pull request`

  .. vale on

* :ref:`Step 8: receiving feedback`
  
  * :ref:`Rework your pull request`

* :ref:`Step 9: testing`
  
  * :ref:`Pull request testing`
  * :ref:`Automated testing`
  * :ref:`Static analysis`

Step 1: review existing issues and pull requests
************************************************

Before working on a change, review the existing issues and PRs to see if someone else raised the same topic or maybe even started working on one by searching :xref:`Mautic repository open issues` on GitHub. You can also ask in the :xref:`Mautic product team Slack`.

Step 2: new feature? Review the roadmap & feature requests
**********************************************************

.. note::

    You can skip this section if you're not planning to build a new feature.

First, please keep in mind that many people are requesting new features. Therefore, the Core Team can only add a limited number of features to new releases.

If you'd like to propose a new feature, please review the :xref:`Mautic Roadmap` and the :xref:`Mautic Forums ideas and features request` topic category in the Mautic Forums to see if someone else has already suggested similar features and/or is already working on it. If you don't see any similar requested feature, you can suggest it in the Forums.

When there is enough interest, you can officially propose it on the :xref:`Mautic propose new features` page so the Community can discuss them. You can then track if it's accepted or rejected on the page :xref:`Mautic proposal progress tracker`.

Features that don't fit within the direction of the Mautic Core goals are more than welcome as third-party Plugins instead. 

Step 3: set up your environment (or use Gitpod)
***********************************************

Install the software stack
==========================

Please see the instructions in the :doc:`/contributing/developer/local_environment_setup` to install the software stack.

Get the Mautic source code
==========================

* Create a :xref:`GitHub join` account and sign in
* Fork the Mautic repository by clicking the "Fork" button
* After the forking process has completed, clone your fork locally using the following command:

    .. code-block:: bash

      git clone https://github.com/USERNAME/mautic.git

  Or, if you use the :xref:`GitHub command-line tool`, run:

    .. code-block:: bash

      gh repo clone mautic/mautic

  Cloning your fork creates a ``mautic`` directory in your local machine.

Step 4: work on your pull request
*********************************

Choose the right branch
=======================

Before working on a PR, you must determine which branch you need to work on. Mautic follows :xref:`Semver`, best illustrated by the below example.

Assuming that:

``a`` = current major release (for example, ``4`` in ``4.4.5``)

``b`` = current minor release (for example, ``4.4`` in ``4.4.5``)

``c`` = future major release (for example, ``5`` in ``5.0``)

* All PRs are made against the ``c.x`` branch in the first instance (for example, ``5.x``)
* If the PR should be merged in an earlier release than the next major release of Mautic, duplicate the PR against the relevant ``a.b`` branch for bug fixes (for example, ``5.0``), or ``a.x`` branch for features and enhancements (for example, ``5.x``).
* Backwards compatibility breaking changes can only be released in a major version, so they should only ever be made against the ``c.x`` branch (for example, ``5.x``)

The exception to this rule is if the last feature release (for example, ``5.4``) has already been made, all features would be made against the ``c.x`` branch (for example, ``6.x``) rather than the ``5.x`` branch. This is usually made clear in release notes, but if you're unsure, please ask in :xref:`Mautic product team Slack`.

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

You can determine on which branch to work as follows:

* ``4.4``, if you are fixing a bug and want your bug included in a ``4.4.x`` release of Mautic, you must also create a duplicate PR for the ``5.x`` branch.
* ``4.x``, if you are adding a new feature or enhancing an existing feature to include in a version of Mautic ``4``, which is the current major release.
* ``5.x``, if you are adding a new feature or enhancing an existing feature that breaks backward compatibility, to include in the next major version of Mautic, Mautic ``5``.

Install Mautic
==============

If you are using DDEV, run:

.. code-block:: bash
  
    ddev start

The Mautic installation process automatically happens at the command line, so you only need to wait for it to complete.

If you aren't using DDEV:

* Go into your Mautic folder and install the PHP Composer dependencies:

  .. code-block:: bash

      cd mautic
      composer install

* Open Mautic in your browser, for example, by going to ``http://localhost/mautic`` depending on your environment if you want to install it in the UI. Follow the steps to install :xref:`install Mautic` locally.

Create a topic branch
=====================

Each time you want to work on a PR for a bug or on an enhancement, create a topic branch from the relevant base branch:

.. code-block:: bash

    git checkout -b BRANCH_NAME 5.x

Or, if you want to provide a bug fix for the ``5.0`` branch, first track the remote ``5.0`` branch locally:

.. code-block:: bash

    git checkout -t origin/5.0

Then create a new branch off the ``5.0`` branch to work on the bug fix:

.. code-block:: bash

    git checkout -b BRANCH_NAME 5.0

.. tip::
  
    Use a descriptive name for your branch. For example, "issue_XXX" is a good convention for bug fixes. Replace the "XXX" with the issue number.

The mentioned ``checkout`` command automatically brings you to the newly created branch. Don't forget to verify the branch you are working on with ``git branch``.

Work on your pull request
=========================

Work on the code as much as you want and commit as much as you want, but keep in mind the following:

.. vale off

* Mautic follows Symfony's :xref:`Symfony coding standards` by implementing a pre-commit git hook running :xref:`php-cs-fixer`. Mautic installs and updates this with ``composer install`` and ``composer update``. This handles all code styling automatically.
* Add unit tests to confirm the bug is fixed or the new feature works.

.. vale on

Backward compatibility breaks
==============================

Try not to break backward compatibility - BC. If you must do so, please provide a compatibility layer to support the old way. PRs that break BC have less chance of acceptance, as they must wait for a major release.

.. vale off

What is BC break?
-----------------

Any change that may break a Plugin either using or extending a class. As Mautic has the Plugin ecosystem, we must consider the impact, even on code we might not use ourselves.

.. vale on

Examples:

* Removing or renaming a public or protected method in a non-final class. Create a new method instead and mark the old one :doc:`deprecated </contributing/governance/code-governance/deprecation_policy>`.
* Changing the signature of a private or public method in a non-final class. This means adding or removing method parameters or adding or changing parameters or return types. Create a new method instead and mark the old one deprecated.
* Changing the behavior of a method so it does something differently.
* Adding a new method to an existing interface. Create a new interface instead.
* Whenever you change a :xref:`Symfony Twig` template, think about the Themes that are overwriting this template. For example, changing the template name can cause issues.

.. vale off

What is not considered a BC break?
----------------------------------

.. vale on

Some changes you can make that aren't considered a BC break:

* Changing the constructor of a PHP service. Services are autowired so there is no harm in changing the dependencies.

.. vale off

Write your code with BC breaks in mind
--------------------------------------

.. vale on

Think about the BC breaks as you write a new code.

* Make new classes final by default. Only remove the final keyword if there is a good reason for it.
* Make a new method private by default. Make it public only if you need to use it outside of the class.
* Prefer composition over inheritance. This way you can use final classes.
* A unit test is not a good reason why a class shouldn't be final. For example, get the final service from the container instead of mocking it. If it's a final DTO object then you don't need to mock it at all.

Step 5: migrations needed?
**************************

Sometimes, a PR needs a migration. An example is when updating a country's regions. 

Say a region contains a typo, where ``Colmbra`` should be ``Coimbra``. What if the Mautic instance already has values in the database with the old value ``Colmbra``? 

That's where migrations come in handy because every time a User updates their Mautic instance, migrations run automatically.

.. note::

  You can skip the instructions below if you don't need migrations in your PR.

To create a migration, you can follow these steps:

#. Run ``bin/console doctrine:migrations:generate`` in your terminal. Doctrine generates a new migration file for you.

#. Open the file by following the path that you can find in your terminal after running the generate command. In this file, you should see two functions, ``preUp()`` and ``up()``:

   * ``preUp()`` allows you to define scenarios where the migration should or shouldn't run. For example, only when a certain database table exists.
    
   * ``up()`` runs the actual migration and allows you to make changes in Mautic's database. You can either take inspiration from other migrations in the ``app/migrations`` folder or learn more about migrations in the `Doctrine's documentation <https://symfony.com/bundles/DoctrineMigrationsBundle/current/index.html>`_.

#. When you're done, test your migrations by running ``migrations:execute --up VERSION``.

#. If all looks good, roll back your changes with ``migrations:execute --down VERSION``.

.. tip::

    You can find an example of migration scenario and code in `this PR <https://github.com/mautic/mautic/pull/8134/files>`_.

Step 6: prepare your pull request for submission
************************************************

You're almost ready to submit your PR. There are three things you still need to look into:

#. Code standards
#. Developer documentation
#. Writing tests

In order to keep Mautic stable and easy to maintain, there is a hard requirement to apply the appropriate code standards and to write automated tests. Mautic can't accept features and/or enhancements without appropriate tests, as it would impact its stability. Why? When you try to build something in a specific part of Mautic, you might accidentally break another part of Mautic. With automated tests, which cover most aspects of Mautic, it's possible to prevent this as much as possible.

Code standards
==============

Mautic follows Symfony's :xref:`Symfony coding standards`_ by implementing pre-commit git hook running :xref:`php-cs-fixer`. The commands ``composer install`` and ``composer update`` install and update this automatically.

The aforementioned git hook automatically deals with any code styling. If you set the git hook correctly - which is the case if you ever run ``composer install`` or ``composer update`` before creating a PR - you can format your code as you like. The git hook converts it to Mautic's code style automatically.

Documentation
=============

.. vale off

Each new feature should include a reference to a PR in the :xref:`Developer Docs GitHub` repository, if applicable. Any enhancements or bug fixes affecting the end-user or developer experience should have a PR mentioned in the description which updates the relevant resources in the documentation.

.. vale on

Writing tests
=============

All code contributions - especially enhancements/features - should include adequate and appropriate unit tests using `PHPUnit <https://phpunit.de/manual/5.7/en/index.html>`_ and/or `Symfony functional tests <https://symfony.com/doc/2.8/testing.html>`_. The Core Team won't merge PRs without these tests. See the :ref:`Automated testing` section for more extensive information.

Step 7: submit your pull request
********************************

.. vale off

Rebase your pull request
========================

.. vale on

Before submitting your PR, you need to update your branch:

.. code-block:: bash

    git checkout 4.x
    git fetch upstream
    git merge upstream/4.x
    git checkout BRANCH_NAME
    git rebase 4.x

.. attention::

    Replace ``4.x`` with the branch you selected previously. For example, ``4.4`` if you are working on a bug fix.

When executing the ``rebase`` command, you might have to fix merge conflicts. Running ``git status`` can show you the un-merged files. Resolve all the conflicts, then continue the rebase:

.. code-block:: bash

    git add ... # add resolved files
    git rebase --continue

Check that all tests still pass and push your branch remotely:

.. code-block:: bash

    git push --force origin BRANCH_NAME

.. vale off

Sometimes if there are a lot of merge conflicts, it can be easier to re-create your PR on an updated version of the branch, especially if you aren't confident in correctly resolving the conflicts. Please ask for help in :xref:`Mautic product team Slack` if you are struggling with rebasing your PR.

.. vale on

Make a pull request
===================

You can now make a PR on the  :xref:`Mautic GitHub repository`.

.. note::

    Take care to point your PR towards ``mautic:4.0`` if you want the Core Team to pull a bug fix based on the ``4.0`` branch.

To ease the Core Team work, always include what you have modified in your PR message and provide steps to test your fix or feature. Keep in mind that not all testers have a thorough knowledge of Mautic's features, nor are they all likely to be developers. Therefore, clear testing steps are crucial.

Step 8: receiving feedback
**************************

All contributors need to follow some best practices to ensure a constructive feedback process.

If you think someone fails to keep this advice in mind and you want another perspective, please request a review of the feedback in the ``#dev`` channel on :xref:`Mautic Community Slack`.

The :xref:`Mautic Product Team` decides which PRs get merged, so their feedback is the most relevant. Please don't feel pressured to refactor your code immediately when someone provides feedback and wait for the Product Team to review it.

Rework your pull request
========================

Based on the feedback on your PR, you might need to make some changes. Before re-submitting the PR, rebase with ``upstream/4.x`` or ``upstream/4.4`` as appropriate - but *don't merge* - and force the push to the origin:

.. code-block:: bash

    git rebase -f upstream/4.x
    git push --force origin BRANCH_NAME

.. tip::
  
    If you want to do a ``push --force``, **always** specify the branch name explicitly to avoid messing up other branches in the repository. The option ``--force`` tells Git that you **really** want to mess with things, so do it carefully.

Step 9: testing
***************

Pull request testing
====================

If you want to test a PR from other developers, see the :ref:`PR review process` section. All PRs require testing by others in the Community, and must have the code reviewed by a member of the Core Team. Read more information in the :doc:`/contributing/governance/code-governance` section.

Automated testing
=================

.. vale off

Mautic uses :xref:`PHPUnit`, :xref:`Selenium`, and :xref:`Codeception` as the suite of testing tools.

.. vale on

PHPUnit
-------

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

.. vale off

Codeception
-----------

.. vale on

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
===============

Mautic uses :xref:`PHPSTAN` for some of its parts during continuous integration tests. To test your specific contribution locally, install PHPSTAN globally with ``composer global require phpstan/phpstan-shim``.

.. vale off

Mautic can't have PHPSTAN as its dev dependency because it requires PHP7+. To execute analysis on a specific bundle, run ``~/.composer/vendor/phpstan/phpstan-shim/phpstan.phar analyse app/bundles/*Bundle``.

.. vale on