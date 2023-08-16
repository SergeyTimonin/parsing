from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

#определил колво страниц
url = 'http://plafoni.ru/index.php?route=product/category&path=25&page=1'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
pagen = int(soup.find('div', class_='pagination-result').text.split()[-2])+1
pagen_list=[]
for i in range(1, pagen):
    pagen_list.append(f'http://plafoni.ru/index.php?route=product/category&path=25&page={i}')
#занполнил pagen_list страницами
#далее приступаю к парсингу цен из этих листов

ttl_price_list = [] # создаю общий список для цен
for page in pagen_list:
    url = page
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    price = soup.find_all('span', class_='price-new')
    prices = []
    #ниже часть по парсингу цен которая вклыдвается в цикл по перебору страниц
    for item in price:
        prices.append(item.text)
    ttl_price_list.append(prices) 
ttl_price_list


#определил колво страниц
url = 'http://plafoni.ru/index.php?route=product/category&path=25&page=1'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
pagen = int(soup.find('div', class_='pagination-result').text.split()[-2])+1
pagen_list=[]
for i in range(1, pagen):
    pagen_list.append(f'http://plafoni.ru/index.php?route=product/category&path=25&page={i}')
#занполнил pagen_list страницами
#далее приступаю к парсингу цен из этих листов

ttl_name_list = [] # создаю общий список для цен
for page in pagen_list:
    url = page
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    name = soup.find_all('a', class_='product-name')
    names = []
    #ниже часть по парсингу цен которая вклыдвается в цикл по перебору страниц
    for n in name:
        names.append(n.text)
    ttl_name_list.append(names) 
ttl_name_list



from itertools import chain
# Преобразование списка списков в один плоский список
article = list(chain.from_iterable(ttl_name_list))
price = list(chain.from_iterable(ttl_price_list))
df = pd.DataFrame({'Цена': price, 'Артикул': article})
excel_file_path = 'Плафоны.xlsx'
df.to_excel(excel_file_path, index=False)