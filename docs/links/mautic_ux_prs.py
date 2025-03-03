from . import link

link_name = "Mautic UX pull requests" 
link_text = "UX" 
link_url = "https://github.com/mautic/mautic/pulls?q=is%3Aopen+is%3Apr+label%3Auser-experience" 

link.xref_links.update({link_name: (link_text, link_url)})
