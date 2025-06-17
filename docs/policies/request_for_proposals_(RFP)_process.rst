Request for Proposals (RFP) process
####################################

Background
**********
In 2020, Mautic launched several Strategic Initiatives announced at Mautic Conference Global. Over the past two years, there have also been numerous community-generated ideas for new features. Some of these ideas require funding and are at various stages of development.

Through experience, Mautic has learned the importance of a well-defined Request for Proposals - RFP - process to manage projects that introduce new features or address major bug fixes in Mautic. This approach takes inspiration from the :xref:`OBS open-source project's model`.

Why does Mautic need an RFP process?
************************************
This process aims to establish an open and transparent workflow for large community-driven projects, whether they focus on new features or significant issue resolutions in Mautic. It provides a clear lifecycle from the initial idea through to release, allowing those who use Mautic to see how features and larger projects get proposed, worked on, and completed.

Additionally, the RFP process helps Mautic better manage compensation for contributors working on these larger projects and provides a means for the community to financially support projects they value.

Workflow
********
The following steps outline the RFP workflow for new projects in Mautic:

1. A project idea thread begins in the Mautic Community Forums under the :xref:`Ideas and Feature Requests` section for community discussion.
2. The Product Team reviews requested features with the Project Lead quarterly and determines which are candidates for consideration on the roadmap. Note that bugs - such as an Integration needing upgrading or something else requiring considerable work - as well as features can also start life as an RFP.
3. The Product Team considers the feedback from the community, and where there's clear interest in moving forward with an idea, collaborates with the original proposer to prepare a detailed proposal, including budget estimates from the Product Team and any necessary community fundraising. The Project Lead reviews this.
4. If the proposal impacts any areas covered by Tiger Teams, the Tiger Teams are key stakeholders throughout the process of the RFP and must sign off before release.
5. Where the Product Team and proposer create the proposal, it's uploaded to the :xref:`Mautic community portal roadmap process` for wider discussion and debate. The proposer tags the key stakeholders in the proposal to ensure they're aware of the proposal, and they must formally endorse it prior to acceptance.
6. If the budget exceeds what the Product Team can provide, the Proposal Status 'Funding required' applies until such a time as the required funds become available. Mautic can create an Open Collective project to raise the necessary funds.
7. When reaching the funding target, the proposal Status moves to 'ready for development'.
8. Where the proposer is a developer, they commence work. Where a developer isn't yet identified, Mautic creates a post in the Commercial forum category and Jobs channel on Slack advertising the project opportunity. The proposer can also source their own developers to work on the project.
9. The Mautic Core Team works with interested developers within the Community Portal to clarify and refine their proposals for implementing the feature.
10. A developer is selected. They become responsible for the proposal work to implement the feature according to their proposal.
11. Proposal status changed to In Progress
12. Pull requests submitted by the developers to implement the proposal.
13. Proposal status changed to Under Review
14. Pull requests reviewed by the Core Team, and the pull request developers make any changes to the pull requests accordingly.
15. Pull requests merged into the appropriate branch.
16. Developers submit an invoice to the Mautic Project Open Collective project for the amount associated with the RFP, which the Project Lead reviews and approves for payment.
17. Proposal status changed to Completed
18. Payment disbursed to developers by the Open Source Collective from Mautic Project collective funds.

.. note::
   :xref:`Mautic Partners` may propose up to three features per calendar year for consideration as an  RFP without going through community voting. These features still require approval by the Product Team and Project Lead.

How to claim a project
***********************
To ensure multiple contributors aren't competing on the same project, and to streamline the merging process, follow these steps:

