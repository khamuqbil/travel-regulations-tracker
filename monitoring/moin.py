import requests
from bs4 import BeautifulSoup
import difflib
import time
from datetime import datetime
from urllib.request import urlopen, Request
import requests

# target URL
url = ('https://www.saudia.com/before-flying/travel-information/travel-requirements-by-international-stations?sc_lang=ar-SA&sc_country=SA')
# act like a browser
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'}

PrevVersion = ""
FirstRun = True
while True:

    # download the page
    response = requests.get(url, headers=headers)


    soup = BeautifulSoup(response.content, 'lxml')
    infos = soup.find('div', class_ = 'component accordion').text


    # remove all '-' sign.
    filtered_info = infos.replace('-',' ')

    #Printout The ResultPage for Testing
    # print(infos)


    # compare the page text to the previous version
    if PrevVersion != filtered_info:
        # on the first run - just memorize the page
        if FirstRun == True:
            PrevVersion = filtered_info
            FirstRun = False
            print ("Start Monitoring On:"+url+ " "+'  at: '+str(datetime.now()))
        else:
            print ("Changes detected at: "+ str(datetime.now()))
            OldPage = PrevVersion.splitlines()
            NewPage = soup.splitlines()
            # compare versions and highlight changes using difflib
            d = difflib.Differ()
            diff = d.compare(OldPage, NewPage)
            out_text = "\n".join([ll.rstrip() for ll in '\n'.join(diff).splitlines() if ll.strip()])
            print (out_text)
            OldPage = NewPage
            # print ('\n'.join(diff))
            PrevVersion = filtered_info
    else:
        print( "No Changes "+ str(datetime.now()))
    time.sleep(600)
    continue
