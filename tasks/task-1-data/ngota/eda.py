#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 12:08:20 2023

@author: ngota
"""

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from category_encoders import OrdinalEncoder, OneHotEncoder
from utils import load_kaggle_dataset, extract_zip

warnings.simplefilter('ignore')

plt.style.use('ggplot')

# Load data
dataset_name = 'thedevastator/employee-attrition-and-factors'
path = load_kaggle_dataset(dataset_name)

filepath = f'{path}/employee-attrition-and-factors.zip'
extract_zip(filepath)

datapath = f'{path}/employee-attrition-and-factors/HR_Analytics.csv.csv'
data = pd.read_csv(datapath, index_col ='EmployeeNumber')

# Basic Strucuture of data
data.shape
data.describe()
data.info()
data.columns
data.nunique()

# Create working file
working = data.copy()

# Based on the analysis conducted, what are the key 
##insights and recommendations for reducing employee 
##attrition in our organization?

# 1. Check high correlation features

## Check distribution of the data



## convert categorical to ordinal
encoder = OrdinalEncoder()
working['Attrition']= encoder.fit_transform(working['Attrition'])

categorical = working.select_dtypes('object').columns


for column in categorical:
    encoder = OrdinalEncoder()
    working[column] = encoder.fit_transform(working[column])
    
working.info()
working[categorical].nunique()

ord_feat = working.corr()['Attrition'].drop('Attrition').abs().sort_values(ascending=False).head(10).index


