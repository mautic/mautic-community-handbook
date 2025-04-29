from . import link

link_name = "Mautic repository open issues" 
link_text = "open issues" 
link_url = "https://github.com/mautic/mautic/issues?q=is%3Aopen+"

link.xref_links.update({link_name: (link_text, link_url)})
