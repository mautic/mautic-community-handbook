from . import link

link_name = "Jira create account" 
link_text = "create a Jira account" 
link_url = "https://www.atlassian.com/try/cloud/signup?bundle=jira-software&edition=free&skipBundles=true" 

link.xref_links.update({link_name: (link_text, link_url)})
