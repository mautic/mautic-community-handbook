---
title: Developer Documentation
taxonomy:
    category:
        - docs
---

## Contributing to the Developer Documentation
---

Developer documentation is available at [https://developer.mautic.org](https://developer.mautic.org) and is generated using Slate.

<!-- ## Table of Contents -->

<!--
Use this site to generate the TOC list elements:

- https://ecotrust-canada.github.io/markdown-toc/

remove the first two lines
-->

  - [Before your first contribution](#before-your-first-contribution)
  - [Your First Documentation Contribution](#your-first-documentation-contribution)
  - [Your Next Documentation Contributions](#your-next-documentation-contributions)
  - [Build the documentation locally](#build-the-documentation-locally)

### Before your first contribution
Before contributing, you need to:

- Sign up for a free [GitHub](https://github.com/) account, which is the service where the Mautic documentation is hosted.
- Be familiar with the [Slate markup language](https://github.com/slatedocs/slate/wiki/Markdown-Syntax), which is used by the Mautic docs.

### Your First Documentation Contribution

In this section, you'll learn how to contribute to the Symfony documentation for the first time. The next section will explain the shorter process you'll follow in the future for every contribution after your first one.

Let's imagine that you want to improve the REST API documentation. In order to make your changes, follow these steps:

1. Go to the official Mautic documentation repository located at https://github.com/mautic/developer-documentation and click on the Fork button to fork the repository to your personal account. This is only needed the first time you contribute to Mautic.
2. Clone the forked repository to your local machine:
```
git clone https://github.com/YOUR-GITHUB-USERNAME/developer-documentation.git
```
3. Create a dedicated new branch for your changes. Use a short and memorable name for the new branch (if you are fixing a reported issue, use fix_XXX as the branch name, where XXX is the number of the issue):
```
git checkout -b fix_1234 upstream/master
```
4. In this example, the name of the branch is `fix_1234` and the `upstream/master` value tells Git to create this branch based on the `master` branch of the upstream remote, which is the original Mautic Developer Docs repository.

5. Now make your changes in the documentation. The files are located in `source/includes`. Add, tweak, reword and even remove any content and do your best to comply with the Documentation Standards. Then commit and push your changes!

```
git add _api_authorization.md
git commit _api_authorization.md
git push
```

6. Everything is now ready to initiate a pull request. Go to your forked repository at https://github.com/YOUR-GITHUB-USERNAME/developer-documentation and click on the Pull Requests link located in the sidebar.
Then, click on the big **New pull request** button.

7. The last step is to prepare the description of the pull request. A short phrase or paragraph describing the proposed changes is enough to ensure that your contribution can be reviewed.

8. Now that you've successfully submitted your first contribution to the Mautic developer documentation, go and celebrate! The documentation managers will carefully review your work in short time and they will let you know about any required change. In case you are asked to add or modify something, don't create a new pull request. Instead, make sure that you are on the correct branch, make your changes and push the new changes.

### Your Next Documentation Contributions

Check you out! You've made your first contribution to the Mautic developer documentation! Somebody throw a party! Your first contribution took a little extra time because you needed to learn a few standards and setup your computer. But from now on, your contributions will be much easier to complete.

Here is a checklist of steps that will guide you through your next contribution to the Symfony docs:

```
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
```

### Build the documentation locally

TODO provide instructions for building locally