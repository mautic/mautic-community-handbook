Tester
######

.. vale off

Every new feature and bug fix that is released in Mautic has undergone testing and code review by members of the community before it makes it into a release.

We are always looking out for people to help us with these processes. Even if you can spare an hour or two a week, it would significantly increase the number of bugs and features that make it out into the hands of Mautic users.

There are two ways to set up your testing environment:

1. On GitHub Codespaces
2. On your local machine with DDEV — **recommended**

Once your testing environment is established, it is very quick and easy to test bugs and features.

.. tip::

  You can watch the short tutorial about :xref:`How to test bugs and features in Mautic` on YouTube, which explains the easy way to do it.

Mautic maintains :xref:`Mautic OSS Fridays board` which shows you a list of all of the bugs and features that we want to get tested.

Setting up a testing environment on GitHub Codespaces
*****************************************************

:xref:`GitHub Codespaces` allows you to spin up a Mautic instance in the cloud, with a pull request — PR — applied. The Mautic instance also has a mail catching tool, MailHog, and PHPMyAdmin available to view database tables. While there are some PRs that can't be tested in this way, such as if they are testing the installation process, the vast majority can.

Setting up a codespace
======================

#. Go to :xref:`Mautic GitHub repository`.
#. Open the PR that you need to test.
#. Click the '<> Code' button on the right top, next to PR's title.
#. Click the 'Codespaces' tab.
#. Click the green 'Create codespace on BRANCH-NAME' or '+' sign to create a codespace.

   .. image:: images/open_codespace_github.png
    :alt: Screenshot highlighting code button and codespaces tab

#. Wait until the codespace finish building and the ``postCreateCommand`` finished its task. It may take a while, so please be patient.

   **Note:** If you get a warning that the codespace is currently running in recovery mode due to a configuration error as in the following screenshot, follow the instructions in the :ref:`Rebuild a codespace` section.

   .. image:: images/codespace_recovery_mode_warning.png
    :alt: Warning message that says this codespace is currently running in recovery mode dues to a container error.

#. Run ``ddev start`` to install Mautic and the dependencies.
#. Type 'Y' and press Enter when you get prompted to ``Permission to beam up? [Y/n] (yes):``.

   It can take a few minutes for the process to complete, so please wait until it does.

   Once the installer is done, it shows the URLs for the Mautic user interface, as well as MailHog and PHPMyAdmin URLs in case you need to check outgoing emails or test things in the database. It also provides you the default credentials to use for the login.

#. Click 'Ports' tab.
#. Find the port that you need to open.
#. Hover over the 'Forwarded Address' tab, right next to the port.
#. Click the globe icon to open the port in the browser.

   .. image:: images/vscode_terminal_ports_tab.png
    :alt: Screenshot of ports tab in vscode terminal highlighting globe icon 

#. Login to Mautic. See the tip below to login to Mautic.

After you setup the environment, you can follow the test instructions in the PR and :ref:`report back your findings<Leaving your review>`. 

.. tip::

   * The default username to login to Mautic is always ``admin``, and the password is ``Maut1cR0cks!``.
   * If you're testing an older version of Mautic than ``5.1``, use the password ``mautic``.
   * You can run ``ddev describe`` command to see the list and detail of available URLs and ports.

Rebuild a codespace
-------------------

Follow this steps to rebuild your codespace:

#. Press ``Cmd/Ctrl + Shift + P``. It opens a search bar on top.
#. Search for 'Codespaces: Rebuild Container', select, and click it.

   .. image:: images/codespaces_rebuild_container.png
    :alt: Screenshot of codespaces rebuild container selection

#. Click the 'Full Rebuild' button.

   .. image:: images/codespaces_rebuild_button.png
    :alt: Screenshot highlighting full rebuild button on Codespaces

Reproduce a bug
---------------

When you need to reproduce a bug before you apply the PR, create a codespace from the branch that you need to test:

#. Go to :xref:`Mautic GitHub repository`.
#. Click the branch dropdown menu on the top left.
#. Select the branch that you need to test.

   .. image:: images/switch_branch_dropwdown_menu_github.png
    :alt: Screenshot highlighting branch dropdown menu on a repository at GitHub

