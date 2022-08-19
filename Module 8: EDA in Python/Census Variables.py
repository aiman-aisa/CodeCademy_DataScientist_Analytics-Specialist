import codecademylib3

# Import pandas with alias
import pandas as pd
import numpy as np
# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

# 1
print(census.head())

#3
print(census.dtypes)

#4
print(census['birth_year'].unique())

#5
census['birth_year'] = census['birth_year'].replace(['missing'], 1967)
print(census['birth_year'].unique())

#6
census['birth_year'] = census['birth_year'].astype('int')
print(census.dtypes)

#7
print(census['birth_year'].mean())

#8
census['higher_tax'] = pd.Categorical(census['higher_tax'], ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'], ordered = True)
print(census['higher_tax'].unique())

#9
census['higher_tax'] = census['higher_tax'].cat.codes
print(census['higher_tax'].median())

#10
#census = pd.get_dummies(data = census, columns = ['marital_status'])
#print(census.head())

#11
print(census['marital_status'].unique())
marital_status_categories = ['single', 'married', 'divorced', 'widowed']
census['marital_status'] = pd.Categorical(census['marital_status'], marital_status_categories, ordered = True)
print(census['marital_status'].unique())
census['marital_codes'] = census['marital_status'].cat.codes
print(census.head())
print(census['marital_codes'].median())

census = pd.get_dummies(data = census, columns = ['marital_status'])
print(census.head())

census['age'] = 2022 - census['birth_year']
age_bins = np.arange(min(census['age'])-4, 100, 5)
census['age_group'] = pd.cut(census['age'], bins = age_bins)
print(census.head())