"""import packages"""
# from input import jornada
# import requests
import sqlite3
from computetotalwd import season
# import datetime

conn = sqlite3.connect('season25.sqlite')
cur = conn.cursor()
conn.text_factory = str


cur.execute('''CREATE TABLE IF NOT EXISTS Partidos (Equipo TEXT,\
            Jornada INTEGER, PJ INTEGER, PG INTEGER, PE INTEGER,\
            PP INTEGER, Date TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Goles (Equipo TEXT,\
            Jornada INTEGER, PJ INTEGER, Goles_a_favor INTEGER,\
            Goles_en_contra INTEGER, Diferencia INTEGER, Date TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Puntos (Jornada INTEGER,\
            Equipo TEXT, PJ INTEGER, Total_Puntos INTEGER, Date TEXT)''')

for d, value in enumerate(season):
#for d in range(0, len(season)):
    # day=datetime.datetime(season[d][9])
    equipo = season[d][0]
    jornada = season[d][1]
    pj = season[d][1]
    pg = season[d][2]
    pe = season[d][3]
    pp = season[d][4]
    gf = season[d][5]
    gc = season[d][6]
    difer = season[d][7]
    puntos = season[d][8]
    # fecha = datetime.datetime.strptime(season[d][9], "%Y-%m-%d")
    fecha = f'{season[d][9]}'

    cur.execute('''INSERT OR IGNORE INTO Partidos (Equipo, Jornada,\
                PJ, PG, PE, PP, Date)  VALUES (?, ?, ?, ?, ?, ?,\
                date(?))''',
                (equipo, jornada, pj, pg, pe, pp, fecha))
    cur.execute('''INSERT OR IGNORE INTO Goles (Equipo, Jornada,\
                PJ, Goles_a_favor, Goles_en_contra, Diferencia, Date)  \
                VALUES (?, ?, ?, ?, ?, ?, date(?))''',
                (equipo, jornada, pj, gf, gc, difer, fecha))
    cur.execute('''INSERT OR IGNORE INTO Puntos (Equipo, Jornada, PJ,\
                Total_Puntos, Date)  VALUES (?, ?, ?, ?, date(?))''',
                (equipo, jornada, pj, puntos, fecha))

    conn.commit()
cur.close()
conn.close()
