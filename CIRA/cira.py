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