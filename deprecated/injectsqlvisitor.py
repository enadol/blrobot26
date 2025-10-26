#from input import jornada
#import requests
from computetotalv import seasonv
import sqlite3

conn = sqlite3.connect('season19.sqlite')
cur = conn.cursor()
conn.text_factory = str


cur.execute('''CREATE TABLE IF NOT EXISTS seasonvisitor (Equipo TEXT, PJ INTEGER, PG INTEGER, PE INTEGER, PP INTEGER, GF INTEGER, GC INTEGER, DIF INTEGER, PUNTOS INTEGER)''')



for d in range(0, len(seasonv)):
    equipo= seasonv[d][0]
    pj = seasonv[d][1]
    pg = seasonv[d][2]
    pe = seasonv[d][3]
    pp = seasonv[d][4]
    gf = seasonv[d][5]
    gc = seasonv[d][6]
    difer = seasonv[d][7]
    puntos = seasonv[d][8]
    
    cur.execute('''INSERT OR IGNORE INTO seasonvisitor (Equipo, PJ, PG, PE, PP, GF, GC, DIF, PUNTOS)  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (equipo, pj, pg, pe, pp, gf, gc, difer, puntos))

    conn.commit()			
cur.close()