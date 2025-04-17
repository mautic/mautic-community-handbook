Community reviews
#################

Mautic is an open source project driven by a large community. If you don't feel ready to contribute code or patches, reviewing issues and pull requests (PRs) can be a great start to get involved and give back. In fact, people who "triage" issues are the backbone to Mautic's success!

.. note::

    Everyone can test submitted features and bug fixes. No programming skills are required. All you have to do is to follow the instructions in this section.

* :ref:`Why reviewing is important`
* :ref:`Be constructive`
* :ref:`Create a GitHub account`
* :ref:`The bug report review process`
* :ref:`The pull request review process`

Why reviewing is important
**************************

Community reviews are essential for the development of Mautic, since there are many more pull requests and bug reports than there are members in the Mautic core team to review, fix and merge them.

On the `Mautic issue tracker <https://github.com/mautic/mautic/issues>`_, you can find many labels in a "`ready-to-test <https://github.com/mautic/mautic/labels/ready-to-test>`_" status:

* Bug Reports: Bug reports need to be checked for completeness. Is any important information missing? Can the bug be reproduced?

* Pull Requests: Pull requests contain code that fixes a bug or implements new functionality. Reviews of pull requests ensure that they are implemented properly, are covered by test cases, don't introduce new bugs and maintain backward compatibility.

.. note::

    Anyone who has some basic familiarity with Mautic and PHP can review bug reports and pull requests. You don't need to be an expert to help.

Be constructive
***************

Before you begin, remember that you are looking at the result of someone else's hard work. A good review comment thanks the contributor for their work, identifies what was done well, identifies what should be improved and suggests a next step.

Create a GitHub account
***********************

Mautic uses `GitHub <https://github.com/>`_ to manage bug reports and pull requests. If you want to do reviews, you need to `create a GitHub account <https://github.com/signup>`_ and log in.

The bug report review process
*****************************

The steps for the review are:

#. **Is the report complete?**

   Good bug reports contain enough information and code samples to reproduce the bug. Issue forms do ensure the basic set of information but sometimes this may not be enough to reproduce the issue. Ask for clarification if you are not sure.

#. **Reproduce the bug**

   Install Mautic locally and test whether the bug can be reproduced on your system. If the reporter did not provide enough information, ask for clarification.

#. **Leave a comment**

   At last, add a comment to the bug report. Thank the reporter for reporting the bug. Here is a sample comment for a bug report that could be reproduced:

..

    Thank you @mautibot for creating this bug report! This indeed looks like a bug. I reproduced the bug in the "kernel-bug" branch of ``https://github.com/example/some-project``.

The pull request review process
*******************************

Every change to Mautic core happens via PRs. Every PR must have a number of successful tests and code review to be merged to the core and released in the next version - the number required depends on the :doc:`tier of the PR </contributing/governance/code-governance>`. Testing a PR is a great way to move Mautic forward and personally improve its quality and stability.

#. `Select a PR <https://github.com/mautic/mautic/pulls>`_ to test.
#. Read the description and steps to test. If it's a bug fix, follow the steps to ensure you can recreate the issue.
#. Use the development environment (above) for testing.
#. `Apply the PR <https://help.github.com/articles/checking-out-pull-requests-locally/#modifying-an-inactive-pull-request-locally>`_
#. Clear cache for development environment (``rm -rf var/cache/*`` or ``bin/console cache:clear -e dev``).
#. Follow the steps from the PR description again to see if the result is as described.
#. Write a comment about how the test went. If there is a problem, provide as much information as possible including error log messages.

.. note::

    We're planning to provide more thorough guidelines for reviewing bug reports and pull requests in the near future. If you want to contribute in the meantime, please click the "Edit this page on GitHub" link at the bottom of this page.
