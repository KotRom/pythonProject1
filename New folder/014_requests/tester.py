import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
url = 'https://www.google.com/search?q=rub+to+eur&source=hp&ei=G91yYOfSHomjUKz2lcgJ&iflsig=AINFCbYAAAAAYHLrK1gJoJinwWKu-zRALJoJg5KWHoMk&oq=rub+&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQRhCCAjICCAAyAggAMgIIADICCAAyAggAMgIIADICCC4yAggAMgIIADoLCC4QxwEQowIQkwI6CAguEMcBEKMCOggILhDHARCvAToLCC4QxwEQrwEQkwJQ0w9YjhZgxCZoAHAAeACAAU6IAYoCkgEBNJgBAKABAaoBB2d3cy13aXo&sclient=gws-wiz'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')

value = soup.find('span', {'class': 'DFlfde SwHCTb'})
# print(value)
# value = float(value.string.replace(',', '.'))
#
# user_amount = float(input('Please enter amount in RUB'))
# print(f'{user_amount * value:.2f}')
#
# print(user_amount // value)

print(value.has_attr('nameee'))