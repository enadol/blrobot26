# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:47:36 2022

@author: enado
"""
# SOLO ACTUALIZAR MD !!
#NO CORRER SOLO!! CORRE EN sel25!!

"""import packages"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.action_chains import ActionChains

MD=1
TORNEO='2025-26'
lst_dates_cumul = []

URL = f'https://kicker.de/bundesliga/spieltag/{TORNEO}/{MD}'

DRIVER_PATH='C:/Users/enado/ChromeDriver'
#driver=webdriver.Firefox()
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver=webdriver.Chrome(DRIVER_PATH)
#driver = webdriver.Chrome(ChromeDriverManager().install())
service = webdriver.ChromeService(executable_path = 'C:/Users/enado/ChromeDriver/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(0.5)
driver.maximize_window()

# 2. Navigate to the Kicker page with all the matchdays
driver.get(f'https://kicker.de/bundesliga/spieltag/{TORNEO}/-1')

# 3. Wait for the "Google Web" option to be clickable
WebDriverWait(driver, 10)

# 4. Click the "Google Web" option
#google_web_option.click()

# 5. Wait for the "Accept" button to be clickable
accept_button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH,"//a[contains(text(), 'Zustimmen & weiter')]")))

# 6. Click the "Accept" button
accept_button.click()

def get_mdd_dates(mday):
    """create empty list to populate with dates"""
    list_mdd_dates = []
    driver.get(f'https://kicker.de/bundesliga/spieltag/{TORNEO}/{mday}')
    dates = driver.find_elements(By.CLASS_NAME, "kick__v100-gameList__header")

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

driver.close()