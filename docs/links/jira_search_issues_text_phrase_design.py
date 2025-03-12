from . import link

link_name = "Jira issues text phrase design" 
link_text = "issues with text phrase Design" 
link_url = "https://mautic.atlassian.net/browse/MCON-201?jql=text%20~%20%22design%22%20AND%20statusCategory%20%3D%20%22To%20Do%22" 

link.xref_links.update({link_name: (link_text, link_url)})
