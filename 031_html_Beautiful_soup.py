import requests
from bs4 import BeautifulSoup as BS

# pip install bs4
# pip install html5lib #v terminale
headers = "{'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}"
url = 'http://www.gammatest.net/course/python'
r = requests.get(url)
#print(r)

#soup = BS(r.content, 'html.parser')
#print(soup)
#print(soup.title.text)
# print(soup.get_text) # tozhe chto i r.text
#print(soup.prettify()) #html code s otstupami i krasivenkij
# print(soup.div) berjot pervyj div
# print(soup.div['class']) itribut div po class

soup = BS(r.content, 'html.parser')
#match = soup.find('div', class_='header') #nahodit div
#match = soup.find('table') # nahodit table
#print(match)
#match = soup.findAll('a')
#for link in match:
    #print(link['href'])
    #print(link.text)


#print(soup.div.get_attribute_list('class')) # tozhe chto i # print(soup.div['class'])




