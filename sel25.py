# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 12:50:41 2021

@author: enado
"""
# WORKFLOW -> sel25 -> MEROBOT A GIT EN SHELL - LAUNCHWD
"""import packages"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.action_chains import ActionChains
from gateSEL import lst_dates_cumul, TORNEO
import codecs

lst_jornadas=[]
lst_clubes=[]
lst_home=[]
lst_away=[]
count=0
countgoles=0
lst_match=[]
lst_MD=[]
lst_goles=[]
lst_goles_home=[]
lst_goles_away=[]
lst_goles_home_half=[]
lst_goles_away_half=[]
lst_indexes_home=[]
lst_indexes_away=[]

DRIVER_PATH='C:/Users/enado/ChromeDriver'
service = webdriver.ChromeService(executable_path = 'C:/Users/enado/ChromeDriver/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(0.5)
driver.maximize_window()

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
klass=["kick__v100-scoreBoard__scoreHolder__score", "kick__v100-scoreBoard__scoreHolder__text"]

clubes=driver.find_elements(By.CLASS_NAME, "kick__v100-gameCell__team__name")
goles=driver.find_elements(By.CLASS_NAME, "kick__v100-scoreBoard__scoreHolder__score")
goles_text=driver.find_elements(By.CLASS_NAME, "kick__v100-scoreBoard__scoreHolder__text")

for club in clubes:
    lst_clubes.append(club.text.strip())

for gol in goles:
    lst_goles.append(gol.text.strip())

def classify_teams():
    for ind, club in enumerate(lst_clubes):
    #count=2
        if ind%2==0:
            lst_home.append(club)
        #count=count+1
        else:
            lst_away.append(club)
            #count=count+1

classify_teams()

def goles_class():
    nbuffer=0
    for n in range(0, len(lst_goles)):
        nbuffer=nbuffer+n
        goal=lst_goles[nbuffer]
        lst_goles_home.append(goal)
        nbuffer=nbuffer+1
        goal=lst_goles[nbuffer]
        lst_goles_home_half.append(goal)
        nbuffer=nbuffer+1
        goal=lst_goles[nbuffer]
        lst_goles_away.append(goal)
        nbuffer=nbuffer+1
        goal=lst_goles[nbuffer]
        lst_goles_away_half.append(goal)
        nbuffer=nbuffer+1
            
jornadas=driver.find_elements(By.CLASS_NAME, "kick__section-headline")

for jornada in jornadas:
    lst_jornadas.append(jornada.text.strip())

def get_goals_away_indexes():
    factor=2
    while(factor<len(lst_goles)):
        lst_indexes_away.append(factor)
        factor=factor+4

def get_goals_home_indexes():
    factor=0
    while(factor<len(lst_goles)):
        lst_indexes_home.append(factor)
        factor=factor+4

get_goals_away_indexes()
get_goals_home_indexes()

for index in lst_indexes_away:
    element=lst_goles[index-1]
    lst_goles_away.append(element)

for index in lst_indexes_home:
    element=lst_goles[index]
    lst_goles_home.append(element)
        
def match_in():
    for i in range(0, len(lst_goles_home)):
        if(i <len(lst_goles_home)):
            #lstMatch.append("    "+ lstHome[i] + "  "+lstGHome[i]+"-"+lstGAway[i]+"  "+ lstAway[i]+"\n")
            lst_match.append(f'    {lst_home[i]}  {lst_goles_home[i]}-{lst_goles_away[i]}  {lst_away[i]}\n')
        
def md_in():
    for j in range(1,35):
        #f.write(lstJornadas[j]+"\n")
        md=match_in()
        lst_MD.append(md)

def me_robot():
    with codecs.open("C:/Users/enado/Proyectos/Python33/merobot/bundesliga-{TORNEO[5:]}.txt", "w", "utf-8") as file:
        file.write("\ufeff")
        count_jornadas=0
        count2=0
        for line in lst_match:
            g=lst_match.index(line)
            if g%9==0:
                file.write(lst_jornadas[count_jornadas]+ "\n")
                file.write(lst_dates_cumul[count_jornadas]+'\n')
                    #file.write("    "+ line)
                file.write(f'    {line}')
                count_jornadas=count_jornadas+1
            else:
                if count2<=len(lst_match):
                        #file.write("    "+line)
                    file.write(f'    {line}')
            count2=count2+1
    file.close() 
        

match_in()
me_robot()

driver.close()