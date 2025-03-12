from . import link

link_name = "Mautic UI pull requests" 
link_text = "UI" 
link_url = "https://github.com/mautic/mautic/pulls?q=is%3Aopen+is%3Apr+label%3Auser-interface" 

link.xref_links.update({link_name: (link_text, link_url)})
