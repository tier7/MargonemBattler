import requests
from bs4 import BeautifulSoup
import json

url = 'https://margoworld.pl/item/*,1?name=&minLvl=&maxLvl=&cl=&p=1'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
numOfTabs = soup.find('div', 'd-flex justify-content-center m-2').find('ul','pagination').find_all("li", "page-item")
numOfTabs = int(numOfTabs[-1].find('a', 'page-link').text)
itemAttribs = ['id', 'name']
ignoreAttribs = ['opis','permbound','quest','nodepo','created','nodesc','artisan_worthless', 'lvlupgcost', 'lvlupgs', 'price', 'binds']
itemborder_elements = soup.find_all('span', class_='itemborder')
for element in itemborder_elements:
    margonem_item = element.find('span', class_='margonem_item')
    if margonem_item:
        data_itemtip = dict(json.loads(margonem_item.get('data-itemtip')))
        itemStats = data_itemtip['stat'].split(';')
        for i in range(len(itemStats)):
           itemStats[i]= itemStats[i].split("=")
        print(itemStats)
        for attribs in itemStats:
            if attribs[0] not in itemAttribs and attribs[0] not in ignoreAttribs:
                itemAttribs.append(attribs[0])




print(itemAttribs)
