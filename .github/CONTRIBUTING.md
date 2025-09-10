# Contributing to Mautic Community Handbook

Contributions are always welcome, no matter how large or small, or at whatever skill level you are. Before contributing, please read the [Code of Conduct](../docs/policies/code_of_conduct/code_of_conduct.rst) and follow the directions in this guide.

---

## Table of Contents

- [Communication Expectation](#communication-expectation)
- [Issues](#issues)
- [Pull Requests (PRs)](#pull-requests-prs)
  - [Before Submitting a PR](#before-submitting-a-pr)
  - [Submitting a PR](#submitting-a-pr)
  - [After Submitting a PR](#after-submitting-a-pr)
- [Getting Started](#getting-started)
- [1. On GitHub](#1-on-github)
- [2. GitHub Codespaces](#2-github-codespaces)
  - [Setting Up a Codespace](#setting-up-a-codespace)
  - [Live Preview on Codespace](#live-preview-on-codespace)
- [3. Local Development](#3-local-development)
  - [Prerequisite](#prerequisite)
  - [Setting Up Local Environment](#setting-up-local-environment)
- [Working With Links](#working-with-links)
  - [Create a New Link](#create-a-new-link)
  - [Check Broken Links](#check-broken-links)
- [Push Changes to Remote Repository](#push-changes-to-remote-repository)
- [Credit](#credit)

---

## Communication Expectation

1. Always leave a detailed description in the pull request (PR). Leave nothing ambiguous for the reviewers.
2. Provide screenshots for visual changes.
3. Always review your code first. Be sure to run the project locally and test it thoroughly before requesting a review.
4. Communicate in the GitHub repository first before Slack. Whether it's in the issue or the PR, keeping the lines of communication open and visible to everyone on the team helps everyone around you.

## Issues

- When you contribute to the project for the first time, please consider checking the [good first issue](https://github.com/mautic/mautic-community-handbook/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22) or [help wanted](https://github.com/mautic/mautic-community-handbook/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22help%20wanted%22) labels.

- If you wish to work on an open issue, please comment on the issue, and a maintainer will assign it to you.

  If an issue isn't assigned, it's assumed to be available for anyone to work on. So, ensure that you're assigned to an issue **before** beginning work to avoid conflicts.

  **Note:** please don't ask maintainers to assign you to another issue before you have finished working on yours and created a PR.

- Did you spot a bug or have an idea for enhancing the Mautic Community Handbook? You can [create an issue](https://github.com/mautic/mautic-community-handbook/issues/new?q=is%3Aissue+state%3Aopen+label%3A%22help+wanted%22) to address it.

  However, the Education Team needs to triage the issue before you can work on it. If you wish to work on the issue you submitted, please inform and tag the `@mautic/education-team-leaders` in the comment.

## Pull Requests (PRs)

PRs are always welcome. However, before working on changes, you must ensure that **you are assigned** to an existing issue and **link your work to the issue in your PR**.

### Before Submitting a PR

1. Ensure that you work on your changes in a new branch.
2. Run and check your changes locally. Ensure that everything functions as intended.

### Submitting a PR

1. Ensure that you address one issue in one PR. If you work on multiple issues, work on them separately and create one PR to address each issue.
2. Make sure you give clear information about your changes in your PR:

   - **A title**. The PR title must describe your changes. For example: `Convert Marketer section into RST`.
   - **A description**. A clear description can help PR reviewers understand what kind of changes you made in your PR. It's always good to walk through the process of how a reviewer can test your changes.
   - **A related issue**. [Link the issue number](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) that you worked on and add a keyword of 'Closes', 'Fixes', or 'Resolves' in front of it. For example, `Closes #123`, `Fixes #234`, etc. You can find the issue number right next to the issue's title. Linking the issue number automatically closes your issue once your PR gets merged.

3. Provide screenshots for visual changes if necessary.

### After Submitting a PR

1. Ensure that all checks pass. If you see the linting build or prose failed, try to debug and fix it until all of them pass. If you have questions or need help, feel free to tag the `@mautic/education-team-leaders` in the comment.
2. Please don't DM maintainers on Slack to review or ask feedback and questions about your PR. 

   If you'd like feedback or ask questions about your PR, tag `@mautic/education-team-leaders` in the comment of your PR or use the `#t-education` channel on Slack. That way, not only maintainers, but the community can help you get unstuck. The team always gets a notification whenever there is an incoming PR. If you haven't received a review within a week, you can tag them in the PR comments to ask for an estimated review time. 

3. Keep your branch up to date while waiting for review.
4. Respond and address the reviewer's feedback. Please don't request a review until you've addressed all feedback.

## Getting Started

This project is built with [Sphinx](https://www.sphinx-doc.org/en/master/) and hosted on the [Read the Docs platform](https://readthedocs.org). The contents are written in [reStructuredText (RST)](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html).

There are three ways to work on changes for the Mautic Community Handbook:

1. Directly on GitHub
2. With [GitHub Codespaces](https://github.com/features/codespaces) on your browser
3. With code editor, such as [VSCode](https://code.visualstudio.com/), on your local machine—**recommended**

## 1. On GitHub

Making changes directly on GitHub is suitable for minor changes, such as fixing a typo. For bigger and more complex changes, please use GitHub Codespaces or work locally.

To work directly on GitHub, follow the steps below:

1. Click the "Edit on GitHub" button on the top right of the page where you noticed the mistake. It takes you to the correct resource on GitHub.

   ![Screenshot of community handbook with a red box highlighting the Edit on GitHub button](edit-on-github.png)
   
2. Click the edit button - which resembles a pencil - and make the necessary changes.

   ![Screenshot of community handbook with a red box highlighting the Edit on GitHub button](edit-button-github.png)

3. Follow the instructions to commit the changes.
4. Select to commit to a new branch. Call the branch something relative to what you are updating.
5. Go back to [https://github.com/mautic/mautic-community-handbook](https://github.com/mautic/mautic-community-handbook) and a green button prompts you to create a PR.
6. Add a description to explain what has changed.
7. Submit it for review.

## 2. GitHub Codespaces

Using GitHub Codespaces enables you to spin up the project in the cloud quickly. Before you start, it's highly recommended to use Chrome or Firefox to work with Codespaces.

<details>
  <summary><strong>Tips to maximize free tier of Codespaces</strong></summary>

  <br />
  <p>To maximize your free tier of Codespaces, you can set the default idle timeout. To do so:</p>
  <ol>
    <li>Click your avatar on the top right.</li>
    <li>Click 'Settings'.</li>
    <li>At the left bar, under 'Code, planning, and automation', click 'Codespaces'.</li>
    <li>Find 'Default idle timeout'.</li>
    <li>Set the idle time, and click 'Save'.</li>
  </ol>

  <p>You can also shut down your codespace whenever you've finished working by following these steps:</p>
  <ol>
    <li>Close your codespace.</li>
    <li>Go to <a href="https://github.com/codespaces" target="_blank">https://github.com/codespaces</a>.</li>
    <li>Scroll down and you should see a list of your Codespaces.</li>
    <li>Click the three dots icon at the codespace that you'd like to shut down.</li>
    <li>Click 'Stop codespace'.</li>
  </ol>
</details>

### Setting Up a Codespace

Follow the instructions below to set up a codespace:

1. [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repository to your own GitHub account.
2. Go to your forked repository on GitHub.
3. Click the green 'Code' button and select the 'Codespaces' tab.
4. Click the green 'Create codespace on main' button to create a new codespace. Codespace automatically sets up the project and opens Visual Studio Code.
5. Wait until the codespace finishes building. Once it's finished, the build prompt closes, and the README preview opens. You can close this preview.
6. Create a new branch to work on your changes:

   - Click the "main" button at the bottom left. It opens a dropdown menu at the top.
   - Click "Create new branch."
   - Type the branch name with anything you like. Preferably, it reflects your changes, for example, `fix-typo`.
   - Hit enter.

     **Info:** once you create a new branch, it automatically switches to your new branch. If you haven't seen the branch changes in your terminal, run `git status`, and you should see your branch name.

7. All contents of the Mautic Community Handbook are available in the `docs/` directory. In your terminal, navigate to the `docs` directory with `cd docs`.
8. Find the folder and file that you need to work on.
9. Work on your changes and use the live preview to view and test your changes in real-time.

### Live Preview on Codespace

1. Run `make html` that generates the `build` folder.
2. Click the preview button at the top to trigger Esbonio, a tool used for live preview. A tab opens, but the preview won't work. You can safely close this tab.
3. At the bottom panel, click 'Port'.
4. Click the globe icon to open the live preview in your browser. Now you can see the project in real-time on localhost.

<br />

<details>
  <summary><strong>Troubleshooting live preview</strong></summary>

  <br />
  <p><strong>Troubleshooting #1</strong></p>
  <p>If you can't see your changes in the live preview, try refreshing the page.</p>

  <p><strong>Troubleshooting #2</strong></p>
  <p>If refreshing doesn't work, try to:</p>
  <ol>
    <li>Delete the <code>build</code> folder in the root.</li>
    <li>Delete the <code>build</code> folder in the <code>docs</code> directory.</li>
    <li>Refresh your codespace browser.</li>
    <li>Ensure that you're in the <code>docs/</code> directory.</li>
    <li>Follow the steps in the <a href="#live-preview-on-codespace">Live Preview on Codespace</a> section.</li>
  </ol>

  <p><strong>Troubleshooting #3</strong></p>
  <p>If the above steps fail:</p>
  <ol>
    <li>Close VS Code and the live preview browsers.</li>
    <li>Go to <a href="https://github.com/codespaces" target="_blank">https://github.com/codespaces</a>.</li>
    <li>At the bottom, you should see a list of your codespaces.</li>
    <li>Click the three dots icon on the right of your project's codespace.</li>
    <li>Click 'Stop codespace'.</li>
    <li>Re-open the codespace by clicking its name.</li>
    <li>Follow the steps in the <a href="#live-preview-on-codespace">Live Preview on Codespace</a> section.</li>
  </ol>
</details>

<br />

> [!TIP]
> - Always refresh the page to view the new changes you have applied.
> - All commands only work within the `docs/`directory. So, if you can't run a command, check if you're in the right directory.
> - Read the "Troubleshooting live preview" if you encounter trouble with the live preview on the codespace.

## 3. Local Development

### Prerequisite

To work locally, you first need to install these on your machine:

1. **VS Code**

   If you haven't, [download and install VS Code](https://code.visualstudio.com/download) on your computer.

2. **DDEV**

   Mautic uses [DDEV](https://ddev.com) to simplify local development and testing of documentation updates. Go to the [Get Started](https://ddev.com/get-started/) page on their website for instructions to install DDEV on your local machine.

   **For Windows users**: you can install and run DDEV on [traditional Windows](https://ddev.readthedocs.io/en/stable/#system-requirements-traditional-windows). However, using [Windows Subsystem for Linux 2 (WSL2)](https://learn.microsoft.com/en-us/windows/wsl/about) gives you faster and better performance. If you're new to WSL, follow the instructions on the [DDEV blog](https://ddev.com/blog/watch-new-windows-installer/) to install and set up WSL and DDEV. 

3. **Vale**

   Mautic uses [Vale](https://vale.sh/) to maintain style guide consistency across the docs. Go to the "[Install](https://vale.sh/docs/install)" page on the official docs to install Vale on your computer.

### Setting Up Local Environment

1. [Fork and clone](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) this repository to your local machine.
2. Navigate into the project directory by running: 

   ```bash
   cd mautic-community-handbook
   ```
3. Start the DDEV environment with this command:

   ```bash
   ddev start
   ```
4. Go to the `docs/` directory:

   ```bash
   cd docs
   ```
5. Find the folder and file that you want to work on.
6. Make changes.
7. Build the project by running:

   ```bash
   ddev build-docs
   ```
8. Run the below command to view your changes live on your browser:

   ```bash
   ddev launch
   ```
   
   This automatically opens your browser and navigates to `https://mautic-community-handbook.ddev.site/`.

> [!TIP]
> - Every time you make changes, run `ddev build-docs` and refresh the page in your browser to see the changes. 
> - If you don't see the configuration take effect, run `ddev restart` to restart the project.

## Working With Links

In this section, you can find the commands that you need for working with links. Ensure that you're in the `docs/` directory to work with these commands.

### Create a New Link

When you need to add a link, you can do so by running the command below—depending on where you work on your changes—in the terminal.

If you work with Codespaces:

```bash
make link
```

If you work locally with DDEV:

```bash
ddev exec make link
```

Then input the answer to all prompts:

- **Enter a Unique Link Name:** the name of the link. 
- **Enter the link text the user sees:** the link that appears on the website.
- **Enter the URL:** the link URL.
- **Enter the .py file name (use_lower_case_and_underscore of link name):** the name of the file.

> [!TIP]
> Ensure that all entries are clear and general so that anyone working with this project can easily search and reuse them.

Here's an example:

```bash
Enter a Unique Link Name: Community Handbook
Enter the link text the user sees: Community Handbook
Enter the URL: https://contribute.mautic.org
Enter the .py file name (use_lower_case_and_underscore of link name): mautic_community_handbook
```   

### Check Broken Links

When there's a broken link, the build fails. So, you need to ensure that there's no broken link. You can check the links by following the instructions below— depending on where you work on your changes—in the terminal.

If you work with Codespaces:

```bash
make checklinks
```

If you work locally with DDEV:

```bash
ddev exec make checklinks
```

You should see a list of links. Find the broken link and fix it. Here's an example of a broken link:

## Push Changes to Remote Repository

If you have finished with your changes and are ready to push them to the remote repository:

1. On the left panel, click the '+' icon next to the name of the file to move it to the 'stage' phase. It means you're adding this file as 'ready' to commit.
2. After you add all the files that you want to commit, add a commit message describing the changes you made. For example, `fix broken links`.
3. Click the green 'Commit' button.
4. Click the 'Publish Branch', which opens a dropdown menu.
5. Select `origin: <YOUR-FORKED-REPOSITORY-URL>`.
6. On the left panel, click the 'Create PR' button.
7. Insert a brief and clear title, along with a detailed description that clearly outlines your changes. Include here your issue number. For example, `Closes #123` or `Fixes #123`.

## Credit

These contributing guidelines are adapted from [OpenSource-Communities/intro](https://github.com/OpenSource-Communities/intro/blob/main/contributing/CONTRIBUTING.md) repository.

Thank you for contributing.