#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, time, json
from SMTPclient import *

lastIP = ""

# Reads configuration file.
with open("config.json", "r") as f:
            rawData = f.read()
config = json.loads(rawData)

# Loads configuration
URL = config["url"]
backup = config["backup"]
smpt_server = config["smpt_server"]
mail_login = config["mail_login"]
password = config["password"]
to = config["mail_to"]


while True:
    # Main loop. tries to connect to the IP provider website.
    # If It couldn't connecto ot it it would ignore the exception
    # and wait 5 minutes and try again.
    
    try:
        response = requests.get(URL)
        # if response.status_code == 503:
        #     response = requests.get(backup)
        newIP = response.text
        if(lastIP != newIP):
            print newIP
            # When the IP is changed the script sends an email to the administrator.
            lastIP = newIP  
            subject = "Nueva IP para Domo.Granada"
            body = "La nueva IP para Domo.Granada es %s." % newIP
            message = composeMail("mail_login", to, subject, body)
            sendMail(message, mail_login, password, to, smpt_server, 587)
    except Exception, e:
        print e
    
    time.sleep(300)
