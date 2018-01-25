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
    #df = pd.read_csv('village_names.csv')
    #places = df[df['Location'] == 'MAHARASHTRA']['Village'].unique()
    states = ['KARNATAKA','ANDHRA PRADESH', 'ANDHRA PRADESH', 'MAHARASHTRA', 'MAHARASHTRA',
              'MAHARASHTRA', 'MAHARASHTRA', 'MAHARASHTRA', 'ANDHRA PRADESH', 'ANDHRA PRADESH',
              'TAMILNADU', 'TELANGANA', 'ANDHRA PRADESH', 'ANDHRA PRADESH', 'ANDHRA PRADESH',
              'TELANGANA', 'TELANGANA', 'ANDHRA PRADESH']

              'BALLARI', 'DUVVURU', 'ELURU', 'MAHARASHTRA1', 'MAHARASHTRA',
       'MAHARASHTRA3', 'MAHARASHTRA4', 'MAHARASHTRA2', 'KURNOOL',
       'PORUMAMILLA', 'CUMBAM', 'SATHUPALLY', 'RAJAHAMANDRY', 'MARKAPUR',
       'S MYDUKUR', 'KARIMNAGAR', 'WARANGAL', 'GUNTUR'

    loc_dict = {'MAHARASHTRA': 'JAKAPUR', 'MAHARASHTRA1': 'GOLEGAON',
                'MAHARASHTRA2': 'KAKANDI', 'MAHARASHTRA3': 'GANPUR'
                'MAHARASHTRA4': 'DAHEGAON }



    df = pd.read_csv('location_village_names.csv')


    with open("location_coord_data.csv", "w") as f:
        wr = csv.writer(f)
        wr.writerow(['State', 'Location', 'Latitude', 'Longitude'])

        for place, state in zip(places, states):

            if 'MAHARASHTRA' in place:
                data = get_loc(loc_dict[place], state)
            else:
                data = get_loc(place, state)

            wr.writerow(data)
            time.sleep(3)
