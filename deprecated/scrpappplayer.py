# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:47:36 2022

@author: enado
"""
import requests
from bs4 import BeautifulSoup

vornamen=[]
nachnamen=[]
kader=[]
team=[]
#md=16
#lstDates=[]
#lstDatesCumul=[]
player="Thomas Müller"

club="Bayern München"
torneo="2022-23"
klassvita=["kick__vita__header__person-detail-kvpair-info"]
klassfrom=["kick__vita__stationline-timeline"]
klasspastclub=["kick__vita__stationline-team"]
klassalturapeso=["kick__vita__header__person-detail-kvpair-info kick__vita__header__person-detail-kvpair-info-s"]
klassnation=["kick__vita__header__person-detail-kvpair--nation"]
klasscompfilter=["kick__vita__liglog"]
klasstrikot=["kick__player__number"]

def modPlayer(player):
    playerdef=""
    playerlow=player.lower()
    playerminus=playerlow.replace(" ", "-")
    if("ü" in playerminus):
        playerminus=playerminus.replace("ü", "ue")
    elif("ö" in playerminus):
        playerminus=playerminus.replace("ö", "oe")
    else:
        playerminus=playerminus.replace("ä", "ae")
    playerdef=playerminus
    return playerdef
    #print(playerdef)
#def getMDDates(mday):
 #   lstMDDates=[]

club3=modPlayer(club)

#urlkader=f"https://www.kicker.de/{club3}/kader/bundesliga/{torneo}" 
#kaderpage= requests.get(urlkader)
#if kaderpage.status_code== 200:
#    kadercontent = kaderpage.content

#soupnames = BeautifulSoup(kadercontent, 'html.parser')
#klassnames=["kick__table--ranking__index kick__t__a__l kick__respt-m-w-190"]

#kadernames=soupnames.find_all("td", attrs={"class": klassnames})

#for nombre in kadernames:
    #namesplit=nombre.text.split(" ")
#    if(len(namesplit)>2):
 #       vornamen.append(namesplit[len(namesplit)-1])
  #      nachnamen.append(namesplit[1]+ " "+ namesplit[0])
   # else:
#    nombres=nombre.find("span")
 #   apellidos=nombre.find("strong")
  #  vornamen.append(nombres.text)
   # nachnamen.append(apellidos.text)
    #kader.append(nombres.text+" "+apellidos.text)


#for knombre in kader:
    
player3=modPlayer(player)
url=f"https://kicker.de/{player3}/spieler/bundesliga/{torneo}/{club3}"
 # EJEMPLO https://www.kicker.de/niclas-fuellkrug/spieler/bundesliga/2022-23/werder-bremen
mdpage= requests.get(url)
if mdpage.status_code== 200:
    content = mdpage.content

soup = BeautifulSoup(content, 'html.parser')


    #print(soup.prettify())
dates=soup.find_all("div", attrs={"class": klassvita})
desde=soup.find_all("td", attrs={"class": klassfrom})
pastclub=soup.find_all("a", attrs={"class": klasspastclub})
altura=soup.find_all("div", attrs={"class": klassalturapeso})
nacion=soup.find_all("div", attrs={"class": klassnation})
trikot=soup.find_all("span", attrs={"class": klasstrikot})

born1=dates[1].text.split(" ")[1][:10]
age=dates[1].text.split(" ")[45][1:3]
ageinclub=desde[0].text.split("seit\n")[1][:10]
fromclub=pastclub[1].text[4:].split("\n")[0]
alturatxt=altura[0].text.split(" ")[1]
pesotxt=altura[1].text.split(" ")[1]
naciontxt=nacion[0].text.split("\r\n")[1].strip()
       
    
comptofilter=soup.find_all("div", attrs={"class": klasscompfilter})
elementindex=[]
for element in comptofilter:
    
    if(element.text.strip()=="Bundesliga"):
           #para partidos jugados en el presente torneo de bl
        datosbl=soup.find_all("td", attrs={"class": "kick__t__a__r"})
            #para demás datos bl menos partidos totales en la bl
        datosbl2=soup.find_all("td")
    #    else:
     #       datosbl=[0]
      #      datosbl2=[0]
        
            
       # if(len(datosbl2)>2):
        for element in datosbl2:
             if("Bundesliga" in element.text):
                indexes=datosbl2.index(element)
                elementindex.append(indexes)

#TODO revisar pplayed en jugadores que no tienen Copa del Mundo
        playedindex=elementindex[1]+1        
        pplayed=datosbl2[playedindex].text.strip()[:2]
        blgamesindex=elementindex[0]+1
        partidosbl=datosbl2[blgamesindex].text.strip().split("S")[0].strip()
        #partidosbl=datosbl2[blgamesindex].text.split("\n")[2]
        golesindex=elementindex[1]+3
        golesbl=datosbl2[golesindex].text.strip()
#golesbl=datosbl2[golesindex].text.split("\r\n")[1]

        assistindex=elementindex[1]+5
        assists=datosbl2[assistindex].text.strip()
#assists=datosbl2[assistindex].text.split("\r\n")[1]

        gelbindex=elementindex[1]+9
        gelbe=datosbl2[gelbindex].text.strip()
#gelbe=datosbl2[gelbindex].text.split("\r\n")[1]

        gelbrotindex=gelbindex+1
        gelbrot=datosbl2[gelbrotindex].text.strip()
#gelbrot=datosbl2[gelbrotindex].text.split("\r\n")[1]

        rotindex=gelbrotindex+1
        rot=datosbl2[rotindex].text.strip()
        
#rot=datosbl2[rotindex].text.split("\r\n")[1]
    #    else:
     #       pplayed=0
      #      partidosbl=0
       #     golesbl=0
        #    assists=0
         #   gelbe=0
          #  gelbrot=0
           # rot=0
    
        if(len(trikot)>0):
           numero=trikot[0].text
        else:
           numero=0
        playerdict={"Jugador": player, "Nacimiento": born1, "Edad": age, "Nación": naciontxt, "Altura": alturatxt, "Peso": pesotxt, "PJ": pplayed, "Goles": golesbl, "Asistencias": assists, "TA": gelbe, "TAR": gelbrot, "TR": rot, "Desde": ageinclub, "De": fromclub, "BL": partidosbl, "Número": numero}
#team.append(playerdict)