---
title: Testing pull requests
taxonomy:
    category:
        - docs
---

## Testing Pull Requests
---

Everyone can test submitted features and bug fixes. No programming skills are required. All you have to do is to follow the steps below.

Every change to Mautic core happens via PRs. Every PR must have 2 successful tests to be merged to the core and released in the next version. Testing a PR is a great way to move Mautic forward and personally improve its quality and stability.

1. [Select a PR][mautic-prs] to test.
2. Read the description and steps to test. If it's a bug fix, follow the steps to ensure you can recreate the issue.
3. Use the development environment (above) for testing.
3. [Apply the PR][apply-pr]
4. Clear cache for development environment (`rm -rf app/cache/*` or `app/console cache:clear -e dev`).
5. Follow the steps from the PR description again to see if the result is as described.
6. Write a comment about how the test went. If there is a problem, provide as much information as possible including error log messages.

[mautic-prs]: <https://github.com/mautic/mautic/pulls>
[apply-pr]: <https://help.github.com/articles/checking-out-pull-requests-locally/#modifying-an-inactive-pull-request-locally>