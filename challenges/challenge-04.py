import os
import requests

def menu():
  choice = str(input("Precisa verificar mais algum site? s/n ")).lower()
  if choice == "s" or choice =="n":
    if choice == "n":
        print("Programa Encerrado!")
        return
    elif choice == "s":
      main()
  else:
    print("Opção inválida.")
    menu()

def main():
  os.system('clear')
  print("Bem-vindo ao Verificador de Sites 1.0!\nInsira as URLs dos sites que deseja verificar o status. (separadas por virgula)\n")
  urls = str(input()).lower().split(",")
  for url in urls:
    url = url.strip()
    if "." not in url:
      print(url, "URL inválida.")
    else:
      if "http" not in url:
        url = f"http://{url}"
      try:
        request = requests.get(url)
        if request.status_code == 200:
          print(url,"Site online!")
        else:
          print(url, "Site offline!")
      except:
          print(url, "Site offline!")
  menu()

main()