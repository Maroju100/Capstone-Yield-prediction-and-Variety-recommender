from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from io import BytesIO, StringIO
import boto3
import selenium
import time
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait

def get_loc(village, location, browser, state_dict):


    #browser.get("https://www.google.com/maps")
    #try:

    #browser.get("https://www.latlong.net/")
    browser.get("https://www.findlatitudeandlongitude.com/")
    time.sleep(2)
    search = browser.find_element_by_name("address")
    #search = browser.find_element_by_id("tc1709").click()
    #search.send_keys('{}, {}, {}'.format(village, location, state_dict[location]))
    search.send_keys('{}, {}'.format(village, state_dict[location]))
    #search.send_keys(Keys.ENTER)
    time.sleep(2)
    #text = browser.page_source
    browser.find_element_by_css_selector('input#load_address_button').click()
    time.sleep(2)
    #coord = browser.current_url.split('@')[1].split(',')
    soup = BeautifulSoup(browser.page_source.encode('utf-8').strip(),
                                                'html.parser')

    coord_lat = soup.find('span', {'id': 'lat_dec'}).find('span',
                                    {'class': 'value'}).get_text()[:8]
    coord_lon = soup.find('span', {'id': 'lon_dec'}).find('span',
                                    {'class': 'value'}).get_text()[:8]

    return location, village, float(coord_lat), float(coord_lon)

    #except:
        #return location, village, '', ''

if __name__ == '__main__':
    #df = pd.read_csv('village_names.csv')
    #places = df[df['Location'] == 'MAHARASHTRA']['Village'].unique()




    loc_dict = {'MAHARASHTRA': 'JAKAPUR', 'MAHARASHTRA1': 'GOLEGAON',
                'MAHARASHTRA2': 'KAKANDI', 'MAHARASHTRA3': 'GANPUR',
                'MAHARASHTRA4': 'DAHEGAON' }


    start = time.time()
    df = pd.read_csv('village_location_duplicates.csv')
    #places = df['Location'].unique()
    df.drop(columns='Unnamed: 0', inplace=True)
    location_groups = df.groupby(by='Location')
    village_dict = {}

    for loc, group in location_groups:
        for vill in set(group['Village'].values):
            village_dict[vill] = loc

    states = ['KARNATAKA', 'TAMILNADU', 'KADAPA, ANDHRA PRADESH', 'KADAPA, ANDHRA PRADESH',
              'W GODAVARI, ANDHRA PRADESH', 'KHAMMAM, TELANGANA','TELANGANA', 'ANDHRA PRADESH',
              'MAHARASHTRA', 'PRAKASAM, ANDHRA PRADESH', 'KADAPA, ANDHRA PRADESH','E GODAVARI, ANDHRA PRADESH',
              'TELANGANA']
    state_dict = dict(zip(df['Location'].unique(), states))

    options = Options()
    options.add_argument('-headless')
    browser = Firefox(executable_path='geckodriver', firefox_options=options)
    s3 = boto3.client('s3')

    with StringIO() as f:
        wr = csv.writer(f)
        wr.writerow(['Location', 'Village', 'Latitude', 'Longitude'])

        for village, location in village_dict.items():
            data = get_loc(village, location, browser, state_dict)
            wr.writerow(data)
            time.sleep(4)

            s3.put_object(Bucket='capstone-web-scrape',
                          Key='duplicates_village_location_data.csv',
                          Body=f.getvalue())
    print (time.time() - start)
'''    with open("location_coord_data.csv", "w") as f:
        wr = csv.writer(f)
        wr.writerow(['State', 'Location', 'Latitude', 'Longitude'])

        for place, state in zip(places, states):

            if 'MAHARASHTRA' in place:
                data = get_loc(loc_dict[place], state)
            else:
                data = get_loc(place, state)

            wr.writerow(data)
            time.sleep(3)'''
