import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
from io import BytesIO, StringIO
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import boto3
import selenium
import time
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
import multiprocessing as mp

def get_temp(village, location, browser, state_dict):

    driver.maximize_window()
    browser.get("https://www.wunderground.com/history/")

    search = browser.find_element_by_id("histSearch")
    search.send_keys('{}, {}, {}'.format(village, location, state_dict[location]))

    select = Select(browser.find_element_by_class_name("day"))
    select.select_by_visible_text('14')

    select2 = Select(browser.find_element_by_class_name("year"))
    select2.select_by_visible_text('2014')

    browser.find_element_by_css_selector("input.button.radius").click()
    time.sleep(2)

    browser.get(browser.current_url.replace('Daily', 'Monthly'))
    time.sleep(2)
    #browser.find_element_by_css_selector("a.contentTabActive.brTop5").click()
    soup = BeautifulSoup(browser.page_source.encode('utf-8').strip(),
                                                    'html.parser')

    data_max = []
    data_min = []
    year = int(soup.find('select',
                                {'class': 'year form-select'}).find('option',
                                {'selected': "selected"}).get_text())

    while '2018' not in browser.current_url.split('?')[0]:
        row_max = []
        row_min = []



        row_max.append(int(soup.find('select',
                                    {'class': 'year form-select'}).find('option',
                                    {'selected': "selected"}).get_text()))
        row_max.append(village)

        row_min.append(int(soup.find('select',
                                    {'class': 'year form-select'}).find('option',
                                    {'selected': "selected"}).get_text()))
        row_min.append(village)

        for i in range(12):

            soup = BeautifulSoup(browser.page_source, 'lxml')
            temp = soup.find_all('span', {'class': 'wx-value'})
            row_max.append(float(temp[0].get_text()))

            if len(temp) > 5:
                row_min.append(float(temp[5].get_text()))
            else:
                row_min.append(0)

            browser.find_element_by_class_name("next-link").click()
            time.sleep(2)

        data_max.append(row_max)
        data_min.append(row_min)

    return data_max, data_min

def write_temp(village_dict, browser, state_dict, s3, kind='max'):

    with StringIO() as f:
        wr = csv.writer(f)

        wr.writerow(['YEAR','Village','1', '2', '3', '4', '5',
                         '6', '7', '8', '9', '10', '11', '12'])

        for village, location in village_dict.items():
            data_max, data_min = get_temp(village, location,
                                          browser, state_dict)
            if kind == 'max':
                wr.writerows(data_max)

            elif kind == 'min':
                wr.writerows(data_min)


            s3.put_object(Bucket='capstone-web-scrape',
                          Key='village_temp_data_{}.csv'.format(kind),
                          Body=f.getvalue())
    return None

if __name__ == '__main__':
    #df = pd.read_csv('village_names.csv')
    #places = df[df['Location'] == 'MAHARASHTRA']['Village'].unique()


    loc_dict = {'MAHARASHTRA': 'JAKAPUR', 'MAHARASHTRA1': 'GOLEGAON',
                'MAHARASHTRA2': 'KAKANDI', 'MAHARASHTRA3': 'GANPUR',
                'MAHARASHTRA4': 'DAHEGAON' }

    start = time.time()

    df = pd.read_csv('village_names.csv')
    #places = df['Location'].unique()
    df.drop(columns='Unnamed: 0', inplace=True)
    location_groups = df.groupby(by='Location')
    village_dict = {}

    for loc, group in location_groups:
        for vill in set(group['Village'].values):
            village_dict[vill] = loc

    states = ['KARNATAKA', 'ANDHRA PRADESH', 'ANDHRA PRADESH', 'MAHARASHTRA',
              'ANDHRA PRADESH', 'ANDHRA PRADESH','TAMILNADU', 'TELANGANA',
              'ANDHRA PRADESH', 'ANDHRA PRADESH', 'ANDHRA PRADESH',
              'TELANGANA', 'TELANGANA', 'ANDHRA PRADESH']

    state_dict = dict(zip(df['Location'].unique(), states))

    options = Options()
    options.add_argument('-headless')
    browser1 = Firefox(executable_path='geckodriver', firefox_options=options)
    browser2 = Firefox(executable_path='geckodriver', firefox_options=options)
    s3 = boto3.client('s3')

    processes = [mp.Process(target=write_temp,
                            args=(village_dict, browser1,
                                  state_dict, s3, 'max')),
                 mp.Process(target=write_temp,
                            args=(village_dict, browser2,
                                  state_dict, s3, 'min'))]
    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print (time.time() - start)
