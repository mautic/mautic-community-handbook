# Mautic community handbook
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-18-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->


A handbook for all things related to the Mautic Community.

To contribute please make a PR for review by the Community Leadership Team.

[![Documentation Status](https://readthedocs.org/projects/mautic-community-handbook/badge/?version=latest)](https://mautic-community-handbook.readthedocs.io/en/latest/?badge=latest)

## Local development setup

Mautic uses [DDEV](https://ddev.com) to simplify local development and testing of documentation updates.

Go to the [Get Started](https://ddev.com/get-started/) page for instructions to install DDEV on your local machine.

---

> [!NOTE]
> **For Windows users**: You can install and run DDEV on [traditional Windows](https://ddev.readthedocs.io/en/stable/#system-requirements-traditional-windows). However, it's recommended that you use [Windows Subsystem for Linux 2 (WSL2)](https://learn.microsoft.com/en-us/windows/wsl/about) for faster and better performance.
>
> If you're new to WSL, follow the instructions on the [DDEV blog](https://ddev.com/blog/watch-new-windows-installer/) to install and set up WSL and DDEV. 

---

After you've installed DDEV, follow these steps:

1. [Fork and clone](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) this repository to your local machine.
2. Navigate into the project directory by running: 

   ```bash
   cd mautic-community-handbook
   ```
3. Start the DDEV environment with this command:

   ```bash
   ddev start
   ```
4. After making changes to documentation files, you need to build the updated docs by running:

   ```bash
   ddev build-docs
   ```
5. Run the below command to view your changes live on your browser:

   ```bash
   ddev launch
   ```
   
   This automatically opens your browser and navigates to `https://mautic-community-handbook.ddev.site/`.

   **Note:** You must ensure that your changes work as expected. Every time you make changes, run `ddev build-docs` and refresh the page in your browser to see the changes.

> [!TIP]
> If you don't see the configuration take effect, run `ddev restart` to restart the project.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://hojtsy.hu"><img src="https://avatars.githubusercontent.com/u/235185?v=4?s=100" width="100px;" alt="Gábor Hojtsy"/><br /><sub><b>Gábor Hojtsy</b></sub></a><br /><a href="https://github.com/mautic/mautic-community-handbook/commits?author=goba" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.schriftrolle.de/?utm_source=github&utm_medium=profilLink"><img src="https://avatars.githubusercontent.com/u/765204?v=4?s=100" width="100px;" alt="Sven Döring"/><br /><sub><b>Sven Döring</b></sub></a><br /><a href="https://github.com/mautic/mautic-community-handbook/commits?author=sdoering" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/deborahsalves"><img src="https://avatars.githubusercontent.com/u/79517214?v=4?s=100" width="100px;" alt="Déborah Salves"/><br /><sub><b>Déborah Salves</b></sub></a><br /><a href="https://github.com/mautic/mautic-community-handbook/commits?author=deborahsalves" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tobsowo"><img src="https://avatars.githubusercontent.com/u/5642737?v=4?s=100" width="100px;" alt="Oluwatobi Owolabi"/><br /><sub><b>Oluwatobi Owolabi</b></sub></a><br /><a href="https://github.com/mautic/mautic-community-handbook/pulls?q=is%3Apr+reviewed-by%3Atobsowo" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.ruthcheesley.co.uk"><img src="https://avatars.githubusercontent.com/u/2930593?v=4?s=100" width="100px;" alt="Ruth Cheesley"/><br /><sub><b>Ruth Cheesley</b></sub></a><br /><a href="https://github.com/mautic/mautic-community-handbook/pulls?q=is%3Apr+reviewed-by%3Archeesley" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://ionutojica.com"><img src="https://avatars.githubusercontent.com/u/96743055?v=4?s=100" width="100px;" alt="IonutOjicaDE"/><br /><sub><b>IonutOjicaDE</b></sub></a><br /><a href="https://github.com/mautic/mautic-community-handbook/pulls?q=is%3Apr+reviewed-by%3AIonutOjicaDE" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/mautic/mautic-community-handbook/commits?author=IonutOjicaDE" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/daniellord32"><img src="https://avatars.githubusercontent.com/u/25160505?v=4?s=100" width="100px;" alt="Daniel Lord"/><br /><sub><b>Daniel Lord</b></sub></a><br /><a href="https://github.com/mautic/mautic-community-handbook/pulls?q=is%3Apr+reviewed-by%3Adaniellord32" title="Reviewed Pull Requests">👀</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/domidc"><img src="https://avatars.githubusercontent.com/u/160307959?v=4?s=100" width="100px;" alt="domidc"/><br /><sub><b>domidc</b></sub></a><br /><a href="https://github.com/mautic/mautic-community-handbook/commits?author=domidc" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.linkedin.com/in/vibhuti019"><img src="https://avatars.githubusercontent.com/u/44270768?v=4?s=100" width="100px;" alt="Vibhuti"/><br /><sub><b>Vibhuti</b></sub></a><br /><a href="https://github.com/mautic/mautic-community-handbook/commits?author=vibhuti019" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/RitaOC"><img src="https://avatars.githubusercontent.com/u/100735810?v=4?s=100" width="100px;" alt="Rita Onwudiwe"/><br /><sub><b>Rita Onwudiwe</b></sub></a><br /><a href="https://github.com/mautic/mautic-community-handbook/commits?author=RitaOC" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://adiati.com"><img src="https://avatars.githubusercontent.com/u/45172775?v=4?s=100" width="100px;" alt="Ayu Adiati"/><br /><sub><b>Ayu Adiati</b></sub></a><br /><a href="https://github.com/mautic/mautic-community-handbook/commits?author=adiati98" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Peacesandy"><img src="https://avatars.githubusercontent.com/u/78281826?v=4?s=100" width="100px;" alt="Peace Sandy"/><br /><sub><b>Peace Sandy</b></sub></a><br /><a href="https://github.com/mautic/mautic-community-handbook/commits?author=Peacesandy" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.linkedin.com/in/favour-kelvin/"><img src="https://avatars.githubusercontent.com/u/39309699?v=4?s=100" width="100px;" alt="Favour Kelvin"/><br /><sub><b>Favour Kelvin</b></sub></a><br /><a href="https://github.com/mautic/mautic-community-handbook/pulls?q=is%3Apr+reviewed-by%3Afakela" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ASHMITA489"><img src="https://avatars.githubusercontent.com/u/143288389?v=4?s=100" width="100px;" alt="ashmita_"/><br /><sub><b>ashmita_</b></sub></a><br /><a href="https://github.com/mautic/mautic-community-handbook/commits?author=ASHMITA489" title="Documentation">📖</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/favour-chibueze"><img src="https://avatars.githubusercontent.com/u/46398983?v=4?s=100" width="100px;" alt="Favour Chibueze "/><br /><sub><b>Favour Chibueze </b></sub></a><br /><a href="https://github.com/mautic/mautic-community-handbook/commits?author=favour-chibueze" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/susanodii"><img src="https://avatars.githubusercontent.com/u/81011757?v=4?s=100" width="100px;" alt="Susan Odii"/><br /><sub><b>Susan Odii</b></sub></a><br /><a href="https://github.com/mautic/mautic-community-handbook/commits?author=susanodii" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://gemission.org"><img src="https://avatars.githubusercontent.com/u/89047449?v=4?s=100" width="100px;" alt="Dalton McGehee"/><br /><sub><b>Dalton McGehee</b></sub></a><br /><a href="https://github.com/mautic/mautic-community-handbook/commits?author=daltonm-GEM" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://second-gazelle-cd0.notion.site/Judith-Etugbo-226582d0eba680e88616f4f60a2d9c5e"><img src="https://avatars.githubusercontent.com/u/110067624?v=4?s=100" width="100px;" alt="Judith Etugbo"/><br /><sub><b>Judith Etugbo</b></sub></a><br /><a href="https://github.com/mautic/mautic-community-handbook/commits?author=Nickyshe" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!