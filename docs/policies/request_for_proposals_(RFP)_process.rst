Request for Proposals process
#############################

Background
**********

.. vale off

In 2020, Mautic launched several Strategic Initiatives announced at Mautic Conference Global. Over the past two years, there have also been numerous community-generated ideas for new features. Some of these ideas require funding and are at various stages of development.

Through experience, Mautic has learned the importance of a well-defined Request for Proposals - RFP - process to manage projects that introduce new features or address major bug fixes in Mautic. This approach takes inspiration from the :xref:`OBS open-source project's model`.

.. vale on

Why does Mautic need an RFP process?
************************************

This process aims to establish an open and transparent workflow for large community-driven projects, whether they focus on new features or significant issue resolutions in Mautic. It provides a clear lifecycle from the initial idea through to release, allowing Mautic users to see how features and larger projects get proposed, worked on, and completed.

Additionally, the RFP process helps Mautic better manage compensation for contributors working on these larger projects and provides a means for the community to financially support projects they value.

Workflow
********

The following steps outline the RFP workflow for new projects in Mautic:

#. A project idea thread begins in the Mautic Community Forums under the :xref:`Ideas and Feature Requests` section for community discussion.
#. The Product Team reviews requested features with the Project Lead quarterly and determines which are candidates for consideration on the roadmap. The Product Team reviews requested features with the Project Lead quarterly and determines which ones are candidates for consideration on the roadmap. Note that bugs - such as an Integration needing upgrade or something else requiring considerable work - as well as features can also start life as an RFP.
#. The Product Team considers feedback from the community, and where there's a clear interest in moving forward with an idea, collaborates with the original proposer to prepare a detailed proposal, including budget estimates from the Product Team and any necessary community fundraising. The Project Lead reviews this.
#. If the proposal impacts any areas covered by Tiger Teams, the Tiger Teams are key stakeholders throughout the RFP process and must sign off before release.
#. When the Product Team and proposer create the proposal, it's uploaded to the :xref:`Mautic community portal roadmap process` for wider discussion and debate. The proposer tags the key stakeholders in the proposal to ensure they're aware of the proposal, and they must formally endorse it prior to acceptance.
#. If the budget exceeds what the Product Team can provide, the proposal status 'Funding required' applies until such a time as the required funds become available. Mautic can create an Open Collective project to raise the necessary funds.
#. When reaching the funding target, the proposal status moves to 'Ready for development'.
#. Where the proposer is a developer, they commence work. Where a developer isn't yet identified, Mautic creates a post in the Commercial forum category and the ``#jobs`` channel on Slack advertising the project opportunity. The proposer can also source their own developers to work on the project.
#. The Mautic Core Team works with interested developers within the Community Portal to clarify and refine their proposals for implementing the feature.
#. A developer is selected. They become responsible for implementing the feature according to the proposal.
#. The proposal status changes to 'In Progress'.
#. The developers submit pull requests to implement the proposal.
#. The proposal status changes to 'Under Review'.
#. The Core Team reviews pull requests, and the developers make any changes to the pull requests accordingly.
#. Pull requests get merged into the appropriate branch.
#. Developers submit an invoice to the Mautic Project Open Collective project for the amount associated with the RFP, which the Project Lead reviews and approves for payment.
#. The proposal status changed to 'Completed'.
#. Payment disbursed to developers by the Open Source Collective from Mautic Project collective funds.

.. note::
   :xref:`Mautic Partners` may propose up to three features per calendar year for consideration as an RFP without going through community voting. These features still require approval by the Product Team and Project Lead.

How to claim a project
**********************

To ensure multiple contributors aren't competing on the same project and to streamline the merging process, follow these steps:

