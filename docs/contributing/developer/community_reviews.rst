Issues and pull request reviews
###############################

.. vale off

Issues and pull requests - PRs - reviewers are the backbone of Mautic's success. Anyone familiar with Mautic and PHP is welcome to triage bug reports and review PRs. You don't need to be an expert to help.

If you don't feel ready to contribute code or patches, triaging issues and reviewing PRs can be a great start to getting involved and giving back.

.. vale on

Why reviewing is important
**************************

.. vale off

There are significantly more PRs and bug reports than members of the Mautic Core Team available to review, fix, and merge them. Community reviews are essential to ensure that reported bugs are happening and that new features and fixes are working as expected and not introducing new problems.

Things to pay attention to when triaging an issue or reviewing a PR:

* **Bug Reports**: Ensure the accuracy and completeness of the issue. Can you reproduce the bug? Is any important information missing?

* **PRs**: PRs contain code that fixes bugs or implements new functionality. When you review a PR, you want to ensure that the fixes or enhancements are implemented correctly and covered by test cases, that new bugs aren't introduced, and that backward compatibility is maintained.

.. vale on

Be constructive
***************

Before you start, remember that you are reviewing the results of someone's hard work. A good review comment should express appreciation for the contributor's effort, acknowledge what they did well, point out areas for improvement, and suggest a next step.

Review processes
****************

.. contents::
  :local:
  :depth: 2

Create a GitHub account
=======================

.. vale off

Mautic uses :xref:`GitHub` to manage bug reports and PRs. You must have a :xref:`GitHub signup` account and log in to do reviews.

The bug report review process
=============================

If you'd like to help triage an issue, explore the :xref:`Mautic repository open issues` in the Mautic repository to find new issues.

Here are the steps to triage a bug report:

#. **Is the report complete?**

   Good bug reports contain enough information, such as a detailed description of the bug, how to reproduce it, and environment details, for example, Mautic version, operation system - OS, etc. It may sometimes include code samples and screenshots or screen recordings.
   
   Issue forms ensure the basic information set, but sometimes, this may not be enough to reproduce the issue. If you are not sure, ask for clarification.

#. **Reproduce the bug**

   You can :doc:`set up your local environment </contributing/developer/local_environment_setup>` and test whether you're can reproduce the bug on your system. If the reporter did not provide enough information, ask for clarification.

#. **Leave a comment**

   At last, add a comment to the bug report. Thank the reporter for reporting the bug. Here is an example:

.. vale on

..

   .. vale off

     Thank you, @mautibot, for creating this bug report. I could reproduce the bug on my end. Feel free to claim this issue if you want to work on it.

   .. vale on

.. _PR review process:

The pull request review process
===============================

.. vale off

Every change to Mautic happens via PRs. Every PR must have a number of successful tests and code reviews to be merged to the core and released in the next version - the number required depends on the :doc:`tier of the PR </governance/code-governance>`. Testing a PR is a great way to move Mautic forward and personally improve its quality and stability.

.. vale on

#. Find a :xref:`Mautic PRs` to test. You can also seek PRs with the label :xref:`Mautic ready-to-test issue label`
#. Read the description and steps to test. If it's a bug fix, follow the steps to ensure you can recreate the issue
#. `Pull the PR <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/checking-out-pull-requests-locally#modifying-an-active-pull-request-locally>`_ to your local machine to use the development environment for testing
#. Clear cache for the development environment by running the ``rm -rf var/cache/*`` or ``bin/console cache:clear -e dev`` command
#. Follow the steps from the PR description again to see if the result is exactly as described
#. `Submit a review <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request#submitting-your-review>`_ in the PR. If there is a problem, provide as much information as possible, including error log messages

.. vale off

.. note::

   The Education Team plans to provide more thorough guidelines for triaging bug reports and reviewing PRs in the near future.

.. vale on