#. Click the green '<> Code' button at the top right.
#. Follow step 4 onwards in the :ref:`Setting up a codespace` section.

Setting up a local testing environment
**************************************

Prerequisites
=============

Before starting, you will need a few pieces of software on your computer:

* :xref:`Docker Desktop`
* :xref:`DDEV get started`
* :xref:`Git downloads`
* :xref:`GitHub CLI`

Once you have these installed, we recommend that you use an editor such as :xref:`VS Code` which will allow you to interact with files, folders, and the command line. There are other editors and Integrated Development Environments (IDEs) so if you already have one that you like, by all means use that.

You will also need to register for an account at :xref:`GitHub signup` if you don't already have one. This allows you to leave comments when you've tested things, and also means you can make fixes yourself in the future.

Downloading Mautic
==================

To start testing, we need to download a copy of Mautic for us to work with.

Before we do that, let's create a folder in your local computer where you'll locate all your local working environments. It's up to you where you save it and what you call it. Within that folder, create a folder where you'll work on this project - perhaps call it mautic4 for example.

Open your editor, and within the editor, open a terminal window.  

In the terminal, we need to move into the directory we just created. Use the following commands:

.. code-block:: bash

   cd users/yourusername/yourfolder/mautic4

If you need to move up an directory, for example, back to ``/yourfolder/``, you can use the command:

.. code-block:: bash

   cd ..

Once you are in the folder you want to work from, we need to pull down a copy of Mautic. To do this, we use a GitHub CLI command:

.. code-block:: bash

   gh repo clone mautic/mautic

The first time you run this command, it will ask you to authenticate with GitHub. Just follow the steps, and once you've set up the authentication it won't bother you for some time.

This will pull down the GitHub repository at :xref:`Mautic GitHub repository` to your local machine, ready for you to start testing with.

Setting up a local DDEV instance
================================

Now we have the files locally, we need to move into the directory which was created using the command:

.. code-block:: bash

   cd mautic

Now we need to spin up a server on our local computer, so that we can use PHP, MySQL and everything else that Mautic needs to run.

To do this, use the command:

.. code-block:: bash

   ddev start

The first time you run this command it might take a little while to run through the process.

When you are prompted whether to install Mautic, choose 'yes'.

This will install all the dependencies that Mautic requires to run, and will install Mautic with a default username and password:

.. code-block:: text

   username: admin
   password: Maut1cR0cks!

.. note::

   If you're testing an older version of Mautic than ``5.1``, use the password ``mautic``.

It will also install some software which allows you to capture outgoing emails, called MailHog, and PHPMyAdmin, which enables you to view and interact with the database.

Once this process has completed, you will be able to access your local testing instance at ``https://mautic.ddev.site``.

Log in with the credentials above, and you're ready to go.

.. tip::

   If you're testing multiple versions of Mautic, such as ``4.x``, ``5.x``, ``6.x``, or ``7.x``, you don't need to manually change the ``name:`` in ``.ddev/config.yaml``. It's best to clone each into a separate folder by running:

   .. code-block:: bash

      git clone --branch 4.x https://github.com/mautic/mautic.git mautic4
      git clone --branch 5.x https://github.com/mautic/mautic.git mautic5
      git clone --branch 6.x https://github.com/mautic/mautic.git mautic6
      git clone --branch 7.x https://github.com/mautic/mautic.git mautic7

   DDEV uses the folder name as the project name, so this automatically gives you clean URLs like:

   * ``https://mautic4.ddev.site``
   * ``https://mautic5.ddev.site``
   * ``https://mautic6.ddev.site``
   * ``https://mautic7.ddev.site``

Using developer mode
********************

When testing Mautic, it is important that you are notified of any errors rather than having them output to the logs. We also don't want to have to constantly rebuild the JavaScript and CSS files when changes are made.

For this reason, we use developer mode when testing in the Mautic Community, which is set in the local environment file. DDEV has dev mode enabled by default - read more about :xref:`Mautic environments docs` on Mautic Developer Documentation.  

