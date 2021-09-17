from xml.etree import ElementTree

tree = ElementTree.parse('xml_files//cd_catalog.xml')
root = tree.getroot()

cd = root[1]
data = next(cd.iter('Y1985'))
data.text = str(int(data.text) + 1000000)
print(data.text)

tree.write('xml_files//cd_catalog_copy.txt')