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

import sys
import logging
import datetime

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

WAIT_TIME = 300

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
    print('Test Started')

    # Checks if test is complete
    WebDriverWait(driver, WAIT_TIME).until(EC.text_to_be_present_in_element((By.ID, "button-text-en"), "Start"))
    print('Test Completed')

    ipv4 = driver.find_element(By.ID, "results-ipv4-address")
    speed = driver.find_element(By.ID, "results-download")

    driver.quit()
except:
    print('Failed')
finally:
    sys.exit()
