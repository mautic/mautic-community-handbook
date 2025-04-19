Developer documentation
#######################

Contributing to the developer documentation
*******************************************

Developer documentation is available at :xref:`Developer Docs` and is generated using reStructuredText (RST).

.. vale off

.. warning::

    We are currently in the process of updating and re-platforming our developer documentation. If you'd like to help with this, please check the issues in the :xref:`Developer Docs GitHub`.

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
* Be familiar with the `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ markup languange, which is used by the Mautic documentation.

Your first documentation contribution
=====================================

In this section, you'll learn how to contribute to the Mautic documentation for the first time. The next section will explain the shorter process you'll follow in the future for every contribution after your first one.

Let's imagine that you want to improve the REST API documentation. In order to make your changes, follow these steps:

#. Go to the official Mautic documentation repository located at :xref:`Developer Docs GitHub` and click on the "Fork" button to fork the repository to your personal account. This is only needed the first time you contribute to Mautic.
#. Clone the forked repository to your local machine:

    .. code-block:: bash

        git clone https://github.com/YOUR-GITHUB-USERNAME/developer-documentation-new.git

#. Create a dedicated new branch for your changes. Use a short and memorable name for the new branch. If you are fixing a reported issue, use ``fix_XXX`` as the branch name, where "XXX" is the number of the issue:

    .. code-block:: bash

        git checkout -b fix_1234 upstream/main

   In this example, the name of the branch is ``fix_1234`` and the ``upstream/main`` value tells Git to create this branch based on the ``main`` branch of the "upstream" remote, which is the original Mautic Developer Documentation repository.

#. Now make your changes in the documentation. The files are located in ``source/includes``. Add, tweak, reword and even remove any content and do your best to comply with the documentation standards. Then, commit and push your changes.

    .. code-block:: bash

        git add _api_authorization.md
        git commit _api_authorization.md
        git push

#. Everything is now ready to initiate a pull request (PR). Go to your forked repository at ``https://github.com/YOUR-GITHUB-USERNAME/developer-documentation-new`` and click on the "Pull requests" link located in the sidebar. Then, click on the green "New pull request" button.

#. Now let's prepare the description of the PR. A short phrase or paragraph describing the proposed changes is enough to ensure that your contribution can be reviewed.

.. vale off

You've successfully submitted your first contribution to the Mautic Developer documentation. Congratulations!

.. vale on

The documentation managers will carefully review your work in short time and they will let you know about any required change. In case you are asked to add or modify something, you don't need to create a new PR. Instead, make sure that you are on the correct branch, make your changes there, and push the new changes.

Your next documentation contributions
=====================================

Your first contribution took a little extra time because you needed to learn a few standards and setup your local environment. But from now on, your contributions will be much easier to complete.

Here is a checklist of steps that will guide you through your next contribution to the Mautic documentation:

.. code-block:: bash

    # Create a new branch
    git fetch upstream
    git checkout -b my_changes upstream/master

    # ... do your changes

    # (optional) add your changes if this is new content
    git add xxx.md

    # commit your changes and push them to your fork
    git commit xxx.md
    git push origin my_changes

    # go to GitHub and create your Pull Request

    # (optional) make the changes requested by reviewers and commit them
    git commit xxx.md
    git push

Build the documentation locally
===============================

.. note::

    We will add instructions for building the documentation locally at a later stage.
