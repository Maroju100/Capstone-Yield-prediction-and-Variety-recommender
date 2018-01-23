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

def get_alt(village, location):
    browser = webdriver.Firefox()
    browser.get("https://www.whatismyelevation.com/##")

    browser.find_element_by_id("change-location").click()
    time.sleep(1)
    search = browser.find_element_by_id("address")
    search.send_keys('{}, {}'.format(village, location))

    search.send_keys(Keys.ENTER)

    text = browser.page_source
    #coord = browser.current_url.split('@')[1].split(',')
    soup = BeautifulSoup(text, "lxml")

    elevation = soup.find('div', {'id':'elevation'})
    altitude = elevation.find('span', {'class': "value"})

    browser.quit()

    return location, village, float(altitude.decode().split('>')[1].split('<')[0].replace(',', ''))

if __name__ == '__main__':
    df = pd.read_csv('village_names.csv')

    places = df[['Location', 'Village']].values
    with open("altitude_data.csv", "w") as f:
        wr = csv.writer(f)
        #wr.writerow(['Location', 'Village', 'Latitude', 'Longitude'])

        for place in places:
            data = get_alt(place[1], place[0])
            wr.writerow(data)
            time.sleep(2)
