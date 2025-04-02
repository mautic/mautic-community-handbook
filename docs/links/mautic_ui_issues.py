from . import link

link_name = "Mautic UI issues" 
link_text = "UI" 
link_url = "https://github.com/mautic/mautic/issues?q=is%3Aopen+is%3Aissue+label%3Auser-interface" 

link.xref_links.update({link_name: (link_text, link_url)})
