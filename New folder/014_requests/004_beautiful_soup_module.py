from bs4 import BeautifulSoup
import requests

html = '<p id="this is id" class="multi class attribute"><a rel="index">Hello world</a></p>'
soup = BeautifulSoup(html, 'html.parser')

# If attribute can't be double
print(soup.p['id'])

# Class can have multiple values, list is returned
print(soup.p['class'])

# Multiple values can be consolidated
print(soup.a['rel'])
soup.a['rel'] = ['rel', 'contents']
print(soup.a['rel'])

# Multiple attribute values can be disabled
soup_no_multi = BeautifulSoup(html, 'html.parser', multi_valued_attributes=None)
print(soup_no_multi.p['class'])

# Can return list also
print(soup.p.get_attribute_list('id'))

# If you parse document as XML there are no multivalued attributes
# xml parser is needed
# pip install lxml
xml_soup = BeautifulSoup(html, 'xml')
print(xml_soup.p['class'])

# String can't be edited but can be replaced
print(soup.a.string)
a_tag = soup.a
a_tag.string.replace_with('Hello planet')
print(a_tag.string)
print(soup.a)

# Soup replacement
soup_footer = BeautifulSoup('<document><content/>INSERT FOOTER HERE</document>', 'xml')
footer = BeautifulSoup('<footer>I AM NEW FOOTER</footer>', 'xml')
print(soup_footer.text)
soup_footer.find(text='INSERT FOOTER HERE').replace_with(footer)
print(soup_footer.text)


r = requests.get('https://www.google.com')
r_soup = BeautifulSoup(r.content, 'html.parser')

# Accessing different tags
print(r_soup.head)
print(r_soup.title)
print(r_soup.body)

# This will get first b tag in a soup
print(r_soup.body.b)

# Tags can be stored into a variable
head_tag = r_soup.head
print(head_tag)
# .contents will return content of a tag
print(head_tag.contents)

title_tag = head_tag.contents[0]
print(title_tag)

# Will return direct children only
for child in title_tag.children:
    print(child)
    print()


# Will return all descendants
for child in head_tag.descendants:
    print(child)
    print()

print(len(list(r_soup.children)))
print(len(list(r_soup.descendants)))

# Getting data from a soup
print(soup.contents)
print(soup.string)

# Printing all strings
for string in r_soup.strings:
    print(repr(string))

# Printing all strings without extra whitespaces
for string in r_soup.stripped_strings:
    print(string)

# Parent will return a parent tag
print(r_soup.title)
print(r_soup.title.parent)

sibling_soup = BeautifulSoup('<a><b>Hello</b><c>World</c></b></a>', 'html.parser')
print(sibling_soup.prettify())

# Will get next sibling to B tag
print(sibling_soup.b.next_sibling)
# Will return previous sibling to C tag
print(sibling_soup.c.previous_sibling)

# Both will return None, because there are no siblings
print(sibling_soup.b.previous_sibling)
print(sibling_soup.c.next_sibling)

# Iterable can be created too
for sibling in r_soup.a.next_siblings:
    print(sibling)

# find_all can be accessed by one attribute
print(r_soup.find_all(class_='gb1'))
print(r_soup.find_all(href='https://calendar.google.com/calendar?tab=wc'))
# also if attribute exists
print(r_soup.find_all(id=True))
# List of atributes
print(r_soup.find_all(attrs={'class': 'gb1', 'href': True}))
# Limit number of output results
print(r_soup.find_all('a', limit=2))
