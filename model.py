import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap
from pandas.plotting import scatter_matrix
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import time
from datetime import datetime


from sklearn.model_selection import train_test_split

#from bs4 import BeautifulSoup
#from urllib.request import urlopen
import csv

#from selenium import webdriver
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.keys import Keys
#import selenium
import time

class MyModel():
    '''
    '''

    def __init__(self):

        self.lr = LinearRegression()
        self.gbr = GradientBoostingRegressor()
        self.rf = RandomForestRegressor()

    def fit(self, X, y):
        self.lr.fit(X, y)
        self.gbr.fit(X, y)
        self.rf.fit(X, y)

    def predict(self, X):
        (self.predictions_lr, self.predictions_gbr, self.predictions_rf
        = self.lr.predict(X), self.gbr.predict(X), self.rf.predict(X))

        return self.predictions_lr, self.predictions_gbr, self.predictions_rf

    def score(self, y):

        return 
