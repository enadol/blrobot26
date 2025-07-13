"""import packages"""
import urllib.request
# import datetime

lstdates = []
clubes = []
locations = []
homes = []
aways = []
played = []
lsthome = []
lstaway = []
lstgoalshome = []
lstgoalsaway = []
matches = []
lstindexes = []
lstrepeats = []
doc = []
dates_structured = []

def build_match(club, pj):
    """create match structure"""
    match = {"club": club,
             "pj": pj}
    return match

def get_puntos(goalshome, goalsaway):
    """compute points"""
    if goalshome > goalsaway:
        pointslocal = 3
        pointsvisitor = 0
    elif goalshome == goalsaway:
        pointslocal = 1
        pointsvisitor = 1
    else:
        pointslocal = 0
        pointsvisitor = 3
    return ([pointslocal, pointsvisitor])

def get_repeats():
    """locate and call data"""
    # lstindexes=[]
    for line in lines:
        if line:  # Check if line is not empty
            if not line.startswith('Spieltag') and not line.startswith('='):
                doc.append(line)
                if line.startswith('[') and not line.startswith('Spieltag'):
                    lstindexes.append(len(doc) - 1)  # Use len(doc) - 1 instead of doc.index(line)

    for repeat in lstindexes:
        i = lstindexes.index(repeat)
        if i == 0:
            newrepeat = 0
            # lstrepeats.append(newrepeat)
        else:
            newrepeat = 9
            lstrepeats.append(newrepeat)
    # print(lstindexes)
    lstrepeats.append(9)
   # print(lstrepeats)

def structure_dates():
    """format and structure dates"""
    for fecha in lstdates:
        i = lstdates.index(fecha)
        for e in range(0, lstrepeats[i]):
            fechaformat = fecha.split(' ')
            fechaformat = fechaformat[1].split(']')
            fechaformat = fechaformat[0].split('.')
            if int(fechaformat[1]) >= 8:
                # change
                year = '2025'
            else:
                # change
                year = '2026'
            fechaformat = year+'-'+fechaformat[1].zfill(2)+'-'+fechaformat[0].zfill(2)
            dates_structured.append(fechaformat)

URL='https://raw.githubusercontent.com/enadol/merobot/master/bundesliga-2026.txt'
with urllib.request.urlopen(URL) as response:
    data = response.read()
    data2 = data.decode('utf-8')
    file_name = "core.txt"
    archivo = open(file_name, "w", newline='\n', encoding='utf-8')
    data2 = data2.replace("ö", "oe")
    data2 = data2.replace("ü", "ue")
    lines = data2.splitlines()

get_repeats()
archivo.close()

for line in lines:
    if line.startswith('['):
        date = line
        lstdates.append(date)
    elif line == ' ':
        vacia = line
    elif line.startswith('Spieltag'):
        mday = line
    elif "Bundesliga" in line:
        titulo = line
    else:
        if line.startswith('  20.30'):
            line = line.split('20.30')[1]
        elif line.startswith('  18.30'):
            line = line.split('18.30')[1]
        elif line.startswith('  15.30'):
            line = line.split('15.30')[1]
        elif line.startswith('  18.00'):
            line = line.split('18.00')[1]
        else:
            line = line

        location = line.split('-', 1)  # puede ser :
        locations.append(location)  # se puede borrar luego
        if len(location) > 1:
            home = location[0]
            homes.append(home.lstrip())
            away = location[1]
            aways.append(away)

for index, value in enumerate(homes):
    local = value.split('  ')
    if local and local[-1].strip():
        goalshome = local[-1].strip()
        lstgoalshome.append(goalshome)
        lsthome.append(local[0].strip())
    visitante = aways[index].split('  ')
    if visitante and visitante[0].strip():
        goalsaway = visitante[0][0]
        lstgoalsaway.append(goalsaway)
        lstaway.append(visitante[1].strip() if len(visitante) > 1 else '')

structure_dates()
for index, value in enumerate(lsthome):
    element = {
        "teamhome": lsthome[index],
        "teamaway": lstaway[index],
        "goalshome": int(lstgoalshome[index]),
        "goalsaway": int(lstgoalsaway[index]),
        "pointslocal": get_puntos(int(lstgoalshome[index]), int(lstgoalsaway[index]))[0],
        "pointsvisitor": get_puntos(int(lstgoalshome[index]), int(lstgoalsaway[index]))[1],
        "date": dates_structured[index]
    }
    matches.append(element)

clubes=list(set(lsthome))

#for club in clubes:
#    count = 0
#    for index, value in enumerate(lsthome):
#        # for y in range(0, len(lsthome)):
#        if lsthome[index] == club or lstaway[index] == club:
#            count = count+1
