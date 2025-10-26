#from input import jornada
#import requests
from computetotal import season
import sqlite3

conn = sqlite3.connect('season21.sqlite')
cur = conn.cursor()
conn.text_factory = str


cur.execute('''CREATE TABLE IF NOT EXISTS Partidos (Equipo TEXT, Jornada INTEGER, PJ INTEGER, PG INTEGER, PE INTEGER, PP INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Goles (Equipo TEXT, Jornada INTEGER, PJ INTEGER, Goles_a_favor INTEGER, Goles_en_contra INTEGER, Diferencia INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Puntos (Jornada INTEGER, Equipo TEXT, PJ INTEGER, Total_Puntos INTEGER)''')



for d in range(0, len(season)):
    equipo= season[d][0]
    jornada = season[d][1]
    pj = season[d][1]
    pg = season[d][2]
    pe = season[d][3]
    pp = season[d][4]
    gf = season[d][5]
    gc = season[d][6]
    difer = season[d][7]
    puntos = season[d][8]
    
    cur.execute('''INSERT OR IGNORE INTO Partidos (Equipo, Jornada, PJ, PG, PE, PP)  VALUES (?, ?, ?, ?, ?, ?)''', (equipo, jornada, pj, pg, pe, pp))
    cur.execute('''INSERT OR IGNORE INTO Goles (Equipo, Jornada, PJ, Goles_a_favor, Goles_en_contra, Diferencia)  VALUES (?, ?, ?, ?, ?, ?)''', (equipo, jornada, pj, gf, gc, difer))
    cur.execute('''INSERT OR IGNORE INTO Puntos (Equipo, Jornada, PJ, Total_Puntos)  VALUES (?, ?, ?, ?)''', (equipo, jornada, pj, puntos))
    
    conn.commit()			
cur.close()