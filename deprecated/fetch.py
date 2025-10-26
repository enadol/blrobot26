# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 08:57:19 2020

@author: Enrique Lopez
"""

from precompute import matches, clubes

MDSolo=[]
md = []

def getClubData(club, match):
    
    pj=0
    pg=0
    pe=0
    pp=0
    puntos=0
    gf=0
    gc=0
    dif=0
    
    if match['teamhome']== club:
        pj= pj +1
        if match['pointslocal'] == 3:
            pg = pg +1
        elif match['pointslocal'] == 1:
            pe = pe +1
        else:
            if match['pointslocal'] == 0:
                pp = pp+1
    
        puntos= match['pointslocal']
        gf = match['goalshome']
        gc = match['goalsaway']
        dif = gf - gc
        
    else:
        if match['teamaway'] == club:
            pj = pj+1
            if match['pointsvisitor'] == 3:
                pg = pg+1
            elif match['pointsvisitor']== 1:
                pe= pe+1
            else:
                if match['pointsvisitor'] == 0:
                    pp = pp+1
        puntos = match['pointsvisitor']
        gf = match['goalsaway']
        gc = match['goalshome']
        dif = gf - gc
            
    return([club, pj,pg,pe,pp,gf,gc,dif, puntos])
    
def getClubMDSolo(club):
        for match in matches:
            if match['teamhome'] == club:
                md = getClubData(match['teamhome'], match)
                MDSolo.append(md)
            else:
                if match['teamaway'] == club:
                    md = getClubData(match['teamaway'], match)
                    MDSolo.append(md)

def injectClubMDs():
    for club in clubes:
        getClubMDSolo(club)
        
injectClubMDs()