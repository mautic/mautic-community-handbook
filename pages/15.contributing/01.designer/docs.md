---
title: Designer
googletitle: 'How can I contribute to Mautic as a Designer?'
googledesc: 'There are many ways to support Mautic as a designer. Find out more in this article.'
twitterenable: true
twittercardoptions: summary
articleenabled: false
orga: {  }
personenabled: false
facebookenable: true
taxonomy:
    category:
        - docs
---

---

Hello designer, and welcome to the Mautic Community!  At the moment we don't have many designers who are actively contributing to Mautic, so it's a great way to make a big difference.  THANK YOU for considering contributing to Mautic, we're super excited to have you join us!

There are several ways you could contribute to Mautic as a designer, and it really depends on what you love doing and how your skills might be best put to use with our current projects.

Some areas you may want to consider include:

- Supporting the Product Team by creating visual resources to explain new features
- Helping the Marketing Team with designing their monthly newsletters
- Creating new designs for our web resources (for example, the mautic.org website)
- Working with the Product Team to improve the user experience of Mautic 
- Contributing to Strategic Initiatives by designing the user experience for new features
- Improving the user documentation by creating illustrations or images that complement the written information
- Building a pattern library to standardise the UI patterns used in Mautic
- Joining the User Experience Tiger Team

## Getting started

The first step is to join us on our Slack instance.  You can get an invitation [here][slack-invite].    

Many of our design tasks will be cross-project rather than relating to a specific team, but you're most welcome to join whatever channels interest you.  

We have a public [#design][mautic-design] channel where we'll post requests for people who might be interested in working on design-related tasks.  Please do introduce yourself in this channel and let us know a bit about how you'd like to get involved. If you don't know yet that's also fine - we can help you find your way!

## Finding tasks to work on

### Jira issues

The best way to find tasks to work on which relate to the wider community (outside of the product) is to take a look at our Jira boards.  There are two main ways to find tasks of interest:

- Search for the [label Design][jira-issues-label]
- Search for the [text phrase Design][jira-issues-design]

When you find an issue on Jira, it will generally be associated with a team or project board. It's a good idea to join the relevant Slack channel and let people know that you're interested in tackling the specific task you've found.  You'll find all of our teams in Slack have a channel prefixed with #t-, initiatives with #i-, tiger teams with #tt- and working groups with #wg-.

You can create a Jira account [here][jira-create-account]. If you have an account and need to be added to our instance, please ask in [#community][community-slack] on Slack.

Once you can log into our instance, you'll be able to assign the issue to yourself and add comments.  Please transition the status as you are working on things, and make sure to add sub-tasks if the task itself should be chunked down into smaller parts.

We generally meet fortnightly, asynchronously on Slack for teams, working groups and tiger teams. This is a great opportunity to report back to the team what you're working on, how you're progressing, and to let people know if you need feedback.

### GitHub issues and pull requests

The best way to find tasks which require input relating to the user experience or user interface within Mautic (the product) is to take a look at our GitHub issue queue and pull requests.

- Search the GitHub issue queue for [UX][ux-issues] or [UI][ui-issues] issues
- Search GitHub to find new features and bug fixes to test relating to [UX][ux-prs] or [UI][ui-prs] improvements

These issues will be reported by users of Mautic or developers who have found problems with aspects of Mautic.  Pull requests will be fixes for bugs or new features which have been submitted to the community for review. If they are approved, they will be released in a future version of Mautic.

If you are able to provide feedback on issues or pull requests, please add a comment in the feed. If you're able to test the pull request and provide feedback from the design perspective, please click on 'files changed' at the right, and then 'start review'. This will allow you to approve or request changes, or just leave a comment.

[//]: # TODO: Add a link to documentation on how to test PRs

## General principles to follow

Whenever you are designing for the Mautic Community, we do require the source files to be shared in our public [Google Drive][google-drive].  

Any images you use must have the appropriate copyright permissions which should be shared with the team lead so that they have a copy of the licenses.  

If you're working on web-based tools please ensure that you work with a personal account where possible (so that it will remain accessible if you were to move jobs), and share with the relevant team lead full access so that they are able to interact with the resources.  Ask the team lead if we already have a community account or team which we can add you to, before you start working with a specific tool!

## Reporting problems with design

We welcome positive, constructive feedback relating to design (and even better if it comes with a proposal for fixing the issue!)

### Within the Mautic product

If you have spotted something that needs to be addressed within Mautic please:

1. [Create an issue on GitHub][github-new-issue] providing as much detail as possible
1. If you're able to address the problem, please indicate this in the issue - we're happy to help you get started with how to do this!
1. If you're not able to address the issue but know where it probably comes from, please leave a hint. This will help people following up to get a jump start.

### Outside of the Mautic product

Please first report the issue in the relevant Slack channel for the team responsible for the defect you have spotted.  They will then be able to direct you how best to proceed with reporting the issue and having it addressed.

[slack-invite]: <https://mautic.org/slack>
[mautic-design]: <https://mautic.slack.com/archives/C02HU8FQM>
[jira-issues-label]: <https://mautic.atlassian.net/browse/TMAR-24?jql=labels%20%3D%20Design%20AND%20statusCategory%20%3D%20%22To%20Do%22>
[jira-issues-design]: <https://mautic.atlassian.net/browse/MCON-201?jql=text%20~%20%22design%22%20AND%20statusCategory%20%3D%20%22To%20Do%22>
[community-slack]: <https://mautic.slack.com/archives/C8B89CLSF>
[jira-create-account]:<https://id.atlassian.com/signup>
[google-drive]: <https://drive.google.com/drive/folders/1OrwJXmDrrlWK3f9nxRuru0YjS7-W-1-e?usp=sharing>
[github-new-issue]: <https://github.com/mautic/mautic/issues/new?assignees=&labels=bug%2Cneeds-triage&template=BUG-REPORT.yml&title=Your+bug+title+goes+here%21>
[ux-issues]: <https://github.com/mautic/mautic/issues?q=is%3Aopen+is%3Aissue+label%3Auser-experience>
[ui-issues]: <https://github.com/mautic/mautic/issues?q=is%3Aopen+is%3Aissue+label%3Auser-interface>
[ux-prs]: <https://github.com/mautic/mautic/pulls?q=is%3Aopen+is%3Apr+label%3Auser-experience>
[ui-prs]: <https://github.com/mautic/mautic/pulls?q=is%3Aopen+is%3Apr+label%3Auser-interface>