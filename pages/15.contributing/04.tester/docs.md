---
title: Tester
taxonomy:
    category:
        - docs
twitterenable: true
twittercardoptions: summary
articleenabled: false
personenabled: false
facebookenable: true
---

---

Every new feature and bug fix that is released in Mautic has undergone testing and code review by members of the community before it makes it into a release.

We are always looking out for people to help us with these processes. Even if you can spare an hour or two a week, it would significantly increase the number of bugs and features that make it out into the hands of Mautic users.

Once you have a local testing environment established (or you have a free account on GitHub which allows you to use Gitpod) it is very quick and easy to test bugs and features.

Here is a video which explains the easy way as outlined below:

<div class="grav-youtube"><iframe width="560" height="315" src="https://www.youtube.com/embed/fqnT3kaDaW4?si=KXwViqwFBZzfog9h" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>

We maintain a board which shows you a list of all of the bugs and features that we want to get tested -  check it out here: [Open Source Friday board][open-source-friday-board].

## The easy way: using Gitpod
Since the [4.1 release][mautic-4.1] support for [Gitpod][gitpod] has been introduced. 

This allows you to quickly spin up a Mautic instance with a pull request applied, in the cloud. The Mautic instance also has a mail catching tool (Mailhog) and PHPMyAdmin available to view database tables.  While there will be some pull requests which can't be tested in this way (for example if they are testing the installation process) the vast majority can be.

Testing  a bug or a new feature with Gitpod is as simple as clicking a button once you have installed the [Gitpod Browser Extension][gitpod-browser] in Chrome and Firefox. 

This will add a green 'Gitpod' button on the right hand side of every pull request, and has the added benefit of also adding the button on the main repository and any branch or tag, allowing you to quickly spin up a specific version of Mautic in Gitpod. You can also copy the URL of the PR and open a Gitpod instance manually on your Gitpod dashboard, or using various automation tools like Alfred or Raycast.  

Once you have the browser extension installed, click the green button -  the first time it will ask you to log in with GitHub.  You may wish to open in a new tab, so that it's easy to reference back to the pull request.  Now you just have to wait for Mautic to be installed for you. 

Once the installer is done, it shows the URLs for the Mautic user interface, as well as for Mailhog and PHPMyAdmin (in case you need to check outgoing emails or test things in the database). It also shows you the default credentials to use for the login. Sometimes it can take a few minutes for the process to complete, so please wait until it does!

