from . import link

link_name = "Mautic UX issues" 
link_text = "UX" 
link_url = "https://github.com/mautic/mautic/issues?q=is%3Aopen+is%3Aissue+label%3Auser-experience" 

link.xref_links.update({link_name: (link_text, link_url)})
