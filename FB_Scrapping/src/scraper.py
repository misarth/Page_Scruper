import requests as _requests
import bs4 as _bs4
from typing import List
import json as _json
#from facebook_scraper import get_posts
import mysql.connector



def _generate_url() -> str:
    url= "https://www.ticad8.tn/content/2/ticads-history"
    return url

def _get_page(url: str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup
    
###scraping the events and time informations from the page######
def events_of_the_day() -> List[str]:
    url = _generate_url()
    page = _get_page(url)
   
    raw_events=page.find_all('h4',class_="flex")
    events=[event.text.strip() for event in raw_events]

    raw_time=page.find_all('time',class_="block")
    time=[time.text.strip() for time in raw_time]
    print(len(time))

    L=[events,time]
    return L


####Storing data in json file############
if __name__ == "__main__":
    events = dict(zip(events_of_the_day()[0],events_of_the_day()[1]))
    with open("events.json", mode="w") as events_file:
        _json.dump(events, events_file, ensure_ascii=False)

####Storing data in MySQL Database#######

db= mysql.connector.connect(user="root",passwd="root",host="127.0.0.1", database="fb")
cursor= db.cursor()
cursor.execute("DROP table if EXISTS TICAD")
cursor.execute("""create table TICAD (name text, time text)""")
r=events_of_the_day()
for i in range(len(r[0])):
    cursor.execute("""INSERT INTO TICAD values(%s,%s)""",(r[0][i],r[1][i]))
    db.commit()
