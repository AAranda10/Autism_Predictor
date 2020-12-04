#!/usr/bin/env python
# coding: utf-8

# In[5]:


import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import wrangle
import prep
from scipy import stats

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score, accuracy_score


'''
    This function will return the results of my findings and provide them to be a callable function with only the results 
    '''

def mvp():
    df = prep.prep_asd_data()
    X_train, y_train, X_validate, y_validate, X_test, y_test = wrangle.train_validate_test(df)
    X_train_scaled, X_validate_scaled, X_test_scaled = wrangle.min_max_scale(X_train, X_validate, X_test)
    #Creating clusters that will be added to dataframe
    X1 = X_train_scaled[['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10']]
    X2 = X_validate_scaled[['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10']]
    X3 = X_test_scaled[['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10']]
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(X1)
    #Adding the clusters to the dataframes
    X_train_scaled['cluster'] = kmeans.predict(X1)
    X_train['cluster'] = kmeans.predict(X1)
    X_validate_scaled['cluster'] = kmeans.predict(X2)
    X_validate['cluster'] = kmeans.predict(X2)
    X_test_scaled['cluster'] = kmeans.predict(X3)
    X_test['cluster'] = kmeans.predict(X3)
    
    logit = LogisticRegression(random_state=123)
    logit.fit(X_train_scaled, y_train)
    test_eval = y_test[['has_asd']].rename(columns={'has_asd': 'actual'})
    test_eval['predict'] = logit.predict(X_test_scaled)
    test_eval['probs'] = logit.predict_proba(X_test_scaled)[:, 1]
    print(classification_report(y_true=test_eval.actual, y_pred=test_eval.predict))
    print('Accuracy of Logistic Regression Model classifier on test set: {:.2f}'
     .format(logit.score(X_test_scaled, y_test)))
    plt.figure(figsize=(16,8))
    plt.hist(test_eval.actual, color='blue', alpha=.5, label="Actual Autism Presence")
    plt.hist(test_eval.predict, color='green', alpha=.5, label="Log Reg Model Predicitons")
    plt.xlabel("Is Child Autistic?")
    plt.ylabel("Number of Cases")
    plt.title("Comparing the Distribution of Actual Autism Cases to Autism Predictions")
    plt.legend()
    plt.show()
    return mvp

print("mvp_model.py functions loaded successfully")



