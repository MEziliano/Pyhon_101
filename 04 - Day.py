import requests

url = "https://br.indeed.com/$adminikptop" 
r_indeed = requests.get(url)
# print(r_indeed.text)
# urlib on python Standart library https://docs.python.org/3/library/urllib.html
# and requests documentation (https://docs.python-requests.org/en/latest/)
# print(r_indeed.status_code)
if r_indeed.status_code ==200:
  print("O site está online")
else:
  print("O site não existe")