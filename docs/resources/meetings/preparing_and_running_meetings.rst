How to prepare & run a Mautic team meeting
##########################################

Meeting cycle - asynchronous versus live meetings
*************************************************

The frequency of team meetings is entirely up to each team to decide - a typical cycle would be **'every 14 days'**. It should normally always be on the same day of week.

When deciding on the hour of the meeting, keep in mind that the Mautic community members live in all time zones of the globe. The primary way to tackle this is to use :doc:`asynchronous meetings <asynchronous_meetings>`,
where all conversation happens in Slack threads - exactly one thread per agenda item - over a period of 24 hours.

There is of course the option to do **live meetings** as well. Some teams do this on a regular basis - for example every second meeting, some 'on demand'. It's highly recommend to add an asynchronous meeting to every live meeting - by writing all highlights from the live meetings down in Slack, and continue from there - to make sure nobody feels excluded, and also to easily capture the minutes from the live part.

Now for those live meetings obviously need an actual time. Even the exact start of an asynchronous meeting isn't irrelevant, since most of the discussion happen within the first 60 minutes or so. And if nothing else, someone - you - has to kick off the meeting at that hour.

So the **exact starting hour** of all scheduled meetings requires a bit of negotiation too. Best practice is: 

a) Find a starting hour that's **convenient for you and most of your active team mates**. 
b) **Consider alternating** between the earliest and the latest convenient hour possible, so that there's the best chances of offering a convenient slot for people in most parts of the world at least every other time.

Always remember to avoid barriers for potential new volunteers - which you are probably not aware of.

Preparing for a meeting
***********************

.. vale off

Add to the Community Portal
===========================

.. vale on

Ensure you add your meeting on your Assembly on the Community Portal. 

High-level agenda
=================

Have a general 'framework' agenda that you typically work with, e.g. 

1. Introductions - who you are, how you're using Mautic 
2. Review last meeting's notes & actions from the Community Portal
3. Review Jira / GitHub board 
4. Specific upcoming events 
5. Any other Business 
6. Ensure that action items are all explicit (ideally: in Jira / GitHub); review priorities
7. Date, time and mode of next team meeting

Feel free to have variations, like: 

- 'swap 1 and 2'
- '1 isn't needed because it's all in Jira / GitHub' 
- '3 doesn't make sense, but ``xyz`` does' 
- 'in 2 it's only needed to look at select items in Jira / GitHub, not the entire backlog' 
- …

Don't forget - please do experiment. Let the structure improve over time, and of course, adopt to temporary circumstances.

Specific topics within the agenda
=================================

Next, collect the existing topics for each top-level agenda item.

This is easy when it comes to 'cards from Jira' or 'Leftover topics from last meeting', but don't forget to be the most forward-thinking person - come up with new areas, thoughts and ideas, and also identify challenges that the time should tackle.

Add an open topic - 'other' - where appropriate.

Example agenda: 

.. code-block:: 
   
   1. Introductions - who you are, how you're using Mautic and whatever else you want to add
   2. Review last meeting's notes & actions 
      1.1 canva.com 

      1.2 Places of Discussion (Slack vs. Trello vs. Forum vs. Github) 

      1.3 Motion to remove Trello integration from t-community

   3. Review Jira  board 

       3.1 Ensure all teams have an onboarding person/workflow …

Make agenda items stick out in Slack
====================================

Instead of regular numbers like 1.4, prefix every item with Slack emojis, for example ``:one:.:four:`` which will show up as:

.. image:: images/slack_emoji_numbers.png
   :width: 60

Your agenda might now look something like this:

.. code-block:: 
   
   :zero: Introductions - who you are, how you're using Mautic and whatever else you want to add

   :one: Review last meeting's (no-Trello) notes & actions 
   :one:.:one: canva.com
   :one:.:two: Places of Discussion (Slack vs. Trello vs. Forum vs. Github)
   :one:.:three: Motion to remove Trello integration from t-community

   :two:  Review Trello board
   :two:.:one: Ensure all teams have an onboarding person/workflow

.. vale off

Share meeting invitation and agenda in Slack
============================================

.. vale on

Remind people about the upcoming meeting, for example the day before.

Most important: 

- Give exact time & date - for example using :xref:`everytimezone` 
- Explain mode of and access to meeting 
- Invite everybody, explicitly including those who haven't previously been active but would like to listen in 
- Mention your team members - using @ mentions - to make sure they actually receive the heads-up

Should you have suitable Social Media channels, feel free to advertise there as well.

If you have your meeting agenda ready, post it on the Community Portal and share it along with the invitation.

Example:
--------

.. code-block:: 

   Hey everyone, we have our #t-community team meeting tomorrow, Thursday:
     UK time: 11:00 am
     Your time: https://everytimezone.com/s/12345 
   This will be an asynchronous meeting so please join the discussion whenever you are available and as often as you can, within the next 24 hours.
   /cc @teammember1 @teammember2 @teammember3 ...

