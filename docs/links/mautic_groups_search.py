from . import link

link_name = "Mautic groups search" 
link_text = "groups search" 
link_url = "https://community.mautic.org/search?filter%5Bterm%5D=&filter%5Bwith_resource_type%5D=Decidim%3A%3AUserGroup&filter%5Bwith_scope%5D=" 

link.xref_links.update({link_name: (link_text, link_url)})
