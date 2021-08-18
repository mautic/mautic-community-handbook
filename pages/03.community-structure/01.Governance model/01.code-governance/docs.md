---
title: 'Code governance'
---

---

Tiers for triaging pull requests
-----------------------------------------

We have adopted a tier-based approach to categorising pull requests (PRs) in the Mautic Community. This allows the Product Team to establish clear governance approaches to how PRs will be dealt with and what the criteria will be for merging.

This allows the processing of minor fixes and improvements more rapidly, while time-boxing community testing for major pull requests, enabling the Product Team to make decisions on whether to merge new features once those time periods have passed.

### Tier 1

Small changes such as typo fixing, bug fixes, translation changes, minor UI improvements or minor enhancements. Most simple bug fixes are probably going to be in Tier 1.

#### Examples

[https://github.com/mautic/mautic/pull/8393](https://github.com/mautic/mautic/pull/8393) (simple bug fix with very few changes)

[https://github.com/mautic/mautic/pull/8116/files](https://github.com/mautic/mautic/pull/8116/files) (very simple bug fix)

#### Requirements for merging a Tier 1 PR

*   Thorough testing to ensure that it does what it’s expected to do and does not break anything else
    
*   Full unit testing coverage
    
*   Code review from 1 core team member
    
*   Full testing and approval by at least one community member (could be the person doing the code review, but should not be from the same company/organisation as the person submitting the PR).  
      
As an example: If an employee or contractor from Company A were to submit a PR, the community testing/approval must come from someone outside Company A’s influence (e.g. not an employee, contractor etc of Company A)

### Tier 2

Minor features or enhancements which do not significantly change any part of Mautic.

More complex bug fixes are also probably going to be in Tier 2, as well as PRs that are related to external services (e.g. Salesforce/HubSpot) for which accounts need to be created in order to test.

#### Examples

[https://github.com/mautic/mautic/pull/6090](https://github.com/mautic/mautic/pull/6090) (new feature, fairly simple and doesn’t significantly change any major part of Mautic)

[https://github.com/mautic/mautic/pull/7432/](https://github.com/mautic/mautic/pull/7432/files) (a lot of new code which extends an existing feature, enhancing reports with a scheduling option)

#### Requirements for merging a Tier 2 PR

*   Thorough testing to ensure that it does what it’s expected to do and does not break anything else
    
*   Full unit/functional test coverage
    
*   Full documentation support if it’s a feature change/addition
    
*   Code review from 1 core team member
    
*   Full testing and approval by at least one community member (could be the person doing the code review, but should not be from the same company/organisation as the person submitting the PR as mentioned above)
    

### Tier 3

Major changes touching multiple parts of Mautic, completely changing the way some aspect of the code works, or large amounts of code changed.

#### Examples

[https://github.com/mautic/mautic/pull/6875](https://github.com/mautic/mautic/pull/6875) (complex code changes across multiple areas, with significant impact)  
  
[https://github.com/mautic/mautic/pull/6584](https://github.com/mautic/mautic/pull/6584) (not too complex but a large visual change in the UI with the potential to cause significant disruption to the end user)

#### Requirements for merging a Tier 3 PR

*   Thorough testing to ensure that it does what it’s expected to do and does not break anything else
    
*   Thorough testing across the whole product
    
*   Full unit/functional test coverage
    
*   Full documentation support
    
*   Code review from 1-2 core team members
    
*   Full testing and approval by at least two community members (could be the people doing the review, but should not be from the same company/organisation as the person submitting the PR as mentioned above)
    
*   2 week community review period - after which Product Team decides via a vote in the next available team meeting whether to merge (assuming code review and all other requirements are in place to permit merging)
    

Note: Tier 3 PRs which relate to new features that impact users of Mautic should be **linked to in an individual forum thread** at [forum.mautic.org/c/ideas](https://forum.mautic.org) and discussed on the forums. This gives the non-technical user base an opportunity to be involved in the discussions on new features.

If a thread doesn’t exist prior to the PR being submitted (a feature created without the community suggesting it, for example), it should be created during triage when a Tier 3 & Feature label is added.

The Github URL should be shared in a single line on the forum thread (enables the ‘onebox’ to be created) which will create a reciprocal link on the Github PR.

Tiers for triaging issues
----------------------------------

The same tiered approach used in triaging pull requests is also used with issues. The triage team are responsible for daily/weekly/monthly and quarterly review processes.

### Tier 1 issues

Minor issues which are non-critical in nature.

#### Examples

[https://github.com/mautic/mautic/issues/8974](https://github.com/mautic/mautic/issues/8974) \- an issue with translations

[https://github.com/mautic/mautic/issues/8986](https://github.com/mautic/mautic/issues/8986) \- checkbox in the wrong place

### Tier 2 issues

Issues which are more complex and/or which may impact a large volume of users.

#### Examples

[https://github.com/mautic/mautic/issues/8621](https://github.com/mautic/mautic/issues/8621) \- impacts all Sparkpost users

[https://github.com/mautic/mautic/issues/7062](https://github.com/mautic/mautic/issues/7062) \- appears often but not always when multiple forms are added on a single page, making it tricky to reproduce

### Tier 3 issues

Complex issues which impact multiple areas of Mautic or which require extensive debugging to identify/resolve.

#### Examples

[https://github.com/mautic/mautic/issues/9072](https://github.com/mautic/mautic/issues/9072) \- will likely touch many areas and is complex to solve, requiring in-depth technical knowledge of PHPUnit

[https://github.com/mautic/mautic/issues/7032](https://github.com/mautic/mautic/issues/7032) \- took a lot of time to confirm the issue and find a proper solution without breaking other things

### Labels

We currently have [quite a lot of labels](https://github.com/mautic/mautic/labels?page=1&sort=name-asc) which are organised as below.

#### Complexity-based labels

*   Tier 1-2-3 \[T1, T2, T3\] (for PR’s and issues) 

#### Semantic versioning related labels

*   BC Break
    
*   Deprecation
    
*   Essential (required to close the milestone)
    
#### Type-based labels

*   Bug
    
*   New feature
    
*   Enhancement
    
*   Dependencies (used by Dependabot)
    
*   Regression

#### Status-based labels

*   Needs triage
    
*   Rebase needed
    
*   WIP
    
*   Requires automated tests
    
*   Requires documentation
    
*   Requires code review
    
*   Pending feedback
    
*   Pending code changes
    
*   Has conflicts
    
*   Ready to test (PR’s only, and only applied when the PR is passing tests, has no conflicts, has automated tests written and is mergeable)
    
*   Pending test confirmation (PR’s only, and only applied when the PR is passing tests, has no conflicts, has automated tests written and is mergeable)
    
*   Ready to commit (PR’s only, and only applied when the PR is passing tests, has no conflicts, has automated tests written, has the required signoff/approvals and is mergeable)

### Area affected labels (which part of the product does this affect?)

*   Assets
    
*   Builders (email and LP)
    
*   Calendar
    
*   Campaigns
    
*   Categories
    
*   Channels
    
*   Companies
    
*   Configuration
    
*   Contacts
    
*   Dashboard
    
*   Dynamic Content
    
*   Editor
    
*   Email
    
*   File Uploader
    
*   Focus Items
    
*   Forms
    
*   Import Export
    
*   Installation
    
*   Integrations
    
*   Landing Pages
    
*   Notifications
    
*   Plugin
    
*   Points/Scoring
    
*   Queue
    
*   Reports
    
*   Roles
    
*   Segments
    
*   SMS
    
*   Social Monitoring
    
*   Stages
    
*   Tags
    
*   Tracking
    
*   Translations
    
*   User Interface
    
*   User Experience
    
*   Webhooks
    
*   Widgets

### Some points of clarification:

**Core team:** individuals selected by the Project Lead with technical ability to manage and maintain the core of Mautic - includes Release Leaders, Core Committers, Maintainers (see [mautic.org/about/governance](https://www.mautic.org/about/governance) ). Currently listed [here](https://github.com/orgs/mautic/teams/core-team/members).

**Product team:** members of the Mautic Product Team. They may also be part of the Core Team, but not necessarily. Currently listed [here](https://github.com/orgs/mautic/teams/product-team/members) .

**Triage Team:** members of the Mautic Product Team who are responsible for triaging issues and PR’s. They may also be part of the Core Team, but not necessarily. Currently listed [here](https://github.com/orgs/mautic/teams/triage-team/members) .

**Code review and testing:** must not be done by the author of the PR.

**Closing stale pull requests:** If the PR is pending feedback or inactive for over 30 days, the Product Team may decide to close the PR.

**Closing stale issues:** If the issue is pending feedback or inactive for over 14 days, the Product Team may decide to close the issue.

## Branching strategy

As we maintain multiple major and minor versions of Mautic (2.x, 3.x, 4.x), we use a defined branching strategy on GitHub. 

If you are not familiar with [Semantic Versioning](https://semver.org/) terminology like “major/minor/patch version”, we recommend checking out [this page](https://semver.org/).

From Mautic 3.0, the following approach is taken:

Mautic follows [Semantic Versioning][semver], which is best illustrated by an example. Let's say we just released a 3.2.0 version of Mautic, the following would apply:

|Mautic version|Breaking changes/features allowed?|New features/enhancements allowed?|Bug fixes allowed?|
|---|---|---|---|
|3.2.1|❌|❌|✅|
|3.3.0|❌|✅|✅|
|4.0.0|✅|✅|✅|

You can determine on which branch to work as follows:

- `3.2` (for example), if you are fixing a bug for an existing version of Mautic
- `features`, if you are adding a new feature

**features branch** is used for active development of new features in Mautic which will be released in the next minor release (e.g. 3.2.0). 

**x.x branches** are used to maintain minor versions of Mautic after they have been released. For example, if we need to provide bug fixes for Mautic 2.16.0, we would check out the 2.16 branch on Git and start working from there. Also, if we’d decide to create a new minor version, like 2.17, and a new major version (like 3.0) has already been released, we’d use the 2.16 branch as the starting point and create 2.17 from there.

By following this branching strategy, we hope it is easier for all parties involved (especially community contributors) to improve Mautic and to maintain multiple versions at the same time. 

We’ve started to create a [Supported Versions table on GitHub](https://github.com/mautic/mautic#supported-versions) and will update that throughout the year with more specific dates.
