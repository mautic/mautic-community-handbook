Membership
##########

.. vale off

Certain areas of the Community Portal have features restricted to members of Mautic's General Assembly, for example, to interact in the General Assembly, to nominate and vote on proposals for elections, and so forth.

Membership is managed via a list which is regularly uploaded to the Community Portal, containing the currently active members.

Uploading the list
******************

This is currently a manual task which is carried out at least once a week, usually on a Friday.

#. Download :xref:`Mautic open collective transactions` from Open Collective - including the name and email address of the 'opposite account' - via a custom export. Filter the list by text in the description field containing 'General Assembly'.

#. Paste the email addresses only - no header row - into the first sheet in this :xref:`Mautic transactions google spreadsheets` - please request access if needed - and go to ``file > download`` to export to CSV.

#. Upload the CSV file under ``admin panel > membership list > Mautic membership list`` in the Community Portal.

#. Next, you need to add the members to the General Assembly. Copy the email address list into the second tab on the sheet, and then paste the names column from your downloaded transactions into the second column and export the sheet.

#. Upload the sheet in ``Assemblies > General Assembly > Private users > Import via CSV``.

   .. image:: images/upload-private-members.png
     :width: 800
     :alt: Upload private members

#. You may need to manually re-send the invitations using 'refresh' icon on the right side, if the user didn't act on the invitation yet.

   .. image:: images/resend-invite-private-participant.png
     :width: 800
     :alt: Resend private participant invitation

.. vale on