from . import link

link_name = "bounty issues" 
link_text = "bounty issues"
link_url = "https://github.com/search?q=label%3Abounty+owner%3Amautic&type=issues&state=open" 

link.xref_links.update({link_name: (link_text, link_url)})