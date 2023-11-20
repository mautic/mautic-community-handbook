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

What follows is the Mautic project's way of operating a bounty program for contributions to Mautic Core and officially supported Plugins via the relevant GitHub repositories.

If you have feedback on this policy, please join the next team meeting on Slack in #t-product - get an invite at [mautic.org/slack][mautic-slack].

## About the program

The Mautic core team is very small, and is always looking for new contributors to the Open Source codebase. Mautic's bounty programme is an opportunity to solve neglected but important issues, and also gives members of Mautic an opportunity to boost the prominence of issues which they care about and want resolved by providing a financial incentive. Contributors who fix issues with a bounty associated receive financial compensation via invoices on Open Collective, providing the contribution meets all requirements and a core team member merges their pull request.

## No compromise on quality
As is already the case, pull requests aren't accepted unless they're:

* Completed to a high standard
* Fully covered by automated tests
* Prepared in a reasonable time frame including timely responses to feedback
* Resolving the linked issue in its entirety
* For bug fixes, you must make the pull request must against the upcoming major release branch - for example, 6.x - and the companion PR made against the current minor release branch - for example, 5.1.  All the preceding factors, plus all other criteria relating to pull request quality must pass, and both the PRs merged, to be eligible for payout.

Mautic wants to attract **quality contributions only**. For general guidelines about what's expected in pull requests to Mautic core, see more info [here][pr-requirements].

The issue is only considered complete and approved by Mautic for payment when a by a member of the Mautic Community Core Team merges all related pull requests. 

Developers should only request to work on tasks and projects that they're confident of completing in their entirety, seen through to completion, and which they're capable of working on at their current knowledge and skill level.

Mautic's Product Team is happy to answer questions and provide some limited support, but don't have the capacity to mentor junior developers working on bounty issues - it's expected developers work on the task **without requiring direct support from the team**.

## Workflow for bounty programme contributors
1. Verify you are [able to be paid by Open Collective][oc-payment-methods], and create an account with [Open Collective][open-collective]
2. Search for issues with attached bounties:
	* 	Issues with [bounties][bounty-issues]
4. Express interest by commenting on the issue and ask the Core Team to assign you the issue
5. Open a Pull Request **within 7 days** of assignment to the issue, asking for feedback and review
6. Incorporate feedback from the Core Team, if applicable, **within 7 days** of receiving feedback
7. PR reviewed, approved, and merged by a member of the Core Team
8. Contributor raises invoice on Open Collective with link to the issue and the PRs
9. Mautic Legal & Finance team reviews request and approves where appropriate
10. Contributor paid by Open Collective - payments processed twice a week on Tuesdays and Thursdays

>>> If you live in some countries, you may need to use some workarounds like paying out into a `Payoneer` account. Check the [Open Collective docs][oc-payment-methods] to confirm

### Important notes:

* There are some regions in the world where Open Collective are unable to send money due to limitations from the payment providers used and due to trade restrictions. For full details please review Mautic's [Financial Policy][finance-policy],
* Contributors are responsible for any tax obligations on any earnings which they make through the programme, and Open Collective may require [relevant forms][tax-questions] before withdrawing in excess of $600 per year in funds,
* Ensure that you discuss with any existing employers before taking on paid tasks that they permit this under the terms of your existing contract.

## Workflow for bounty providers
If there is an issue that you want to provide a bounty for, follow these steps.

>>> Please note that providing a bounty doesn't guarantee issue resolution, or that the Core Team accepts the contributions. It also doesn't affect prioritisation by the Core Team and doesn't guarantee a specific release date, or indeed its acceptance into Core.

The Core Team, or any other Mautic member, is able to add funds to the Bounties Project on Open Collective, for a specific issue. To do this:

1. Ensure you're logged in on Open Collective.
2. Go to the [Bounties Project][bounties-project], and scroll down to the Donation button.
3. Enter the amount you wish to donate, and ensure on the next screen that you select the appropriate [Organization][oc-org], if you want an organization to pay and/or display as the funding source. Otherwise it's associated to your individual profile.
4. Provide the necessary payment details and complete payment.
5. Add a comment on the issue with a link to the transaction, stating the amount added to the Bounty pot - a member of the Triage Team can update the issue title with the appropriate amount and add the Bounty label.
6. Wait for - or find - a developer to work on the issue
7. When the pull request is available, **ensure that you test it thoroughly and provide an approval review on Github** - it's a **mandatory requirement** for the Core Team to consider it for merging
8. When merging the pull request - and ensuring any companion pull request is also merged - the contributor raises an invoice on Open Collective and the Core Team representative on the Legal & Finance team approves it for payment.

[mautic-slack]: <https://mautic.org/slack>
[pr-requirements]: </contributing-to-mautic/developer/code/pull-requests>
[bounties-project]: <https://opencollective.com/mautic/projects/bounties>
[oc-payment-methods]:<https://docs.opencollective.com/help/expenses-and-getting-paid/submitting-expenses#payout-methods>
[oc-org]: <https://docs.opencollective.com/help/financial-contributors/organizations>
[open-collective]:<https://opencollective.com>
[bounty-issues]: <https://github.com/search?q=label%3Abounty+owner%3Amautic&type=issues&state=open>
[finance-policy]: </policies/financial-policy#10-foreign-assets-control>
[tax-questions]: <https://docs.opencollective.com/help/expenses-and-getting-paid/tax-information>