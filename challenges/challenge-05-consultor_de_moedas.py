import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"
countries = []
# faz requests and Soup
requests = requests.get(url)
soup = BeautifulSoup(requests.text, 'html.parser')
# Estruturando
table = soup.find("table") # podia ter pego o tbody...
rows = table.find_all('tr')[1:] # ou remove no zero
# ou usar o td
#cuidado para não salvar o cabeçalho

# for row in rows:
#   print(row)
#   print("-------")

for row in rows:
  items = row.find_all("td") 
  name = items[0].text
  code = items[2].text
  if name and code:
    if name != "No universal currency":
      country = {
        'name': name, 
        'code': code
      }
      countries.append(country)


def menu():
  try:
    choice = int(input("#: "))
    if choice > len(countries):
      print("Escolha um país da lista:")
      menu()
    else:
      country = countries[choice]
      print(f"Você escolheu:{country['name']}\n ea moeda é {country['code']}")
      print("Escolha outro país")
      menu()
  except ValueError:
    print("Só pode números, tente novamente")
    menu()
    
print("Bem vindo! \n Escolha o país que quer consultar pelo numero\n")

for index, country in enumerate(countries):
  print(f"{index} {country['name']}")



menu()