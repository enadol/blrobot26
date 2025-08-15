"""import packages"""
import codecs
from datetime import datetime
from playwright.sync_api import Playwright, sync_playwright
from gatePLAY import lst_dates_cumul, TORNEO

# WORKFLOW -> sel25 -> MEROBOT A GIT EN SHELL - LAUNCHWD

lst_jornadas = []
lst_clubes = []
lst_home = []
lst_away = []
lst_match = []
lst_goles = []
lst_goles_home = []
lst_goles_away = []
lst_goles_home_half = []
lst_goles_away_half = []
lst_indexes_home = []
lst_indexes_away = []
lst_dates_filtered = []
dates_final = []

def run(playwright: Playwright) -> None:
    """Main function to run the Playwright script"""
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.kicker.de/")
    page.get_by_role("link", name="Zustimmen & weiter").click()
    get_clubes_stats(page)
    # ---------------------
    context.close()
    browser.close()


def convert_dates(lst_dates_cumul):
    """Function to convert date strings to datetime objects and filter /
    them using date mathematics"""
    for index, value in enumerate(lst_dates_cumul):
        if index < len(lst_dates_cumul) - 1:
            element_list_one = lst_dates_cumul[index].split(".")
            element_list_two = lst_dates_cumul[index + 1].split(".")
            date_first = datetime(int(element_list_one[2]), int(element_list_one[1]), \
                                  int(element_list_one[0]))
            date_last = datetime(int(element_list_two[2]), int(element_list_two[1]), \
                                 int(element_list_two[0]))

            if index == 0:
                date_first_str = datetime.strftime(date_first, '%d.%m.%Y')
                lst_dates_filtered.append(date_first_str)
            else:
                if (date_last - date_first).days > 1:
                    # convertir el objeto de fecha a un string con el formato deseado
                    date_last_str = datetime.strftime(date_last, '%a. %d.%m.%Y')
                    lst_dates_filtered.append(date_last_str)
    return lst_dates_filtered

dates_final = convert_dates(lst_dates_cumul)

def get_clubes_stats(page):
    """Function to get the clubs stats from the Bundesliga page"""
    page.goto(f'https://kicker.de/bundesliga/spieltag/{TORNEO}/-1')
    clubes = page.locator(".kick__v100-gameCell__team__name").all_inner_texts()
    jornadas = page.locator(".kick__section-headline").all_inner_texts()
    goles = page.locator(".kick__v100-scoreBoard__scoreHolder__score").all_inner_texts()
    # para torneo 2025 solamente o irregularidades cambiando el index
    goles.insert(486, "0")
    goles.insert(487, "2")
    lst_clubes = clubes
    lst_goles = goles
    for jornada in jornadas:
        lst_jornadas.append(jornada)

    classify_teams(lst_clubes)
    get_goals_away_indexes(lst_goles)
    get_goals_home_indexes(lst_goles)
    set_goles_home(lst_goles)
    set_goles_away(lst_goles)
    goles_class()
    match_in()
    me_robot()
    #print(len(clubes))
    #print(len(jornadas))
    #print(len(goles))

def classify_teams(lst_clubes):
    """Function to classify teams into home and away lists"""
    for ind, club in enumerate(lst_clubes):
        if ind % 2 == 0:
            lst_home.append(club)
        else:
            lst_away.append(club)

def goles_class():
    """Function to classify goals into goals home and goals away lists"""
    nbuffer = 0
    for n in range(0, len(lst_goles)):
        nbuffer = nbuffer + n
        if nbuffer < len(lst_goles):
            goal = lst_goles[nbuffer]
            lst_goles_home.append(goal)
            nbuffer = nbuffer + 1
            if nbuffer < len(lst_goles):
                goal = lst_goles[nbuffer]
                lst_goles_home_half.append(goal)
                nbuffer = nbuffer + 1
                if nbuffer < len(lst_goles):
                    goal = lst_goles[nbuffer]
                    lst_goles_away.append(goal)
                    nbuffer = nbuffer + 1
                    if nbuffer < len(lst_goles):
                        goal = lst_goles[nbuffer]
                        lst_goles_away_half.append(goal)

def get_goals_away_indexes(lst_goles):
    """Function to get indexes of away goals in the goals list jumping halftime scores"""
    factor = 2
    while factor < len(lst_goles):
        lst_indexes_away.append(factor)
        factor = factor + 4

def get_goals_home_indexes(lst_goles):
    """Function to get indexes of home goals in the goals list jumping halftime scores"""
    factor = 0
    while factor < len(lst_goles):
        lst_indexes_home.append(factor)
        factor = factor + 4

def set_goles_away(lst_goles):
    """Function to set away goals based on the indexes collected"""
    for index in lst_indexes_away:
        if index < len(lst_goles):
            element = lst_goles[index - 1]
            lst_goles_away.append(element)

def set_goles_home(lst_goles):
    """Function to set home goals based on the indexes collected"""
    for index in lst_indexes_home:
        if index < len(lst_goles):
            element = lst_goles[index]
            lst_goles_home.append(element)

def match_in():
    """Function to create a structured list of matches with home and away teams and their scores"""
    for i in range(0, min(len(lst_goles_home), len(lst_goles_away))):
        lst_match.append(f'    {lst_home[i]}  {lst_goles_home[i]}-{lst_goles_away[i]} \
{lst_away[i]}\n')
    return lst_match

def me_robot():
    """Function to write the match data into a text file with the tournament name"""
    with codecs.open(f'C:/Users/enado/Proyectos/Python33/merobot/\
bundesliga-{TORNEO[5:]}.txt', "w", "utf-8") as file:
        file.write("\ufeff")
        count_jornadas = 0
        for line in lst_match:
            g = lst_match.index(line)
            if g % 9 == 0:
                file.write(lst_jornadas[count_jornadas] + "\n")
                if count_jornadas < len(dates_final):
                    file.write(dates_final[count_jornadas] + '\n')
                file.write(f'    {line}')
                count_jornadas += 1
            else:
                file.write(f'    {line}')

with sync_playwright() as playwright:
    run(playwright)
