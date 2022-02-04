from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import requests
import csv
import time, os
from csv import writer
import json


options = Options()
options.headless = True
options.add_argument("--disable-infobars")

options.add_argument("start-maximized")

options.add_argument("--disable-extensions")

# options.add_experimental_option("prefs",
#                                {"profile.default_content_setting_values.notifications": 2
#                                 })
# options.add_Argument("--disable-notifications")

driver = webdriver.Firefox(options=options)
link = "https://www.reliancedigital.in/asus-hx019t-rog-strix-g17-gaming-laptop-amd-ryzen-7-4800h-8gb-512gb-ssd-4-gb-nvidia-geforce-gtx-1650-windows-10-fhd-43-94-cm-17-3-inch-/p/491997666"
driver.get(link)

def getPrice():
    try:
        price = driver.find_element(By.XPATH, '//*[@class="pdp__offerPrice"]/span[2]').text
    except:
        price = "Error"

    return price
    
def closeAlert():
    try:
        driver.find_element(By.XPATH, '//*[@id="wzrk-cancel"]').click()
    except:
        # print("No Alert")
        pass

def isOOS():
    #Check If Product is Out Of Stock
    try:
        closeAlert()
        OOS = len(driver.find_elements(By.CLASS_NAME, 'pdp__noStockBlock')) > 0
    except:
        OOS = False
    return OOS

def runEndlessly():

    while True:
        driver.get(link)
        price = getPrice()
        iOOS = isOOS()
        if iOOS:
            print("Currently OOS")

        print("Current Price=> " , price)
        time.sleep(2)

# runEndlessly()