import requests
from bs4 import BeautifulSoup
import difflib
import time
from datetime import datetime

# target URL
url = ('https://www.saudia.com/before-flying/travel-information/travel-requirements-by-international-stations?sc_lang=ar-SA&sc_country=SA')
# act like a browser
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'}
PrevVersion = ""
FirstRun = True
while True:

    # download the page
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage
    soup = BeautifulSoup(response.text, "lxml")
    infos = soup.find('div', class_ = 'component accordion')
    # remove all scripts and styles
    for script in infos(["script", "style"]):
        script.extract()
    infos = infos.get_text()
    # compare the page text to the previous version
    if PrevVersion != infos:
        # on the first run - just memorize the page
        if FirstRun == True:
            PrevVersion = infos
            FirstRun = False
            print ("Start Monitoring "+url+ ""+ str(datetime.now()))
        else:
            print ("Changes detected at: "+ str(datetime.now()))
            OldPage = PrevVersion.splitlines()
            NewPage = infos.splitlines()
            # compare versions and highlight changes using difflib
            d = difflib.Differ()
            diff = d.compare(OldPage, NewPage)
            out_text = "\n".join([ll.rstrip() for ll in '\n'.join(diff).splitlines() if ll.strip()])
            print (out_text)
            OldPage = NewPage
            #print ('\n'.join(diff))
            PrevVersion = infos
    else:
        print( "No Changes "+ str(datetime.now()))
    time.sleep(1200)
    continue
