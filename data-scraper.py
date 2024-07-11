import requests
from bs4 import BeautifulSoup
import json


eqPartIds = {'1h': 1, '2h': 2, '1.5h': 3, 'shield': 14, 'bow': 4, 'secondWeapon': 5, 'wand': 6, 'orb': 7, 'arrow': 29,
             'armor': 8, 'helmet': 9, 'boots': 10, 'gloves': 11, 'ring': 12, 'necklace': 13}
itemAttribs = ['id', 'name']
ignoreAttribs = ['opis', 'permbound', 'quest', 'nodepo', 'created', 'nodesc', 'artisan_worthless', 'lvlupgcost',
                 'lvlupgs', 'price', 'binds', 'enhancement_upgrade_lvl', 'nodepoclan', 'lvlnext', 'noauction', 'amount', 'cansplit', 'capacity', 'cursed', 'soulbound' ]
url = f'https://margoworld.pl/item/*,1?name=&minLvl=&maxLvl=&cl=&p=1'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

for name,number in eqPartIds.items():
    numOfTabs = soup.find('div', 'd-flex justify-content-center m-2').find('ul', 'pagination').find_all("li",                                                                                                  "page-item")
    numOfTabs = int(numOfTabs[-1].find('a', 'page-link').text)
    for tab in range(1,numOfTabs+1):
        url = f'https://margoworld.pl/item/*,{number}?name=&minLvl=&maxLvl=&cl=&p={tab}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        itemborder_elements = soup.find_all('span', class_='itemborder')
        for element in itemborder_elements:
            margonem_item = element.find('span', class_='margonem_item')
            if margonem_item:
                data_itemtip = dict(json.loads(margonem_item.get('data-itemtip')))
                itemStats = data_itemtip['stat'].split(';')
                for i in range(len(itemStats)):
                    itemStats[i] = itemStats[i].split("=")
                for attribs in itemStats:
                    if attribs[0] not in itemAttribs and attribs[0] not in ignoreAttribs:
                        itemAttribs.append(attribs[0])
    print(name, "=", itemAttribs)
    itemAttribs = ['id', 'name']
