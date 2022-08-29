import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency
os.system("clear")

url = "https://www.iban.com/currency-codes"
countries = []

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
  items = row.find_all("td")
  name = items[0].text
  code =items[2].text
  if name and code:
    if name != "No universal currency":
      country = {
        'name':name.capitalize(),
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
      print(f"Você escolheu {country['name']}\nO código da moeda é {country['code']}")
  except ValueError:
    print("Isso não é um número!")
    return countries
    menu()

print("Bem-vindo ao Negociador de Moedas!\nEscolha pelo número da lista o país que desja consultar o código da moeda.\n")

for index, country in enumerate(countries):
  print(f"#{index} {country['name']}")
  
menu()


def main(countries):
  lista_para_return=[]
  print()
  try:
    choice = int(input('Informe pelo número o país de origem: '))
    
    while choice<0:
      escolha = int(input('Escolha um número entre 0 e 267 para escolher o país de origem: '))

    if choice>=0 and choice<=len(countries):
      print(f'  [ x ] - {countries[choice]["pais"]}')
      origem=countries[choice]["codigo"]

    if choice>len(countries):
      print('Não existe, escolha uma opção na lista')
      return lista_para_return

    else:
      try:
        escolha_conversao=int(input('quer negociar com qual país?: '))
        
        while escolha_conversao<0:
          escolha_conversao=int(input('Escolha um número entre 0 e 267 para o país com o qual você quer negociar: '))


        if escolha_conversao>=0 and escolha_conversao<=len(countries):
          print(f'  [ x ] - {countries[escolha_conversao]["pais"]}')
          destino=countries[escolha_conversao]["codigo"]

          quantos=float(input(f'e quantos {countries[escolha]["codigo"]} você quer converter para {countries[escolha_conversao]["codigo"]}: '))
          
          lista_para_return=[origem,destino,quantos]
          return lista_para_return

        if escolha_conversao>len(lista):
          print('Não existe, escolha uma opção na lista')
          return lista_para_return

      except:
        print('Isto não é um número')
        return lista_para_return
  except:
    print('Isto não é um número')
    return lista_para_return
 
def personaliza_url(lista_para_return):
  if len(lista_para_return)==0:
    print('Tente novamente')
  else:
    origem=lista_para_return[0]
    destino=lista_para_return[1]
    quantos=lista_para_return[2]

    url=f'https://transferwise.com/gb/currency-converter/{origem}-to-{destino}-rate?amount={quantos}'
    return url

#print(format_currency(quantos, destino))
main()