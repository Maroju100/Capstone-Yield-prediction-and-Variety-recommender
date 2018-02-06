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

import multiprocessing as mp
from sklearn.model_selection import train_test_split, GridSearchCV, KFold

#from bs4 import BeautifulSoup
#from urllib.request import urlopen
import csv

#from selenium import webdriver
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.keys import Keys
#import selenium
from transform import *

class MyModel():
    '''
    '''

    def __init__(self):

        self.lr = LinearRegression()
        self.gbr = GradientBoostingRegressor()
        self.rf = RandomForestRegressor()

    def fit(self, X, y):

        processes = [mp.Process(target=self.lr.fit,
                                args=(X, y)),
                     mp.Process(target=self.gbr.fit,
                                args=(X, y)),
                     mp.Process(target=self.rf.fit,
                                args=(X, y))]
        for p in processes:
            p.start()

        for p in processes:
            p.join()

    def predict(self, X):

        (self.predictions_lr,
        self.predictions_gbr,
        self.predictions_rf) = (self.lr.predict(X),
                                self.gbr.predict(X),
                                self.rf.predict(X))

        return self.predictions_lr, self.predictions_gbr, self.predictions_rf

    def score(self, y):

        self.score_lr = mean_squared_error(self.predictions_lr, y)
        self.score_gbr = mean_squared_error(self.predictions_gbr, y)
        self.score_rf = mean_squared_error(self.predictions_rf, y)

        return self.score_lr, self.score_gbr, self.score_rf

    def cv_params(self, X, y, param_grid_rf, param_grid_gb, cv=5):

        cv_params_rf = GridSearchCV(estimator=self.rf, param_grid=param_grid_rf,
                                    scoring="mean_squared_error", n_jobs=-1,
                                    cv=cv, refit=True)

        cv_params_gbr = GridSearchCV(estimator=self.gbr, param_grid=param_grid_gb,
                                    scoring="mean_squared_error", n_jobs=-1,
                                    cv=cv, refit=True)

        processes = [mp.Process(target=cv_params_rf.fit,
                                args=(X, y.values.reshape(1, -1))),
                     mp.Process(target=cv_params_gbr.fit,
                                args=(X, y.values.reshape(1, -1)))]
        for p in processes:
            p.start()

        for p in processes:
            p.join()
        cv_params_rf.set_params()
        cv_params_gbr.set_params()
        #rf_best_params = (cv_params_rf.best_estimator_,
        #                 cv_params_rf.best_score_,
        #                 cv_params_rf.best_params_)

        #gbr_best_params = (cv_params_gbr.best_estimator_,
        #                 cv_params_gbr.best_score_,
        #                 cv_params_gbr.best_params_)
        return cv_params_rf.cv_results_, cv_params_gbr.cv_results_

    def cv_score(self, X, y, param_grid_rf, param_grid_gb, k=5):

        RMS_train_rf = []
        RMS_test_rf = []
        RMS_train_gb = []
        RMS_test_gb = []
        kf = KFold(n_splits=k)

        for train_index, test_index in kf.split(X):

            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

            rf_params, gbr_params = self.cv_params(X_train, y_train,
                                                   param_grid_rf,
                                                   param_grid_gb)

            model_rf = rf_params[0]
            model_gb = gbr_params[0]
            train_predicted_rf = model_rf.predict(X_train)
            test_predicted_rf = model_rf.predict(X_test)
            train_predicted_gb = model_gb.predict(X_train)
            test_predicted_gb = model_gb.predict(X_test)

            RMS_train_rf.append(mean_squared_error(y_train, train_predicted_rf))
            RMS_test_rf.append(mean_squared_error(y_test, test_predicted_rf))
            RMS_train_gb.append(mean_squared_error(y_train, train_predicted_gb))
            RMS_test_gb.append(mean_squared_error(y_test, test_predicted_gb))
            #RMS.append(np.sqrt(mean_squared_error(Y_test, test_predicted)))
        return ('RF Train MSE  : {}'.format(np.mean(RMS_train_rf)),
                'RF Test  MSE  : {}'.format(np.mean(RMS_test_rf)),
                'GB Train MSE  : {}'.format(np.mean(RMS_train_gb)),
                'GB Test  MSE  : {}'.format(np.mean(RMS_test_gb)))

    def cv_score_parallel(self, model, X, y, param_grid_rf, param_grid_gb, k=5):

        RMS_train_rf = []
        RMS_test_rf = []
        RMS_train_gb = []
        RMS_test_gb = []
        kf = KFold(n_splits=k)

        for train_index, test_index in kf.split(X):

            X_train, X_test = X.iloc[train_index], X.iloc[test_index]
            y_train, y_test = y.iloc[train_index], y.iloc[test_index]


            train_predicted = model_rf.predict(X_train)
            test_predicted = model_rf.predict(X_test)

            RMS_train.append(mean_squared_error(y_train, train_predicted))
            RMS_train.append(mean_squared_error(y_test, test_predicted))
            #RMS.append(np.sqrt(mean_squared_error(Y_test, test_predicted)))
        return ('RF Train : {}'.format(np.mean(RMS_train)),
                'RF Test  : {}'.format(np.mean(RMS_test)),
                'GB Train : {}'.format(np.mean(RMS_train)),
                'GB Test  : {}'.format(np.mean(RMS_test)))

