# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:33:25 2020

@author: Enrique Lopez
"""
lstTotalsClubv=[]
lstTotalMDRowsv=[]
seasonv=[]


from computevisitor import MDSolov
from precompute import clubes

def getTotalsClubv():

    for club in clubes:
        MDBufferv=['', 0,0,0,0,0,0,0,0]
        for h in range(0, len(MDSolov)):
            if MDSolov[h][0]==club:
                for e in range(0, len(MDBufferv)):
                    if e > 0:
                        MDBufferv[e]=MDBufferv[e]+MDSolov[h][e]
                    else:
                        MDBufferv[0]=MDSolov[h][0]
        lstTotalsClubv.append(MDBufferv)
    
#getTotalsClub()

def getAll():
    for club in clubes:
        bufferpjv=0
        bufferpgv=0
        bufferpev=0
        bufferpgv=0
        bufferppv=0
        buffergfv=0
        buffergcv=0
        bufferdifv=0
        bufferpuntosv=0
        
        for g in range(0, len(MDSolov)):
            if MDSolov[g][0]==club:
                equipov = club
                bufferpjv = bufferpjv + MDSolov[g][1]
                bufferpgv = bufferpgv + MDSolov[g][2]
                bufferpev= bufferpev + MDSolov[g][3]
                bufferppv = bufferppv + MDSolov[g][4]
                buffergfv = buffergfv + MDSolov[g][5]
                buffergcv = buffergcv + MDSolov[g][6]
                bufferdifv = bufferdifv + MDSolov[g][7]
                bufferpuntosv= bufferpuntosv +MDSolov[g][8]
                seasonv.append([equipov, bufferpjv, bufferpgv, bufferpev, bufferppv, buffergfv, buffergcv, bufferdifv, bufferpuntosv])
                
                
getAll()