Then follow the test instructions in the pull request, and [report back your findings][report-findings].  The default username will always be admin, and the password will be `Maut1cR0cks!` (note, if you're testing an older version of Mautic than 5.1, use the password `mautic`.

If you are testing a bug and you need to reproduce this before you apply the pull request, you can use the link [https://gitpod.io/#https://github.com/mautic/mautic][gitpod-default] to spin up a Mautic instance based on our default branch.

### Top tips

#### Installing sample data

To quickly install sample data, use the command `ddev exec bin/console d:f:l` which loads the Doctrine fixtures. It gives you a big head start with testing! 

#### Build the segments after install   

It's always worth building the segments once you install the sample data, using the command `ddev exec bin/console m:s:r`.  

#### Testing with different databases / PHP versions

In DDEV we can set the database and PHP version in a file located in the folder `.ddev/config.yaml`. 

1. Open Gitpod from the PR you are testing and immediately stop the build process as soon as the terminal window is displayed, using command+c or ctrl+c on your keyboard.
2. Delete anything that has already been started with the command `ddev delete --omit-snapshot --yes && rm -rf var/cache && rm app/config/local.php`
3. Edit the file in `.ddev/config.yaml` and change the setting - eg change DB from mariaDB 10.3 to mysql8 - remember to save the file!

```
mariadb_version: ""
mysql_version: "8.0"
```

4. Type ddev start in the console to continue with installation
5. Run the installer in the UI or command line as preferred
6. Check you are using the right version in the system information within Mautic
7. Remember to make sure you are using dev mode (index_dev.php on the end of the URL)
8. If you make a mistake, open your Gitpod dashboard and delete the instance and start again.

## Setting up a local testing environment

### Prerequisites

Before starting you will need a few pieces of software on your computer:
* [Docker Desktop][docker-desktop]
* [DDEV][ddev]
* [Git][git]
* [GitHub CLI][github-cli]

Once you have these installed, we recommend that you use an editor such as [Visual Studio Code][vscode] which will allow you to interact with files, folders and the command line.  There are other editors and Integrated Development Environments (IDEs) so if you already have one that you like, by all means use that!

You will also need to register for an account at [github.com][github] if you don't already have one.  This allows you to leave comments when you've tested things, and also means you can make fixes yourself in the future.

### Downloading Mautic

To start testing, we need to download a copy of Mautic for us to work with.

Before we do that, let's create a folder in your local computer where you'll locate all your local working environments. It's up to you where you save it and what you call it.  Within that folder, create a folder where you'll work on this project - perhaps call it mautic4 for example.

Open your editor, and within the editor, open a terminal window.  

In the terminal, we need to move into the directory we just created.  Use the following commands:

`cd users/yourusername/myfolder/mautic4`

If you need to move up an directory, for example back to /myfolder/, you can use the command:

`cd ..`

Once you are in the folder you want to work from, we need to pull down a copy of Mautic.  To do this, we use a GitHub CLI command:

`gh repo clone mautic/mautic`

The first time you run this command, it will ask you to authenticate with GitHub. Just follow the steps, and once you've set up the authentication it won't bother you for some time.

This will pull down the GitHub repository at [https://github.com/mautic/mautic][mautic-repo] to your local machine, ready for you to start testing with.

### Setting up a local DDEV instance

Now we have the files locally, we need to move into the directory which was created using the command:

`cd mautic`

Now we need to spin up a server on our local computer, so that we can use PHP, MySQL and everything else that Mautic needs to run.

To do this, use the command:

`ddev start`

The first time you run this command it might take a little while to run through the process.

When you are prompted whether to install Mautic, choose `yes`.

This will install all the dependencies that Mautic requires to run, and will install Mautic with a default username and password:

username: admin
password: Maut1cR0cks!

It will also install some software which allows you to capture outgoing emails, called Mailhog, and PHPMyAdmin which enables you to view and interact with the database.

Once this process has completed, you will be able to access your local testing instance at:

`https://mautic.ddev.site`

Log in with the credentials above, and you're ready to go!

## Using developer mode
When testing Mautic, it is important that you are notified of any errors rather than having them output to the logs.  We also don't want to have to constantly rebuild the Javascript and CSS files when changes are made.

For this reason, we use developer mode when testing in the Mautic Community.  

This requires you to add `index_dev.php` to the URL:

`https://mautic.ddev.site/index_dev.php`

## Testing your first pull request

The first step when testing a bug is to attempt reproducing the bug and making sure that you are experiencing the problem that the developer is fixing.

Generally there will be instructions in the description of the pull request, but sometimes you might have to refer to an issue which reported the bug in order to find instructions for reproducing the issue.  If you don't understand, or can't reproduce the issue, please leave a comment and the developer will get back to you with further instructions.

Once you have confirmed the bug, we need to apply the fix.  We do this with another GitHub CLI command:

`gh pr checkout NUMBER`

We replace NUMBER with the ID number of the pull request. You can see this in the address bar, or next to the title of the pull request.

This command pulls down the changes that the developer has made, and applies it to your local Mautic instance. It will also clear your cache automatically.

If you ever need to clear the cache, you can either delete the cache folder manually or use the command:

`ddev exec bin/console cache:clear --env=dev`

Note that we have to prefix any commands with `ddev exec`so that they run inside the Docker container.  We also use the `--env=dev`argument to specify that we need to clear the development (rather than production) cache.

Now that you have the pull request applied, the next step is to re-test the bug or check out the new feature.  Make sure you are thorough in your testing. Really think about every possible thing that might be affected by the changes being made in the pull request, and test it in detail.

It's very helpful if you can write a comment and explain what you have tested.

## Leaving your review

Within GitHub, there is a built-in system for people to leave reviews.  At the top of the pull request you will see a tab which is called 'Files Changed'. In this tab, at the top right, you'll see a green button which allows you to start a review.

From this point, you can write what you have found when testing the pull request. You can select whether you approve the pull request, whether you think there are changes needed (e.g. if you weren't able to get the results that you expected) or just leave a comment if you're not sure either way, or just want to leave some feedback.

## Unloading the pull request

Once you are done with testing the pull request, it is good practice to get back to the original state. To do this use the command:

`git checkout 5.x`

Where 5.x is the branch that you want to return to.

This will check out the branch called `5.x` which is where we started from.  Now you're ready to go and find another pull request to test! Have a little celebration, you helped make Mautic even more awesome! THANK YOU!


[gitpod-browser]: <https://www.gitpod.io/docs/configure/user-settings/browser-extension>
[docker-desktop]: <https://www.docker.com/products/docker-desktop>
[ddev]: <https://ddev.readthedocs.io/en/stable/#installation>
[github-cli]: <https://cli.github.com>
[git]: <https://git-scm.com/download/>
[vscode]: <https://code.visualstudio.com/download>
[github]: <https://github.com/join>
[mautic-repo]: <https://github.com/mautic/mautic>
[mautic-4.1]: <https://github.com/mautic/mautic/releases/tag/4.1.0>
[gitpod]: <https://www.gitpod.io>
[gitpod-default]: <https://gitpod.io/#https://github.com/mautic/mautic>
[report-findings]: <https://contribute.mautic.org/contributing-to-mautic/tester#leaving-your-review>
[open-source-friday-board]: <https://github.com/orgs/mautic/projects/13?pane=info>
