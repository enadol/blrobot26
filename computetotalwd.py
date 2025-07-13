# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:33:25 2020

@author: Enrique Lopez
"""
lstTotalsClub=[]
lstTotalMDRows=[]
season=[]


from fetchwd import MDSolo
from precomputewd import clubes

def getTotalsClub():

    for club in clubes:
        MDBuffer=['', 0,0,0,0,0,0,0,0,""]
        for h in range(0, len(MDSolo)):
            if MDSolo[h][0]==club:
                for e in range(0, len(MDBuffer)):
                    if e > 0:
                        MDBuffer[e]=MDBuffer[e]+MDSolo[h][e]
                    else:
                        MDBuffer[0]=MDSolo[h][0]
        lstTotalsClub.append(MDBuffer)
    
#getTotalsClub()

def getAll():
    for club in clubes:
        bufferpj=0
        bufferpg=0
        bufferpe=0
        bufferpg=0
        bufferpp=0
        buffergf=0
        buffergc=0
        bufferdif=0
        bufferpuntos=0
        bufferdates=""
        for g in range(0, len(MDSolo)):
            if MDSolo[g][0]==club:
                equipo = club
                bufferpj = bufferpj + MDSolo[g][1]
                bufferpg = bufferpg + MDSolo[g][2]
                bufferpe= bufferpe + MDSolo[g][3]
                bufferpp = bufferpp + MDSolo[g][4]
                buffergf = buffergf + MDSolo[g][5]
                buffergc = buffergc + MDSolo[g][6]
                bufferdif = bufferdif + MDSolo[g][7]
                bufferpuntos= bufferpuntos +MDSolo[g][8]
                bufferdates=MDSolo[g][9]
                season.append([equipo, bufferpj, bufferpg, bufferpe, bufferpp, buffergf, buffergc, bufferdif, bufferpuntos, bufferdates])
                
                
getAll()