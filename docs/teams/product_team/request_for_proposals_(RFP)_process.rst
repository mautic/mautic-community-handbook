Request for Proposals (RFP) Process
####################################

Background
**********
In 2020, we launched several Strategic Initiatives announced at Mautic Conference Global. Over the past two years, we have also seen numerous community-generated ideas for new features. Some of these ideas require funding and are at various stages of development.

Through experience, we have learned the importance of a well-defined Request for Proposals (RFP) process to manage projects that introduce new features or address major bug fixes in Mautic. Our approach is inspired by the :xref:`OBS open-source project’s model`.

Why Do We Need an RFP Process?
******************************
This process aims to establish an open and transparent workflow for large community-driven projects, whether they focus on new features or significant issue resolutions in Mautic. It provides a clear lifecycle from the initial idea through to release, allowing users to see how features and larger projects are added, worked on, and completed.

Additionally, the RFP process helps us better manage compensation for contributors working on these larger projects and provides a means for the community to financially support projects they value.

Workflow
********
The following steps outline the RFP workflow for new projects in Mautic:

1. A project idea is shared in the Mautic Community Forums under the :xref:`Ideas and Feature Requests` section for community discussion.
2. The Product Team reviews requested features with the Project Lead quarterly and determines which are candidates for consideration on the roadmap.  Note that bugs (such as an integration needing to be upgraded or something else requiring considerable work) as well as features can also be considered for an RFP.
3. The Product Team collaborates with the original proposer to prepare a detailed RFP, including budget estimates from the Product Team and any necessary community fundraising. The Project Lead reviews this.
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

.. note::
   :xref:`Mautic Community Partners` may propose up to three features per calendar year to be considered for RFP without going through community voting. These features still require approval by the Product Team and Project Lead.

How to Claim a Project
***********************
To ensure multiple contributors are not competing on the same project, and to streamline the merging process, follow these steps:

1. Read the Request For Proposal document completely.
2. If you want to move forward, submit a proposal to the Product Team on your suggested implementation by replying to the RFP posting. Be sure to include as many details as requested by the spec, and be sure to address each of the completion criteria. For proposals that include UI changes, mockups are strongly encouraged (we use Miro but whatever tool you use, please ensure that it has the ability for us to collaborate and provide feedback).
3. Be sure to consult the `Tips for Writing a Good Proposal <#tips>`_ for advice on how to author a good proposal.
4. Work with the Product Team to finalize plans for the best implementation. Proposals will be judged on their maintainability, design quality, and adherence to spec. Note that other developers may submit competing proposals at this time as well.
5. If your proposal is accepted, you may begin code implementation that adheres to your proposal and following the Mautic contributing guidelines.
6. Submit code as a draft PR in the appropriate Mautic repositories so that the Core Team can track progress.
7. Once code is complete, remove draft status and notify the Core Team (use @mautic/core-team to ping them).
8. Update code with feedback from the Core Team as needed.
9. Wait for your code to be merged into the appropriate branch.
10. Submit an expense to Open Collective for the amount of the project.

Collaboration with the Mautic Product Team
******************************************
Collaborating with the Product and Core Teams is essential for successful code integration into Mautic. During the proposal process, address any questions early on. During development, use the pull request comment feature for feedback. For additional communication, the #dev channel in :xref:`Mautic Community Slack` is available, though we encourage keeping discussions on the RFP and PRs for transparency.

Deadlines
*********
If no code commits or interactions are shown for two weeks in an accepted project, the RFP may be reassigned. If the task remains in the Accepting Proposals state, and the team can demonstrate work on the feature, they can reclaim the task. Notify the Product Team if you wish to withdraw from a granted project, allowing it to be reset to "Accepting Proposals."

Funding Evaluation
******************
The Mautic team uses a basic rubric to determine RFP pricing, Generally speaking, RFPs are evaluated based on two main criteria:

* How complex is the project?
	* How long do we expect it may take to complete?
	* How much specialized knowledge do we expect it will require to implement?
* How high a demand is there for this project?
	* How many people do we expect this to impact?
	* How frequently are we asked about this feature or bug?
	* How urgently does this need to be implemented?

In general, issues that are higher in complexity and higher in demand are given greater value.

The Product Team has a fixed allocation each year to use for funding these projects, which is directly related to the amount of funds available in the budget.  In the event that a project requires more funds than the Product Team has available, a project on Open Collective will be opened to raise the required amount.

What about Strategic Initiatives?
*********************************

Strategic Initiatives follow the same proposal process and are funded separately. Proposed by the Project Lead, they do not undergo community voting.

As Strategic Initiatives are larger projects, they may be divided into smaller projects. The RFP should clarify how each component fits into the larger initiative.

How Do We Budget for Funding RFPs?
**********************************

Starting in 2022, a portion of the budget (decided by the Community Council) is allocated to the Product Team to fund the RFP process. This is maintained in a separate project on Mautic Open Collective, allowing targeted donations.

If an RFP or Strategic Initiative requires additional funds, a dedicated fundraising project can be launched. Strategic Initiatives will continue to have a separate budget and may have their own Open Collective project.

Tips for Writing a Good Proposal
********************************

The Mautic Community is now soliciting proposals for a number of features and bugs that we want to direct community efforts toward. We are using a "Request For Proposals" system as detailed above, whereby each project acts as a specification, and requests that potential developers submit proposals for how they would approach the design and development of the specified feature or bug.

This document is intended to be a guide for would-be contributors to the project who wish to submit a proposal to ensure their proposal has sufficient detail in order to be considered for acceptance.

Tips
****
* Be sure your proposal addressed all requirements in the "Request For Proposal" section of the RFP.
* If your proposal includes changes to the UI, include mockups where possible. These do not need to be fancy, but should at least communicate the concept behind what you intend to change.
* If your proposal requires the use of a new library, please include a discussion of why you chose the given library, and why you did not go with alternatives.
* Implementation details should err on the side of specificity. Details on any new planned APIs, data structures, and architectural considerations are appreciated.
* Time estimates are not required by any means, and we know that commitment level can vary given open source work is largely done during people's free time. However, a very rough estimate would be appreciated, if reasonable for you to include.

Credits
*******
This process is heavily inspired by the :xref:`OBS open-source project’s model`, which uses a similar workflow for its bounty program.