import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model, feature_selection

beer = pd.read_csv('beer.tsv', delimiter='\t')
beer = beer.dropna()

def good(x):
	if x > 4.3:
		return 1
	else:
		return 0
beer_types = ['Ale', 'Stout', 'IPA', 'Lager']
for t in beer_types:
        beer[t] = beer['Type'].str.contains(t) * 1
beer['Good'] = beer['WR'].apply(good)
#dummies = pd.get_dummies(beer['Type'])
#beer= beer.join(dummies)
select = ['Reviews', 'ABV', 'Ale', 'Stout', 'IPA', 'Lager']
input = beer[select].values
good = beer['Good'].values

# drop good and non-numeric features to see which features are relevant
del beer['Good']
del beer['Name']
del beer['Brewery']
del beer['Type']
print "Feature selection:", feature_selection.univariate_selection.f_regression(beer, good)

logm = linear_model.LogisticRegression()
logm.fit(input, good)
logm.predict(input)
print "Beer selection score:", logm.score(input, good)
