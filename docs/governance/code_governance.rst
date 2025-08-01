Code governance
###############

Tiers for triaging pull requests
********************************

Mautic uses a tier-based approach to categorising pull requests - PRs - in the Mautic Community. This allows the Product Team to establish clear governance approaches for dealing with PRs and what the criteria is for merging.

This permits the processing of minor fixes and improvements more rapidly, while time-boxing community testing for major pull requests, enabling the Product Team to make decisions on whether to merge new features once those time periods have passed.

Tier 1
======

Small changes such as typo fixing, bug fixes, translation changes, minor UI improvements or minor enhancements. Most simple bug fixes are probably going to be in Tier 1.

.. vale off

Examples - Tier 1
-----------------

.. vale on

:xref:`github_pr_8393`- simple bug fix with very few changes

:xref:`github_pr_8116`- very simple bug fix

.. vale off

Requirements for merging a Tier 1 PR
------------------------------------

.. vale on
 
* Thorough testing to ensure that it does what its expected to do and doesn't break anything else
* Full unit testing coverage
* Code review from 1 Core Team member
* Full testing and approval by at least one community member - could be the person doing the code review, but shouldn't be from the same company/organization as the person submitting the PR

For example, if an employee or contractor from Company A were to submit a PR, the community testing/approval must come from someone outside Company A influence - not an employee, contractor, etc, of Company A

Tier 2
======

Minor features or enhancements which don't significantly change any part of Mautic.

More complex bug fixes are also probably going to be in Tier 2, as well as PRs relating to external services - for example, Salesforce/HubSpot - for which you need to create an account to test.

.. vale off

Examples - Tier 2
------------------

.. vale on

:xref:`github_pr_6090`- new feature, fairly simple and doesn't significantly change any major part of Mautic

:xref:`github_pr_7432`- a lot of new code which extends an existing feature, enhancing reports with a scheduling option

.. vale off

Requirements for merging a Tier 2 PR
------------------------------------

.. vale on

* Thorough testing to ensure that it does what it's expected to do and doesn't break anything else
* Full unit testing coverage
* Full documentation support if it's a feature change/addition
* Code review from 1 Core Team member
* Full testing and approval by at least one community member - could be the person doing the code review, but shouldn't be from the same company/organisation as the person submitting the PR as mentioned previously.

Tier 3
======

Major changes touching multiple parts of Mautic, completely changing the way some aspect of the code works, or large amounts of code changed.

.. vale off

Examples - Tier 3
-----------------

.. vale on

:xref:`github_pr_6875`- complex code changes across multiple areas, with significant impact

:xref:`github_pr_6584`- not too complex but a large visual change in the UI with the potential to cause significant disruption to the end user

.. vale off

Requirements for Merging a Tier 3 PR    
------------------------------------

.. vale on

* Thorough testing to ensure that it does what it's expected to do and doesn't break anything else
* Thorough testing across the whole product
* Full unit/functional test coverage
* Full documentation support
* Code review from 1 to 2 Core Team members
* Full testing and approval by at least two community members - could be the people doing the review, but shouldn't be from the same company/organisation as the person submitting the PR as mentioned above
* 2 week community review period - after which Product Team decides via a vote in the next available team meeting whether to merge, assuming code review and all other requirements are in place to permit merging

.. note::
	
	   You should link Tier 3 PRs which relate to new features that impact users of Mautic to an **individual forum thread** at :xref:`Ideas and Feature Requests` and there should be discussions made on the forums. This gives the non-developer user base an opportunity to have a say in the discussions on new features.

If a thread doesn't exist prior to PR submission - for example, a feature created without the community suggesting it - create one during triage when adding a Tier 3 & Feature label.

You should share the GitHub URL in a single line on the forum thread - this enables the 'onebox' creation - which makes a reciprocal link on the GitHub PR.

Tiers for triaging issues
*************************

The same tiered approach used in triaging PRs is also used with issues. The triage team are responsible for daily/weekly/monthly and quarterly review processes.

