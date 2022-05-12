import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

url = 'https://store.steampowered.com/search/?term=gta'

def get_data():
    r = requests.get(url)
    return r.text

# Processing data
def parse(data):
    result = []
    soup = BeautifulSoup(data, 'html.parser')
    contents = soup.find('div', attrs={'id': 'search_resultsRows'})
    games = contents.find_all('a')

    try:
        os.mkdir('json.result')
    except FileExistsError:
        pass

    for game in games:
        link = game['href']

        # Parsing data
        title = game.find('span', attrs={'class': 'title'}).text.strip().split('£')
        price = game.find('div', attrs={'class': 'search_price'}).text.strip().split('£')[0]
        release = game.find('div', attrs={'class': 'search_released'}).text.strip().split('£')[0]

        if release == '':
            release = 'None'

        # Sorting data
        data_dict = {
            'title': title,
            'price': price,
            'released': release,
            'link': link
        }

        # Append
        result.append(data_dict)
    return result

    # Writing JSON
    with open('json_result.json', 'w') as outfile:
        json.dump(result, outfile)
    return result


# Reading JSON
def load_data():
    with open('json_result.json') as json_file:
        data = json.load(json_file)


# Proccess cleaned data from parser
def output(datas: list):
    for i in datas:
        print(i)


# Convert data to excel
def generate_data(result, filename):
    df = pd.DataFrame(result)
    df.to_excel(f"{filename}.xlsx", index=False)
