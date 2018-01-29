import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv



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

def get_temp(village, location, browser, state_dict):

    browser.get("https://www.wunderground.com/history/")

    search = browser.find_element_by_id("histSearch")
    search.send_keys('{}, {}, {}'.format(village, location, state_dict[location]))

    select = Select(browser.find_element_by_class_name("day"))
    select.select_by_visible_text('14')

    select2 = Select(browser.find_element_by_class_name("year"))
    select2.select_by_visible_text('2014')

    browser.find_element_by_css_selector("input.button.radius").click()
    time.sleep(2)
    browser.find_element_by_css_selector("a.contentTabActive.brTop5").click()

    data_max = []
    data_min = []
    year = int(soup.find('h2', {'class': 'history-date'}).get_text()[-4:])

    data_max.append(['YEAR','Village','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
    data_min.append(['YEAR','Village','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])

    while '2016' not in browser.current_url.split('?')[0]:
        row_max = []
        row_min = []

        soup = BeautifulSoup(browser.page_source, 'lxml')
        
        row_max.append(int(soup.find('h2', {'class': 'history-date'}).get_text()[-4:]))
        row_max.append('Ballari')

        row_min.append(int(soup.find('h2', {'class': 'history-date'}).get_text()[-4:]))
        row_min.append('Ballari')

        for i in range(12):
            row_max.append(float(temp[0].get_text()))
            row_min.append(float(temp[-1].get_text()))
            browser.find_element_by_class_name("next-link").click()
            time.sleep(2)
        #row = ['Ballari', float(temp[0].get_text()), float(temp[-1].get_text())]
        data_max.append(row_max)
        data_min.append(row_min)

    return data
