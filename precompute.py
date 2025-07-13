import urllib.request

lstdates=[]
clubes = []
locations=[]
homes=[]
aways=[]
played=[]
lsthome= []
lstaway = []
lstgoalshome=[]
lstgoalsaway=[]
matches=[]

def buildMatch(club, pj):
    match= {"club": club,
            "pj": pj}
    return(match)

def getPuntos(goalshome, goalsaway):
    if goalshome > goalsaway:
        pointslocal=3
        pointsvisitor =0
    elif goalshome == goalsaway:
        pointslocal = 1
        pointsvisitor = 1
    else:
        pointslocal= 0
        pointsvisitor = 3
        
    return([pointslocal, pointsvisitor])

clubcodes={"Eintracht Frankfurt": "FFM","TSG Hoffenheim": "HOF","Bayern Muenchen": "FCB","VfL Wolfsburg": "WOB","Borussia Dortmund": "BVB","FC Augsburg": "FCA","RB Leipzig": "RBL","SC Freiburg":"SCF","Hertha BSC":"BSC","SpVgg Greuther Fuerth": "greuther","Bor. Moenchengladbach":"BMG", "Bayer 04 Leverkusen":"B04","VfL Bochum":"bochum","1. FSV Mainz 05":"M05", "VfB Stuttgart": "STU", "1. FC Koeln": "KOE", "1. FC Union Berlin": "FCU", "Arminia Bielefeld": "BIE"}
clubkeys={"Eintracht Frankfurt":"frankfurt", "TSG Hoffenheim":"hoffenheim","Bayern Muenchen": "bayern","VfL Wolfsburg":"wolfsburg","Borussia Dortmund":"dortmund","FC Augsburg":"augsburg","RB Leipzig": "leipzig","SC Freiburg":"freiburg","Hertha BSC":"herthabsc","SpVgg Greuther Fuerth":"greuther","Bor. Moenchengladbach": "mgladbach","Bayer 04 Leverkusen":"leverkusen","VfL Bochum":"bochum","1. FSV Mainz 05":"mainz", "VfB Stuttgart": "stuttgart", "1. FC Koeln": "KOE", "1. FC Union Berlin": "FCU", "Arminia Bielefeld": "BIE"}

for item in clubcodes:
    clubes = list(clubcodes.keys())

with urllib.request.urlopen('https://raw.githubusercontent.com/enadol/bundesliga/main/bundesliga-2022.txt') as response:
	data = response.read()

	data2 = data.decode('utf-8')

	filename = "core.txt"

	archivo = open(filename, "w", newline = '\n')

	data2 = data2.replace("ö", "oe")

	data2 = data2.replace("ü", "ue")

	lines = data2.splitlines()
    
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
        
        
        
        location = line.split('-', 1) #puede ser :
        locations.append(location) #se puede borrar luego
        if len(location) > 1:
            home = location[0]
            homes.append(home.lstrip())
            away = location[1]
            aways.append(away)
        
for i in range(0, len(homes)):
    local = homes[i].split('  ')
    if local[len(local)-1] != '':
        if local[len(local)-1] !=' ':
            goalshome = local[len(local)-1]
            lstgoalshome.append(goalshome.strip())
            lsthome.append(local[0])
            
    visitante = aways[i].split('  ')
    #visitante = visitante[0].split(' ', 1)            

    if visitante[0] != '':
        goalsaway = visitante[0][0]
        lstgoalsaway.append(goalsaway)
        lstaway.append(visitante[1].strip())
        i = i+1

 
for f in range(0, len(lsthome)):
    
    element={
            "teamhome": lsthome[f],
            "teamaway": lstaway[f],
            "goalshome": int(lstgoalshome[f]),
            "goalsaway": int(lstgoalsaway[f]),
            "pointslocal": getPuntos(int(lstgoalshome[f]), int(lstgoalsaway[f]))[0],
            "pointsvisitor": getPuntos(int(lstgoalshome[f]), int(lstgoalsaway[f]))[1]
            }
    matches.append(element) 

for club in clubes:
    count = 0
    for y in range(0, len(lsthome)):
        if lsthome[y]==club or lstaway[y] == club:
            count = count+1


      