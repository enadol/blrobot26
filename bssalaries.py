# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 12:50:41 2021

@author: enado
"""

import requests
from bs4 import BeautifulSoup
#import codecs

#import pandas as pd
#import numpy as np

page= requests.get('https://capology.com/de/1-bundesliga/salaries/')


if page.status_code== 200:
    content = page.content

    
klass=["th-inner sortable both", "th-inner sortable desc"]

soup = BeautifulSoup(content, 'html.parser')
#print(soup.prettify())
#clubes=soup.find_all("div", attrs={"class": "kick__v100-gameCell__team__name"})
fields=soup.find_all("div", attrs={"class": klass} )
#odds=soup.find_all("span", attrs={"class": "oddsServe-odd-value"})
salaries=soup.find_all("td", attrs={"class": "money-column"} )
players=soup.find_all("td", attrs={"class": "name-column"} )

