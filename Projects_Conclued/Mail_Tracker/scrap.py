import requests
from bs4 import BeautifulSoup

base_url = 'https://www.linkcorreios.com.br/'


def tracking_info(code):
    tracking_data = []
    url = f"{base_url}?id={code}"
    r_correios = requests.get(url)

    html_correios = r_correios.text

    soup = BeautifulSoup(html_correios, "html.parser")

    card = soup.find('div', class_="card-header")
    uls = card.find_all('ul', class_="linha_status")

    for ul in uls:
        lis = ul.find_all('li')
        status = lis[0].text
        data = lis[1].text
        origem = lis[2].text
        destino = lis[3].text

        data = {
            'status': status,
            'date': data,
            'origin': origem,
            'destination': destino,
        }
        tracking_data.append(data)

    print(tracking_data)
    return f"{data['status']}\n{data['data']}\n{data['origim']}\n{data['destino']}"