'''    def cv(self, X_train, y_train, k=5):

        RMS = []
        kf = KFold(n_splits=k)

        for train_index, test_index in kf.split(X_train):

            x_train, x_test = X_train[train_index], X_train[test_index]
            Y_train, Y_test = y_train[train_index], y_train[test_index]

            linear =  LinearRegression()
            linear.fit(x_train, Y_train)

            train_predicted = linear.predict(x_train)
            test_predicted = linear.predict(x_test)

            RMS.append(mean_squared_error(Y_test, test_predicted) ** 0.5)
            #RMS.append(np.sqrt(mean_squared_error(Y_test, test_predicted)))
        return np.mean(RMS)'''

if __name__ == '__main__':
    from model import MyModel as m
    start = time.time()
    org_df = pd.read_excel('Downloads/Monsanto Dataset Sample.xlsx', header=1)
    rainfall_df = pd.read_csv('weather_data.csv')

    altitude_df = pd.read_csv('Downloads/new_village_altitude_data.csv')
    lat_lon_df = pd.read_csv('complete_vill_loc.csv')
    location_df = lat_lon_df[lat_lon_df['Location'] == 'MAHARASHTRA']

    un_merged = transform_orginal(org_df, location_df)
    merged = merge_transform(un_merged, rainfall_df, altitude_df, lat_lon_df)

    X_cols = ['Sowing Week of Year',
          'Sown \nDate', 'YEAR', 'Sow Month',
          'Days Till Harvest', 'Rainfall', 'Elevation', 'Latitude',
          'Longitude', 'Wet Ear to Raw Seed Recovery']

    y_col = ['Dry Yield Per Acre']

    dummy_col = ['Variety']

    X, y = featurize(merged, X_cols, y_col, dummy_col, split=False)

    rf_param_grid = {'max_features': [0.33, 0.5, 'auto'],
                     'min_samples_leaf': [15, 45, 75],
                     'n_estimators': [10000],
                     'oob_score': [True],
                     'n_jobs': [-1]}

    gb_param_grid = {'min_samples_split': [1000, 1500, 2000],
                     'min_samples_leaf': [15, 45, 75],
                     'max_depth': [4, 5, 7],
                     'max_features': ['sqrt'],
                     'subsample': [0.8],
                     'n_estimators': [10000]}
    model = m()
    #print (model.cv_score(X, y, param_grid_rf = rf_param_grid,
    #                      param_grid_gb = gb_param_grid,
    #                      k=10))
    gsearch_rf = GridSearchCV(RandomForestRegressor(), rf_param_grid, cv=5)
    gsearch_rf.fit(X, y)

    gsearch_gb = GridSearchCV(GradientBoostingRegressor(), gb_param_grid, cv=5)
    gsearch_gb.fit(X, y)
    print ("RF")
    print (gsearch_rf.cv_results_)
    print ('*' * 50)
    print ("RF")
    print (gsearch_gb.cv_results_)
    print ('*' * 50)
    print (time.time() - start)
