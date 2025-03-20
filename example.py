import os
import requests
from pystyle import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from time import sleep
import keyboard as kb
import json
import undetected_chromedriver as uc
os.system(f'cls & title gmail ~ unofficialdxnny')
options = Options()
options.page_load_strategy = 'eager'
options.headless = False
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--log-level=OFF")
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
print('gmail')
driver = webdriver.Chrome(options=options)
driver.get("https://gmail.com")
wait = WebDriverWait(driver, 100)
## driver.maximize_window()

click = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")))
click.click()
click.clear()
click.send_keys('example@gmail.com')
click = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span")))
click.click()
