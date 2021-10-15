import requests
from bs4 import BeautifulSoup as BS
import re

headers = "{'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}"
url = 'http://www.gammatest.net/course/python'
r = requests.get(url)

soup = BS(r.content, 'html.parser')
#print(soup.find_all(['a', 'table']))
#print(soup.find_all(True))

#print(soup.find_all(class_=re.compile('md')))
#print(soup.find_all('h2', string=True)) # vse h2 v kotoryh  est' stroka

#result = soup.find_all('h2', string=True)
#for tag in result:
#    print(tag.text)


#for tag in soup.find_all(True):
#    print(tag.name)

#print(soup.find_all('title'))
#print(soup.title)


#print(soup.find_all('a'))
#print(soup.a) # vydajot pervyj a

match = soup.find('a', text='Перейти')
#print(match)
#print(match.find_next('a'))
match2 = match.find_parent().find_parent().find_parent()
chld = match2.findChildren()
for child in chld:
    print(child.findChildren())
