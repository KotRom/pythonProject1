from bs4 import BeautifulSoup
import requests
import time

# https://www.crummy.com/software/BeautifulSoup/bs4/doc
# pip install bs4

r = requests.get('https://www.google.com')
print(r)

# Will create a soup from html
soup = BeautifulSoup(r.content, 'html.parser')
print(soup)

# Prettify() will make html more readable
print(soup.prettify())

# Html tags can be accessed by .tag
print(soup.title)

# Will get text from html tag
print(soup.title.string)
print(soup.title.text)

# Parent tags can also be accesed
print(soup.title.parent)
print(soup.title.parent.name)

# Also tag parameters can be called
print(soup.p)
print(soup.p['style'])

# Link can be accessed through a tag
print(soup.a)
print(soup.a['href'])

# find_all method will return all <a> in html
print(soup.find_all('a'))
for link in soup.find_all('a'):
    print(link.get('href'))

# find will return one tag, with parameter in ()
print(soup.find(class_="gb1"))

# Gets all text from html webpage
print(soup.get_text())


# Modification samples
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
print(type(tag))
print(tag.name)

tag['id'] = 'verybold'
tag['another-attribute'] = 1
print(tag)

del tag['id']
del tag['another-attribute']
print(tag)

# # Will raise key error
# print(tag['id'])
# WIll return None instead of error
print(tag.get('id'))

