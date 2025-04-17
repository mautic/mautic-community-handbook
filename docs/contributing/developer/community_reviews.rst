---
title: Community reviews
slug: community-reviews
taxonomy:
    category:
        - docs
---

## Community reviews
---

Mautic is an open source project driven by a large community. If you don't feel ready to contribute code or patches, reviewing issues and pull requests (PRs) can be a great start to get involved and give back. In fact, people who "triage" issues are the backbone to Mautic's success!

>>>>> Everyone can test submitted features and bug fixes. No programming skills are required. All you have to do is to follow the steps below.

- [## Community reviews](#h2-id%22community-reviews-41%22community-reviewsh2)
- [Why Reviewing Is Important](#why-reviewing-is-important)
- [Be constructive](#be-constructive)
- [Create a GitHub account](#create-a-github-account)
- [The Bug Report Review Process](#the-bug-report-review-process)
- [The Pull Request Review process](#the-pull-request-review-process)

## Why Reviewing Is Important

Community reviews are essential for the development of Mautic, since there are many more pull requests and bug reports than there are members in the Mautic core team to review, fix and merge them.

On the [Mautic issue tracker][mautic-issue-tracker], you can find many items in a [Ready To Test][ready-to-test-issues] status:

- Bug Reports: Bug reports need to be checked for completeness. Is any important information missing? Can the bug be reproduced?

- Pull Requests: Pull requests contain code that fixes a bug or implements new functionality. Reviews of pull requests ensure that they are implemented properly, are covered by test cases, don't introduce new bugs and maintain backward compatibility.

>>>>> Note that **anyone who has some basic familiarity with Mautic and PHP can review bug reports and pull requests**. You don't need to be an expert to help.

## Be constructive

Before you begin, remember that you are looking at the result of someone else's hard work. A good review comment thanks the contributor for their work, identifies what was done well, identifies what should be improved and suggests a next step.

## Create a GitHub account

Mautic uses [GitHub][github] to manage bug reports and pull requests. If you want to do reviews, you need to [create a GitHub account][create-github-account] and log in.

## The bug report review process

The steps for the review are:

1. **Is the report complete?**

Good bug reports contain enough information and code samples to reproduce the bug. Issue forms do ensure the basic set of information but sometimes this may not be enough to reproduce the issue. Ask for clarification if you are not sure.

2. **Reproduce the bug**

Install Mautic locally and test whether the bug can be reproduced on your system. If the reporter did not provide enough information, ask for clarification.

3. **Leave a comment**

At last, add a comment to the bug report. Thank the reporter for reporting the bug. Here is a sample comment for a bug report that could be reproduced:

> Thank you @mautibot for creating this bug report! This indeed looks like a bug. I reproduced the bug in the "kernel-bug" branch of https://github.com/example/some-project.

## The pull request review process

Every change to Mautic core happens via PRs. Every PR must have a number of successful tests and code review to be merged to the core and released in the next version - the number required depends on the [tier of the PR][code-governance]. Testing a PR is a great way to move Mautic forward and personally improve its quality and stability.

1. [Select a PR][mautic-prs] to test.
2. Read the description and steps to test. If it's a bug fix, follow the steps to ensure you can recreate the issue.
3. Use the development environment (above) for testing.
3. [Apply the PR][apply-pr]
4. Clear cache for development environment (`rm -rf var/cache/*` or `bin/console cache:clear -e dev`).
5. Follow the steps from the PR description again to see if the result is as described.
6. Write a comment about how the test went. If there is a problem, provide as much information as possible including error log messages.

>>> We're planning to provide more thorough guidelines for reviewing bug reports and pull requests in the near future. If you want to contribute in the meantime, please click the "Edit this page on GitHub" link at the bottom of this page.

[mautic-prs]: <https://github.com/mautic/mautic/pulls>
[apply-pr]: <https://help.github.com/articles/checking-out-pull-requests-locally/#modifying-an-inactive-pull-request-locally>
[mautic-issue-tracker]: <https://github.com/mautic/mautic/issues>
[ready-to-test-issues]: <https://github.com/mautic/mautic/issues?q=is%3Aopen+is%3Aissue+label%3A%22Ready+To+Test%22>
[github]: <https://github.com/>
[create-github-account]: <https://help.github.com/github/getting-started-with-github/signing-up-for-a-new-github-account>
[code-governance]: </community-structure/governance/code-governance>


