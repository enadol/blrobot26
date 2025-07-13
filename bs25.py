# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 12:50:41 2021

@author: enado
"""
# WORKFLOW - bs23 - MEROBOT A GIT EN SHELL - LAUNCHWD
import codecs
import requests
from bs4 import BeautifulSoup
from gdate import lst_dates_cumul, TORNEO

lstJornadas = []
lst_clubes = []
lstHome = []
lstAway = []
count = 0
countgoles = 0
lstMatch = []
lstMD = []
lstGoles = []
lstGHome = []
lstGAway = []
lstGHomeH = []
lstGAwayH = []
lstIndexesH = []
lstIndexesA = []
# lstOdds=[]

page = requests.get(f'https://kicker.de/bundesliga/spieltag/{TORNEO}/-1', timeout=10)


if page.status_code == 200:
    content = page.content


klass = ["kick__v100-scoreBoard__scoreHolder__score", "kick__v100-scoreBoard__scoreHolder__text"]

soup = BeautifulSoup(content, 'html.parser')
# print(soup.prettify())
clubes = soup.find_all("div", attrs={"class": "kick__v100-gameCell__team__name"})
goles = soup.find_all("div", attrs={"class": klass})
# odds=soup.find_all("span", attrs={"class": "oddsServe-odd-value"})


for club in clubes:
    lst_clubes.append(club.text.strip())


for gol in goles:
    lstGoles.append(gol.text.strip())

# ESTAS DOS LÍNEAS PARA ARREGAR LA LISTA EN 2021/2022 LUEGO BORRAR!
# lstGoles[938]="0"
# lstGoles.insert(939, "0")

# for odd in odds:
#    lstOdds.append(odd.text.strip())


def classify_teams():
    """isolate home and away teams"""
    for ind, club in enumerate(lst_clubes):
        # count=2
        if ind % 2 == 0:
            lstHome.append(club)
        # count=count+1
        else:
            lstAway.append(club)
        # count=count+1


classify_teams()

# por partido suspendido hasta el 6 de abril
# del lstHome[161]
# del lstAway[161]


def goles_class():
    """isolate home and away goals"""
    nbuffer = 0
    for n in range(0, len(lstGoles)):
        nbuffer = nbuffer+n
        goal = lstGoles[nbuffer]
        lstGHome.append(goal)
        nbuffer = nbuffer+1
        goal = lstGoles[nbuffer]
        lstGHomeH.append(goal)
        nbuffer = nbuffer+1
        goal = lstGoles[nbuffer]
        lstGAway.append(goal)
        nbuffer = nbuffer+1
        goal = lstGoles[nbuffer]
        lstGAwayH.append(goal)
        nbuffer = nbuffer+1


jornadas = soup.find_all("h3", attrs={"class": "kick__section-headline"})

for jornada in jornadas:
    lstJornadas.append(jornada.text.strip())


def get_ga_indexes():
    """collect indexes"""
    factor = 2
    while factor < len(lstGoles):
        lstIndexesA.append(factor)
        factor = factor+4


def get_gh_indexes():
    """isolate home goals"""
    factor = 0
    while factor < len(lstGoles):
        lstIndexesH.append(factor)
        factor = factor+4


get_ga_indexes()
get_gh_indexes()


for index in lstIndexesA:
    element = lstGoles[index-1]
    lstGAway.append(element)


for index in lstIndexesH:
    element = lstGoles[index]
    lstGHome.append(element)


def match_in():
    """list of matches"""
    for index, item in enumerate(lstGHome):
    #for i in range(0, len(lstGHome)):
        if int(index) < len(lstGHome):
            lstMatch.append(f'    {lstHome[index]}  {lstGHome[index]}-{lstGAway[index]}  {lstAway[index]}\n')
    return lstMatch


def md_in():
    """list of match days"""
    for j in range(1, 35):
        # f.write(lstJornadas[j]+"\n")
        match_day = match_in()
        lstMD.append(match_day)


def me_robot():
    """write .txt file"""
    with codecs.open("C:/Users/enado/Proyectos/Python33/merobot/bundesliga-2025.txt", "w", "utf-8") as file:
        file.write("\ufeff")
        countjornadas = 0
        count2 = 0
        for line in lstMatch:
            g = lstMatch.index(line)
            if g % 9 == 0:
                file.write(lstJornadas[countjornadas] + "\n")
                file.write(lst_dates_cumul[countjornadas]+'\n')
                # file.write("    "+ line)
                file.write(f'    {line}')
                countjornadas = countjornadas+1
            else:
                if count2 <= len(lstMatch):
                    # file.write("    "+line)
                    file.write(f'    {line}')
            count2 = count2+1

            # else:
            # file.write("    "+line)
    file.close()


match_in()
me_robot()
