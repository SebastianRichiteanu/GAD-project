import os
import csv
import json
import requests
# import urlilib.request
from pathlib import Path
from bs4 import BeautifulSoup


def billboard_webscraping():
    url = 'https://www.billboard.com/charts/artist-100'
    columns = ['Rank', 'Name', 'Last', 'Peak', 'Weeks']
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find('div', {'class': 'chart-list chart-details__left-rail'})
    table_rows = table.find_all('div', {'class': 'chart-list-item'})

    full_list = []
    for table_row in table_rows:
        rank = table_row.find('div', {'class': 'chart-list-item__rank'}).text.strip()
        name = " ".join(table_row.find('span', {'class': 'chart-list-item__title-text'}).text.split())
        info = table_row.find_all('div', {'class': 'chart-list-item__ministats-cell'})
        last_week = info[0].text.strip().split("\xa0")[0]
        peak = info[1].text.strip().split("\xa0")[0]
        weeks = info[2].text.strip().split("\xa0")[0]

        row_tuple = (rank, name, last_week, peak, weeks)
        full_list.append(row_tuple)

    return full_list

