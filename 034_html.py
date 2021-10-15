import requests
from bs4 import BeautifulSoup as BS

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

r = requests.get('https://www.google.com/search?q=rub+to+eur&oq=rub+&aqs=chrome.1.69i57j0i433i512j0i512l3j0i395i512l2j0i10i395i512j0i395i512l2.3244j1j15&sourceid=chrome&ie=UTF-8', headers=headers)
soup = BS(r.content, 'html.parser')
conv = soup.find_all('span', class_='DFlfde SwHCTb')
print(conv, )


