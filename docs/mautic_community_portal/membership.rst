Membership
##########

Certain areas of the Community Portal have features restricted to members of Mautic's General Assembly, for example, to interact in the General Assembly, to nominate and vote on proposals for elections, and so forth.

Membership is managed via a list which is regularly uploaded to the Community Portal, containing the currently active members.

Uploading the list
******************

This is currently a manual task which is carried out at least once a week, usually on a Friday.

#. Download [transactions](https://opencollective.com/mautic/transactions) from Open Collective, including the name and email address of the 'opposite account' via a custom export. Filter the list by text in the description field containing 'General Assembly'.
#. Paste the email addresses only (no header row) into the first sheet in [this spreadsheet](https://docs.google.com/spreadsheets/d/1-KEEDalZaFgOJjvs21OIkAnyAYpnny5DGY5T4mgNyqE/edit?usp=sharing) (request access if needed) and go to ``file > download`` to export to csv.
#. Upload the csv file under ``admin panel > membership list > Mautic membership list`` in the Community Portal.
#. Next we need to add the members to the General Assembly. Copy the email address list into the second tab on the sheet, and then paste the names column from your downloaded transactions into the second column and export the sheet
#. Upload the sheet in ``Assembiles > General Assembly > Private users > Import via CSV``.

   .. image:: images/upload-private-members.png
     :width: 800
     :alt: Upload private members

#. You may need to manually re-send the invitations using this icon, if the user did not act on the invitation yet.

   .. image:: images/resend-invite-private-participant.png
     :width: 800
     :alt: Resend private participant invitaion
