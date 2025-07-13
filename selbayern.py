# -*- coding: utf-8 -*-
"""
Created on Wed May 17 07:50:40 2023

@author: enado
"""

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
#import pandas as pd

DRIVER_PATH='C:/Users/enado/ChromeDriver/chromedriver'
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver=webdriver.Chrome(executable_path=DRIVER_PATH)
driver.implicitly_wait(0.5)
driver.maximize_window()

driver.get("https://de.wikipedia.org/wiki/Liste_der_Fu%C3%9Fballspieler_des_FC_Bayern_M%C3%BCnchen")
tabla=driver.find_element(By.TAG_NAME, "table")

filas=tabla.find_elements(By.TAG_NAME, "tr")

