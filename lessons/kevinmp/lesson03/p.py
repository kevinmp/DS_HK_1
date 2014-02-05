#!/usr/bin/python

import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')
df
df.describe()
df[:10]

dfg = df[['Age','Impressions','Clicks']].groupby(['Age']).agg([np.mean])
dfg[:10]

def map_age_category(x):
	if x < 18:
		return '1'
	elif x < 25:
		return '2'
	elif x < 32:
		return '3'
	elif x < 45:
		return '4'
	else:
		return '5'
df['age_categories'] = df['Age'].apply(map_age_category)