Tier 1 issues
=============

Minor issues which are non-critical in nature.

.. vale off

Examples - Tier 1 issues
------------------------

.. vale on

:xref:`github_pr_8974` - an issue with translations

:xref:`github_pr_8986` - checkbox in the wrong place

Tier 2 issues
==============

Issues which are more complex and/or which may impact a large volume of users.

.. vale off

Examples - Tier 2 issues
------------------------

.. vale on

:xref:`github_pr_8621`- impacts all SparkPost users

:xref:`github_pr_7062`- appears often but not always when adding multiple forms on a single page, making it tricky to reproduce

Tier 3 issues
=============

Complex issues which impact multiple areas of Mautic or which require extensive debugging to identify/resolve.

.. vale off

Examples - Tier 3 issues
------------------------

.. vale on

:xref:`github_pr_9072`- likely touches many areas and is complex to solve, requiring in-depth technical knowledge of PHPUnit

:xref:`github_pr_7032`- took a lot of time to confirm the issue and find a proper solution without breaking other things

Labels
======

There are quite a lot of :xref:`Mautic labels`, organized as below:

Complexity-based labels
-----------------------

* Tier 1-2-3 [T1, T2, T3] - used for both pull requests and issues

Semantic versioning related labels
----------------------------------

* BC Break
* Deprecation
* Essential - required to close the milestone

Type-based labels
-----------------

* Bug
* New feature
* Enhancement
* Dependencies - used by Dependabot
* Regression

Status-based labels
-------------------

* Needs triage
* rebase needed
* WIP - Work In Progress
* Requires automated tests
* Requires documentation
* Requires code review
* Pending feedback
* Pending code changes
* Has conflicts
* Ready to test - PRs only, and only applied when the PR is passing tests, has no conflicts, has automated tests written and considered ready for merging
* Pending test confirmation - PRs only, and only applied when the PR is passing tests, has no conflicts, has automated tests written and considered ready for merging
* Ready to commit - PRs only, and only applied when the PR is passing tests, has no conflicts, has automated tests written, has the required signoff/approvals and considered ready for merging

Area Affected Labels - which part of the product does this affect?
==================================================================

* Assets
* Builders - email and LP
* Calendar
* Campaigns
* Categories
* Channels
* Companies
* Configuration
* Contacts
* Dashboard
* Dynamic Content
* Editor
* Email
* File Uploader
* Focus Items
* Forms
* Import Export
* Installation
* Integrations
* Landing Pages
* Notifications
* Plugin
* Points/Scoring
* Queue
* Reports
* Roles
* Segments
* SMS
* Social Monitoring
* Stages
* Tags
* Tracking
* Translations
* User Interface
* User Experience
* Webhooks
* Widgets

Some points of clarification
============================

**Core Team:** individuals with technical ability to manage and maintain the core of Mautic - includes Release Leaders, Core Committers, Maintainers - see :ref:`Contributors, Maintainers, and the Core Team` for more details.

**Product Team:** members of the Mautic :doc:`/teams/product_team`. They may also be part of the Core Team, but not necessarily. Currently listed on the :xref:`Mautic Product Team` page.

**Triage Team:**  members of the Mautic Product Team who are responsible for triaging issues and PRs. They may also be part of the Core Team, but not necessarily.

**Code review and testing:** by people other than the author of the PR.

**Closing Stale PRs:** if the PR is pending feedback or inactive for over 30 days, the Product Team may decide to close the PR.

**Closing stale issues:** if the issue is pending feedback or inactive for over 14 days, the Product Team may decide to close the issue.

Branching strategy
******************

As Mautic maintains multiple major and minor versions of Mautic  - for example ``5.x``, ``6.x`` and ``7.x``, there is a defined branching strategy in use on GitHub.

Please refer to the resources in the :doc:`Contributing to Mautic </contributing/contributing_docs_rst>` page to understand the branching strategy.

Mautic has started to create a :xref:`Supported Versions` table on GitHub and updates that throughout the year with more specific dates.
