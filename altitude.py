from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import selenium
import time
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait


def get_alt(village, location, browser):
    #executable_path = './phantomjs-2.1.1-linux-x86_64/bin/phantomjs'

    #service_log_path = './log/ghostdriver.log'

    #browser = webdriver.PhantomJS()#(executable_path=executable_path, service_log_path=service_log_path)


    browser.get("https://www.whatismyelevation.com/##")

    browser.find_element_by_id("change-location").click()
    time.sleep(2)
    search = browser.find_element_by_id("address")
    search.send_keys('{}, {}'.format(village, location))

    search.send_keys(Keys.ENTER)
    time.sleep(3)
    text = browser.page_source
    #coord = browser.current_url.split('@')[1].split(',')
    soup = BeautifulSoup(text, "lxml")

    elevation = soup.find('div', {'id':'elevation'})
    altitude = elevation.find('span', {'class': "value"})

    #browser.quit()
    #print (altitude.decode().split('>')[1].split('<')[0].replace(',', ''))
    if len(altitude.decode().split('>')[1].split('<')[0].replace(',', '')) > 0:
        alt = float(altitude.decode().split('>')[1].split('<')[0].replace(',', ''))
    else:
        alt = altitude.decode().split('>')[1].split('<')[0].replace(',', '')

    return location, village, alt

if __name__ == '__main__':
    df = pd.read_csv('village_names.csv')

    places = df['Location'].unique()

    states = ['KARNATAKA', 'ANDHRA PRADESH', 'ANDHRA PRADESH', 'MAHARASHTRA', 'ANDHRA PRADESH', 'ANDHRA PRADESH',
              'TAMILNADU', 'TELANGANA', 'ANDHRA PRADESH', 'ANDHRA PRADESH', 'ANDHRA PRADESH',
              'TELANGANA', 'TELANGANA', 'ANDHRA PRADESH']

    options = Options()
    options.add_argument('-headless')
    browser = Firefox(executable_path='geckodriver', firefox_options=options)

    with open("location_altitude_data.csv", "w") as f:
        wr = csv.writer(f)
        wr.writerow(['State', 'Location', 'Altitude'])

        for location, state in zip(places, states):
            data = get_alt(location, state, browser)
            wr.writerow(data)
            time.sleep(2)