Testing your first pull request
*******************************

The first step when testing a bug is to attempt reproducing the bug and making sure that you are experiencing the problem that the developer is fixing.

Generally there will be instructions in the description of the pull request, but sometimes you might have to refer to an issue which reported the bug in order to find instructions for reproducing the issue. If you don't understand, or can't reproduce the issue, please leave a comment and the developer will get back to you with further instructions.

Once you have confirmed the bug, we need to apply the fix. We do this with another GitHub CLI command:

.. code-block:: bash

   gh pr checkout <number>

Replace ``<number>`` with the ID number of the pull request. You can see this in the address bar, or next to the title of the pull request.

This command pulls down the changes that the developer has made, and applies it to your local Mautic instance. It will also clear your cache automatically.

If you ever need to clear the cache, you can either delete the cache folder manually or use the command:

.. code-block:: bash

   ddev exec bin/console cache:clear --env=dev

Note that we have to prefix any commands with ``ddev exec`` so that they run inside the Docker container. We also use the ``--env=dev`` argument to specify that we need to clear the development (rather than production) cache.

Now that you have the pull request applied, the next step is to re-test the bug or check out the new feature. Make sure you are thorough in your testing. Really think about every possible thing that might be affected by the changes being made in the pull request, and test it in detail.

It's very helpful if you can write a comment and explain what you have tested.

Top tips
========

Installing sample data
----------------------

To quickly install sample data, use the command ``ddev exec bin/console d:f:l`` which loads the Doctrine fixtures. It gives you a big head start with testing.

Build the segments after install
--------------------------------

It's always worth building the segments once you install the sample data, using the command ``ddev exec bin/console m:s:r``.  

Testing with different databases / PHP versions
-----------------------------------------------

In DDEV we can set the database and PHP version in a file located in the folder ``.ddev/config.yaml``. 

#. Open Gitpod from the PR you are testing and immediately stop the build process as soon as the terminal window is displayed, using ``command+c`` or ``ctrl+c`` on your keyboard.

#. Delete anything that has already been started with the command ``ddev delete --omit-snapshot --yes && rm -rf var/cache && rm app/config/local.php``

#. Edit the file in ``.ddev/config.yaml`` and change the setting. For instance, change DB from mariaDB 10.3 to mysql8. Always remember to save the file.

   .. code-block:: yaml

      mariadb_version: ""
      mysql_version: "8.0"

#. Type ``ddev start`` in the console to continue with installation.

#. Run the installer in the UI or command line as preferred.

#. Check you are using the right version in the system information within Mautic.

#. Remember to make sure you are using dev mode - DDEV should start in dev mode by default, with the Symfony toolbar at the bottom of the page.

#. If you make a mistake, open your Gitpod dashboard and delete the instance and start again.

Resetting your local testing environment
----------------------------------------

To quickly reset your local testing environment by deleting the DDEV containers without a database snapshot, removing the cache directory, and removing the ``local.php`` file, you can run ``ddev delete --omit-snapshot --yes && rm -rf var/cache && rm app/config/local.php``. 

Note that from Mautic 5, the location of the ``local.php`` file is now ``config/local.php``.

Leaving your review
*******************

Within GitHub, there is a built-in system for people to leave reviews. At the top of the pull request you will see a tab which is called 'Files Changed'. In this tab, at the top right, you'll see a green button which allows you to start a review.

From this point, you can write what you have found when testing the pull request. You can select whether you:

* approve the pull request,
* need to ask for some changes, for instance, if you weren't able to get the results that you expected,
* leave a comment if you're not sure either way,
* want to leave some feedback.

Unloading the pull request
**************************

Once you are done with testing the pull request, it is good practice to get back to the original state. To do this, use the command:

.. code-block:: bash

   git checkout 5.x

Where ``5.x`` is the branch that you want to return to.

This will check out the branch called ``5.x`` which is where we started from. Now you're ready to go and find another pull request to test. Have a little celebration because you helped make Mautic even more awesome. Thank you for your contribution.

.. vale on