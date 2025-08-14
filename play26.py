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
from datetime import datetime, date

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
lst_dates_filtered = []
dates_final = []

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.kicker.de/")
    page.get_by_role("link", name="Zustimmen & weiter").click()
    get_clubes_stats(page)
    # ---------------------
    context.close()
    browser.close()

klass=["kick__v100-scoreBoard__scoreHolder__score", "kick__v100-scoreBoard__scoreHolder__text"]

# convertir los elementos de lst_dates_cumul a un formato de fecha y crear con ellos una nueva lista
# los elementos de la nueva lista deben quedar en integer y separados por comas
def convert_dates(lst_dates_cumul):
    for index, value in enumerate(lst_dates_cumul):
        if index < len(lst_dates_cumul)-1:
            element_list_one= lst_dates_cumul[index].split(".")
            element_list_two= next(lst_dates_cumul[index]).split(".")
            date_first= datetime(int(element_list_one[2]), int(element_list_one[1]), int(element_list_one[0]))
            date_last = datetime(int(element_list_two[2]), int(element_list_two[1]), int(element_list_two[0]))

            if index == 0:
                date_first_str = datetime.strftime(date_first, '%d.%m.%Y')
                lst_dates_filtered.append(date_first_str)
            else:
                if (date_last - date_first).days > 1:
            # convertir el objeto de fecha a un string con el formato deseado
                   date_last_str = datetime.strftime(date_last, '%d.%m.%Y')
                   lst_dates_filtered.append(date_last_str)
            #dates_final.append(date_second_str)
    return lst_dates_filtered

dates_final=convert_dates(lst_dates_cumul)

def get_clubes_stats(page):
    page.goto(f'https://kicker.de/bundesliga/spieltag/{TORNEO}/-1')
    clubes = page.locator(".kick__v100-gameCell__team__name").all_inner_texts()
    #print(clubes)
    jornadas=page.locator(".kick__section-headline").all_inner_texts()
    goles = page.locator(".kick__v100-scoreBoard__scoreHolder__score").all_inner_texts()
    #goles = page.locator(".kick__v100-scoreBoard__scoreHolder__text").all_inner_texts()
    # para torneo 2025 solamente o irregularidades cambiando el index
    goles.insert(486, "0")
    goles.insert(487, "2")
    #for club in clubes:
    #    lst_clubes.extend(club)
    lst_clubes= clubes
    #for gol in goles:
     #   lst_goles.extend(gol.strip())
    lst_goles = goles
    for jornada in jornadas:
        lst_jornadas.append(jornada)
    #lst_jornadas = jornadas

    classify_teams(lst_clubes)
    get_goals_away_indexes(lst_goles)
    get_goals_home_indexes(lst_goles)
    set_goles_home(lst_goles)
    set_goles_away(lst_goles)
    goles_class()
    match_in()
    me_robot()
    print(len(clubes))
    print(len(jornadas))
    print(len(goles))

def classify_teams(lst_clubes):
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
            
def get_goals_away_indexes(lst_goles):
    factor=2
    while(factor<len(lst_goles)):
        lst_indexes_away.append(factor)
        factor=factor+4

def get_goals_home_indexes(lst_goles):
    factor=0
    while(factor<len(lst_goles)):
        lst_indexes_home.append(factor)
        factor=factor+4

def set_goles_home(lst_goles):
    for index in lst_indexes_away:
        element=lst_goles[index-1]
        lst_goles_away.append(element)

def set_goles_away(lst_goles):
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
            if g%9 == 0:
                file.write(lst_jornadas[count_jornadas]+ "\n")
                file.write(dates_final[count_jornadas]+'\n')
                    #file.write("    "+ line)
                file.write(f'    {line}')
                count_buffer = count_jornadas + 1
                count_jornadas=count_buffer
            else:
                if count2<=len(lst_match):
                        #file.write("    "+line)
                    file.write(f'    {line}')
            count2=count2+1
    file.close() 

with sync_playwright() as playwright:
    run(playwright)
