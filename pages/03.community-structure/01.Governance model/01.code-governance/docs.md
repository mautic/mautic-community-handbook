---
title: 'Code governance'
---

---
## New branching strategy

As we will be maintaining multiple major and minor versions of Mautic from now on (2.x and 3.x), we are also introducing a new branching strategy on GitHub. 

If you are not familiar with [Semantic Versioning](https://semver.org/) terminology like “major/minor/patch version”, we recommend checking out [this page](https://semver.org/).

As soon as 3.0 is released, we will take the following approach:

**master branch** is used for active development of Mautic (e.g. version 4). As soon as we “feature freeze” a new version (that is, all major new features are done and we’re ready to release an alpha or beta), we move development efforts to a release-x.x branch (e.g. release-3.0 for Mautic 3.0)

**release-x.x branches** are used to maintain minor versions of Mautic after they have been released. For example, if we need to provide bug fixes for Mautic 2.16.0, we’d check out the release-2.16 branch on Git and start working from there. Also, if we’d decide to create a new minor version, like 2.17, and a new major version (like 3.0) has already been released, we’d use the release-2.16 branch as the starting point and create release-2.17 from there.

By following this branching strategy, we hope to make it easier for all parties involved (especially community contributors) to improve Mautic and to maintain multiple versions at the same time. 

We’ve started to create a [Supported Versions table on GitHub](https://github.com/mautic/mautic#supported-versions) and will update that throughout the year with more specific dates.
