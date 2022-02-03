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


# options = Options()
# options.headless = True


driver = webdriver.Firefox()

def Scraper():
    try:
        link = "https://www.reliancedigital.in/asus-hz071ts-rog-zephyrus-g14-gaming-laptop-amd-ryzen-7-5800hs-8gb-512gb-ssd-4gb-nvidia-geforce-gtx-1650-graphics-windows-10-mso-full-hd-35-56-cm-14-inch-/p/492573909"
        driver.get(link)
        price = driver.find_element(By.XPATH, '//*[@class="pdp__offerPrice"]/span[2]').text
        print("₹" + price)
    except:
        price = "Error"
    return price
    
print(Scraper())