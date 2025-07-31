from . import link

link_name = "Mautic ready-to-test issue label" 
link_text = "ready-to-test" 
link_url = "https://github.com/mautic/mautic/labels/ready-to-test" 

link.xref_links.update({link_name: (link_text, link_url)})
