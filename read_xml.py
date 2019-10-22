from lxml import etree

# не работате!

with open('data_dump/Comments.xml', 'r') as xmlfile:
    tree = etree.parse(xmlfile)

