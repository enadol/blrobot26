# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 08:57:19 2020

@author: Enrique Lopez
"""
from precomputewd import matches, clubes

MDSolol = []
md = []

def get_club_data(club, match):
    """compute club data"""
    pj = 0
    pg = 0
    pe = 0
    pp = 0
    puntos = 0
    gf = 0
    gc = 0
    dif = 0

    if match['teamhome'] == club:
        pj += 1
        if match['pointslocal'] == 3:
            pg += 1
        elif match['pointslocal'] == 1:
            pe += 1
        else:
            if match['pointslocal'] == 0:
                pp += 1
        puntos = match['pointslocal']
        gf = match['goalshome']
        gc = match['goalsaway']
        dif = gf - gc

    elif match['teamaway'] == club:
        pj += 1
        if match['pointsvisitor'] == 3:
            pg += 1
        elif match['pointsvisitor'] == 1:
            pe += 1
        else:
            if match['pointsvisitor'] == 0:
                pp += 1
        puntos = match['pointsvisitor']
        gf = match['goalsaway']
        gc = match['goalshome']
        dif = gf - gc

    return [club, pj, pg, pe, pp, gf, gc, dif, puntos]

def get_club_md_solo(club):
    """compute club data local"""
    for match in matches:
        if match['teamhome'] == club or match['teamaway'] == club:
            md = get_club_data(club, match)
            MDSolol.append(md)

def inject_club_mds():
    """inject club data local"""
    MDSolol.clear()
    for club in clubes:
        get_club_md_solo(club)

inject_club_mds()

