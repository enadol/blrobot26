# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 12:50:41 2021

@author: enado
"""
# WORKFLOW -> sel25 -> MEROBOT A GIT EN SHELL - LAUNCHWD
"""import packages"""
import re
from playwright.sync_api import Playwright, sync_playwright, expect
from gatePLAY import lst_dates_cumul, TORNEO
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

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.kicker.de/")
    page.get_by_role("link", name="Zustimmen & weiter").click()
    get_clubes_stats(page)
    classify_teams()
    get_goals_away_indexes()
    get_goals_home_indexes()
    match_in()
    me_robot()
    # ---------------------
    context.close()
    browser.close()

klass=["kick__v100-scoreBoard__scoreHolder__score", "kick__v100-scoreBoard__scoreHolder__text"]


def get_clubes_stats(page):
    page.goto(f'https://kicker.de/bundesliga/spieltag/{TORNEO}/-1')
    clubes = page.locator(".kick__v100-gameCell__team__name").all_inner_texts()
    #print(clubes)
    jornadas=page.locator(".kick__section-headline").all_inner_texts()
    goles = page.locator(".kick__v100-scoreBoard__scoreHolder__score").all_inner_texts()
    #goles = page.locator(".kick__v100-scoreBoard__scoreHolder__text").all_inner_texts()
    for club in clubes:
        lst_clubes.extend(club.strip())
    for gol in goles:
        lst_goles.extend(gol.strip())
    for jornada in jornadas:
        lst_jornadas.extend(jornada.strip())
    print(len(clubes))
    print(len(jornadas))
    print(len(goles))

# pendiente 10 AGOSTO

def classify_teams():
    for ind, club in enumerate(lst_clubes):
    #count=2
        if ind%2==0:
            lst_home.append(club)
        #count=count+1
        else:
            lst_away.append(club)
            #count=count+1

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
    print(lst_match)

def me_robot():
    with codecs.open(f'C:/Users/enado/Proyectos/Python33/merobot/bundesliga-add-{TORNEO[5:]}.txt', "w", "utf-8") as file:
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
        

with sync_playwright() as playwright:
    run(playwright)
