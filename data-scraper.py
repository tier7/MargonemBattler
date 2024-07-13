import sqlite3

import requests
from bs4 import BeautifulSoup
import json
import time

def create_table(conn, table_name, columns):
    c = conn.cursor()
    columns_sql = ", ".join([f"{col} TEXT" for col in columns])
    c.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql})")
    conn.commit()
def insert_item(conn, table_name, item_data):
    c = conn.cursor()
    columns = ", ".join(item_data.keys())
    placeholders = ", ".join(["?" for _ in item_data.values()])
    c.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", list(item_data.values()))
    conn.commit()

startTime = time.time()
eqPartIds = {'1h': 1, '2h': 2, '1_5h': 3, 'shield': 14, 'bow': 4, 'secondWeapon': 5, 'wand': 6, 'orb': 7, 'arrow': 29,
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
    itemAttribs = ['id', 'name']
    all_items = []
    itemCount = 0

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
                item_data = {'id':data_itemtip.get('id'), 'name': data_itemtip.get('name')}
                for stat in itemStats:
                    if '=' in stat:
                        key,value = stat.split('=')
                        if key not in ignoreAttribs:
                            item_data[key] = value
                            if key not in itemAttribs:
                                itemAttribs.append(key)
                all_items.append(item_data)
    table_name = f'eq_{name}'
    conn = sqlite3.connect('items.db')
    create_table(conn, table_name, itemAttribs)
    for item in all_items:
        insert_item(conn, table_name, item)
        itemCount += 1
        print(f"{name}: {itemCount} items added")
    conn.close()
endTime = time.time()
executeTime = endTime - startTime
print(f"Time taken to scrap full data: {executeTime:.2f} seconds")
