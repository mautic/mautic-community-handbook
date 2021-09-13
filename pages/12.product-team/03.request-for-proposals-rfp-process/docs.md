---
title: 'Request for Proposals (RFP) process'
twitterenable: true
twittercardoptions: summary
articleenabled: false
personenabled: false
facebookenable: true
---

## Background
In 2020 we kick-started the development of several Strategic Initiatives which were announced at Mautic Conference Global.  We have also had several community-generated ideas for new features which have been proposed over the past two years, some of which have required funding and are at varying stages of completion.

We have learned a lot and as a result, we are implementing a clearly defined Request for Proposals (RFP) process outlining how we manage projects which bring features or larger bug fixes into Mautic.  Some aspects of this are based on the model used by the [OBS open source project][obs].

## Why do we need an RFP process?

The aim of this process is to create an open and transparent workflow for larger projects which are being planned or are 'in flight' within the community. Projects may relate to new features, but could equally be fixing a large or complex problem in Mautic.

The process gives greater clarity throughout the whole lifecycle to Mautic users regarding how features and larger projects are added to the roadmap, worked on, and eventually released.

It is also hoped that this process allows us to better manage compensating contributors for working on these larger projects while also allowing community members to decide to financially support projects that they care about.

## Workflow

The following workflow will be followed for new projects within Mautic:

1. An idea is shared on the Mautic Community Forums ‘[Ideas and Feature Requests][ideas-forum]’ section for discussion by the community.
2. The Product Team reviews the requested features with the Project Lead on a quarterly basis and determines which are candidates for consideration on the roadmap.  Note that bugs (such as an integration needing to be upgraded or something else requiring considerable work) as well as features can also be considered for an RFP.
3. The Product Team works with the original proposer of the idea to prepare a detailed Request for Proposal (RFP) including stating what funds would be allocated to the project (both from the Product Team budget and from Community fundraising if required) which is reviewed by the Project Lead.
4. If the proposal impacts any areas covered by Tiger Teams, the Tiger Teams will be key stakeholders throughout the process of the RFP and be the final sign off before release.
5. Where the RFP is accepted, the Product Team publishes a RFP on GitHub Discussions describing in detail the feature, key requirements and deliverables, timelines, and the project budget available.
6. If further funding is required above what the Product Team can provide, the Proposal Status will be set to Fundraising until such a time as the required budget has been raised.
7. When the funding target has been reached, the proposal Status is set to Accepting Proposals.
8. Developers write proposals for how they would implement the feature described in the RFP.
9. The Mautic Core Team works with developers within the GitHub Discussion thread to clarify and refine their proposals.
10. A proposal is accepted. The developer(s) responsible for the proposal work to implement the feature according to their proposal.
11. Proposal status changed to In Progress
12. Pull requests are submitted to implement the proposal by the developers.
13. Initiative status changed to Under Review
14. Pull requests are reviewed by the Core Team, and the pull request developers make any changes to the pull requests accordingly.
15. Pull requests are merged into the appropriate branch.
16. Developer(s) submit an invoice to the Mautic Project Open Collective project for the amount associated with the RFP, which will be reviewed and approved for payment by the Project Lead.
17. Initiative status changed to Completed
18. Payment disbursed to developer(s) by the Open Source Collective from Mautic Project collective funds.

>>>>> [Mautic Community Partners][partners] have the option to propose up to three features per calendar year which can be considered for inclusion as an RFP without going through the community voting process (but must still be approved by the Product Team and Project Lead) - for example if there are features which they would like to see in Mautic but they don’t have the resources internally to work on them, but could put some money towards someone in the community working on that project.

## How to Claim a Project
We've created a process to ensure multiple contributors aren’t competing on the same project, and to make sure work is properly merged into Mautic once completed.

1. Read the Request For Proposal document completely.
2. If you want to move forward, submit a proposal to the Product Team on your suggested implementation by replying to the RFP posting. Be sure to include as many details as requested by the spec, and be sure to address each of the completion criteria. For proposals that include UI changes, mockups are strongly encouraged (we use Miro but whatever tool you use, please ensure that it has the ability for us to collaborate and provide feedback).
3. Be sure to consult the [Tips for Writing a Good Proposal][tips] for advice on how to author a good proposal.
4. Work with the Product Team to finalize plans for the best implementation. Proposals will be judged on their maintainability, design quality, and adherence to spec. Note that other developers may submit competing proposals at this time as well.
5. If your proposal is accepted, you may begin code implementation that adheres to your proposal and following the Mautic contributing guidelines.
6. Submit code as a draft PR in the appropriate Mautic repositories so that the Core Team can track progress.
7. Once code is complete, remove draft status and notify the Core Team (use @mautic/core-team to ping them).
8. Update code with feedback from the Core Team as needed.
9. Wait for your code to be merged into the appropriate branch.
10. Submit an expense to Open Collective for the amount of the project.

