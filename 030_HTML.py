import requests
# pip install requests
# import antigravity


#r = requests.get('https://xkcd.com/353/', timeout=5)
#print(r)
# <Response [200]> - udachnoe podkljuchenie
#print(dir(r))
#print(r.text)
#print(r.content) tozhe chto i r.text, no kak baitovaja stroka - bez perenosov i oformlenija - v odnu stroku


#kopiruem kartinku s saite
#r = requests.get('https://imgs.xkcd.com/comics/python.png')
#with open('comic.png', 'wb') as file:
#    file.write(r.content)

r = requests.get('https://xkcd.com/353/')
print(r.status_code)
#print(r.ok) boolean code of connection - True or False
#print(r.headers) #nastroiki brauzera na vremja otkrytija

