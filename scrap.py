import requests
from bs4 import BeautifulSoup
import difflib
import time
import os
# import datetime

def tracker():

    #Headers
    headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'}
    # Url
    url = ('https://www.saudia.com/before-flying/travel-information/travel-requirements-by-international-stations?sc_lang=ar-SA&sc_country=SA')

    #request
    req = requests.get(url, headers=headers)

    #settings_timer
    local_time = time.ctime()

    filename = "/SaudiAirlines"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Parent Directory path
    # parent_dir = "/"
    # now = datetime.datetime.now()

    #Scraping
    soup = BeautifulSoup(req.content, 'lxml')
    infos = soup.find('div', class_ = 'component accordion')
    contries = infos.find_all('li', class_ = 'item')
    for index, info in enumerate (contries):
        with open(f'{filename}{index}/{index}-{local_time}.txt','w') as f:
            contry = info.find_next('div', class_='field-heading').text.replace(' ',' ')
            date = info.find('p').text
            content = info.find('div', class_='field-content').text.replace(' ',' ')

            f.write(f' الدولة: {contry.strip()} \n')
            f.write(f' التاريخ: {content.strip()} \n')
            # f.write(f' التاريخ: {date.strip()} \n')
        print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        tracker()
        time_wait = 10
        print(f'Waiting {time_wait} minutes ...')
        time.sleep(time_wait + 60)
