from . import link

link_name = "doc role documentation" 
link_text = ":doc: role documentation" 
link_url = "https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html#the-doc-role" 

link.xref_links.update({link_name: (link_text, link_url)})
