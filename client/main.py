# Copyright 2022 Allen Padilla
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Supported with funding from the Internet Society Manitoba Chapter Inc. (www.internetsocietymanitoba.ca) 

# Top level variables to change depending on requirements
VERSION="2"

# TCP_IP = 'localhost'
# TCP_PORT=81
# Get server info from file outside of compiled code

with open('server.ini') as server:
    contents = server.readlines()
    print(contents)
    TCP_IP = contents.read(0)
    TCP_PORT = contents.read(1)

WAIT_TIME=30

# IMPORTS
import sys
import json
import socket
import locale
import ctypes
import logging
import tkinter
import requests
import datetime
import webbrowser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from tkinter import *
from configparser import ConfigParser
from subprocess import CREATE_NO_WINDOW
# END OF IMPORT

# Language information
en_CA = r'''This computer is set to run an internet speed test from the site https://performance.cira.ca/ when it starts up and then from time to time. No personal information is collected. 

This test runs silently so you will not see anything happening. It will not affect your internet connection, it does not consume very much data, and there is no cost. 

The purpose of this test is to provide researchers with an accurate and up to date status of the internet available to residents in your area. 

You may choose to opt-out of this service at any time by going to "C:\Program Files\Unattened IPT\settings.ini" and change "allow" from YES to NO and then save the file. 

For more information, read the Terms and Conditions of Use for the CIRA Internet Performance Test, and the M-Lab Privacy Policy.'''

fr_CA = r'''Modalités et conditions d'utilisation (pour le test de performance Internet de CIRA )

Cet ordinateur commencera à exécuter un test de vitesse Internet du site web https://performance.cira.ca/ dès qu’il démarre et encore de temps en temps. Aucun renseignement personnel sera recueilli.

Ce test s'exécute en mode silencieux afin que vous ne voyiez rien se produire. Cela n'affectera pas votre connexion internet, il ne consomme pas beaucoup de données et il n'y a aucun coût.

Le but de ce test est de fournir aux chercheurs un état précis et à jour de l’internet disponible aux résidents de votre région.

Vous pourriez choisir de désactiver ce service à tout moment en allant à « C:\Program Files\Unattened IPT\settings.ini » et en changeant « allow » de YES à NO et ensuite sauvegardant le fichier.

Pour plus d'informations, lisez les Conditions générales d’utilisation du test de performance Internet CIRA et la Politique de confidentialité de M-Lab.'''

# Get the user's current Windows UI language
windll = ctypes.windll.kernel32
windll.GetUserDefaultUILanguage()
language = locale.windows_locale[windll.GetUserDefaultUILanguage()][:2]

# Check what language they have on their system, and change the message box depending on the UI.
if language == "fr":
    message = fr_CA
    checkLabel = "Ouvrir les termes et conditions et les politiques de confidentialité dans votre navigateur"
    buttonLabel = "Ne plus afficher"
    
    termsURL = "https://www.cira.ca/fr/soutenir-linternet-canadien/test-de-performance-internet/a-propos-du-test/modalites-et-conditions"
    privacyURL = "http://www.measurementlab.net/privacy/"
else:
    message = en_CA
    checkLabel = "Open terms and conditions, and privacy policies in your browser"
    buttonLabel = "Do not show again"
    
    termsURL = "https://www.cira.ca/improving-canadas-internet/initiatives/internet-performance-test/how-internet-performance-test-3"
    privacyURL = "http://www.measurementlab.net/privacy/"

