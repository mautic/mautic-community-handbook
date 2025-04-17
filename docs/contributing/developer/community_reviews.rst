Community reviews
#################

Mautic is an open source project driven by a large community. If you don't feel ready to contribute code or patches, reviewing issues and pull requests (PRs) can be a great start to getting involved and giving back. Issues and PR reviewers are the backbone of Mautic's success.

.. note::

    Everyone can test submitted features and bug fixes. No programming skills are required. All you have to do is to follow the instructions in this section.

* :ref:`Why reviewing is important`
* :ref:`Be constructive`
* :ref:`Create a GitHub account`
* :ref:`The bug report review process`
* :ref:`The pull request review process`

Why reviewing is important
**************************

Community reviews are essential for developing Mautic since there are many more PRs and bug reports than members in the Mautic core team to review, fix, and merge them.

Things you need to check in an issue or PR:

* **Bug Reports**: Ensure the accuracy and completeness of the issue. Can you reproduce the bug? Is any important information missing?

.. vale off

* **PRs**: PRs contain code that fixes bugs or implements new functionality. When you review a PR, you want to ensure that the fixes or enhancements are implemented correctly and covered by test cases, that new bugs aren't introduced, and that backward compatibility is maintained.

.. vale on

Explore the `Mautic issue tracker <https://github.com/mautic/mautic/issues>`_ to find new issues you can help triage. If you want to contribute by testing features and bug fixes, seek PRs with the label `ready-to-test <https://github.com/mautic/mautic/labels/ready-to-test>`_.

.. note::

 Anyone familiar with Mautic and PHP can review bug reports and PRs. You don't need to be an expert to help.

Be constructive
***************

Before you start, remember that you are reviewing the results of someone else's hard work. A good review comment should express appreciation for the contributor's effort, acknowledge what they did well, point out areas for improvement, and suggest a next step.

Create a GitHub account
***********************

Mautic uses `GitHub <https://github.com/>`_ to manage bug reports and PRs. You must have a `GitHub account <https://github.com/signup>`_ and log in to do reviews.

The bug report review process
*****************************

Here are the steps to review a bug report:

#. **Is the report complete?**

   Good bug reports contain enough information, such as a detailed description of the bug, how to reproduce it, and environment details, for example, Mautic version, operation system (OS), etc. It may sometimes include code samples and screenshots or screen recordings.
   
   Issue forms ensure the basic information set, but sometimes, this may not be enough to reproduce the issue. If you are not sure, ask for clarification.

#. **Reproduce the bug**

   You can :doc:`set up your local environment </contributing/developer/local_environment_setup>` and test whether you're able to reproduce the bug on your system. If the reporter did not provide enough information, ask for clarification.

#. **Leave a comment**

   At last, add a comment to the bug report. Thank the reporter for reporting the bug. Here is an example:

..

    Thank you, @mautibot, for creating this bug report! I could reproduce the bug on my end. Feel free to claim this issue if you want to work on it.

The pull request review process
*******************************

Every change to Mautic core happens via PRs. Every PR must have a number of successful tests and code reviews to be merged to the core and released in the next version - the number required depends on the :doc:`tier of the PR </contributing/governance/code-governance>`. Testing a PR is a great way to move Mautic forward and personally improve its quality and stability.

#. `Select a PR <https://github.com/mautic/mautic/pulls>`_ to test.
#. Read the description and steps to test. If it's a bug fix, follow the steps to ensure you can recreate the issue.
#. Use the development environment (above) for testing.
#. `Apply the PR <https://help.github.com/articles/checking-out-pull-requests-locally/#modifying-an-inactive-pull-request-locally>`_
#. Clear cache for the development environment (``rm -rf var/cache/*`` or ``bin/console cache:clear -e dev``).
#. Follow the steps from the PR description again to see if the result is as described.
#. Write a comment about how the test went. If there is a problem, provide as much information as possible, including error log messages.

.. note::

 We're planning to provide more thorough guidelines for reviewing bug reports and pull requests in the near future. If you want to contribute, please click the "Edit this page on GitHub" link at the bottom.
