#!/usr/bin/env python
# coding: utf-8

# # Datetime
# Para treinar o uso da biblioteca datetime, execute as funções do código a seguir, tentando prever os seus resultados:

# In[2]:


import datetime

d = datetime.date(2001, 9, 11)
tday = datetime.date.today()
print(tday, d)


# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

tdelta = datetime.timedelta(hours=12)
print(tday + tdelta)


bday = datetime.date(2016, 9, 24)
till_bday = bday - tday
print(till_bday.days)

dt_agora = datetime.datetime.now()
print(dt_agora.strftime('%B %d, %Y'))

dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime - Datetime para String
# strptime - String para Datetime


# Exemplo da Aula

# In[3]:


import requests as r


# In[6]:


url ="https://api.covid19api.com/dayone/country/brazil"
resp = r.get(url)


# In[7]:


resp.status_code


# In[8]:


raw_data = resp.json()


# In[9]:


raw_data[0]


# In[12]:


final_data = []
for obs in raw_data:
    final_data.append([obs["Confirmed"], obs['Deaths'],  obs['Active'] ,obs['Recovered'], obs['Date']])


# In[15]:


final_data.insert(0, ['confirmados', 'obitos', 'ativos','recuperados', 'data'])
final_data


# In[16]:


confirmados = 0 
obitos = 1
recuperados = 2
ativos = 3
data = 4


# In[17]:


for i in range(1, len(final_data)):
    final_data[i][data] = final_data[i][data][:10]


# In[19]:


final_data


# In[20]:


import datetime as dt


# In[23]:


print(dt.time(12,6,21,7), 'Hora:minuto:segundo:microsegundo')
print('----')
print(dt.date(2020, 4, 25), "Ano-Mês-Dia")
print('----')
print(dt.datetime(2020, 4, 25, 12,6,21,7), 'Ano-Mês-Dia Hora:minuto:segundo:microsegundo')


# In[24]:


natal = dt.date(2020, 12, 25)
reveillon = dt.date(2021, 1, 1)

print(reveillon -  natal)
print((reveillon - natal).days)
print((reveillon- natal).seconds)
print((reveillon - natal).microseconds)


# In[25]:


import csv 


# In[26]:


with open('brasil-covid.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)


# In[28]:


for i in range(1, len(final_data)):
    final_data[i][data] = dt.datetime.strptime(final_data[i][data], '%Y-%m-%d')


# In[29]:


final_data


# https://quickchart.io/documentation/

# In[33]:


def get_dataset(y, labels):
    if type(y[0])== list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label': labels[i], 
                'data': y[i]
            })
        return datasets
    else:
        return [
            {
                'label': labels[0], 
                'data': y
            }
        ]


# In[35]:


def set_title(title=" "):
    if title !=" ":
        display = 'true'
    else:
            display = 'false'
    return {
        'title': title, 
        'display': display
    }


# In[36]:


def create_chart(x, y, labels, kind="bar", title=''):
    datasets = get.datasets(y,labels)
    options = set_title(title)
    
    chart ={
        'type': kind, 
        'data': {
            'labels': x, 
            'datasets': datasets
        },
        'options': options
    }
    
    return


# In[37]:


def get_api_chart(chart):
    url_base ='https://quickchart.io/chart'
    resp = r.get(f'{url_base}?c={str(chart)}')
    return resp.content


# In[38]:


def save_image(path, content):
    with open(path, 'wb') as image:
        image.write(content)


# In[41]:


from PIL import Image 
from IPython.display import display


# In[45]:


def display_image(path):
    img_pil = Image.open(path)
    display(img_pil)


# In[46]:


y_data_1 = []
for obs in final_data[1::10]:
    y_data_1.append(obs[confirmados])
    
y_data_2 = []
for obs in final_data[1::10]:
    y_data_1.append(obs[recuperados])
    
labels = ["confirmados", 'recuperados']

x = []
for obs in final_data[1::10]:
    x.append(obs[data].strftime('%d/%m/%Y'))
    
charts = create_chart(x, [y_data_1, y_data_2], labels, title="Gráfico Confirmados vs. Recuperados")
chart_content = get_api_chart(chart)
save_image("meu-primeiro-gráfico.png", chart_content)
display_image('meu-primeiro-gráfico.png')


# In[48]:


from urllib.parse import quote


# In[49]:


def get_api_qrcode(link):
    text = quote(link) 
    url_base = "https://quickchart.io/qr"
    resp = r.get(f'{url_base}?text={text}')
    return resp.content


# In[50]:


url_base = 'https://quickchart.io/chart'
link =f'{url_base}?c={str(chart)}'
save_image = ('qr-code.png', get_api_qrcode(link))
display_image(qr-code.png)


# In[ ]:





# In[ ]:




