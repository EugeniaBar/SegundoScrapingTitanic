
from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
#print(soup.prettify())

box = soup.find('article', class_='main-article') #box= caja

title = box.find('h1').get_text()
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

# borrar espacios: Codigo ESTÁ dentro de .get_text()

#exportar data a archivo txt:

with open(f'{title}.txt', 'w') as file:
    file.write(transcript)


#Usar variable title, con cadena f, para que cambie, cuando cambie el title: 
#with open(f'{title}.text', 'w') as file:
# file.write(transcript)