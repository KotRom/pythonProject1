import requests
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
url = ('https://www.google.com/search?q=rub+to+eur&oq=rub+&aqs=chrome.1.69i57j0i433i512j0i512l3j0i395i512l2j0i10i395i512j0i395i512l2.3244j1j15&sourceid=chrome&ie=UTF-8')
r = requests.get(url, headers=headers)
soup = BS(r.content, 'html.parser')
conv = soup.find_all('span', class_='DFlfde SwHCTb')
print(conv, )