### Collaboration with the Mautic Product Team
Collaboration with the Product and Core Team is crucial to having your code pulled into Mautic. 

During the proposal process, clarify any questions you or your team may have as early as possible. 

During development, use the pull request commenting feature. At any time, you can also comment in the #dev channel in the Mautic Slack instance here: https://mautic.org/slack, though we encourage you to keep as much discussion on the RFP and pull requests as possible to keep the discussion public.

### Deadlines
If your team does not show code commits or interaction for two weeks at a time as part of an accepted project, then the RFP will be released for another team to work on. If the task remains in the Accepting Proposals state, and the team can demonstrate work on the feature, they can reclaim the task.

If you no longer wish to work on a project that has been granted to you, please notify the Product Team to reset the RFP as Accepting Proposals.

## Funding Evaluation
The Mautic team currently uses a simple rubric to determine how to price an RFP. Generally speaking, RFPs are evaluated based on two main criteria:

* How complex is the project?
	* How long do we expect it may take to complete?
	* How much specialized knowledge do we expect it will require to implement?
* How high a demand is there for this project?
	* How many people do we expect this to impact?
	* How frequently are we asked about this feature or bug?
	* How urgently does this need to be implemented?

In general, issues that are higher in complexity and higher in demand are given greater value.

The Product Team has a fixed allocation each year to use for funding these projects, which is directly related to the amount of funds available in the budget.  In the event that a project requires more funds than the Product Team has available, a project on Open Collective will be opened to raise the required amount. 

## What about Strategic Initiatives?
Strategic Initiatives will be proposed in the same way going forward, and will be funded from a separate budget line. Proposals will be sought and approved as detailed above.

Strategic Initiatives are proposed by the Project Lead, and do not go through the community voting process.

As Strategic Initiatives are often larger projects, it is likely that they may consist of several smaller projects. This should be made clear in the RFP with a ‘big picture’ overview being provided of how it fits into the wider Initiative.

## How do we budget for funding RFPs?
From the 2022 budget forward, a percentage of the budget (to be agreed by the Community Council) will be allocated to the Product Team for the purpose of funding the RFP process. 

This will be maintained in a separate project on the Mautic Open Collective, so that people can make donations there if they specifically want their funds to be used for this purpose.

If an RFP or Strategic Initiative requires more funding than is available through the budget, a separate project can be established and fundraising from the community can be undertaken to raise the required amounts.

Strategic Initiatives will continue to have a separate budget line and will also generally have a separate project on the Mautic Open Collective.

## Tips for Writing a Good Proposal
The Mautic Community is now soliciting proposals for a number of features and bugs that we want to direct community efforts toward. We are using a "Request For Proposals" system as detailed above, whereby each project acts as a specification, and requests that potential developers submit proposals for how they would approach the design and development of the specified feature or bug.

This document is intended to be a guide for would-be contributors to the project who wish to submit a proposal to ensure their proposal has sufficient detail in order to be considered for acceptance.

### Tips
* Be sure your proposal addressed all requirements in the "Request For Proposal" section of the RFP.
* If your proposal includes changes to the UI, include mockups where possible. These do not need to be fancy, but should at least communicate the concept behind what you intend to change.
* If your proposal requires the use of a new library, please include a discussion of why you chose the given library, and why you did not go with alternatives.
* Implementation details should err on the side of specificity. Details on any new planned APIs, data structures, and architectural considerations are appreciated.
* Time estimates are not required by any means, and we know that commitment level can vary given open source work is largely done during people's free time. However, a very rough estimate would be appreciated, if reasonable for you to include.

## Credits

This process has drawn heavily from the [OBS Project][obs] who have adopted a similar workflow for their bounty programme with their GitHub repository and Open Collective.

[obs]: <https://github.com/obsproject/obs-studio/wiki/OBS-Project-Bounty-Program>
[ideas-forum]: <https://forum.mautic.org/ideas>
[partners]: <https://mautic.org/mautic-community-partners>
[tips]: <#tips>