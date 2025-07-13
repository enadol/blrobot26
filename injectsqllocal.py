#from input import jornada
#import requests
from computetotall import seasonl
import sqlite3

conn = sqlite3.connect('season19.sqlite')
cur = conn.cursor()
conn.text_factory = str


cur.execute('''CREATE TABLE IF NOT EXISTS seasonlocal (Equipo TEXT, PJ INTEGER, PG INTEGER, PE INTEGER, PP INTEGER, GF INTEGER, GC INTEGER, DIF INTEGER, PUNTOS INTEGER)''')



for d in range(0, len(seasonl)):
    equipo= seasonl[d][0]
    pj = seasonl[d][1]
    pg = seasonl[d][2]
    pe = seasonl[d][3]
    pp = seasonl[d][4]
    gf = seasonl[d][5]
    gc = seasonl[d][6]
    difer = seasonl[d][7]
    puntos = seasonl[d][8]
    
    cur.execute('''INSERT OR IGNORE INTO seasonlocal (Equipo, PJ, PG, PE, PP, GF, GC, DIF, PUNTOS)  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (equipo, pj, pg, pe, pp, gf, gc, difer, puntos))

    conn.commit()			
cur.close()