#. Read the Proposal document completely.
#. If you want to move forward, submit a pitch via the comments on the proposal to the Product Team on your suggested implementation. Be sure to include as many details as requested by the spec and address each of the completion criteria. For proposals that include UI changes, mock-ups are strongly encouraged - Mautic uses Figma, but whatever tool you use, please ensure that it allows everyone to collaborate and provide feedback.
#. Be sure to consult the :ref:`Tips for writing a good pitch` for advice on how to write a good pitch.
#. Work with the Product Team to finalize plans for the best implementation. The Core Team judges pitches on their maintainability, design quality, and adherence to spec. Note that other developers may submit competing pitches at this time.
#. If the Core Team accepts your pitch, you may begin code implementation that adheres to your proposal and ensure you follow the Mautic contributing guidelines.
#. Submit the code as a draft PR in the appropriate Mautic repositories so that the Core Team can track the progress.
#. Once the code is complete, remove the draft status and notify the Core Team - use ``@mautic/core-team`` to ping them.
#. Update the code with feedback from the Core Team as needed.
#. Write the documentation required - this might include developer and/or end-user documentation.
#. Wait for the maintainers to merge your code into the appropriate branch.
#. Submit an expense to Open Collective for the amount of the project.

.. vale off

Collaboration with the Mautic Product Team
******************************************

.. vale on

Collaborating with the Product and Core Teams is essential for successful code integration into Mautic. During the proposal process, address any questions early on. During development, use the pull request comment feature for feedback. For additional communication, the ``#dev`` channel in :xref:`Mautic Community Slack` is available, though it's encouraged to keep discussions on the RFP and PRs for transparency.

Deadlines
*********

If no code commits or interactions happen over two weeks in an accepted project, the Core Team may reassign the RFP to another developer. If the task remains in the 'Accepting Proposals' state, and the team can demonstrate work on the feature, they can reclaim the task. Notify the Product Team if you wish to withdraw from a granted project so they can reset it to the 'Accepting Proposals' state.

Funding evaluation
******************

The Mautic team uses a basic rubric to determine RFP pricing. Generally speaking, the team evaluates requests for proposals based on two main criteria:

* How complex is the project?
	* How long is it expected that it may take to complete?
	* What level of specialized knowledge is required from the developer for implementation?
* How high demand is there for this project?
	* How many people is it going to impact?
	* How frequently do people ask about this feature or bug?
	* How urgent is the need for this implementation?

In general, issues that are more complex and in higher demand attract greater value.

The Product Team has a fixed allocation each year to use for funding these projects, which is directly related to the amount of funds available in the budget. In the event that a project requires more funds than the Product Team has available, a project on Open Collective can help raise the amount needed.

.. vale off

What about Strategic Initiatives?
*********************************

.. vale on

Strategic Initiatives follow the same proposal process, but they're separately funded. Proposed by the Project Lead, they don't undergo community voting.

As Strategic Initiatives are larger projects, they may consist of smaller projects. The RFP should clarify how each project fits into the larger initiative.

How does Mautic budget for funding requests for proposals?
**********************************************************

Starting in 2022, the Council may allocate a portion of the budget to the Product Team to fund the RFP process. These funds exist in a separate project on Mautic Open Collective, allowing targeted donations.

If an RFP or Strategic Initiative requires additional funds, a dedicated fundraising project or seeking grant funding may help. Strategic Initiatives continue to have a separate budget and may have their own Open Collective project.

Tips for writing a good pitch
*****************************

The Mautic Community is now soliciting proposals for a number of features and bugs that require attention. A 'Request For Proposals' system, as detailed previously, is in use, whereby each proposal acts as a specification and requests that potential developers submit a pitch for how they would approach the design and development of the specified feature or bug.

It's intended that this proposal serves as a guide for potential contributors to the project who wish to submit a pitch, ensuring their pitch includes sufficient detail for consideration.

Tips
====

* Be sure your proposal addresses all requirements in the 'Request For Proposal' section of the RFP.
* If your proposal includes changes to the UI, include mock-ups where possible. These don't need to be fancy, but they should at least communicate the concept behind what you intend to change so that the UX/UI Tiger Team can provide input and direction.
* If your proposal requires the use of a new library, please include a discussion of why you chose the given library and why you didn't go with alternatives. Ideally, this should happen as a debate on the Community Portal.
* Implementation details should err on the side of specificity. Details on any new planned API endpoints, data structures, and architectural considerations can be helpful.
* Time estimates help the Product Team to plan releases, and while it's understood that commitment level can vary given open source work is largely done during people's free time, you must provide a rough estimate of when the work should be ready for testing.

Credits
*******

.. vale off

This process is heavily inspired by the :xref:`OBS open-source project's model`, which uses a similar workflow for its bounty program.

.. vale on