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

def get_loc(village, location):
    browser = webdriver.Firefox()
    browser.get("https://www.google.com/maps")

    search = browser.find_element_by_id("searchboxinput")
    search.send_keys('{}, {}'.format(village, location))

    search.send_keys(Keys.ENTER)
    time.sleep(3)
    text = browser.page_source
    coord = browser.current_url.split('@')[1].split(',')
    #soup = BeautifulSoup(text, "lxml")
    browser.quit()
    return location, village, float(coord[0]), float(coord[1])

if __name__ == '__main__':
    df = pd.read_csv('village_names.csv')

    places = df[df['Location'] == 'MAHARASHTRA']['Village'].unique()
    with open("location_data.csv", "a") as f:
        wr = csv.writer(f)
        #wr.writerow(['Location', 'Village', 'Latitude', 'Longitude'])

        for place in places[84:]:
            data = get_loc(place, 'MAHARASHTRA')
            wr.writerow(data)
            time.sleep(3)
