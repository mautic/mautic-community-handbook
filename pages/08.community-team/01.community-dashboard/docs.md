---
title: 'Community Dashboard'
twitterenable: true
twittercardoptions: summary
articleenabled: false
orga: {  }
personenabled: false
facebookenable: true
taxonomy:
    category:
        - docs
---

The Community Dashboard uses the open-source [GrimoireLab](https://chaoss.github.io/grimoirelab/) tool to import, analyze and visualize data from multiple sources in one central location.

It is located at [https://dashboard.mautic.org](https://dashboard.mautic.org) and runs on a Digital Ocean droplet, managed by the Mautic Community Infrastructure Working Group.

Currently the dashboad imports:

* All repositories listed under github.com/mautic 
* Specified channels from mautic.slack.com
* All threads on forums.mautic.org
* Specified meetup.com groups

Data sources for GitHub, Slack and Meetup are manually specified in the projects.json file in the root of the instance, so new repositories, channels or meetup groups will not appear automatically.

The data is initially fetched and a 'raw' index is created.  This index is then 'enriched', with individuals and organisations being associated and any other associations being made.

Users can be associated with organisations using the GUI for SortingHat, called Hatstall. This needs an SSH tunnel to be established in order to interrogate and manipulate the data, so you will need to have SSH access to perform these tasks.

The data will automatically update and refresh at regular intervals - you can see when it was last refreshed under the 'Data Status' dashboard.
