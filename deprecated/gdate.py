# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:47:36 2022

@author: enado
"""
# SOLO ACTUALIZAR MD !!
# NO CORRER SOLO!! CORRE EN BS23!!
import requests
from bs4 import BeautifulSoup

MD = 19
TORNEO = '2024-25'
lstDates = []
lst_dates_cumul = []


def get_mdd_dates(MD):
    """create empty list to populate with dates"""
    list_mdd_dates = []
    mdpage = requests.get(f'https://kicker.de/Bundesliga/spieltag/{TORNEO}/{MD}', timeout=10)
    if mdpage.status_code == 200:
        content = mdpage.content
    else:
        mdpage = requests.get(f'https://kicker.de/bundesliga/spieltag/{TORNEO}/{MD}', timeout=10)
        if mdpage.status_code == 200:
            content = mdpage.content
    klass = ["kick__v100-gameList__header"]
    soup = BeautifulSoup(content, 'html.parser')
    # print(soup.prettify())
    dates = soup.find_all("div", attrs={"class": klass})

    for date in dates:
        list_mdd_dates.append(date.text.strip())

    mddate1 = list_mdd_dates[0][:2].strip()
    mddate2 = list_mdd_dates[0].split(',')[1].split('.')[0].strip().lstrip("0")
    mddate3 = list_mdd_dates[0].split(',')[1].split('.')[1].lstrip("0")

    md_date_def = f'[{mddate1}. {mddate2}.{mddate3}.]'
    lst_dates_cumul.append(md_date_def)
    return lst_dates_cumul


for i in range(1, MD+1):
    agg_date = get_mdd_dates(i)