Or, if it's a live meeting:

.. code-block:: 

   Hey everyone, we have our #t-community team meeting tomorrow, Thursday:
     UK time: 11:00 am
     Your time: https://everytimezone.com/s/12345 
   This will be a live meeting, everyone who can make it is very welcome to attend in person via Audio (optionally Video): https://meet.jit.si/mautic-community-team

   For continuation (and also for everybody who can not make it to the live call) we will turn every meeting topic into a thread right here in Slack, so you can still join the asynchronous follow-up discussion whenever you are available and as often as you can, within the next 24 hours.
   /cc @teammember1 @teammember2 @teammember3 ...

Prepare your meeting content
============================

For each sub-level Agenda item, 

1. Prepare contextual information - like link to Jira / GitHub card, 
2. Think hard what you want to achieve, tell or ask on this item, and write that in words, 
3. Even if you have nothing specific, come up with an opening statement for the item.

- Even for the first item - Introductions - it's nice to update your words for every meeting.

As a result, your prepared notes could now look like this:

.. code-block:: 

   :zero: Introductions - who you are, how you're using Mautic and <whatever else you want to add>
   Hi! I'm Ekke, acting team lead, and also part of the largest Mautic agency in the universe. Currently very busy preparing our anniversary party which we're throwing tomorrow. If you're in the area, please come :)

   :one: Review last meeting's (no-Trello) notes & actions 
   https://forum.mautic.org/t/notes-from-meeting-on-28th-february-2020/13153

   :one:.:one: canva.com
   from https://mautic.slack.com/archives/CQV40ULMA/p1582808881044700?thread_ts=1582804260.027100&cid=CQV40ULMA

   :one:.:two: Places of Discussion (Slack vs. Trello vs. Forum vs. Github)
   from https://mautic.slack.com/archives/CQV40ULMA/p1582805125033800

   :one:.:three: Motion to remove Trello integration from t-community
   from https://mautic.slack.com/archives/CQV40ULMA/p1582805125033800 

   :two:  Review Trello board
   https://trello.com/b/OOB4fS1p/mautic-community-team

   :two:.:one: Ensure all teams have an onboarding person/workflow
   We're almost there, so cool!
   @someteammember did you get any feedback from t-xyz already? 

Running the asynchronous meeting
================================

Opening the meeting
-------------------

At exactly the scheduled time, you should hit the enter button and send the opening text for the meeting. Here's an example:

.. code-block:: 

   Hi everyone... Welcome to our team meeting! 

   We're doing this one as asynchronously. If you haven't done an asynchronous meeting before: It's really simple and self-explaining, all you need to remember is
   ---> Please respond in threads :smiley:

   ------
   Also note you can start a reply with 
   :bust_in_silhouette:
    to be anon, or 
   :no_entry_sign:
    to go off the record and not be included in the notes, which will be exported and saved to the Community Portal.

   IMPORTANT: This team meeting starts now and will be open on Slack for 24 hours, after which the notes will be exported. People may comment thereafter but these won't be included in the notes.
   ----
   Let's get going! 
   :arrow_down:

Or, if it's a live meeting:

.. code-block:: 

   Hi everyone... Welcome to our team meeting! 
   We're doing this one live (https://meet.jit.si/mautic-community-team), but add threads in Slack in parallel for asynchronous attendance. If you haven't done an asynchronous meeting before: It's really simple and self-explaining, all you need to remember is
   ---> Please respond in threads  :smiley:

   Also note you can start a reply with 
   :bust_in_silhouette:
    to be anon, or 
   :no_entry_sign:
    to go off the record and not be included in the notes, which will be exported and saved to Google Docs, and posted on the Community Forums.

   --
   This team meeting starts with the live call on https://meet.jit.si/mautic-community-team and will be open on Slack for 24 hours, after which the notes will be exported to the Forum. People may comment thereafter but these won't be included in the meeting notes.
   ----
   Let's get going! 
   :arrow_down:

Kicking off and discussing the agenda items
-------------------------------------------

Next, post the agenda items one by one. Create a thread for each item immediately, using the prepared statements / questions. Hint: try hard to concentrate - it's so easy to mix up posts and threads.

The pace for this can vary, but better get all agenda items launched in the first 15 minutes or so.

Afterwards - or in parallel if you like - you can join the actual discussion. Finally.

Ending the meeting
------------------

After 24 hours - doesn't have to be really exact - you should explicitly end the meeting. One way to do so is by responding to the ``Hi everyone… Welcome to our team meeting!`` post, with the 'Also send to #name of channel' checkbox ticked, something like Thanks everyone, this meeting is now officially over and now is the time to move the content to the forum.

Moving the content to the forum
===============================

Use the :ref:`meeting parser tool <Exporting Slack meetings>`

Live meetings
*************

- Use team's jit.si channel
- Remember to record the meeting
- Take brief notes, place those in the agenda item threads after live ended - adjust agenda if needed
- Upload recording to Google drive :xref:`Mautic Google Drive`