import os
import csv
import json
import requests
# import urlilib.request
from pathlib import Path
from bs4 import BeautifulSoup


def billboard_webscraping():
    url = 'https://www.billboard.com/charts/artist-100'
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


def news_webscraping():
    url = 'https://www.nme.com/news/music'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find('div', {'id': 'tdi_85'})
    table_rows = table.find_all('div', {'class': 'tdb_module_loop td_module_wrap td-animation-stack'})
    full_list = []

    for table_row in table_rows:
        tab = table_row.find('a', {'class': 'td-image-wrap'})
        title = tab.get('title', 'None')
        current_url = tab.get('href', 'None')
        img = table_row.find('span', {'class': 'entry-thumb'}).get('data-img-url', 'None')
        sub_title = table_row.find('div', {'class': 'td-excerpt'}).text
        full_list.append((title, sub_title, img, current_url))
    return full_list
