Developer documentation
#######################

Contributing to the developer documentation
*******************************************

Developer documentation is available at :xref:`Developer Docs` and is generated using reStructuredText (RST).

.. vale off

.. warning::

    The Developer documentation is currently in the process of being updated and re-platformed. If you'd like to help with this, please check the issues in the :xref:`Developer Docs GitHub`.

.. vale on

Table of contents
*****************

* :ref:`Before your first contribution`
* :ref:`Your first documentation contribution`
* :ref:`Your next Documentation contributions`
* :ref:`Build the documentation locally`

Before your first contribution
==============================

Before contributing, you need to:

* Sign up for a free `GitHub account <https://github.com/signup>`_, which is the service where the Mautic documentation is hosted.
* Be familiar with the `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ markup language, which is used by the Mautic documentation.

Your first documentation contribution
=====================================

In this section, you'll learn how to contribute to the Mautic documentation for the first time.

Imagine that you want to improve some details on Mautic's Categories in the REST API documentation. In order to make your changes, follow instructions below.

Forking and cloning a repository
--------------------------------

For you who are new to open source, you might not know what do "fork" and "clone" mean. "Fork" means creating a copy of the original repository (usually refers as ``upstream``) to your GitHub account. Your forked repository is usually referred as ``origin`` repository. While "clone" means creating a copy of a repository to your local machine.

#. Go to the official Mautic documentation repository located at :xref:`Developer Docs GitHub` and click the "Fork" button on the top right.
#. Click the green "Code" button and copy the URL of your forked repository.
#. Clone the forked repository to your local machine.

   .. code-block:: bash

     git clone https://github.com/YOUR-GITHUB-USERNAME/developer-documentation-new.git

Creating a new branch and working on changes
--------------------------------------------

You always want to create a new branch from the default branch of a repository. To know the default branch of a repository, click the dropdown menu at the top left. Then click the branch that has a "default" label to set it.

Now follow the steps below to create a new branch and work on your changes:

#. Create a new branch to work on your changes from the default branch.

   Use a short and descriptive name for the new branch. For example, if you are working on an issue, use ``fix_XXX`` as the branch name, where "XXX" is the number of the issue.

   .. code-block:: bash

     git checkout -b BRANCH_NAME

   For example:

   .. code-block:: bash

     git checkout -b fix_1234
   
   In this example, the ``checkout -b`` command tells Git to create a new branch called ``fix_1234`` and automatically switch to this branch. However, you want to make sure that you're in the right branch by running ``git status``.

#. Open the file you want to work on, make the changes, and do your best to comply with the documentation standards. Then, add, commit, and push your changes to the remote repository.

   .. code-block:: bash

     git add FILE_PATH
     git commit -m "your commit message"
     git push -u origin BRANCH_NAME

   For example:

   .. code-block:: bash

     git add docs/rest_api/categories.rst
     git commit -m "add a detail in categories.rst"
     git push -u origin fix_1234

   This commands tell Git to:
   
   * add the changes in the file onto the staging area,
   * save the changes in the file by committing the changes and record the changes with the commit message,
   * bring all changes in the ``fix_1234`` branch to your forked repository by pushing it from your local machine to the ``origin`` remote repository.

You're now ready to initiate a pull request (PR).

Creating a pull request
-----------------------

#. Go to your forked repository at ``https://github.com/YOUR-GITHUB-USERNAME/developer-documentation-new``. Click the green "Compare & pull request" button on the orange banner at the top.
#. Write a title and a description of the PR. A short phrase or paragraph describing the proposed changes is enough to ensure that your contribution can be reviewed.
#. Click the green "Create pull request" button at the bottom.

.. vale off

You've successfully submitted your first contribution to the Mautic Developer documentation. Congratulations!

The documentation managers will carefully review your work. They will either merge your PR or let you know if you need to make some changes.

.. vale on

In case you are asked to add or modify something, you don't need to create a new PR. What you need to do:

* Run ``git status`` to make sure that you are on the correct branch.
* Make your changes.
* Add, commit, and push your changes.

Your next documentation contributions
=====================================

To make your next contribution, you don't need to fork and clone the ``upstream`` repository. You only need to follow the steps starting from the :ref:`Creating a new branch and working on changes` section.

Build the documentation locally
===============================

.. vale off

.. note::

    The instructions for building the documentation locally will be added at a later stage.

.. vale on
