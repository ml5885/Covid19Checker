import pandas as pd
import numpy as np

# data visualization library 
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# machine learning library
from sklearn.preprocessing import LabelEncoder
e=LabelEncoder()

# info about dataset
    # 1=above 60, 0 = below
    # 0=none, 1=female, 2=male
    # 0=other, 1=abroad, 2=contact with confirmed


# reading the dataset 
covid = pd.read_csv('./data/corona_tested_individuals_ver_006.english.csv')

covid['cough']=e.fit_transform(covid['cough'])
covid['fever']=e.fit_transform(covid['fever'])
covid['sore_throat']=e.fit_transform(covid['sore_throat'])
covid['shortness_of_breath']=e.fit_transform(covid['shortness_of_breath'])
covid['head_ache']=e.fit_transform(covid['head_ache'])
covid['corona_result']=e.fit_transform(covid['corona_result'])
covid['age_60_and_above']=e.fit_transform(covid['age_60_and_above'])
covid['gender']=e.fit_transform(covid['gender'])
covid['test_indication']=e.fit_transform(covid['test_indication'])

print(covid.describe(include='all'))

