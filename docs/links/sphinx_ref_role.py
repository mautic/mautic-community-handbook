from . import link

link_name = "ref role documentation" 
link_text = ":ref: role documentation" 
link_url = "https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html#the-ref-role" 

link.xref_links.update({link_name: (link_text, link_url)})
