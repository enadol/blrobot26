# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:27:19 2022

@author: enado
"""
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support.ui import Select
import pandas as pd

DRIVER_PATH='C:/Users/enado/ChromeDriver/chromedriver'
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver=webdriver.Chrome(executable_path=DRIVER_PATH)
driver.implicitly_wait(0.5)
driver.maximize_window()

driver.get('https://capology.com/de/1-bundesliga/salaries')
l = driver.find_element(By.XPATH, "//a[text()='All']")
#l = driver.find_element(By.XPATH, "*//[@id='panel']/div[3]/div/div[4]/div[3]/div[2]/div[1]/div/div/div/a[6]")
l.click()
#sel = Selector(text=driver.page_source)

#players=driver.find_elements(By.XPATH, "//tr/td[@class='name-column']")
#salaries=driver.find_elements(By.XPATH, "//tr/td[@class='money-column']")

#playerlst=[]
#sallst=[]

#for item in players:
#    playerlst.append(item.text)

#for item in salaries:
#    sallst.append(item.text)

players=[]
salariesgpw=[]
salariesgpy=[]
contractlst=[]
clublst=[]
pos1lst=[]
pos2lst=[]
agelst=[]
countrylst=[]

playerlst=driver.find_elements(By.CSS_SELECTOR, 'td:nth-child(1)')
for item1 in playerlst:
    players.append(item1.text)


salweek=driver.find_elements(By.CSS_SELECTOR, 'td:nth-child(3)')
for item2 in salweek:
    salariesgpw.append(item2.text)


salyear=driver.find_elements(By.CSS_SELECTOR, 'td:nth-child(4)')
for item3 in salyear:
    salariesgpy.append(item3.text)


contract=driver.find_elements(By.CSS_SELECTOR, 'td:nth-child(7)')
for item4 in contract:
    contractlst.append(item4.text)


club=driver.find_elements(By.CSS_SELECTOR, 'td:nth-child(16)')
for item5 in club:
    clublst.append(item5.text)

pos1=driver.find_elements(By.CSS_SELECTOR, 'td:nth-child(11)')
for item6 in pos1:
    pos1lst.append(item6.text)

pos2=driver.find_elements(By.CSS_SELECTOR, 'td:nth-child(12)')
for item7 in pos2:
    pos2lst.append(item7.text)

age=driver.find_elements(By.CSS_SELECTOR, 'td:nth-child(14)')
for item8 in age:
    agelst.append(item8.text)

country=driver.find_elements(By.CSS_SELECTOR, 'td:nth-child(15)')
for item9 in country:
    countrylst.append(item9.text)


fields=['PLAYER', 'GROSS P/W', 'GROSS P/Y', 'CONTRACT EXP.', 'CLUB', 'AGE', 'POS BASIC', 'POS SPECIFIC', 'NATIONALITY']
df=pd.DataFrame([players,salariesgpw, salariesgpy, contractlst, clublst, agelst, pos1lst, pos2lst, countrylst], index=fields)

#parsed=[]

#players_list=[]
#for item in sel.xpath("//tr/td"):
#    players_list.append(item)
#    parsed.append({
#        'player': item.css('.name-column::text').get()
#        })


#parsed = []
#for item in sel.xpath("//div[(@class,'tw-tower')]/div[@data-target]"):
#for item in sel.xpath("//td[(@name-column)]"):
#    parsed.append({
#        'player': item.css('.firstcol::text').get()
        #'title': item.css('h3::text').get(),
 #       'url': item.css('.tw-link::attr(href)').get(),
  #      'username': item.css('.tw-link::text').get(),
   #     'tags': item.css('.tw-tag ::text').getall(),
    #    'viewers': ''.join(item.css('.tw-media-card-stat::text').re(r'(\d+)')),
 #   })
driver.refresh()

df.T.to_csv("salarios-bundesliga.csv")