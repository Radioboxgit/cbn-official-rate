"""
Created on Wed Jun  1 17:02:46 2022

@author: Chinedu
"""

#importing the necessary libs
import pandas as pd
from datetime import date
import json
import datetime
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#lambda credentilas
lambda_test_username='your user name '
lambda_access_token='your access token'
gridUrl = "hub.lambdatest.com/wd/hub"


capabilities = {
    'LT:Options': {
        "build": "cbn_rate_version_1.0",
        "name": "official_cbn_rate",
        "platformName": "Windows 10",
        "headless":True
    },
    "browserName": "Firefox",
    "browserVersion": "100.0",
}


executor_url = "https://"+lambda_test_username+":"+lambda_access_token+"@"+gridUrl


driver = webdriver.Remote(
    command_executor=executor_url,
    desired_capabilities=capabilities
)



URL='https://www.cbn.gov.ng/rates/exchratebycurrency.asp?beginrec=1&endrec=100&currencytype'

driver.get(URL)

timeout_in_seconds = 40
WebDriverWait(driver, timeout_in_seconds).until(EC.invisibility_of_element_located((By.CLASS_NAME, "dataTables_empty")))

html = driver.page_source
df_list = pd.read_html(html)
table=df_list[3] #the table of interest

driver.quit()
