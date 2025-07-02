from . import link

link_name = "Mautic donation page" 
link_text = "donate here" 
link_url = "https://opencollective.com/mautic/donate" 

link.xref_links.update({link_name: (link_text, link_url)})
