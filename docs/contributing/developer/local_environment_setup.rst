Local environment setup
#######################

.. vale off

This page guides you through setting up your local environment to use and develop Mautic.

.. vale on

Development/build process requirements
**************************************

.. vale off

.. tip::

   We recommend working with :xref:`DDEV` since it includes almost all required software out of the box - PHP, Composer, MySQL - and has some handy features like MailHog, PHPMyAdmin, dynamic PHP version switching, and much more.

   You can find Mautic-specific installation instructions for DDEV in the `Local Mautic development with DDEV` blog post.

#. Mautic uses Git as a version control system. Download and install :xref:`Git` for your OS
#. Install a server, PHP, and MySQL to run Mautic locally. Read :xref:`Local Mautic development with DDEV` blog post to use DDEV (recommended) or use an :xref:`AMP software bundle` package for your OS
#. Install :xref:`Composer`, the dependency manager for PHP
#. Install :xref:`npm`
#. Install :xref:`Grunt`
#. Install :xref:`GitHub command-line tool`

.. vale on

Mautic requirements
*******************

.. vale off

#. See the :xref:`Mautic requirements` page for details of the required PHP version, PHP extensions, database, and web servers
#. PHP modules - already included in DDEV and most AMP packages:

   * required: ``zip``, ``xml``, ``mcrypt``, ``imap``, ``mailparse``
   * recommended: ``openssl``, ``opcache`` / ``apcu`` / ``memcached``
   * recommended for development: ``xdebug``
#. Recommended memory limit: minimal 256 MB for testing and 512 MB or more for production
#. Recommended MySQL defaults. It can be set by running the queries ``SET GLOBAL innodb_default_row_format=DYNAMIC; SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));``

.. vale on

Installation
************

#. Open a terminal/console window
#. Change directory to the server root. For example, ``cd /var/www`` if your local server root is at ``/var/www``
#. Clone the repository by running ``gh repo clone mautic/mautic``
#. Change directory to ``mautic`` by running ``cd mautic``
#. Install dependencies with ``composer install`` if you aren't using DDEV. If you're using DDEV, run ``ddev start``
#. Open Mautic in a browser - probably at ``http://localhost/mautic`` - and follow the installation steps
#. If you're using DDEV, the installer sets up Mautic for you. Then you can access the instance at ``https://mautic.ddev``

Keeping up-to-date
******************

Source files
============

Each time you update Mautic's source after the initial setup/installation via a new checkout, download, git pull, etc., you need to clear the cache. To do so, run the following command:


 .. code-block:: bash

	$ cd /your/mautic/directory

	$ php bin/console cache:clear

.. vale off

.. note::

	If you're accessing Mautic through the dev environment via ``index_dev.php``, you must add ``--env=dev`` to the PHP command above.

.. vale on

Vendors
=======

.. vale off

Run ``composer install`` to ensure new vendors are installed and/or existing upgrades are made.

Database Schema
===============

.. important::

	Before running these commands, please make a backup of your database.

If updating from a :xref:`Mautic tagged releases` to a tagged release, Schema changes will be included in a migrations file. To apply the changes, run:

.. vale on

.. code-block:: php

	$ php bin/console doctrine:migrations:migrate

If you are updating to the latest source - remember this is alpha - first run:

.. code-block:: php

    $ php bin/console doctrine:schema:update --dump-sql

.. vale off

This will list out the queries Doctrine wants to execute to get the schema up-to-date (no queries are actually executed). Review the queries to ensure there is nothing detrimental to your data.

.. vale on

If you're satisfied with the queries, execute them with:

.. code-block:: php

    $ php bin/console doctrine:schema:update --force

Your schema should now be up-to-date with the source.

Development environment
***********************

Mautic downloaded from GitHub has the development environment. You can access it by adding ``index_dev.php`` after the Mautic URL. For example, ``http://localhost/mautic/index_dev.php/s/``. Or in case of CLI commands, add ``--env=dev`` attribute to it.

This development environment displays the PHP errors, warnings, and notices directly as the output, so you don't have to open the log to see them. It also loads translations without a cache, so every change you make is visible without clearing it. The only changes which require clearing the cache are in the ``config.php`` files.

.. vale off

Regarding assets like JavaScript and CSS, the source files are loaded instead of concatenated, minified files. This way, the changes in those files will be directly visible when refreshed. If you want to see the change in the production environment, run the ``bin/console mautic:assets:generate`` command.

In many cases, the CSS files are built from LESS files. To compile the changes in the LESS files, run the ``grunt compile-less`` command.

.. vale on

If you don't have Grunt installed, first run ``npm install -g grunt-cli`` to install the Grunt command line interface - CLI - globally. Then go to the Mautic root directory and run ``npm install``. After that, you can run the ``grunt compile-less`` command.