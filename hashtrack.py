import time
import hashlib
import smtplib, ssl
from urllib.request import urlopen, Request



url = Request('https://www.saudia.com/before-flying/travel-information/travel-requirements-by-international-stations?sc_lang=ar-SA&sc_country=SA',
    headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'})

# to perform a GET request and load the
# content of the website and store it in a var
response = urlopen(url).read()

# to create the initial hash
currentHash = hashlib.sha224(response).hexdigest()
print("running")
time.sleep(10)
while True:
    try:
        # perform the get request and store it in a var
        response = urlopen(url).read()

        # create a hash
        currentHash = hashlib.sha224(response).hexdigest()

        # wait for 30 seconds
        time.sleep(30)

        # perform the get request
        response = urlopen(url).read()

        # create a new hash
        newHash = hashlib.sha224(response).hexdigest()

        # check if new hash is same as the previous hash
        if newHash == currentHash:
            continue

        # if something changed in the hashes
        else:
            # notify
            local_time = time.ctime()
            print(f"something changed at :{local_time}")

    #         req = requests.get(url, headers=headers)
    #         content = req.text
    #         soup = BeautifulSoup(req.content, 'html.parser')
    #         infos = soup.find('div', class_ = 'component accordion').text
    #
    #         text_file = open('saudi5feb.txt','w')
    # text_file.write(infos)
    # text_file.close()
            # port = 465  # For SSL
            # smtp_server = "smtp.gmail.com"
            # sender_email = "travelregulations.khamuqbil@gmail.com"  # Enter your address
            # receiver_email = "khamuqbil@gmail.com"  # Enter receiver address
            # password = ("")
            # message = """\
            # Subject: Hi there
            #
            # There is an UPDATES from SaudiAirlines at: {local_time} follow up ."""
            #
            # context = ssl.create_default_context()
            # with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            #     server.login(sender_email, password)
            #     server.sendmail(sender_email, receiver_email, message)


            # again read the website
            response = urlopen(url).read()

            # create a hash
            currentHash = hashlib.sha224(response).hexdigest()

            # wait for 30 seconds
            time.sleep(30)
            continue

    # To handle exceptions
    except Exception as e:
        print("error")
