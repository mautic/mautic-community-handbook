from . import link

link_name = "Create a new issue for Mautic" 
link_text = "issue" 
link_url = "https://github.com/mautic/mautic/issues/new?assignees=&labels=bug%2Cneeds-triage&template=BUG-REPORT.yml&title=Your+bug+title+goes+here%21" 

link.xref_links.update({link_name: (link_text, link_url)})
