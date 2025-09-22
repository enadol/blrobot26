"""This script uses Playwright to scrape matchday dates from the Kicker website for/
 the Bundesliga season 2025-26.
It collects the dates for each matchday and stores them in a cumulative list."""
from playwright.sync_api import Playwright, sync_playwright, expect

MD=4
TORNEO='2025-26'
lst_dates_cumul = []

def get_mdd_dates(mday, page):
    """create empty list to populate with dates"""
    list_mdd_dates = []
    page.goto(f'https://kicker.de/bundesliga/spieltag/{TORNEO}/{mday}')
    dates = page.locator(".kick__v100-gameList__header").all_inner_texts()
    #dates = re.findall(r'\d{1,2}\.\s\w+\.\s\d{4}', date)
    for date in dates:
        date_formatted = date.split(" ")[1].strip()
        #list_mdd_dates.append(date_formatted.strip())
        list_mdd_dates.append(date_formatted)
    return list_mdd_dates

def run(playwright: Playwright) -> None:
    """Main function to run the Playwright script"""
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.kicker.de/")
    page.get_by_role("link", name="Zustimmen & weiter").click()
    for i in range(1, MD+1):
        list_mdd_dates = get_mdd_dates(i, page)
        lst_dates_cumul.extend(list_mdd_dates)
    #print(lst_dates_cumul)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
