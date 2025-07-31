from . import link

link_name = "Mozilla writing guide" 
link_text = "Mozilla Knowledge Base writing guide" 
link_url = "https://support.mozilla.org/en-US/kb/write-articles-knowledge-base" 

link.xref_links.update({link_name: (link_text, link_url)})