# Performance testing method, check if they are opted in and if they are send information
# Connects to performance cira via a headless edge browser, and clicks Start
def performanceTest():
    optedIn = config['settings']['allow']
    if optedIn == "YES":
        config.set('settings','version', VERSION)

        with open(r"settings.ini", 'w') as configfile:
                config.write(configfile)

        # Setup a headless Edge driver
        service = Service(EdgeChromiumDriverManager().install())
        service.creationflags = CREATE_NO_WINDOW

        options = Options()
        options.add_argument("headless")
        driver = webdriver.Edge(service=service, options=options)

        # URL of the Performance CIRA website
        url = "https://performance.cira.ca/mini"

        # Open the website
        driver.get(url)

        try:
            WebDriverWait(driver, WAIT_TIME).until(EC.text_to_be_present_in_element((By.ID, "button-text-en"), "Start"))
            button = driver.find_element(By.ID, "button-start-test")
            button.click()

            # Checks if test started
            WebDriverWait(driver, WAIT_TIME).until(EC.text_to_be_present_in_element((By.ID, "button-text-en"), "Wait"))
            logging.info('Test has started')
            
            # Checks if test is complete
            WebDriverWait(driver, WAIT_TIME).until(EC.text_to_be_present_in_element((By.ID, "button-text-en"), "Start"))
            print('Test complete')

            ipv4 = driver.find_element(By.ID, "results-ipv4-address")
            speed = driver.find_element(By.ID, "results-download")

            logging.info("Test complete Last run: "+datetime.datetime.now().strftime("%Y/%m/%d:%H:%M:%S") + " - " + ipv4.get_attribute('innerHTML') + " Downloading @ " + speed.get_attribute('innerHTML'))

            driver.quit()
        except:
            logging.error("Test failed")
        finally:
            sys.exit()
    else:
        sys.exit()
# End of performance test method

# Terms and conditions pop up
# If they toggle the check box, show the two different websites, and create the settings file
def termsAndConditions(answer):
    window.destroy()
    if answer == 1:
        if language == "fr":
            webbrowser.open(termsURL, new=2)
            webbrowser.open(privacyURL, new=2)
        else:
            webbrowser.open(termsURL, new=2)
            webbrowser.open(privacyURL, new=2)

        config.add_section('settings')
        config.set('settings','version', VERSION)
        config.set('settings','allow','YES')

        with open(r"settings.ini", 'w') as configfile:
                config.write(configfile)

        performanceTest()

    elif answer == 0:
        config.add_section('settings')
        config.set('settings','version', VERSION)
        config.set('settings','allow','YES')

        with open(r"settings.ini", 'w') as configfile:
                config.write(configfile)

        performanceTest()
    elif answer == 3:
        sys.exit()
# End of terms and conditions

# Initialize the config parser
config = ConfigParser()
config.read('settings.ini')
logging.basicConfig(filename="log.log", level=logging.INFO)

# Try to connect to the Internet Society server to log information
try:
    tcp_socket = socket.create_connection((TCP_IP, TCP_PORT))
    try:
        hostname = socket.gethostname()
        ipv4 = requests.get('http://ip.42.pl/raw').text
        pc_info = {'version': VERSION,'hostname': hostname,'ipv4': ipv4}
        data = json.dumps(pc_info)
        tcp_socket.sendall(bytes(data, encoding="utf-8"))
    except:
        logging.error('Unable to connect to server')
    finally:
        tcp_socket.close()
except:
    logging.error('Unable to connect to server')

# Main functions
if not config.has_option('settings', 'allow'):
    window = tkinter.Tk()
    answer = IntVar()

    # Change the Window Title based on the system language
    if language == "fr":  
        window.title('Enquête sur les performances internet')
    else:
        window.title('Internet Performance Survey')
                 
    # Change the window sizing depending on the system language
    if language == "fr":    
        window_width = 500
        window_height = 150
    else:
        window_width = 500
        window_height = 420

    # Calculate window size to fit the program in the middle of the screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    # Create a centered label
    label = Label(window, text=message, wraplength=300, justify="center")
    label.pack(ipadx=10, ipady=10)

    # Create a check box that will change the answer variable
    chk_box = Checkbutton(window,text=checkLabel,variable=answer).pack()

    # Create a button that clicks into the terms and conditions method
    btn_answer = Button(window,text=buttonLabel,command=lambda : termsAndConditions(answer.get()), padx=100, pady=10, relief=RIDGE).pack()

    window.mainloop()
else:
    performanceTest()
