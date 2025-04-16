Bugs
####

Reporting a bug
***************

If you encounter a bug, please report it to help improve Mautic for everyone.

However, before submitting a bug:

* You must make sure there are no problems with your local installation, such as permission problems, outdated cache, etc. For assistance, please refer to the Mautic's :xref:`Mautic troubleshooting` guide.
* If you're unsure whether the problem is a bug, please ask for help first in the :xref:`Mautic Community Forums`.

When you are confident that the problem is a bug, please `create a new issue <https://github.com/mautic/mautic/issues/new/choose>`_ in the GitHub repository and provide as many details as possible (reproduction steps, Mautic/PHP versions, etc.).

.. vale off

.. warning::

    If you have found a security vulnerability, please report it by submitting an :xref:`Mautic GitHub advisory form` with as much detail as possible.

    The Core Team will review the vulnerability and, if found applicable, will create the patch in a private repository. The vulnerability will be disclosed once the patch has been included in a release.

        .. tip::

            You can read more about Mautic's Security Team, what kind of security issues Mautic responds to, who's on the team, and how to report an issue in the :xref:`Mautic security team` section.

.. vale on

Fixing a bug
************

If you're able to fix a bug, whether you discovered it or something reported by someone in the community, please make a :doc:`pull request </contributing/developer/pull-requests>`. Be sure to link the pull request to any issues it resolves by including "fixes #XXX" in your description. Change the "XXX" to the issue number. 

Providing test instructions is extremely important. Please don't assume the person testing your pull request is a developer. You must always provide clear, step-by-step instructions for reproducing the bug and testing your pull request.