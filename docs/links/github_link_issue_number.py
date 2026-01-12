from . import link

link_name = "link issue number" 
link_text = "Link the issue number" 
link_url = "https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue" 

link.xref_links.update({link_name: (link_text, link_url)})
