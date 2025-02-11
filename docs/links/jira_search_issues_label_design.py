from . import link

link_name = "Jira issues label" 
link_text = "issues with label Design" 
link_url = "https://mautic.atlassian.net/browse/TMAR-24?jql=labels%20%3D%20Design%20AND%20statusCategory%20%3D%20%22To%20Do%22" 

link.xref_links.update({link_name: (link_text, link_url)})
