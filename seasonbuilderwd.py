# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:33:25 2020

@author: Enrique Lopez
"""
from fetchwd import MDSolo
from precomputewd import clubes

lstTotalsClub = []
lstTotalMDRows = []
season = []

def get_totals_club():
    """compute totals for each club"""
    for club in clubes:
        MDBuffer = ['', 0, 0, 0, 0, 0, 0, 0, 0, ""]
        for index, value in enumerate(MDSolo):
            if MDSolo[index][0] == club:
                for e, e_value in enumerate(MDBuffer):
                    if int(e) > 0 and e < 9:
                        MDBuffer[e] += MDSolo[index][e]
                    else:
                        MDBuffer[0] = MDSolo[index][0]
        lstTotalsClub.append(MDBuffer)

def get_all():
    """compute all data"""
    for club in clubes:
        bufferpj = 0
        bufferpg = 0
        bufferpe = 0
        bufferpp = 0
        buffergf = 0
        buffergc = 0
        bufferdif = 0
        bufferpuntos = 0
        bufferdates = ""
        for g, value in enumerate(MDSolo):
            if MDSolo[g][0] == club:
                equipo = club
                bufferpj += MDSolo[g][1]
                bufferpg += MDSolo[g][2]
                bufferpe += MDSolo[g][3]
                bufferpp += MDSolo[g][4]
                buffergf += MDSolo[g][5]
                buffergc += MDSolo[g][6]
                bufferdif += MDSolo[g][7]
                bufferpuntos += MDSolo[g][8]
                bufferdates = MDSolo[g][9]
                season.append([equipo, bufferpj, bufferpg, bufferpe,
                                bufferpp, buffergf, buffergc, bufferdif, bufferpuntos, bufferdates])

get_totals_club()
get_all()
 