1. Read the Proposal document completely.
2. If you want to move forward, submit a pitch via the comments on the proposal to the Product Team on your suggested implementation. Be sure to include as many details as requested by the spec, and be sure to address each of the completion criteria. For proposals that include UI changes, mock-ups are strongly encouraged - we use Figma but whatever tool you use, please ensure that it has the ability for everyone to collaborate and provide feedback.
3. Be sure to consult the :ref:`Tips for writing a good pitch` for advice on how to write a good pitch.
4. Work with the Product Team to finalize plans for the best implementation. The Core Team judges pitches on their maintainability, design quality, and adherence to spec. Note that other developers may submit competing pitches at this time.
5. If the Core Team accepts your pitch, you may begin code implementation that adheres to your proposal and following the Mautic contributing guidelines.
6. Submit code as a draft PR in the appropriate Mautic repositories so that the Core Team can track progress.
7. Once code is complete, remove draft status and notify the Core Team - use ``@mautic/core-team`` to ping them.
8. Update code with feedback from the Core Team as needed.
9. Write the documentation required - this might include developer and/or end-user documentation.
10. Wait for the maintainers to merge your code into the appropriate branch.
11. Submit an expense to Open Collective for the amount of the project.

.. vale off

Collaboration with the Mautic Product Team
******************************************

.. vale on

Collaborating with the Product and Core Teams is essential for successful code integration into Mautic. During the proposal process, address any questions early on. During development, use the pull request comment feature for feedback. For additional communication, the #dev channel in :xref:`Mautic Community Slack` is available, though it's encouraged to keeping discussions on the RFP and PRs for transparency.

Deadlines
*********
If no code commits or interactions happen over two weeks in an accepted project, the Core Team may reassign the RFP to another developer. If the task remains in the Accepting Proposals state, and the team can demonstrate work on the feature, they can reclaim the task. Notify the Product Team if you wish to withdraw from a granted project, allowing it to be reset to "Accepting Proposals."

Funding evaluation
******************
The Mautic team uses a basic rubric to determine RFP pricing, Generally speaking, the team evaluates requests for proposals based on two main criteria:

* How complex is the project?
	* How long is it expected that it may take to complete?
	* How much specialized knowledge is it expected that the developer requires to implement?
* How high a demand is there for this project?
	* How many people is it going to impact?
	* How frequently do people ask about this feature or bug?
	* How urgently does this need implementing?

In general, issues that are higher in complexity and higher in demand attract greater value.

The Product Team has a fixed allocation each year to use for funding these projects, which is directly related to the amount of funds available in the budget. In the event that a project requires more funds than the Product Team has available, a project on Open Collective can help to raise the required amount.

.. vale off

What about Strategic Initiatives?
*********************************

.. vale on

Strategic Initiatives follow the same proposal process but they're separately funded. Proposed by the Project Lead, they don't undergo community voting.

As Strategic Initiatives are larger projects, they may consist of smaller projects. The RFP should clarify how each project fits into the larger initiative.

How do Mautic budget for funding requests for proposals?
********************************************************

Starting in 2022, the Council may allocate a portion of the budget to the Product Team to fund the RFP process. These funds exist in a separate project on Mautic Open Collective, allowing targeted donations.

If an RFP or Strategic Initiative requires additional funds, a dedicated fundraising project or seeking grant funding may help. Strategic Initiatives continue to have a separate budget and may have their own Open Collective project.

Tips for writing a good pitch
*****************************

The Mautic Community is now soliciting proposals for a number of features and bugs that need work. A 'Request For Proposals' system as detailed previously is in use, whereby each proposal acts as a specification, and requests that potential developers submit a pitch for how they would approach the design and development of the specified feature or bug.

It's intended that this proposal be a guide for would-be contributors to the project who wish to submit a pitch to ensure their pitch has sufficient detail for consideration.

Tips
====
* Be sure your proposal addressed all requirements in the 'Request For Proposal' section of the RFP.
* If your proposal includes changes to the UI, include mock-ups where possible. These don't need to be fancy, but should at least communicate the concept behind what you intend to change so that the UX/UI Tiger Team can provide input and direction.
* If your proposal requires the use of a new library, please include a discussion of why you chose the given library, and why you didn't go with alternatives. Ideally this should happen as a debate on the Community Portal.
* Implementation details should err on the side of specificity. Details on any new planned API endpoints, data structures, and architectural considerations can be helpful.
* Time estimates help the Product Team to plan releases, and while it's understood that commitment level can vary given open source work is largely done during people's free time, you must provide a rough estimate of when the work should be ready for testing.

Credits
*******
This process is heavily inspired by the :xref:`OBS open-source project's model`, which uses a similar workflow for its bounty program.