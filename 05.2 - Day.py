from bs4 import BeautifulSoup
import requests 


url_indeed = "https://br.indeed.com/empregos-de-python"
r_indeed = requests.get(url_indeed)

# exemplos do requests
#print(r_indeed)
# print(r_indeed.text)

#salva o html no html_indeed
html_indeed = r_indeed.text
soup = BeautifulSoup(html_indeed, 'html.parser')
cards = soup.find_all('div', class_='result')
jobs= []

for card in cards:
  # print(card) #COD FONTE DE UM CARD
  job ={
    'title': card.find('a').find('span').get('title'),
    #'company': card.find('span', class_='companyName').get_text(),
    'location': card.find('div', class_='companyLocation').string,
    'how_old': card.find('span', class_='date').get_text(),
    'link': f"https://br.indeed.com{card.find('a').get('href')}"
  } 
  jobs.append(job)
print(jobs)