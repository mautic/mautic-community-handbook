Slack - asynchronous - meetings
###############################

Slack threads are a great way to hold meetings because:

- They don't rely on everybody being available to attend the meeting at a specific time - often asynchronous meetings are open for 24 hours
- They don't require the ability to keep pace with a verbal conversation, which can be tricky for those with disabilities or for whom English isn't their first language
- There is a written record of the meeting which can be easily exported

Mautic uses asynchronous Slack meetings heavily in the Mautic community, and it's likely that you'll at some point need to run one.

.. vale off

Running an asynchronous Slack meeting
*************************************

.. vale on

Here are some tips for running a great meeting:

1. Prepare for the meeting as you would for any other - share an agenda at least 24 hours before the meeting is due to start, ideally on Slack, the Community Portal and on the forums, to remind people, to give them time to prepare, and to encourage involvement/engagement
2. Send a reminder 24 hours before the meeting in the relevant Slack channel with the agenda - mention people directly if they're a required attendee
3. Prepare your topics in advance based on the agenda, so that you can copy and paste them into the Slack channel without manually typing them at the time. You can send them to yourself in Slack, so that you have an easy-to-access record.
4. Remember to use the welcome post and the introduction thread - this welcomes people, explains how the meeting works, and allows people to say who they're, and what they do - don't assume that people joining know this, they might be completely new to the community.
5. Take the meeting at the normal pace you would a regular meeting - give people time to chime in on the topic and have the discussions before posting the next topic. This helps to avoid distraction during the meeting and thread-jumping.
6. Always welcome new meeting attendees, and follow up if people have dropped off and stopped attending
7. Encourage participation by mentioning people who might want to discuss the topic, or consider taking on a task
8. Close the meeting by thanking people for joining
9. Don't forget to export the notes 24 hrs - approximately - after the meeting started

.. vale off

Exporting Slack meetings
************************

.. vale on

Mautic uses a fork of a Chrome extension created by the Drupal community to scrape Slack meeting notes into HTML, which is then posted onto the forums.

Instructions are in the GitHub repository: :xref:`Mautic Meeting Parser`

Sample meeting structure
************************

Welcome message
===============

.. code-block:: 
   
   Welcome to the team meeting!
   
   If you haven't done an asynchronous meeting before, please respond in threads :slightly_smiling_face:

   Also note you can start a reply with :bust_in_silhouette: to be anon, or :no_entry_sign: to go off the record and not be included in the notes, which will be exported and saved to Google Docs, and posted on the Community Forums.

   The meeting will be open for 24 hours, after which the notes will be exported. People may comment thereafter but these won't be included in the notes.

   Let's get going! :arrow_down:

Topics
======

.. code-block:: 

   :zero:- Introductions : Who are you, where are you based, and how are you involved with this team?

   :one:- Review last meeting's notes and actions (Share a link to the notes in a threaded reply, and call out any actions as sub tasks)

   :one:.:one:- Action item 1 
   :one:.:two:- Action item 2

   :two:- Review Trello tasks (share a link to the Trello board in a threaded reply, and call out any tasks as appropriate)

   :two:.:one:- Task 1 (Link to task in a threaded reply, brief explanation of status or actions needed)
   
   (continue through the open tasks)

   :three:- Any other business

   Thank people for participating and give the date/time/format for the next meeting and who will be leading it