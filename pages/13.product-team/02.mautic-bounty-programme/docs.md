---
title: 'Mautic Bounty Programme'
taxonomy:
    category:
        - docs
twitterenable: true
twittercardoptions: summary
articleenabled: false
orgaenabled: false
orga:
    ratingValue: 2.5
orgaratingenabled: false
personenabled: false
facebookenable: true
---

A bounty programme in Open Source projects is when a monetary reward is offered for completing a task.

What follows is an initial proposal to implement a bounty programme which we will be trialling for six months (January to June 2021) for contributions to Mautic Core via the Github repository.

If you have feedback on this, please join the next team meeting on Slack in #t-product (get an invite at [mautic.org/slack][mautic-slack]).

## About the program

The Mautic Community Product Team is small, and we're always looking for new contributors to our Open Source codebases. Our Bounty programme will enable community members to financially reward developers who work on the issues they care about through our partnership with [Bountysource][bountysource].

With Bountysource, issues in the Github issue queue can have a bounty associated with them by one or more people or organisations. This means that one person could add a single bounty of $500 or 10 people could add a bounty of $50, with the person resolving the issue receiving the funds from Bountysource when the fix or feature is merged.

## No compromise on quality
As is already the case, we will not accept pull requests unless they are:

* Completed to a high standard
* Fully covered by automated tests
* Prepared in a reasonable timeframe
* Resolving the linked issue in its entirety

We want to attract **quality contributions only**. For general guidelines about what's expected in pull requests to Mautic core, see more info [here][pr-requirements].

The issue will only be considered complete and approved by BountySource for payment if the pull request is merged by a member of the Mautic Community Core Team. Read more in the [BountySource FAQs][bs-faq].

Developers may only be assigned tasks and projects that they are confident can be completed in their entirety, seen through to completion, and which they are capable of working on at their current knowledge and skill level.

Our Product Team is happy to answer questions and provide some limited support, but don't have the capacity to mentor junior developers working on bounty issues - developers are expected to work on the task **without requiring direct support from the team**.

## Workflow for Bounty Programme Contributors
1. Create an account with Bountysource
2. Search for issues with attached bounties:
	* 	Issues with [bounties][bounty-issues]
4. Express interest by commenting on the issue and ask to be assigned
5. Open a Pull Request **within 7 days** of being assigned the issue asking for feedback and review
6. Incorporate feedback from the Core Team, if applicable, **within 7 days** of receiving feedback
7. PR is reviewed, approved, and merged by a member of the Core Team
8. Bounty poster/s accept the fix and approve the release of funds
9. Contributor paid by Bountysource

### Important notes:

* There are some regions in the world where we are unable to send money due to limitations from the payment providers used and due to trade restrictions. For full details please check our [Financial Policy][finance-policy],
* Developers will be responsible for any tax obligations on any earnings which they make through the programme, and Bountysource may require [relevant forms][tax-questions] to be completed before withdrawing any funds,
* Ensure that you discuss with any existing employers before taking on paid tasks that this is permitted under the terms of your existing contract.

## Workflow for Bounty Providers
If there is an issue that you want to provide a bounty for, follow these steps.

>>> Please note that providing a bounty does not guarantee that the issue will be resolved, or that the Core Team will accept the contributions. It also does not affect prioritisation by the Core Team and does not guarantee a specific release date, or indeed that it will be merged at all.

1. Create an account with Bountysource
2. Find the issue you wish to support at https://www.bountysource.com/teams/mautic/issues
3. Post your bounty (minimum of $5) - currently you may use regular money (via PayPal) or cryptocurrency (requires Metamask) to post a bounty
4. Choose if you wish to set an expiration date for your bounty if you are contributing more than $100 - this means that if the fix for the issue has not been contributed and merged by the core team by that date, funds will be returned
5. Make the payment using PayPal or Cryptocurrency
6. Wait for (or find) a developer to work on the issue
7. When the pull request is available, ensure that you test it thoroughly and provide an approval review on Github - it is a **mandatory requirement** for the PR to be considered for merging
8. When the pull request is merged, approve the payment for the developer who contributed the work

Read more and find answers to many questions in the [Bountysource FAQs][bs-faq].

[mautic-slack]: <https://mautic.org/slack>
[pr-requirements]: </contributing-to-mautic/developer/code/pull-requests>
[bountysource]: <https://www.bountysource.com/teams/mautic>
[bs-faq]: <https://github.com/bountysource/core/wiki/Frequently-Asked-Questions>
[bounty-issues]: <https://www.bountysource.com/teams/mautic/issues>
[finance-policy]: </policies/financial-policy#10-foreign-assets-control>
[tax-questions]: <https://github.com/bountysource/core/wiki/Frequently-Asked-Questions#do-i-have-to-pay-taxes-on-bounties-i-collect>