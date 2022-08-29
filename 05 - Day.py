import requests 
from bs4 import BeautifulSoup

url_indeed = "https://br.indeed.com/empregos-de-python"
r_indeed = requests.get(url_indeed)

# exemplos do requests
#print(r_indeed)
# print(r_indeed.text)

#salva o html no html_indeed
html_indeed = r_indeed.text
soup = BeautifulSoup(html_indeed, 'html.parser')

# print(soup.prettify())# deixa bonitinho
# pega o title
 # print(soup.title)
# pega link (a href")
# print(soup.find_all('a'))
todos_a = soup.find_all('a') #salva como uma lista
# se é uma lista posso acessar como tal...
# print(todos_a[0]) 
# print(todos_a[4])
# print(todos_a[11])

#pega link
# links = soup.find_all('a')

# for link in links:
#   print(link.get('href'))

title = soup.find(id="22d7ce555383096d")
print(soup.title)
print(soup.get('title'))
# title_text = title.get('title')
# print(title_text)
soup.find('div').get('title')
